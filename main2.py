import pandas
from abc import ABC, abstractmethod
from numpy.ma.core import squeeze

# С dtype={"id": str} pandas прочитает id как текст (строка):
df = pandas.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    watermark = 'the real estate company'

    def __init__(self, hotel_id):
        self.id = hotel_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()

    def book_hotel(self):
        '''book a hotel by changing availability to no'''
        df.loc[df['id'] == self.id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        '''checks if the hotel is available'''
        availability = df.loc[df['id'] == self.id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # ✅ ПРАВИЛЬНО:
    def __eq__(self, other):
        """Сравниваем два отеля по id"""
        if not isinstance(other, Hotel):
            return False
        return self.id == other.id

    # ❌ НЕПРАВИЛЬНО (твой код):
    # def __eq__(self):  # <- параметр other отсутствует!
    #     if self.id == self.id:  # <- сравнивает сам с собой, всегда True!
    #         return True
    #     else:
    #
    #
    #         return False

class Ticket(ABC):
    @abstractmethod
    def generate(self):
         pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
       Thank you for your reservation!
       Here are you booking data:

       Name: {self.customer_name}
       Hotel: {self.hotel.name}
    """
        return content

    @property
    def the_customer_name(self):
        """Это ТОЛЬКО для чтения (getter)"""
        name = self.customer_name.strip()
        name = name.title()
        return name

    # Если хочешь присваивать значения, добавь setter:
    @the_customer_name.setter
    def the_customer_name(self, value):
        """Позволяет присваивать значения"""
        self.customer_name = value

    @staticmethod
    def convert(amount):
        return amount * 1.2


# ═════════════════════════════════════════════
# ИСПОЛЬЗОВАНИЕ
# ═════════════════════════════════════════════

hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="123")

print(hotel1.name)
print(hotel2.name)

ticket = ReservationTicket(customer_name="alex megane", hotel=hotel1)

# ✅ ПРАВИЛЬНО - читаем свойство:
print(ticket.the_customer_name)  # "Alex Megane"

# ✅ ПРАВИЛЬНО - присваиваем (если есть @setter):
ticket.the_customer_name = "John Doe"
print(ticket.the_customer_name)  # "John Doe"

# ❌ НЕПРАВИЛЬНО (твой код):
# ticket.the_customer_name = hotel1.name
# Это присваивает строку "Grand Hotel" вместо имени человека






class DigitalTicket(Ticket):
    def generate(self):
        return 'Hi, this is your digital ticket'
    def download(self):
        pass








