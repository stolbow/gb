#импортируем библиотеки для реализации данного задания в виде бота
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN #берем токен, который храниться в переменной TOKEN, файл config.py
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sql_module as SQL


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#решения заданий
#Задание 1.1
def ex1_1(a):
    answer = a ** 2
    return answer
#Задание 2
def ex2(summ_sec):
    summ_min = summ_sec // 60
    min = summ_min % 60
    if len(str(min)) == 1:
        min = f"0{min}"
    sec = summ_sec % 60
    if len(str(sec)) == 1:
        sec = f"0{sec}"
    hours = summ_min // 60
    answer = f"{ hours }:{ min }:{ sec }"
    return answer
#Задание 3
def ex3(n):
    answer = n + int(str(n)*2) + int(str(n)*3)
    return answer
#Задание 4
def ex4_helthy(numbers):
    answer = 0
    for i in numbers:
        if int(answer) < int(i):
            answer = i
    return answer
#Снова задание 4 искренне не понимаю зачем тут юзать While, когда есть for, но по приколу вот решение через While
def ex4_kurilshika(numbers):
    answer = 0
    i = 0
    while i < len(numbers):
        if int(answer) < int(numbers[i]):
            answer = numbers[i]
        i+=1
    return answer
#Задание 5
def ex5(info):
    if int(info[0]) > int(info[1]):
        answer = f"Дебет больше Кредита!\nПрибыль на человека составляет: {(int(info[0]) - int(info[1])) / int(info[2])}"
    elif int(info[0]) < int(info[1]):
        answer = f"Дебет меньше Кредита!\nУбыток компании составляет: {int(info[1]) - int(info[0])}"
    elif int(info[0]) == int(info[1]):
        answer = "Дебет равен Кредиту!\nФирма работает в ноль, обратитесь за бизнес консультацией в Digital Agency Alavenir"
    return answer
#Задание 6
def ex6(info):
    answer = 1
    result = float(info[0])
    while result < float(info[1]):
        result*=1.1
        answer+=1
    return answer


#тексты
hello_message = "Я отвечу на все твои вопросы\nНо сначала, отправь мне свой номер телефона\nДля этого нажми на кнопку внизу"
cancel = "Главное меню"
ex1_text = "1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран"
ex2_text = "2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.\nВведи положительное, целое число (секунды)"
ex3_text = "3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.\nВведи положительное, целое число n"
ex4_text = "4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.\nВведи положительное, целое число"
ex5_text = "5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.\nВведи через пробел 3 числа:\n1) Доходы\n2) Расходы\n3) Количество сотрудников в фирме\n Например:\n1000 900 2"
ex6_text = "6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.\n Введи через пробел 2 числа:\n1) Текущий результат a\n2) Желаемый результат b\n Например:\n3 5"

#кнопки
main_menu = ["Задание 1", "Задание 2", "Задание 3", "Задание 4", "Задание 5", "Задание 6"]
ex1_menu = ["a^2", "Представиться по имени", cancel]
ex2_menu = [cancel]
ex3_menu = ["", cancel]
ex4_menu = ["", cancel]
ex5_menu = ["", cancel]
ex6_menu = ["", cancel]

#функции
def change_stage(new_stage, user):
    SQL.UPDATE("users", update_param1="stage", update_value1=new_stage, where_param1="telegram_id", where_value1=user["telegram_id"])

#Отправка номера
def make_keyboard_for_registration():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_phone = KeyboardButton(text='Отправить свой номер телефона 📞', request_contact=True)
    keyboard.add(button_phone)
    return keyboard

def make_keyboard_Nbutton(texts, one_time_keyboard = True):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard = one_time_keyboard)
    for text1 in texts:
        button = KeyboardButton(text=text1)
        keyboard.add(button)
    return keyboard

async def Send_message(message, text, chat_id = None, keyboard = None):
    if chat_id == None:
        await message.answer(text, reply_markup = keyboard)
    else:
        await bot.send_message(chat_id, text, reply_markup = keyboard)

# команда старт
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(hello_message, reply_markup=make_keyboard_for_registration())

@dp.message_handler(content_types=['contact'])
async def registration(message):
    try:
        number = message.contact.phone_number[-10:]

        telegram_id_list = SQL.SELECT("users", select_param1 = "telegram_id")
        telegram_id_list = [user["telegram_id"] for user in telegram_id_list]


        if str(message.from_user.id) == str(message.contact.user_id) and str(message.from_user.id) not in telegram_id_list:

            SQL.INSERT("users", insert_param1 = "telegram_id", insert_value1 = message.from_user.id, insert_param2 = "number", insert_value2 = number)
            await Send_message(message, "Авторизация пройдена", keyboard = make_keyboard_Nbutton(main_menu, one_time_keyboard = False))

        else:
            await Send_message(message, "Вы уже зарегистрированы", keyboard = make_keyboard_Nbutton(main_menu, one_time_keyboard = False))
            print(main_menu[0])
    except Exception as e:
        print(e)


@dp.message_handler()
async def echo(message: types.Message):
    try:
        user = SQL.Get_user(message)

        if user is not None:
            #Главное меню
            if message.text.lower() == str.lower(cancel):
                change_stage(0, user)
                await Send_message(message, "Вы в меню", keyboard=make_keyboard_Nbutton(main_menu, one_time_keyboard = False))
            #Задание 1
            elif message.text.lower() == str.lower(main_menu[0]):
                change_stage(1, user)
                #Текст задания + вывод меню
                await Send_message(message, ex1_text, keyboard=make_keyboard_Nbutton(ex1_menu, one_time_keyboard = False))
            #Задание 1.1 - a^2
            elif message.text.lower() == str.lower(ex1_menu[0]):
                change_stage(1.1, user)
                await Send_message(message, "Введи число a", keyboard=make_keyboard_Nbutton(ex1_menu, one_time_keyboard=False))

            #Задание 1.2 - Hello, name!
            elif message.text.lower() == str.lower(ex1_menu[1]):
                change_stage(1.2, user)
                await Send_message(message, "Как тебя зовут?", keyboard=make_keyboard_Nbutton([cancel], one_time_keyboard=False))
            #Задание 2
            elif message.text.lower() == str.lower(main_menu[1]):
                change_stage(2, user)
                # Текст задания + вывод меню
                await Send_message(message, f"{ex2_text}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            # Задание 3
            elif message.text.lower() == str.lower(main_menu[2]):
                change_stage(3, user)
                # Текст задания + вывод меню
                await Send_message(message, ex3_text, keyboard=make_keyboard_Nbutton(ex3_menu, one_time_keyboard = False))
            # Задание 4
            elif message.text.lower() == str.lower(main_menu[3]):
                change_stage(4, user)
                # Текст задания + вывод меню
                await Send_message(message, ex4_text, keyboard=make_keyboard_Nbutton(ex4_menu, one_time_keyboard = False))
            # Задание 5
            elif message.text.lower() == str.lower(main_menu[4]):
                change_stage(5, user)
                # Текст задания + вывод меню
                await Send_message(message, ex5_text, keyboard=make_keyboard_Nbutton(ex5_menu, one_time_keyboard = False))
            # Задание 6
            elif message.text.lower() == str.lower(main_menu[5]):
                change_stage(6, user)
                # Текст задания + вывод меню
                await Send_message(message, ex6_text, keyboard=make_keyboard_Nbutton(ex6_menu, one_time_keyboard = False))
            #работаем с ответами пользвателя в зависимости от stage
            elif user["stage"] == 1.1:
                change_stage(0, user)
                n = int(message.text)
                await Send_message(message, f"a^2 = {ex1_1(n)}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            elif user["stage"] == 1.2:
                change_stage(0, user)
                SQL.UPDATE("users", update_param1="name", update_value1=message.text, where_param1="telegram_id", where_value1=user["telegram_id"])
                await Send_message(message, f"Привет, {message.text}!", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            elif user["stage"] == 2:
                change_stage(0, user)
                await Send_message(message, f"Ответ: {ex2(int(message.text))}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            elif user["stage"] == 3:
                change_stage(0, user)
                await Send_message(message, f"Ответ: {ex3(int(message.text))}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            elif user["stage"] == 4:
                change_stage(0, user)
                await Send_message(message, f"Ответ методом курильщика(while): {ex4_kurilshika(list(str(message.text)))}\nОтвет методом здорового человека(for): {ex4_helthy(list(str(message.text)))}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            elif user["stage"] == 5:
                change_stage(0, user)
                if user['name'] is not None:
                    await Send_message(message, f"Уважаемый, {user['name']}!\n{ex5(list(map(int, message.text.split())))}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard=False))
                else:
                    await Send_message(message, f"Ответ:\n{ex5(list(map(int, message.text.split())))}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard=False))
            elif user["stage"] == 6:
                change_stage(0, user)
                await Send_message(message, f"Ответ: {ex6(list(map(int, message.text.split())))}", keyboard=make_keyboard_Nbutton(ex2_menu, one_time_keyboard = False))
            else:
                change_stage(0, user)
                await Send_message(message, "Я не понял тебя, попробуй выбрать подходящий пункт меню", keyboard=make_keyboard_Nbutton(main_menu, one_time_keyboard = False))
        else:
            # Приветствие
            await message.answer(hello_message, reply_markup=make_keyboard_for_registration())




    except Exception as e:
        print(e)


if __name__ == '__main__':
    executor.start_polling(dp)