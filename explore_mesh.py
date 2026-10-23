"""Разведка МЭШ: выясняем, каким JSON-запросом страница «Домашние задания»
получает данные. Скрипт ТОЛЬКО читает: открывает страницы и слушает ответы.

Логин и пароль не запрашиваются и нигде не хранятся: вход вы делаете сами
в открывшемся окне браузера. Сессия остаётся в папке .session (в .gitignore).

В отчёт попадает только СТРУКТУРА ответов (имена полей и типы) и URL без
значений параметров. Тексты заданий, фамилии, токены и заголовки в отчёт
не пишутся, так что отчёт можно показывать мне.
"""

import json
import re
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

from playwright.sync_api import sync_playwright, Response

SESSION_DIR = Path(".session")          # persistent context: cookies и localStorage
REPORT_FILE = Path("discovery_report.json")
START_URL = "https://school.mos.ru/"
HOMEWORK_URL = "https://school.mos.ru/diary/homeworks/homeworks/"

# Метки капчи/проверок: если увидим, сразу останавливаемся (обходить не будем).
CHALLENGE_MARKERS = ("captcha", "капча", "я не робот", "smartcaptcha")

found: list[dict] = []  # собранные описания JSON-ответов


def shape(value, depth: int = 0):
    """Описывает структуру JSON без значений: ключи и типы."""
    if depth > 6:
        return "…"
    if isinstance(value, dict):
        return {k: shape(v, depth + 1) for k, v in value.items()}
    if isinstance(value, list):
        # Для списка берём форму первого элемента + длину.
        return [f"len={len(value)}", shape(value[0], depth + 1)] if value else []
    return type(value).__name__


def on_response(resp: Response) -> None:
    """Запоминает каждый JSON-ответ школьного портала (только структуру)."""
    try:
        host = urlsplit(resp.url).netloc
        ctype = resp.headers.get("content-type", "")
        if "mos.ru" not in host or "json" not in ctype:
            return
        body = resp.json()
    except Exception:
        return
    parts = urlsplit(resp.url)
    found.append({
        "method": resp.request.method,
        "host": parts.netloc,
        "path": parts.path,
        # имена параметров запроса без значений (в значениях могут быть id)
        "query_params": sorted(parse_qs(parts.query).keys()),
        "status": resp.status,
        "shape": shape(body),
        # сырой ответ кладём ЛОКАЛЬНО в .session, в отчёт он не попадает
        "_raw": body,
    })


def page_has_challenge(page) -> bool:
    text = page.content().lower()
    return any(m in text for m in CHALLENGE_MARKERS)


def main() -> None:
    SESSION_DIR.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            user_data_dir=str(SESSION_DIR), headless=False,
        )
        ctx.on("response", on_response)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        page.goto(START_URL)
        input("Войдите в МЭШ вручную в окне браузера, затем нажмите Enter здесь... ")

        if page_has_challenge(page):
            print("Обнаружена капча/проверка. Я её не обхожу: пройдите её сами "
                  "или остановитесь и сообщите мне.")
            input("Когда пройдёте проверку, нажмите Enter... ")

        found.clear()  # интересуют только запросы со страницы заданий
        page.goto(HOMEWORK_URL)
        print("\nОткрылась страница заданий. Если это не она, перейдите вручную: "
              "«Домашние задания» → вкладка «Ближайшие».")
        input("Когда задания видны на экране, нажмите Enter... ")

        ctx.close()

    # Сырые ответы кладём в .session (локально), в отчёт — только структура.
    raw_dir = SESSION_DIR / "raw"
    raw_dir.mkdir(exist_ok=True)
    report = []
    for i, item in enumerate(found):
        raw = item.pop("_raw")
        (raw_dir / f"{i:02d}.json").write_text(
            json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
        # Помечаем «подозрительные» ответы: в JSON есть слова про домашку.
        blob = json.dumps(raw, ensure_ascii=False).lower()
        item["looks_like_homework"] = bool(
            re.search(r"homework|домашн|subject|предмет", blob))
        item["raw_file"] = str(raw_dir / f"{i:02d}.json")
        report.append(item)

    REPORT_FILE.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                           encoding="utf-8")
    print(f"\nНайдено JSON-ответов: {len(report)}. Отчёт: {REPORT_FILE}")
    for i, it in enumerate(report):
        mark = "  <-- похоже на задания" if it["looks_like_homework"] else ""
        print(f"[{i:02d}] {it['method']} {it['host']}{it['path']} "
              f"params={it['query_params']}{mark}")


if __name__ == "__main__":
    main()
