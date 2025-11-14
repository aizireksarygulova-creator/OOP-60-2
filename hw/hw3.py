import random
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password

    def deposit(self, amount, password):
        if password == self.__password:
            self._balance += amount
            return self._balance
        return "Неверный пароль!"

    def withdraw(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"
        if amount > self._balance:
            return "Недостаточно средств!"
        self._balance -= amount
        return self._balance

    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            return "Старый пароль неверный"
        self.__password = new_password
        return "Пароль изменён"

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        return "Неверный пароль!"

    def reset_pin(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return new_pin

    def __generate_pin(self):

        return "5832"


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

    def get_service(self):
        return f"Сервис: {self._service}"


class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    def send(self, message, recipient):
        return f"Email sent to {recipient}"


class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"


class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"


class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        bal = self.account.get_balance(password)
        if isinstance(bal, (int, float)):

            print(self.notifier.send(f"Успешный вход: {self.username}", "system"))
            return True
        return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        result = self.account.withdraw(amount, password)
        if result == "Неверный пароль!":
            return "Неверный пароль!"
        if result == "Недостаточно средств!":
            return "Недостаточно средств!"

        recipient_account._balance += amount


        print(self.notifier.send(f"Перевод {amount} отправлен", "system"))
        print(self.notifier.send(f"Получено {amount} от {self.username}", "system"))

        return f"Перевод успешен. Новый баланс: {self.account._balance}"


if __name__ == "__main__":

    print("=== Тест BankAccount ===")
    john = BankAccount("John", 200, "secret")
    print(john.deposit(50, "secret"))          # 250
    print(john.withdraw(100, "secret"))        # 150
    print(john.get_balance("secret"))          # 150
    print(john.change_password("wrong", "new"))
    print(john.change_password("secret", "new"))
    pin = john.reset_pin("new")
    print(pin)                                 # 5832
    print(john.get_balance(pin))               # 150


    print("=== Тест NotificationSender ===")
    email = EmailSender()
    print(email.send("Привет", "test@mail.ru"))# Email sent to test@mail.ru
    print(email.get_service())                 # Сервис: Gmail
    sms = SmsSender()
    print(sms.get_service())                   # Сервис: Twilio


    print("=== Тест UserAuth ===")
    john_for_auth = BankAccount("John", 150, "secret")
    alice = BankAccount("Alice", 50, "pass123")
    notifier = SmsSender()
    auth = UserAuth("john_doe", john_for_auth, notifier)
    auth.login("secret")
    print(auth.transfer(70, "secret", alice))
    print(f"John balance: {john_for_auth._balance}")
    print(f"Alice balance: {alice._balance}")
