import telebot
import datetime
import sqlite3
import config
from telebot import types

TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)
phy_answers_index = 0
admins = [772501986]
@bot.message_handler(content_types=['text'])


def reaction(message):
    print(message.chat.id)
    global phy_answers_index
    class_matrix = []
    result = []
    con = sqlite3.connect('BotUsers.db')
    cur = con.cursor()
    results = cur.execute("""SELECT * FROM Users""").fetchall()
    for elem in results:
        result.append(elem[0])
    if message.from_user.username not in result:
        query = """INSERT INTO Users(Username, First_name, Last_name, Class) VALUES(?, ?, ?, ?)"""
        data = [message.from_user.username, message.from_user.first_name, message.from_user.last_name, 2]
        cur.execute(query, data)
    else:
        class_matrix_index = 2
    query = """SELECT Class FROM Users WHERE Username = ?"""
    data = [message.from_user.username]
    class_matrix_index = cur.execute(query, data).fetchall()[0][0]
    con.commit()
    con.close()
    day = datetime.date.today().isoweekday()
    if day == 7:
        day = 0
    message.text = message.text.lower()
    lessons_matrix_10b = [
        'Ааэа...понедельничные\n1)Биология 8:30 - 9:10\n2)Алгебра 9:25 - 10:05\n3)Физика 10:20 - 11:00\n4)Физика 11:15 - 11:55\n5)Литература 12:15 - 12:55\n' \
        '6)Геометрия 13:15 - 13:55\nНу, более менее...',
        'Ааэа...вторнечные\n1)Алгебра 8:30 - 9:10\n2)Физра 9:25 - 10:05\n3)Информатика 10:20 - 11:00\n4)Информатика 11:15 - 11:55\n5)Русский язык 12:15 - 12:55\n' \
        '6)Литература 13:15 - 13:55\nНу, более менее...',
        'Ааэа...средичные\n1)Литература 8:30 - 9:10\n2)Химия 9:25 - 10:05\n3)Алгебра 10:20 - 11:00\n4)Алгебра 11:15 - 11:55\n5)История России 12:15 - 12:55\n' \
        '6)Физра 13:15 - 13:55\n7)Английский язык 14:00 - 14:40\nААААААААА СЕМЬ УРОКОВ!!!!!!',
        'Ааэа...четреничные\n1)Физика 8:30 - 9:10\n2)Физика 9:25 - 10:05\n3)География 10:20 - 11:00\n4)Обществознание 11:15 - 11:55\n5)Обществознание 12:15 - 12:55\n' \
        '6)Английский язык 13:15 - 13:55\n7)Техпроект\nААААААА ТУПОЙ ТЕХПРОЕКТ, А ВЫ ДАЖЕ НОУ НЕ ДЕЛАЛИ!!!!!',
        'Ааэа...пятничные\n1)Геометрия 8:30 - 9:10\n2)Геометрия 9:25 - 10:05\n3)Физика 10:20 - 11:00\n4)Физика 11:15 - 11:55\n5)Химия 12:15 - 12:55\n' \
        '6)Всеобщая история 13:15 - 13:55\nНу, более менее...',
        'Ааэа...субботние\n1)ОБЖ  8:30 - 9:10\n2)Английский язык 9:20 - 10:00\n3)Физра 10:15 - 10:55\n4)Литературоведение 11:05 - 11:45\n5)Алгебра 11:55 - 12:35\n' \
        '6)Основы бизнеса 12:50 - 13:30\nНу, более менее...',
        'ТЫ ШО ТУПОЙ, В ВОСКРЕСЕНЬЕ НЕТ УРОКОВ'
        ]
    lessons_matrix_10a_s = [
        'Ааэа...понедельничные\n1)Физика 8:30 - 9:10\n2)Алгебра 9:25 - 10:05\n3)Алгебра 10:20 - 11:00\n4)Литература 11:15 - 11:55\n5)Право 12:15 - 12:55\n' \
        '6)Право 13:15 - 13:55\nНу, более менее...',
        'Ааэа...вторнечные\n1)География 8:30 - 9:10\n2)Обществознание 9:25 - 10:05\n3)Обществознание 10:20 - 11:00\n4)Алгебра 11:15 - 11:55\n5)Английский язык 12:15 - 12:55\n' \
        '6)Физкультура 13:15 - 13:55\nНу, более менее...',
        'Ааэа...средичные\n1)Английский язык 8:30 - 9:10\n2)Литература 9:25 - 10:05\n3)История 10:20 - 11:00\n4)Экономика 11:15 - 11:55\n5)Экономика 12:15 - 12:55\n' \
        '6)ОБЖ 13:15 - 13:55\nНу, более менее...!!!!!!',
        'Ааэа...четреничные\n1)История 8:30 - 9:10\n2)Химия 9:25 - 10:05\n3)Физика 10:20 - 11:00\n4)Русский язык 11:15 - 11:55\n5)Литература 12:15 - 12:55\n' \
        '6)Физкультура 13:15 - 13:55\n7)Английский язык 14:00 - 14:40\nААААААА СЕМЬ УРОКОВ!!!!!',
        'Ааэа...пятничные\n1)Алгебра 8:30 - 9:10\n2)Общесвознание 9:25 - 10:05\n3)Что-то непонятное 10:20 - 11:00\n4)Геометрия 11:15 - 11:55\n5)Информатика 12:15 - 12:55\n' \
        '6)Информатика 13:15 - 13:55\nНу, более менее...',
        'Не алё, но у 10Б:\nАаэа...субботние\n1)ОБЖ  8:30 - 9:10\n2)Английский язык 9:20 - 10:00\n3)Физра 10:15 - 10:55\n4)Литературоведение 11:05 - 11:45\n5)Алгебра 11:55 - 12:35\n' \
        '6)Основы бизнеса 12:50 - 13:30\nНу, более менее...',
        'ТЫ ШО ТУПОЙ, В ВОСКРЕСЕНЬЕ НЕТ УРОКОВ'
    ]
    lessons_matrix_10a_ch = [
        'Ааэа...понедельничные\n1)Физика 8:30 - 9:10\n2)Алгебра 9:25 - 10:05\n3)Алгебра 10:20 - 11:00\n4)Литература 11:15 - 11:55\n5)Биология 12:15 - 12:55\n' \
        '6)Биология 13:15 - 13:55\nНу, более менее...',
        'Ааэа...вторнечные\n1)География 8:30 - 9:10\n2)Физика 9:25 - 10:05\n3)Физика 10:20 - 11:00\n4)Алгебра 11:15 - 11:55\n5)Английский язык 12:15 - 12:55\n' \
        '6)Физкультура 13:15 - 13:55\nНу, более менее...',
        'Ааэа...средичные\n1)Английский язык 8:30 - 9:10\n2)Литература 9:25 - 10:05\n3)История 10:20 - 11:00\n4)Химия 11:15 - 11:55\n5)Химия 12:15 - 12:55\n' \
        '6)ОБЖ 13:15 - 13:55\nНу, более менее...!!!!!!',
        'Ааэа...четреничные\n1)История 8:30 - 9:10\n2)Биология 9:25 - 10:05\n3)Физика 10:20 - 11:00\n4)Русский язык 11:15 - 11:55\n5)Литература 12:15 - 12:55\n' \
        '6)Физкультура 13:15 - 13:55\n7)Английский язык 14:00 - 14:40\nААААААА СЕМЬ УРОКОВ!!!!!',
        'Ааэа...пятничные\n1)Алгебра 8:30 - 9:10\n2)Общесвознание 9:25 - 10:05\n3)Обществознание 10:20 - 11:00\n4)Геометрия 11:15 - 11:55\n5)Информатика 12:15 - 12:55\n' \
        '6)Информатика 13:15 - 13:55\nНу, более менее...',
        'Не алё, но у 10Б:\nАаэа...субботние\n1)ОБЖ  8:30 - 9:10\n2)Английский язык 9:20 - 10:00\n3)Физра 10:15 - 10:55\n4)Литературоведение 11:05 - 11:45\n5)Алгебра 11:55 - 12:35\n' \
        '6)Основы бизнеса 12:50 - 13:30\nНу, более менее...',
        'ТЫ ШО ТУПОЙ, В ВОСКРЕСЕНЬЕ НЕТ УРОКОВ'
    ]
    class_matrix.append(lessons_matrix_10a_s)
    class_matrix.append(lessons_matrix_10a_ch)
    class_matrix.append(lessons_matrix_10b)
    if '/start' in message.text or '/change' in message.text:
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_10a_s = types.InlineKeyboardButton(text='10A(соц-эконом)', callback_data='10a_s')
        keyboard.add(key_10a_s)
        key_10a_ch = types.InlineKeyboardButton(text='10A(хим-био)', callback_data='10a_ch')
        keyboard.add(key_10a_ch)
        key_10b = types.InlineKeyboardButton(text='10Б ', callback_data='10b')
        keyboard.add(key_10b)
        bot.send_message(message.chat.id, 'Выбери класс', reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            global class_matrix_index
            if call.data == "10a_s":
                class_matrix_index = 0
            elif call.data == "10a_ch":
                class_matrix_index = 1
            elif call.data == "10b":
                class_matrix_index = 2
            con = sqlite3.connect('BotUsers.db')
            cur = con.cursor()
            query = """UPDATE Users SET Class = ? WHERE Username = ?"""
            data = [class_matrix_index, message.from_user.username]
            cur.execute(query, data)
            con.commit()
            con.close()
    elif 'почему' in message.text:
        bot.send_message(message.chat.id, 'Потому что ты - пи**р')
    elif 'все пользователи' in message.text:
        if message.chat.id in admins:
            for elem in results:
                user_class = ''
                if elem[3] == 2:
                    user_class = '10Б'
                elif elem[3] == 0:
                    user_class = '10A Соц-Эконом'
                elif elem[3] == 1:
                    user_class = '10A Хим-Био'
                bot.send_message(message.chat.id, f'''Username: @{elem[0]}\nИмя: {elem[1]}\nФамилия: {elem[2]}\nВыбран класс: {user_class}''')
        else:
            bot.send_message(message.chat.id, 'Секретная информация')
            img = open('data/бык.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
    elif 'количество пользователей' in message.text:
        bot.send_message(message.chat.id, f'''На данный момент мной пользуются {len(results)} человек''')
    elif 'ответы' in message.text or '/answers' in message.text:
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_t = types.InlineKeyboardButton(text='Задачи', callback_data='t')
        keyboard.add(key_t)
        key_q = types.InlineKeyboardButton(text='Вопросы', callback_data='q')
        keyboard.add(key_q)
        bot.send_message(message.chat.id, 'Задачи или вопросы?', reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            global phy_answers_index
            if call.data == "t":
                phy_answers_index = 0
            elif call.data == "q":
                phy_answers_index = 1
    elif message.text.isdigit():
        if phy_answers_index == 0:
            try:
                img = open('data/{}.png'.format(message.text), 'rb')
                bot.send_message(message.chat.id,'Ответ на задачу №{}'.format(message.text))
                bot.send_photo(message.chat.id, img)
            except Exception:
                bot.send_message(message.chat.id, 'Такого номера нет в базе ответов, попробуй ещё раз')
        else:
            try:
                img = open('data/a_{}.jpg'.format(message.text), 'rb')
                bot.send_message(message.chat.id,'Ответ на вопрос №{}'.format(message.text))
                bot.send_photo(message.chat.id, img)
            except Exception:
                bot.send_message(message.chat.id, 'Такого номера нет в базе ответов, попробуй ещё раз!')
    elif 'что задали на сегодня' in message.text or '/hw_for_today' in message.text:
        dz_date_today = str(datetime.date.today()).split('-')
        dz_date_today[2] = str(int(dz_date_today[2]) + 1)
        dz_date_today.reverse()
        bot.send_message(message.chat.id, 'Я не алё, посмотри в дневнике\nhttps://schools.dnevnik.ru/homework.aspx?school=1000006325847&tab=&studyYear=2019&subject=&datefrom={}&dateto={}&choose=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C'.format('.'.join(dz_date_today), '.'.join(dz_date_today)))
    elif 'что задали на завтра' in message.text or '/hw_for_tomorrow' in message.text:
        today = datetime.date.today()
        dz_date_tomorrow = today + datetime.timedelta(days=1)
        dz_date_tomorrow = str(dz_date_tomorrow).split('-')
        dz_date_tomorrow.reverse()
        bot.send_message(message.chat.id, 'Я не алё, посмотри в дневнике\nhttps://schools.dnevnik.ru/homework.aspx?school=1000006325847&tab=&studyYear=2019&subject=&datefrom={}&dateto={}&choose=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C'.format('.'.join(dz_date_tomorrow), '.'.join(dz_date_tomorrow)))
    elif 'привет' in message.text:
        bot.send_message(message.chat.id,
                         'Приветствую, я - бот ИльяС, у меня ты можешь узнать:\n/monday - Какие уроки в понедельник\n/tuesday - Какие уроки во вторник\n/wednesday - Какие уроки в среду\n/thursday - Какие уроки в четверг\n/friday - Какие уроки в пятницу\n/saturday - Какие уроки в субботу\n/all - Расписание на все дни\n/today - Какие уроки сегодня\n/tomorrow - Какие уроки завтра')
        img = open('data/hello.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'сортировка говно' in message.text:
        bot.send_message(message.chat.id, 'Ты шо на Сортировку, я тебя ща обоссу!!!1!11')
        img = open('data/бык.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'букины говно' in message.text:
        bot.send_message(message.chat.id, 'Ты шо петух, Букины топ, Гена Букин лучший!!!1!11')
        img = open('data/бык.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'какие уроки сегодня' in message.text or message.text == '/today':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][day - 1])
    elif 'какие уроки завтра' in message.text or message.text == '/tomorrow':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][day - 1])
    elif 'расписание' in message.text or message.text == '/all':
        for day in class_matrix[class_matrix_index]:
            bot.send_message(message.chat.id, day)
    elif 'какие уроки в понедельник' in message.text or message.text == '/monday':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][0])
    elif 'какие уроки во вторник' in message.text or message.text == '/tuesday':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][1])
    elif 'какие уроки в среду' in message.text or message.text == '/wednesday':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][2])
    elif 'какие уроки в четверг' in message.text or message.text == '/thursday':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][3])
    elif 'какие уроки в пятницу' in message.text or message.text == '/friday':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][4])
    elif 'какие уроки в субботу' in message.text or message.text == '/saturday':
        bot.send_message(message.chat.id, class_matrix[class_matrix_index][5])
    else:
        bot.send_message(message.chat.id, 'Я не алё')


bot.polling(none_stop=True)