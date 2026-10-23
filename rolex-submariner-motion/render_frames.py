"""Render every frame of the film deterministically via window.__render(ms).

python3 render_frames.py PAGE.html OUTDIR FPS WORKER NWORKERS
PAGE must be the page wrapped in a document (the #film hash switches the stage to full window).
"""
import sys, asyncio, os
from playwright.async_api import async_playwright

page_path, out, fps, wi, nw = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
        await pg.goto('file://' + os.path.abspath(page_path) + '#film')
        await pg.evaluate('document.fonts.ready')
        await pg.wait_for_timeout(800)
        total = await pg.evaluate('window.__total')
        n = round(total / 1000 * fps)
        for i in range(wi, n, nw):
            await pg.evaluate(f'window.__render({i * 1000 / fps})')
            await pg.screenshot(path=f'{out}/f{i:05d}.jpg', type='jpeg', quality=93)
        await b.close()
        print('worker', wi, 'done', n)

asyncio.run(main())
