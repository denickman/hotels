import pandas
from numpy.ma.core import squeeze

# С dtype={"id": str} pandas прочитает id как текст (строка):
df = pandas.read_csv('hotels.csv', dtype={"id": str})

#  dtype={"id": str} - читать столбец 'id' как текст, не как число.
# df.loc[] возвращает результат в виде таблицы (Series), даже если это одна ячейка:
# .squeeze() извлекает значение из таблицы и превращает его в обычное значение /  обычную строку:.

class Hotel:

    watermark = 'the real estate company'

    def __init__(self, hotel_id):
        self.id = hotel_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()

    def book_hotel(self):
        '''book a hotel by changing availability to no'''

        # Находит строку где id == self.id
        # Присваивает значение 'no' в столбец 'available'
        df.loc[df['id'] == self.id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)  # <- нужно передать имя файла

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


class ReservationTicket:
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
        return content  # <- добавь return

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert():
        return amount



hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="123")


print(hotel1.name)
print(hotel2.name)


ticket = ReservationTicket(customer_name="alex megane", hotel=hotel1)
ticket.the_customer_name = hotel1.name