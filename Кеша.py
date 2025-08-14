from gtts import gTTS
import speech_recognition as sr
import pygame
import os
import time
import random
import keyboard
import webbrowser
from datetime import datetime
import AppOpener
import threading
import queue
import psutil
import os
import time
import threading
import queue
import tempfile
import pygame
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import keyboard
from datetime import datetime
import psutil
import AppOpener
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from youtube_search import YoutubeSearch
from help_meneger import *


def search_and_open_youtube(query):
    """
    Ищет видео на YouTube по запросу и открывает первое найденное видео в браузере.
    
    :param query: Строка поискового запроса.
    :return: None (открывает ссылку в браузере).
    """
    # Получаем результаты поиска
    results = YoutubeSearch(query, max_results=1).to_dict()  # Берём только первый результат
    
    if not results:
        print("Ничего не найдено.")
        return
    
    # Формируем полную ссылку на видео
    video_url = f"https://youtube.com{results[0]['url_suffix']}"
    
    # Открываем ссылку в браузере
    webbrowser.open(video_url)
    print(f"Открываю видео: {results[0]['title']}")

def quiz():
    questions = {
        "Общие знания": [
        {
        "question": "Сколько планет в Солнечной системе?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
        },
        {
        "question": "Какая самая длинная река в мире?",
        "options": ["Амазонка", "Нил", "Янцзы", "Миссисипи"],
        "answer": "Амазонка"
        },
        {
        "question": "Столица Австралии?",
        "options": ["Сидней", "Мельбурн", "Канберра", "Брисбен"],
        "answer": "Канберра"
        },
        {
        "question": "Сколько континентов на Земле?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
        },
        {
        "question": "Какая самая большая страна по площади?",
        "options": ["Китай", "США", "Канада", "Россия"],
        "answer": "Россия"
        },
        {
        "question": "Какое животное является символом Австралии?",
        "options": ["Коала", "Кенгуру", "Утконос", "Эму"],
        "answer": "Кенгуру"
        },
        {
        "question": "Как называется самая большая пустыня в мире?",
        "options": ["Гоби", "Сахара", "Аравийская", "Антарктическая"],
        "answer": "Антарктическая"
        },
        {
        "question": "В каком году началась Вторая мировая война?",
        "options": ["1937", "1939", "1941", "1943"],
        "answer": "1939"
        },
        {
        "question": "Какой газ преобладает в составе атмосферы Земли?",
        "options": ["Кислород", "Углекислый газ", "Азот", "Аргон"],
        "answer": "Азот"
        },
        {
        "question": "Какой океан самый большой по площади?",
        "options": ["Атлантический", "Индийский", "Северный Ледовитый", "Тихий"],
        "answer": "Тихий"
        },
        {
        "question": "Какая страна имеет самое большое население в мире?",
        "options": ["Индия", "США", "Китай", "Индонезия"],
        "answer": "Индия"
        },
        {
        "question": "Как называется самая высокая гора в мире?",
        "options": ["Килиманджаро", "Эверест", "Аконкагуа", "Мак-Кинли"],
        "answer": "Эверест"
        },
        {
        "question": "Кто изобрел телефон?",
        "options": ["Томас Эдисон", "Александр Белл", "Никола Тесла", "Гульельмо Маркони"],
        "answer": "Александр Белл"
        },
        {
        "question": "Какое самое глубокое озеро в мире?",
        "options": ["Виктория", "Байкал", "Танганьика", "Каспийское море"],
        "answer": "Байкал"
        },
        {
        "question": "В каком году человек впервые полетел в космос?",
        "options": ["1957", "1961", "1969", "1975"],
        "answer": "1961"
        },
        {
        "question": "Какой химический элемент обозначается как 'Hg'?",
        "options": ["Серебро", "Золото", "Ртуть", "Германий"],
        "answer": "Ртуть"
        },
        {
        "question": "Какое самое быстрое наземное животное?",
        "options": ["Лев", "Гепард", "Антилопа гну", "Борзая собака"],
        "answer": "Гепард"
        },
        {
        "question": "Сколько цветов в радуге согласно традиционному делению?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
        },
        {
        "question": "Какой мобильный оператор использует логотип в виде пчелы?",
        "options": ["МТС", "Билайн", "МегаФон", "Tele2"],
        "answer": "Билайн"
        },
        {
        "question": "Как называется самая популярная ОС для смартфонов?",
        "options": ["iOS", "Android", "HarmonyOS", "Windows Phone"],
        "answer": "Android"
        }
        ],
        "Литература": [
        {
        "question": "Кто написал 'Войну и мир'?",
        "options": ["Достоевский", "Толстой", "Чехов", "Тургенев"],
        "answer": "Толстой"
        },
        {
        "question": "Кто написал 'Ромео и Джульетту'?",
        "options": ["Чарльз Диккенс", "Уильям Шекспир", "Лев Толстой", "Марк Твен"],
        "answer": "Уильям Шекспир"
        },
        {
        "question": "Кто автор 'Преступления и наказания'?",
        "options": ["Толстой", "Достоевский", "Гоголь", "Тургенев"],
        "answer": "Достоевский"
        },
        {
        "question": "Какой поэт написал 'Я помню чудное мгновенье...'?",
        "options": ["Лермонтов", "Пушкин", "Тютчев", "Некрасов"],
        "answer": "Пушкин"
        },
        {
        "question": "Кто создал Шерлока Холмса?",
        "options": ["Агата Кристи", "Артур Конан Дойл", "Стивен Кинг", "Чарльз Диккенс"],
        "answer": "Артур Конан Дойл"
        },
        {
        "question": "Какое произведение написал Михаил Булгаков?",
        "options": ["Тихий Дон", "Доктор Живаго", "Мастер и Маргарита", "Петр Первый"],
        "answer": "Мастер и Маргарита"
        },
        {
        "question": "Кто автор 'Гарри Поттера'?",
        "options": ["Дж. Р. Р. Толкин", "Дж. К. Роулинг", "Клайв Льюис", "Стивен Кинг"],
        "answer": "Дж. К. Роулинг"
        },
        {
        "question": "Какое произведение принадлежит перу Эрнеста Хемингуэя?",
        "options": ["1984", "Старик и море", "Улисс", "Над пропастью во ржи"],
        "answer": "Старик и море"
        },
        {
        "question": "Кто написал 'Три мушкетера'?",
        "options": ["Виктор Гюго", "Александр Дюма", "Жюль Верн", "Оноре де Бальзак"],
        "answer": "Александр Дюма"
        },
        {
        "question": "Какой русский писатель автор 'Мертвых душ'?",
        "options": ["Толстой", "Достоевский", "Гоголь", "Тургенев"],
        "answer": "Гоголь"
        },
        {
        "question": "Кто написал 'Алису в Стране чудес'?",
        "options": ["Льюис Кэрролл", "Дж. М. Барри", "Редьярд Киплинг", "Алан Милн"],
        "answer": "Льюис Кэрролл"
        },
        {
        "question": "Какое произведение принадлежит Льву Толстому?",
        "options": ["Отцы и дети", "Обломов", "Анна Каренина", "Идиот"],
        "answer": "Анна Каренина"
        },
        {
        "question": "Кто автор 'Фауста'?",
        "options": ["Фридрих Шиллер", "Иоганн Вольфганг Гёте", "Генрих Гейне", "Франц Кафка"],
        "answer": "Иоганн Вольфганг Гёте"
        },
        {
        "question": "Какое произведение написал Антон Чехов?",
        "options": ["Вишневый сад", "На дне", "Отцы и дети", "Дворянское гнездо"],
        "answer": "Вишневый сад"
        },
        {
        "question": "Кто автор 'Властелина колец'?",
        "options": ["Дж. К. Роулинг", "Дж. Р. Р. Толкин", "Клайв Льюис", "Терри Пратчетт"],
        "answer": "Дж. Р. Р. Толкин"
        },
        {
        "question": "Какое произведение принадлежит Джорджу Оруэллу?",
        "options": ["451° по Фаренгейту", "1984", "О дивный новый мир", "Мы"],
        "answer": "1984"
        },
        {
        "question": "Кто написал 'Дон Кихота'?",
        "options": ["Мигель де Сервантес", "Федерико Гарсиа Лорка", "Пабло Неруда", "Габриэль Гарсиа Маркес"],
        "answer": "Мигель де Сервантес"
        },
        {
        "question": "Какое произведение принадлежит Федору Достоевскому?",
        "options": ["Война и мир", "Идиот", "Отцы и дети", "Обломов"],
        "answer": "Идиот"
        },
        {
        "question": "Кто автор 'Маленького принца'?",
        "options": ["Антуан де Сент-Экзюпери", "Жюль Верн", "Виктор Гюго", "Гюстав Флобер"],
        "answer": "Антуан де Сент-Экзюпери"
        },
        {
        "question": "Какое произведение написал Николай Гоголь?",
        "options": ["Ревизор", "Горе от ума", "Гроза", "Бесы"],
        "answer": "Ревизор"
        }
        ],
        "Наука": [
        {
        "question": "Сколько элементов в периодической таблице?",
        "options": ["108", "118", "128", "138"],
        "answer": "118"
        },
        {
        "question": "Какой химический элемент обозначается как 'Au'?",
        "options": ["Серебро", "Железо", "Золото", "Алюминий"],
        "answer": "Золото"
        },
        {
        "question": "Какой газ преобладает в составе атмосферы Земли?",
        "options": ["Кислород", "Углекислый газ", "Азот", "Аргон"],
        "answer": "Азот"
        },
        {
        "question": "Сколько хромосом у здорового человека?",
        "options": ["23", "46", "64", "32"],
        "answer": "46"
        },
        {
        "question": "Какая самая высокая гора в Солнечной системе?",
        "options": ["Эверест", "Олимп (Марс)", "Килиманджаро", "Мауна-Кеа"],
        "answer": "Олимп (Марс)"
        },
        {
        "question": "Как называется самая большая кость в человеческом теле?",
        "options": ["Позвоночник", "Бедренная", "Череп", "Лопатка"],
        "answer": "Бедренная"
        },
        {
        "question": "Какое самое быстрое наземное животное?",
        "options": ["Лев", "Гепард", "Антилопа", "Леопард"],
        "answer": "Гепард"
        },
        {
        "question": "Какой ученый сформулировал теорию относительности?",
        "options": ["Исаак Ньютон", "Альберт Эйнштейн", "Никола Тесла", "Стивен Хокинг"],
        "answer": "Альберт Эйнштейн"
        },
        {
        "question": "Какой орган человеческого тела самый большой?",
        "options": ["Печень", "Мозг", "Кожа", "Сердце"],
        "answer": "Кожа"
        },
        {
        "question": "Какая планета ближе всего к Солнцу?",
        "options": ["Венера", "Марс", "Меркурий", "Земля"],
        "answer": "Меркурий"
        },
        {
        "question": "Как называется наука о растениях?",
        "options": ["Зоология", "Ботаника", "Биология", "Экология"],
        "answer": "Ботаника"
        },
        {
        "question": "Какой элемент самый легкий?",
        "options": ["Гелий", "Водород", "Литий", "Кислород"],
        "answer": "Водород"
        },
        {
        "question": "Сколько костей в теле взрослого человека?",
        "options": ["156", "206", "256", "306"],
        "answer": "206"
        },
        {
        "question": "Как называется процесс фотосинтеза у растений?",
        "options": ["Поглощение кислорода", "Выделение углекислого газа",
        "Преобразование света в энергию", "Испарение воды"],
        "answer": "Преобразование света в энергию"
        },
        {
        "question": "Какой газ растения поглощают днем?",
        "options": ["Кислород", "Углекислый газ", "Азот", "Водород"],
        "answer": "Углекислый газ"
        },
        {
        "question": "Какая самая твердая природная субстанция в организме человека?",
        "options": ["Кость", "Зубная эмаль", "Ноготь", "Хрящ"],
        "answer": "Зубная эмаль"
        },
        {
        "question": "Какой ученый открыл закон всемирного тяготения?",
        "options": ["Галилео Галилей", "Исаак Ньютон", "Николай Коперник", "Альберт Эйнштейн"],
        "answer": "Исаак Ньютон"
        },
        {
        "question": "Как называется самая маленькая частица вещества?",
        "options": ["Молекула", "Атом", "Электрон", "Кварк"],
        "answer": "Атом"
        },
        {
        "question": "Какой элемент является основой органической химии?",
        "options": ["Кислород", "Углерод", "Водород", "Азот"],
        "answer": "Углерод"
        },
        {
        "question": "Какой витамин вырабатывается в коже под действием солнечного света?",
        "options": ["Витамин A", "Витамин C", "Витамин D", "Витамин E"],
        "answer": "Витамин D"
        }
        ],
        "IT": [
        {
        "question": "Какой язык программирования самый популярный в 2023 году?",
        "options": ["Python", "JavaScript", "Java", "C++"],
        "answer": "Python"
        },
        {
        "question": "Что означает аббревиатура 'HTTP'?",
        "options": ["HyperText Transfer Protocol",
        "High Transfer Text Protocol",
        "Hyper Transfer Text Protocol",
        "HighText Transfer Protocol"],
        "answer": "HyperText Transfer Protocol"
        },
        {
        "question": "Какой оператор в Python используется для целочисленного деления?",
        "options": ["/", "//", "%", ""],
        "answer": "//"
        },
        {
        "question": "Что выведет print(2 + 2 * 2) в Python?",
        "options": ["6", "8", "4", "Ошибку"],
        "answer": "6"
        },
        {
        "question": "Как называется стандартная библиотека Python для работы с регулярными выражениями?",
        "options": ["regex", "re", "pyregex", "pattern"],
        "answer": "re"
        },
        {
        "question": "Какой тип данных в Python является неизменяемым?",
        "options": ["Список", "Словарь", "Множество", "Кортеж"],
        "answer": "Кортеж"
        },
        {
        "question": "Кто создал язык Python?",
        "options": ["Билл Гейтс", "Гвидо ван Россум", "Линус Торвальдс", "Деннис Ритчи"],
        "answer": "Гвидо ван Россум"
        },
        {
        "question": "Какой язык программирования используется для стилей веб-страниц?",
        "options": ["HTML", "CSS", "JavaScript", "PHP"],
        "answer": "CSS"
        },
        {
        "question": "Что означает аббревиатура 'HTML'?",
        "options": ["HyperText Markup Language",
        "HighText Machine Language",
        "HyperText Machine Language",
        "HighText Markup Language"],
        "answer": "HyperText Markup Language"
        },
        {
        "question": "Какой язык программирования разработала компания Microsoft?",
        "options": ["Java", "C#", "Python", "Ruby"],
        "answer": "C#"
        },
        {
        "question": "Какой метод Python используется для добавления элемента в список?",
        "options": [".add()", ".append()", ".insert()", ".push()"],
        "answer": ".append()"
        },
        {
        "question": "Что делает метод .strip() в Python?",
        "options": ["Разделяет строку", "Удаляет пробелы по краям", "Переводит в верхний регистр", "Заменяет подстроку"],
        "answer": "Удаляет пробелы по краям"
        },
        {
        "question": "Какой оператор используется для возведения в степень в Python?",
        "options": ["^", "", "*", "^^"],
        "answer": "**"
        },
        {
        "question": "Что выведет print(type(3.14)) в Python?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'decimal'>", "<class 'number'>"],
        "answer": "<class 'float'>"
        },
        {
        "question": "Как называется оператор ... if ... else ... в Python?",
        "options": ["Условный оператор", "Тернарный оператор", "Логический оператор", "Оператор выбора"],
        "answer": "Тернарный оператор"
        },
        {
        "question": "Какой язык используется для создания интерактивности на веб-страницах?",
        "options": ["HTML", "CSS", "JavaScript", "PHP"],
        "answer": "JavaScript"
        },
        {
        "question": "Какой язык программирования разработал Брендан Эйх?",
        "options": ["Python", "Java", "JavaScript", "Ruby"],
        "answer": "JavaScript"
        },
        {
        "question": "Что означает аббревиатура 'SQL'?",
        "options": ["Structured Query Language",
        "Simple Query Language",
        "Standard Query Language",
        "System Query Language"],
        "answer": "Structured Query Language"
        },
        {
        "question": "Какой язык программирования используется для разработки приложений под Android?",
        "options": ["Swift", "Kotlin", "C#", "Ruby"],
        "answer": "Kotlin"
        },
        {
        "question": "Какой язык программирования разработала Apple?",
        "options": ["Kotlin", "Swift", "Dart", "Go"],
        "answer": "Swift"
        }
        ]
    }

    def select_category():
        print("\nДоступные категории вопросов:")
        categories = list(questions.keys())
        for i, category in enumerate(categories, 1):
           print(f"{i}. {category} ({len(questions[category])} вопросов)")
        while True:
                try:    
                    choice = int(input("\nВыберите номер категории: "))
                    if 1 <= choice <= len(categories):
                        return categories[choice-1]
                    print(f"Пожалуйста, введите число от 1 до {len(categories)}")
                except ValueError:
                    print("Пожалуйста, введите число!")

    def run_quiz():
        print("\033[1;32m" + '                🚀 Викторина 🚀' + "\033[0m")
        
        # Выбор категории
        category = select_category()
        category_questions = questions[category].copy()
        random.shuffle(category_questions)
        
        print("\033[1;32m" + f'Ответьте на {len(category_questions)} вопросов по категории "{category}"' + "\033[0m")
        print("\033[1;32m" + 'У вас 2 минуты' + "\033[0m")
        print('\033[1m'+ '\n')
        
        score = 0
        
        for i, q in enumerate(category_questions, 1):
            options = q["options"].copy()
            correct_answer = q["answer"]
            random.shuffle(options)
            
            correct_index = options.index(correct_answer) + 1
            
            print(f'\nВопрос №{i}. {q["question"]}')
            for idx, option in enumerate(options, 1):
                print(f'{idx}. {option}')
            
            while True:
                inp = input('Введите номер вашего ответа (1-4): ')
                if inp.isdigit() and 1 <= int(inp) <= 4:
                    break
                print("Ошибка! Пожалуйста, введите число от 1 до 4.")
            
            if options[int(inp)-1] == correct_answer:
                print("✅ Правильно! +1 балл")
                score += 1
            else:
                print(f"❌ Неверно! Правильный ответ: {correct_index}. {correct_answer}")
            
            time.sleep(1)
        print('\n' + '='*40 + '\n' + f'Ваш результат {score} из {len(category_questions)}\n' + '='*40)
        if score == len(category_questions):
            print("Идеально! Вы настоящий эрудит! 🎯")
        elif score >= len(category_questions) * 0.7:
            print("Отличный результат! 👍")
        elif score >= len(category_questions) * 0.5:
            print("Хороший результат! 😊")
        else:
            print("Попробуйте еще раз! 💪")
        print('='*40)
        while True:
            p = input('Хотите сыграть ещё раз? (да/нет): ').lower()
            if p in ('да', 'нет'):
                break
            print('Пожалуйста, введите "да" или "нет"')
        while True:
            if p == 'да':
                quiz()
            else:
                return
    # Основной цикл программы
    while True:
        if not run_quiz():
            break

def game_visel():
    hangman_stages = [
        """
        +---+
        |   |
        |
        |
        |
        |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |
        |
        |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |   |
        |
        |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |  /|
        |
        |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |  /|\
        |
        |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |  /|\
        |  / \
        |
        ======
        """
    ]

        # Список слов для угадывания
    words = (
            'солнце',
            'мармелад',
            'ледокол',
            'аттракцион',
            'дрессировка',
            'ошейник',
            'карамель',
            'водолаз',
            'защита',
            'батарея',
            'решётка',
            'квартира',
            'дельфин',
            'туча',
            'вход',
            'пешеход',
            'перекрёсток',
            'башня',
            'стрелка',
            'градусник'
    )
        
    lives = 6
    secret_word = random.choice(words)
    len_s = len(secret_word)
    s = '_' * len_s
        
    print('Здравствуйте! Это игра "Виселица", где вам нужно угадать слово, называя буквы.')
    print(f'Загаданное слово: {s}')
    print('У вас 6 попыток')
    while lives > 0:
            put = input('Напишите строчную букву: ').lower()
            
            if len(put) != 1 or not put.isalpha():
                print('Пожалуйста, введите одну строчную букву!')
                continue
                
            for i in range(len_s):
                if secret_word[i] == put:
                    s = s[:i] + put + s[i+1:]
            
            if put not in secret_word:
                lives -= 1
                print(f'Такой буквы нет в слове.')
            
            print(f'Текущее слово: {s}\n')
            
            if s == secret_word:
                print(f'Поздравляем! Вы угадали слово: {secret_word}!')
                print('Хотите сыграть ещё раз? (Да/Нет)')
                ans = input('Напишите Да или Нет: ')
                if ans.lower() == 'да':
                    game_visel()
                else:
                    break
            else:
                if lives == 5:
                    print(hangman_stages[0])
                elif lives == 4:
                    print(hangman_stages[1])
                elif lives == 3:
                    print(hangman_stages[2])
                elif lives == 2:
                    print(hangman_stages[3])
                elif lives == 1:
                    print(hangman_stages[4])
                elif lives == 0:
                    print(hangman_stages[5])
                
                print(f'Осталось попыток: {lives}')
            if lives <= 0:
                print(f'Игра окончена! Загаданное слово было: {secret_word}')
                print('Хотите сыграть ещё раз? (Да/Нет)')
                ans = input('Напишите Да или Нет: ')
                if ans.lower() == 'да':
                    game_visel()
                elif ans.lower() == 'нет':
                    return
                else:
                    print('Пожалуйста, введите "да" или "нет".')

def rand_game():
    cc = random.randint(1, 100)
    print('\033[1m' + 'Здравствуйте! Это игра "Угадай число".')
    print('Я загадываю случайное число от 1 до 100. Вы должны угадать число.')
    print('Я буду подсказывать "больше" или "меньше".')

    while True: 
            try:
                put = int(input('Введите число от 1 до 100: '))
                if put < 1 or put > 100:  
                    print("Число должно быть от 1 до 100!")
                    continue
            except ValueError:
                print('Пожалуйста, введите число!')
                continue  

            if put < cc:
                print("Загаданное число больше.")
            elif put > cc:
                print("Загаданное число меньше.")
            else:
                print("Поздравляю, вы угадали число!")
                break  
                                                        
    while True:  
            k = input('Хотите сыграть ещё раз? (да/нет): ').lower()
            if k == 'да':
                print('\n'*3)
                rand_game()  
            elif k == 'нет':
                return 
            else:
                print('Пожалуйста, введите "да" или "нет".')

def knb():
    sp = ['камень','ножницы','бумага']
    ai = random.choice(sp)
    print('\033[1m'+'Здраствуйте! Это игра камень,ножницы,бумага. ')
    print('Как играть: к = камень, н = ножницы, б = бумага')
    try:
        while True:
            i = str(input('Введите к/н/б:')).lower().strip()
            if i not in 'кнб':
              print('Пожалуйста введите к, н или б')
              continue
            elif len(i) != 1:
                print('Пожалуйста введите к, н или б')
                continue
            elif i == '':
               print('Пожалуйста введите к, н или б')
               continue
            else:
                break
    except ValueError:
        print('Пожалуйста введите к, н или б')
        
    if ai == 'камень':
            ai = 'к'
    elif ai == 'ножницы':
            ai = 'н'
    elif ai == 'бумага':
            ai = 'б'

    if i == ai :
            print('Ничья!')
    elif i == 'к' and ai == 'н':
            print('Вы выиграли!')
    elif i == 'н' and ai == 'б':
            print('Вы выиграли!')
    elif i == 'б' and ai == 'к':
            print('Вы выиграли!')
    else:
            print('Вы проиграли!')

    print('Хотите сыграть ещё раз? (да/нет)')
    while True:
            ans = input('Напишите Да или Нет: ')
            if ans.lower() == 'да':
                print('\n'+'НОВАЯ ИГРА'+'\n')
                knb()
            elif ans.lower() == 'нет':
                return
            else:
                print('Пожалуйста, введите "да" или "нет".')

def tictactoe():
    ALL_SPACES = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    X, O, BLANK = 'X', 'O', ' '

    class TicTacToeBoard:
        def __init__(self):
            """Create a new, blank tic-tac-toe board."""
            self._spaces = {}
            for space in ALL_SPACES:
                self._spaces[space] = BLANK

        def drawBoard(self):
            """Display a text-representation of the board."""
            print(f'''
    {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
    -+-+-
    {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
    -+-+-
    {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9\n''')

        def isWinner(self, mark):
            """Return True if mark is a winner on this TicTacToeBoard."""
            bo, m = self._spaces, mark  
            return ((bo['1'] == m and bo['2'] == m and bo['3'] == m) or
                    (bo['4'] == m and bo['5'] == m and bo['6'] == m) or
                    (bo['7'] == m and bo['8'] == m and bo['9'] == m) or
                    (bo['1'] == m and bo['4'] == m and bo['7'] == m) or
                    (bo['2'] == m and bo['5'] == m and bo['8'] == m) or
                    (bo['3'] == m and bo['6'] == m and bo['9'] == m) or
                    (bo['3'] == m and bo['5'] == m and bo['7'] == m) or
                    (bo['1'] == m and bo['5'] == m and bo['9'] == m))

        def getPlayerMove(self, player):
            """Let the player type in their move."""
            space = None
            while space not in ALL_SPACES or not self._spaces[space] == BLANK:
                print(f'Как ходит {player}? (1-9)\n')
                space = input().upper()
            return space

        def isBoardFull(self):
            """Return True if every space on the board has been taken."""
            for space in ALL_SPACES:
                if self._spaces[space] == BLANK:
                    return False
            return True

        def setSpace(self, space, mark):
            """Sets the space on the board to mark."""
            self._spaces[space] = mark

    def main():
        """Runs a game of Tic-Tac-Toe."""
        print('Добро пожаловать в крестики-нолики!')
        gameBoard = TicTacToeBoard()
        turn, nextTurn = X, O

        while True:
            gameBoard.drawBoard()
            move = gameBoard.getPlayerMove(turn)
            gameBoard.setSpace(move, turn)

            if gameBoard.isWinner(turn):
                gameBoard.drawBoard()
                print(turn + ' выграл игру!\n')
                break
            elif gameBoard.isBoardFull():
                gameBoard.drawBoard()
                print('Игра заканчивается вничью!')
                break

            turn, nextTurn = nextTurn, turn
    main()

jokes = [
# Программистские
"Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
"Сколько программистов нужно, чтобы вкрутить лампочку? Ни одного, это hardware проблема!",
"Программист звонит в техподдержку: 'У меня проблема...' 'Решено', - отвечают ему.",

# Про студентов
"Студент на экзамене: 'Я знал ответ, но забыл'. Преподаватель: 'Жаль, что вы не забыли прийти'",
"Лекция в университете. Профессор: 'Это должно быть очевидно...' Студент встаёт и выходит: 'Тогда я вам не нужен'",
"Студент спрашивает у профессора: 'А можно я сдам работу завтра?' Профессор: 'Конечно, но я не обещаю, что буду завтра жив'",

# Про животных
"Почему курица перешла дорогу? Чтобы доказать опоссуму, что это можно сделать!",
"Два хомяка в колесе. Один говорит: 'Ну что, бежим?' Второй: 'Нет, я в прошлый раз так набегался, что до сих пор кручусь'",
"Кот написал на ковёр. Хозяин тычет его носом: 'Будешь ещё писать?' Кот думает: 'Ну теперь-то точно буду...'",

# Про работу
"Начальник сотруднику: 'Вы уволены!' 'Но я же только вчера устроился!' 'Да, и уже опоздали сегодня!'",
"Работник спрашивает начальника: 'Можно мне зарплату?' 'Можно, но только не всю сразу'",
"Объявление: 'Требуется человек, который ничего не делает. Зарплата — как за полный рабочий день'",

# Про семью
"Муж жене: 'Дорогая, я починил розетку!' 'Как ты это сделал без инструментов?' 'Я просто вынул вилку из другой розетки'",
"Ребёнок спрашивает отца: 'Пап, а почему у тебя так мало волос?' 'Потому что я много думал, сынок' 'А почему тогда у дедушки совсем нет волос?'",
"Жена мужу: 'Я похожа на цаплю?' 'Нет' 'А я стою на одной ноге уже час, пока ты рыбачишь!'",

# Детские
"Почему карандаш плохо писал? Потому что он был тупой!",
"Мама говорит сыну: 'Если будешь есть морковку, будешь видеть в темноте!' 'Мама, я и так вижу в темноте!' 'Как?' 'Я же не ем морковку!'",
"Учитель: 'Кто может назвать пять диких животных?' Вовочка: 'Тигр, три тигра и ещё один тигр!'",

# Медицинские
"Врач пациенту: 'У вас редкое заболевание' 'Доктор, это хорошо?' 'Нет, это плохо. Просто я редко ошибаюсь'",
"Пациент: 'Доктор, я не могу вспомнить, что мне нужно делать' Доктор: 'Забыли?' 'Да!' 'Тогда приходите завтра'",
"Доктор: 'Вам нужно бросить курить, пить и есть жирное' Пациент: 'И сколько я тогда проживу?' 'Не знаю, но время будет тянуться очень медленно'",

# Про технику
"Почему компьютер плохо спал? Потому что у него была Windows!",
"Телефон говорит другому телефону: 'Привет!' 'Извини, я на проводе'",
"Жена мужу: 'Почему ты купил такой дорогой телефон?' 'Он умный!' 'Тогда пусть сам зарабатывает!'",

# Исторические
"Иван Грозный спрашивает у придворного: 'Почему ты дрожишь?' 'Ваше Величество, я не дрожу, я танцую!'",
"На раскопках нашли древний компьютер. Археологи думают — то ли калькулятор, то ли каменный ноутбук...",
"Первобытный человек изобрёл колесо. Другой первобытный человек: 'А теперь приделай к нему ещё три и получится машина!'",

# Про деньги
"Банкир спрашивает клиента: 'Вы хотите взять кредит?' 'Нет, я хочу деньги!'",
"Муж жене: 'Дорогая, я нашёл способ экономить!' 'Какой?' 'Мы будем меньше тратить!'",
"Объявление: 'Даю деньги в долг под 0%. Первому, кто поверит'",

# Шуточные диалоги
"- Ты где был? - Да так, нигде... - А где это?",
"- Почему ты не отвечаешь на мои сообщения? - Я их не получал! - Как не получал? Я же вижу, что ты прочитал! - Ну вот, теперь получил...",
"- Ты помнишь, как мы познакомились? - Нет - И я не помню. Кажется, нас познакомили...",

# Про спорт
"Футболист после матча: 'Я бежал так быстро, что даже забыл мяч!'",
"Тренер команде: 'Вы играете как стадо баранов!' Капитан: 'Тренер, это оскорбление!' 'Для баранов — да!'",
"Боксёр перед боем: 'Я не боюсь соперника!' Тренер: 'Тогда зачем ты надел мои шорты?'",

# Про науку
"Учёные изобрели новую элементарную частицу — лень. Но изучать её пока не хотят...",
"Физик говорит другу: 'Я изобрёл машину времени!' 'И что?' 'Да ничего, просто похвастаться'",
"Математик тонет в реке и кричит: 'Помогите! Я не умею плавать!' Прохожий: 'Так встаньте на дно!' 'А оно есть?'",

# Про путешествия
"Турист спрашивает у местного: 'Как пройти к морю?' 'Миллион лет прямо, потом направо'",
"Почему путешественник взял с собой лестницу? Чтобы подняться на Эверест ступенька за ступенькой!",
"Таможенник спрашивает туриста: 'У вас есть что-то ценное?' 'Да, моя жена!' 'Хм... Можете проходить'",

# Про еду
"Почему хлеб грустный? Потому что его все режут!",
"Шеф-повар ученику: 'Ты пересолил суп!' 'Но я ещё не солил!' 'Вот именно!'",
"Муж жене: 'Что на ужин?' 'Сюрприз!' 'Опять яичница...'",

# Про армию
"Солдат докладывает командиру: 'Товарищ генерал, противник сдаётся!' 'Отлично! А кто это такой противник?'",
"Рекрута спрашивают: 'Почему вы хотите служить в армии?' 'Чтобы научиться отдавать честь!' 'Кому?' 'Всем подряд!'",
"Сержант новобранцу: 'Вы что, совсем дурак?' 'Нет, я только по средам!'",

# Про школу
"Учитель: 'Кто может назвать самое быстрое существо?' Вовочка: 'Мысль! Она за секунду вокруг света!' 'А пример?' 'Я только что подумал об каникулах!'",
"Директор школы учителю: 'Почему у вас в классе так шумно?' 'Это не шум, это коллективное обсуждение!'",
"Ученик спрашивает учителя: 'А правда, что раньше люди жили до 300 лет?' 'Нет, это миф' 'Тогда зачем вы мне поставили 300 лет домашней работы?'",

# Про транспорт
"Почему поезд опоздал? Потому что его рельсы были в другом часовом поясе!",
"Пассажир водителю автобуса: 'Вы проехали мою остановку!' 'Не волнуйтесь, следующая через 500 метров!' 'Но я же пешком иду!'",
"ГАИшник останавливает машину: 'Вы превысили скорость!' 'Но я только начал движение!' 'Вот именно!'",

# Про искусство
"Художник показывает картину: 'Это абстракционизм!' 'А где рамка?' 'Это и есть абстракция!'",
"Музыкант жалуется: 'Моя скрипка не играет!' 'Может, её надо включить?'",
"Актёр на прослушивании: 'Я могу сыграть любую роль!' 'Тогда сыграйте зрителя!'"
]  

# Инициализация аудио системы
pygame.mixer.init()
TEMP_DIR = tempfile.gettempdir()
command_queue = queue.Queue()

# Настройки голосового помощника
class Config:
    WAKE_WORDS = ['кеша', 'кеш', 'гоша', 'кэш','валера','чебурек']
    SENSITIVITY = 0.5
    ENERGY_THRESHOLD = 1000
    PAUSE_THRESHOLD = 2
    DYNAMIC_ENERGY = True
    TIMEOUT = 1.5
    PHRASE_LIMIT = 3

# Инициализация управления громкостью
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))
    VOLUME_CONTROL_ENABLED = True
except:
    VOLUME_CONTROL_ENABLED = False
    print("Не удалось инициализировать управление громкостью")

class AudioManager:
    """Управление воспроизведением аудио"""
    def __init__(self):
        self._init_mixer()
        self.playback_thread = None

    def _init_mixer(self):
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        except:
            print("Ошибка инициализации аудио микшера")

    def say(self, text):
        """Асинхронное воспроизведение текста"""
        if not text.strip():
            return

        try:
            filename = os.path.join(TEMP_DIR, f"voice_{int(time.time()*1000)}.mp3")
            tts = gTTS(text=text, lang='ru', slow=False)
            tts.save(filename)

            if self.playback_thread and self.playback_thread.is_alive():
                pygame.mixer.music.stop()
                self.playback_thread.join(timeout=0.1)

            try:
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
            except:
                self._init_mixer()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

            self.playback_thread = threading.Thread(
                target=self._cleanup_audio,
                args=(filename,),
                daemon=True
            )
            self.playback_thread.start()

        except Exception as e:
            print(f"Ошибка воспроизведения: {e}")

    def _cleanup_audio(self, filename):
        """Очистка аудиофайлов после воспроизведения"""
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass

audio_manager = AudioManager()

class VoiceRecognizer:
    """Распознавание голосовых команд"""
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = Config.ENERGY_THRESHOLD
        self.recognizer.pause_threshold = Config.PAUSE_THRESHOLD
        self.recognizer.dynamic_energy_threshold = Config.DYNAMIC_ENERGY

    def listen(self, timeout=1.5):
        """Слушаем микрофон с таймаутом"""
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout,
                    phrase_time_limit=Config.PHRASE_LIMIT
                )
                return self.recognizer.recognize_google(audio, language='ru-RU').lower()
            except (sr.WaitTimeoutError, sr.UnknownValueError):
                return ""
            except Exception as e:
                print(f"Ошибка распознавания: {e}")
                return ""

def re(text):
    """Быстрый вывод и озвучивание текста"""
    print(text)
    audio_manager.say(text)

def listen_for_wake_word():
    """Прослушивание ключевого слова для активации"""
    recognizer = VoiceRecognizer()
    re("Готов к работе, жду ключевое слово...")
    print("кеша, кеш, гоша, кэш, валера, чебурек")
    while True:
        try:
            text = recognizer.listen(timeout=Config.TIMEOUT)
            if any(word in text for word in Config.WAKE_WORDS):
                command_queue.put("wake_word_detected")
        except Exception as e:
            print(f"Ошибка в listen_for_wake_word: {e}")
            time.sleep(0.1)

def recognize_command():
    """Распознавание команды после активации"""
    recognizer = VoiceRecognizer()
    re("Слушаю...")
    return recognizer.listen()

def process_commands():
    """Обработка команд из очереди"""
    while True:
        command = command_queue.get()
        if command == "wake_word_detected":
            command_text = recognize_command()
            if command_text:
                threading.Thread(
                    target=handle_command,
                    args=(command_text,),
                    daemon=True
                ).start()
            else:
                re("Я вас не расслышал, повторите пожалуйста")

def set_system_volume(level):
    """Установка громкости системы"""
    if not VOLUME_CONTROL_ENABLED:
        return False
    try:
        volume_control.SetMasterVolumeLevelScalar(level, None)
        return True
    except:
        return False

def get_system_volume():
    """Получение текущей громкости"""
    if not VOLUME_CONTROL_ENABLED:
        return 0.5
    try:
        return volume_control.GetMasterVolumeLevelScalar()
    except:
        return 0.5

def change_volume(direction):
    """Изменение громкости"""
    current = get_system_volume()
    if direction == 'up':
        new_vol = min(1.0, current + 0.1)
    elif direction == 'down':
        new_vol = max(0.0, current - 0.1)
    else:
        return current

    if set_system_volume(new_vol):
        return new_vol
    return current

def handle_command(text):
    """Обработка конкретной команды"""
    if not text:
        return

    print(f"Распознанная команда: {text}")
    text = text.lower().strip()
    try:
        if any(word in text for word in ['пока', 'выход', 'стоп']):
            re('До свидания!')
            os._exit(0)

        elif 'найди в ютуби' in text:
            quertty = text.replace("найди в ютуби", "").strip()
            if quertty:
                search_and_open_youtube(quertty)
                re('Вот что я нашёл')
            else:
                re('Что именно вам найти?')

        elif 'переведи на' in text:
                if 'английский' in text:
                    m = text.replace("переведи на английский", "").strip()
                    while True:
                        try:
                            webbrowser.open(f'https://translate.yandex.ru/?from=tableau_yabro&source_lang=ru&target_lang=en&text={m}')
                            time.sleep(2)
                            for i in range(13):
                                time.sleep(0.0000001)
                                keyboard.send('Tab')
                            re(f'{m} на английском')
                            time.sleep(2)
                            keyboard.send('alt+ctrl+V')
                            break
                        except:
                            keyboard.send('alt+Shift')
                            keyboard.send('alt+ctrl+V')
                            break

                elif 'русский' in text:
                    m = text.replace("переведи на русский", "").strip()
                    while True:
                        try:
                            webbrowser.open(f'https://translate.yandex.ru/?from=tableau_yabro&source_lang=en&target_lang=ru&text={m}')
                            time.sleep(2)
                            for i in range(13):
                                time.sleep(0.0000001)
                                keyboard.send('Tab')
                            re(f'{m} на русском')
                            time.sleep(2)
                            keyboard.send('alt+ctrl+V')
                            break
                        except:
                            keyboard.send('alt+Shift')
                            keyboard.send('alt+ctrl+V')
                            break

        elif 'youtube' in text:
            webbrowser.open('https://www.youtube.com/')
            re('Открываю YouTube')
        
        elif 'камень ножницы бумага' in text:
            re('Запускаю игру камень ножницы бумага\n')
            knb()

        elif 'виселиц' in text:
            re('Запускаю игру виселица\n')
            game_visel()

        elif 'викторин' in text:
            re('Запускаю игру викторина\n')
            quiz()

        elif 'крестики-нолики' in text:
            re('Запускаю игру крестики нолики\n')
            tictactoe()

        elif 'угадай число' in text:
            re('Запускаю игру угадай число\n')
            rand_game()

        elif any(word in text for word in ['дипси', 'deep', 'deepseek']):
            re('Открываю нейросеть дипсик')
            webbrowser.open('https://chat.deepseek.com/a/chat/s/5e62a9fe-9717-452d-9a82-89c2ca2dd30b')

        elif 'переводчик' in text:
            re('Открываю переводчик')
            webbrowser.open('https://translate.yandex.ru/?111=')

        elif 'игры' in text:
            re('Открываю яндекс игры')
            webbrowser.open('https://yandex.ru/games/')

        elif 'как дела' in text:
           re('Всё отлично!Будет ещё лучше если я смогу вам помочь')

        elif 'молодец' in text:
            re('Спасибо!Всегда к вашим услугам')

        elif 'привет' in text:
            re('Привет! Чем могу помочь?')

        elif 'найди' in text:
            querty = text.replace("найди", "").strip()
            if querty:
                webbrowser.open_new_tab(f'https://yandex.ru/search/?text={querty}')
                re(f'Ищу {querty}')
            else:
                re('Что именно вам найти?')

        elif 'погода' in text:
            webbrowser.open_new_tab('https://yandex.ru/pogoda/')
            re('Открываю прогноз погоды')

        elif 'открой настройки' in text:
            keyboard.send('Win + I')
            re('Есть')

        # Для тех у кого умный дом

        elif 'включи свет' in text:
            webbrowser.open('https://alice.yandex.ru?')
            time.sleep(2)
            keyboard.write('Включи светильник')
            keyboard.send('Enter')
            re('Ок')
        
        elif 'выключи свет' in text:
            webbrowser.open('https://alice.yandex.ru?')
            keyboard.write('Выключи свет')
            keyboard.send('Enter')
            re('Ок')

        elif 'поставь таймер на' in text:
            w = text.replace("поставь таймер на", "").strip()
            w = w.replace("минуту", "").strip()
            w = w.replace("минут", "").strip()
            w = w.replace("ы", "").strip()
            if w:
                path = meneger.search_file_path('Таймер.py')
                meneger.open_file(path)
                time.sleep(2)
                keyboard.write(w)
                keyboard.send('Enter') 
                re('Таймер успешно запущен') 
            else:
                re('Уточните на сколько поставить таймер')

        elif 'музыка' in text:
            q = text.replace("музыка", "").strip()
            if q:
                webbrowser.open(f'https://rus.hitmotop.com/search?q={q}')
                time.sleep(1)
                keyboard.send('Tab')
                keyboard.send('space')
                re('Взгляните, что я нашёл')
            else:
                webbrowser.open('https://rus.hitmotop.com')
                re('Открываю')

        elif 'открой проводник' in text:
            keyboard.send('Win + E')
            re('Есть')

        elif 'дальше' in text:
            keyboard.send('shift + N')
            re('Есть')

        elif 'пробел' in text:
            keyboard.send('space')
            re('Есть')

        elif 'полный экран' in text:
            keyboard.send('F')
            re('Есть')

        elif 'время' in text:
            current_time = datetime.now().strftime("%H:%M")
            re(f'Сейчас {current_time}')

        elif 'времени' in text:
            current_time = datetime.now().strftime("%H:%M")
            re(f'Сейчас {current_time}')    

        elif 'состояние' in text or 'батарея' in text:
            battery = psutil.sensors_battery()
            if battery.power_plugged:
                status = "заряжается"
            else:
                status = "работает от батареи"
            re(f'Батарея {status}, уровень заряда {battery.percent}%')

        elif any(word in text for word in ['громче', 'увеличь громкость']):
            new_vol = change_volume('up')
            re(f'Громкость увеличена до {int(new_vol * 100)}%')

        elif any(word in text for word in ['тише', 'уменьши громкость']):
            new_vol = change_volume('down')
            re(f'Громкость уменьшена до {int(new_vol * 100)}%')

        elif 'громкость' in text:
            try:
                vol_level = int(''.join(filter(str.isdigit, text)))
                vol_level = max(0, min(100, vol_level))
                if set_system_volume(vol_level / 100):
                    re(f'Установлена громкость {vol_level}%')
            except:
                re('Скажите, например, "поставь громкость 50"')

        elif 'открой' in text:
            app = text.replace("открой", "").strip()
            if app:
                try:
                    AppOpener.open(app,True)
                    re(f'Открываю {app}')
                except:
                    re(f'Не удалось открыть {app}')
            else:
                re('Какое приложение открыть?')

        elif 'анекдот' in text:
            re(random.choice(jokes))

        elif 'закрой' in text:
            app = text.replace("закрой", "").strip()
            if app:
                try:
                    AppOpener.close(app,True)
                    re(f'Закрываю {app}')
                except:
                    re(f'Не удалось закрыть {app}')
            else:
                re('Какое приложение закрыть?')

        elif 'выключи компьютер' in text:
            re('Выключаю компьютер через 10 секунд')
            os.system("shutdown /s /t 10")

        else:
            re('Не понял команду. Попробуйте еще раз.')

    except Exception as e:
        re('Произошла ошибка при обработке команды')
        print(f"Ошибка: {e}")

def main():
    """Основная функция"""
    print("\033[1;32m" + ' 🚀 Голосовой помощник активирован 🚀' + "\033[0m")
    print("Для выхода скажите кеша пока/стоп/выход")
    print("Доступные команды:")

    print("- Привет/Молодец/Как дела")
    print("- Мызыка/Музыка [название]")
    print("- Поставь таймер на [минут]")
    print("- Включи свет/Выключи свет (Для тех у кого есть умный дом алисой)")
    print("- Переведи на английский [слово]")
    print("- Дальше/Пауза")
    print("- Найди в ютубе [запрос]")
    print("- Найди [запрос]")
    print("- Открой/Закрой [приложение] (иногда не работает)-")
    print("- Погода")
    print("- Переводчик")
    print("- Время")
    print("- Состояние батареи")
    print("- Громче/Тише")
    print("- Громкость [громкость от 1 до 100]")
    print("- Выключи компьютер")

    print("Доступные игры:")

    print("Что бы начать игру скажите Кеше название игры")

    print("- Игры - Открывает яндекс игры")
    print("- Виселица - ")
    print("- Крестики-Нолики - ")
    print("- Угадай число - ")
    print("- Викторина - ")
    print("- Камень ножницы бумага - ")
    print("- Угадай число - ")

    # Запуск потоков
    threading.Thread(target=listen_for_wake_word, daemon=True).start()
    threading.Thread(target=process_commands, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        re("Выключаюсь")
        os._exit(0)

if __name__ == "__main__":
    main()