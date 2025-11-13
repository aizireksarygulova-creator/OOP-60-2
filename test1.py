

from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp=0):
        super().__init__(name, lvl, hp, mp)
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    bank_name = "Simba"
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = int(balance)
        self.__password = str(password)
    def login(self, password):
        return self.__password == password
    @property
    def full_info(self):
        return f"{self.hero.name} | lvl: {self.hero.lvl} | Баланс: {self._balance} SOM"
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    @staticmethod
    def bonus_for_level(lvl):
        return int(lvl) * 10
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        raise TypeError
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl

class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": f"{phone}"}

if __name__ == "__main__":
    merlin = MageHero("Merlin", 30, 1000, 150)
    conan = WarriorHero("Conan", 50, 3000)
    acc_merlin = BankAccount(merlin, 5000, "m_pass")
    acc_conan = BankAccount(conan, 3000, "c_pass")
    print(merlin.action())
    print(conan.action())
    print(str(acc_merlin))
    print(str(acc_conan))
    print("Банк:", BankAccount.get_bank_name())
    print("Бонус за 50 уровень:", BankAccount.bonus_for_level(50), "SOM")
    kg = KGSms()
    print(kg.send_otp("+996777123456") + ".")
