from pprint import pprint

from Parse import NBU


class User:
    COMANDER = ["info", 'calc', 'assistant']
    DB: list
    ACTION = ["BUY", "SALE"]
    CURRENCY = ["UAH", "USD", "EUR", "RUB"]
    CONVERT = {"USD": 0, "EUR": 1, "RUB": 2}

    def assistant(self) -> None:
        print("Info......")
        print("Сalc......")
        print("Help......")
        print("EXIT......")

    def listen(self) -> None:
        while True:
            comand = input("input comand " + "\n").lower()
            if comand == "info":
                self.get_info()

            elif comand == "calc":
                self.dataset()
            elif comand == "exit":
                self.log_out()
            else :
                self.assistant()
    def dataset(self) -> list:
        self.info()
        COUNT = self.input_count()
        flag = True
        count = 0
        while flag:
            if count > 0:
                print("Mistake, Enter again!!!")
            with_VALUE = self.input_data(self.CURRENCY, "Enter  source with currency:")
            to_VALUE = self.input_data(self.CURRENCY, "Enter source to currency:")
            if not with_VALUE == to_VALUE:
                flag = False
        ACT = self.input_data(self.ACTION, "Enter your act:").lower()

        self.calc(COUNT, ACT, with_VALUE, to_VALUE)

    def calc(self, COUNT: float, ACT: str, with_VALUE: str, to_VALUE: str) -> None:

        if with_VALUE == "UAH":
            convert_value = self.CONVERT[to_VALUE]
            tmp = float(self.DB[convert_value][ACT])
            res = str(COUNT / tmp)
        else:
            convert_value = self.CONVERT[with_VALUE]
            tmp = float(self.DB[convert_value][ACT])
            print(tmp)
            res1 = tmp * COUNT
            print(res1)
            convert_value = self.CONVERT[to_VALUE]
            tmp1 = float(self.DB[convert_value][ACT])
            res = str(res1 / tmp1)

        print("Result: {} {}".format(res, to_VALUE))

    def info(self):
        URL = ' https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        BANK = NBU(url=URL)
        BANK.connect()
        self.DB = BANK.DATA

    def input_count(self) -> int:
        count = 0
        flag = True
        while flag:
            if count > 0:
                print("Mistake, Enter again!!!")
            count += 1

            try:
                inp = float(input("enter quantity to transfer" + "\n"))
                flag = False
            except Exception as e:
                print(e)

        return inp

    def input_data(self, pattern: str, text: str) -> str:
        flag = True
        count = 0
        while flag:
            if count > 0:
                print("Mistake, Enter again!!!")
            inp = input(text + '\n').upper()
            count += 1
            if inp in pattern:
                flag = False
        return inp

    def get_info(self):
        self.info()
        pprint(self.DB)

    def log_out(self):
        exit(-1)


