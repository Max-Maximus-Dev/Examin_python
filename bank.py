from random import randint


numbers = []
baza_number = []
baza_password = []
kartas = []

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.number = 0
        self.balance = 0
        self.logged_in_to_card = False
        self.czas = 0
        self.credit = 0

    def register(self):
        number = input("Введіть ваш номер: ")
        password = input("Введіть ваш пароль: ")
        if number not in baza_number:
            baza_number.append(number)
            baza_password.append(password)
            print("Реєстрація успішна!")
            print("Тепер ввійдіть щоб продовжити")
        else:
            print("Користувач з таким номером вже існує.")

    def change_password(self):
        password = input("Введіт старий пароль: ")
        if password in baza_password:
            baza_password.remove(password)
            new_password = input("Введіть новий пароль: ")
            baza_password.append(new_password)
            print(f"Ваш новий пароль {new_password}")
        else:
            print("Ви не парвильно ввели старий пароль")

    def work(self):
        zarobitok = randint(100, 10000)
        self.balance += zarobitok
        print(f"Ви попрацювали та заробили {zarobitok}. Новий баланс: {self.balance}")

    def rob_bank(self):
        chance = randint(1, 10)
        if chance == 2 or chance == 4 or chance == 6 or chance == 8  or chance == 10:
            grabioz = randint(100000, 1000000)
            self.balance += grabioz
            print(f"Ви успішно пограбували банк та заробили {grabioz}. Новий баланс: {self.balance}")
        else:
            shtraf = randint(1000, 10000)
            self.balance -= shtraf
            print(f"Під час пограбування вас вспіймали та оштрафували на {shtraf}. Новий баланс: {self.balance}")

    def login(self):
        number = input("Введіть ваш номер для входу: ")
        password = input("Введіть ваш пароль: ")
        if number in baza_number and password in baza_password:
            print(f"Вхід успішний, привіт {number}")
            self.number = number
            return True
        else:
            print("Невірний номер або пароль.")
            return False

    def create_card(self):
        self.number = input("Введіть ваш номер телефону для реєстрації карти(з нулем): ")
        if self.number in numbers:
            print("Вже зареєстрована карта для цього номера.")
        else:
            karta = randint(1000000000000000, 9000000000000000)
            kartas.append(karta)
            numbers.append(self.number)
            print(f"Номер вашої карти: {karta}")
            print()
            print("Ввійдіть ан карту щоби продовжити.")
            print()

    def logincard(self):
        self.number = input("Введіть ваш номер телефону для входу на карту: ")
        if self.number in numbers:
            self.logged_in_to_card = True
            print("Ви успішно ввійшли на карту")
        else:
            print("Такого номеру немає в базі")

    def info(self):
        print(f"""Ім'я: {self.name}
        Електронна адреса: {self.address}
        Баланс карти: {self.balance}
        Кредит: {self.credit}""")

    def popvnutu_baalnce(self):
        howmuch = float(input("Скільки ви хочете покласти на карту? "))
        self.balance += howmuch
        print(f"Баланс успішно поповнено. Новий баланс: {self.balance}")

    def zniatu(self):
        howmuch = float(input("Скільки хочете зняти з карти? "))
        if howmuch > self.balance:
            print("Недостатньо коштів")
        else:
            self.balance -= howmuch
            print(f"Знято {howmuch}. Новий баланс: {self.balance}")

    def perekaz(self):
        nomer_of_card = int(input("Введіть номер карти на яку хочете перекинути кошти: "))
        if len(str(nomer_of_card)) != 16:
            print("Неправильно введена карта отримувача")
        else:
            howmuch = float(input("Введіть суму скільки хочете переказати: "))
            if howmuch > self.balance:
                print("Недостатньо коштів")
            else:
                self.balance -= howmuch
                print(f"Переказано {howmuch}. Новий баланс: {self.balance}")

    def credi(self):
        credit = int(input("Введіть скільки хочете взяти кредитних коштів: "))
        if 5000 <= credit <= 10000:
            print(f"В цьому випадку через 12 місяців ви виплатите {credit} та 5% річних від цієї суми")
            answ = input("Ви згодні? (Так/Ні)")
            if answ == "Так":
                self.balance += credit
                credit_czas = self.czas + 12
                new_credit = credit + credit * 0.05
                self.credit += new_credit
                print(f"Ви взяли кредит на суму {credit}, до {credit_czas} ви маєте сплатити кредит")
            elif answ == "Ні":
                print("Добре.")
            else:
                print("Ви не правильно ввели команду")
        elif 10001 <= credit <= 50000:
            print(f"В цьому випадку через 12 місяців ви виплатите {credit} та 3.5% річних від цієї суми")
            answ = input("Ви згодні? (Так/Ні)")
            if answ == "Так":
                self.balance += credit
                credit_czas = self.czas + 12
                new_credit = credit + credit * 0.035
                self.credit += new_credit
                print(f"Ви взяли кредит на суму {credit}, до {credit_czas} ви маєте сплатити кредит")
            elif answ == "Ні":
                print("Добре.")
            else:
                print("Ви не правильно ввели команду")
        elif 50001 <= credit <= 100000:
            print(f"В цьому випадку через 12 місяців ви виплатите {credit} та 2% річних від цієї суми")
            answ = input("Ви згодні? (Так/Ні)")
            if answ == "Так":
                self.balance += credit
                credit_czas = self.czas + 12
                new_credit = credit + credit * 0.02
                self.credit += new_credit
                print(f"Ви взяли кредит на суму {credit}, до {credit_czas} ви маєте сплатити кредит")
            elif answ == "Ні":
                print("Добре.")
            else:
                print("Ви не правильно ввели команду")
        else:
            print("""Недопустима сума кредиту!
            Допустима сума: від 5000 до 100000""")

    def splatutu_credi(self):
        if self.credit == 0:
            print("У вас немає кредиту. Напишіть команду \"3\" для того, щоб взнати суму вашого кредиту")
        else:
            print(f"Сума вашого кредиту: {self.credit}")
            answ = input("Ви готові сплатити кредит (Так/Ні): ")
            if answ == "Так":
                answ_credit = int(input("Скільки ви хочете спалтити кредиту? "))
                self.balance -= answ_credit
                self.credit -= answ_credit
                print(f"Ви сплатили {answ_credit} кредиту. Залишок кредиту: {self.credit}. Новий баланс: {self.balance}")
            elif answ == "Ні":
                print("Добре.")
            else:
                print("Ви не правильно ввели команду")

    def czass(self):
        self.czas += 1
        print(f"Ви користуєтесь нашим банком вже {self.czas} місяців")

    def colectors(self):
        if self.balance < 0:
            chance = randint(1, 10)
            if chance == 5:
                dodatok = randint(100, 1000)
                print(f"В тебе борг країні(відємний баланс), і це побачили колектори, які прийшли до тебе і \"поговоривши\" з тобою додали тобі до боргу {dodatok}")
            else:
                print("В цей раз тобі повезло і твій борг країні(відємний баланс) колектори не побачили")
        else:
            pass


name = input("Введіть ваше ім'я: ")
address = input("Введіть вашу електронну адресу: ")
bankstart = Bank(name, address)

while True:
    answ = input("Що ви хочете зробити? (Зареєструватись/Ввійти): ").strip()
    if answ == "Зареєструватись":
        bankstart.register()
    elif answ == "Ввійти":
        if bankstart.login():
            break
    else:
        print("Ви не правильно ввели команду. Спробуйте ще раз.")

while True:
    bankstart.colectors()
    bankstart.czass()
    answ_command = input("""Виберіть команду(напишіть число):
    1) Створити карту
    2) Ввійти на карту
    3) Інфо про користувача
    4) Поповнити баланс
    5) Зняти гроші
    6) Переказ коштів
    7) Змінити пароль
    8) Пограбувати банк
    9) Попрацювати
    10) Взяти кредит
    11) Сплатити кредит
    12) Вийти
    """).strip()

    if answ_command == "1":
        bankstart.create_card()
    elif answ_command == "2":
        bankstart.logincard()
    elif answ_command == "3" and bankstart.logged_in_to_card:
        bankstart.info()
    elif answ_command == "4" and bankstart.logged_in_to_card:
        bankstart.popvnutu_baalnce()
    elif answ_command == "5" and bankstart.logged_in_to_card:
        bankstart.zniatu()
    elif answ_command == "6" and bankstart.logged_in_to_card:
        bankstart.perekaz()
    elif answ_command == "7" and bankstart.logged_in_to_card:
        bankstart.change_password()
    elif answ_command == "8" and bankstart.logged_in_to_card:
        bankstart.rob_bank()
    elif answ_command == "9" and bankstart.logged_in_to_card:
        bankstart.work()
    elif answ_command == "10" and bankstart.logged_in_to_card:
        bankstart.credi()
    elif answ_command == "11" and bankstart.logged_in_to_card:
        bankstart.splatutu_credi()
    elif answ_command == "12":
        print("До побачення!")
        break
    else:
        print("Невірна команда або ви ще не увійшли на карту. Спробуйте ще раз.")
