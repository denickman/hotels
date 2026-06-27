import pandas
from numpy.ma.core import squeeze

# С dtype={"id": str} pandas прочитает id как текст (строка):
df = pandas.read_csv('hotels.csv', dtype={"id": str})



# df.loc[] возвращает результат в виде таблицы (Series), даже если это одна ячейка:
# .squeeze() извлекает значение из таблицы и превращает его в обычное значение.

class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()

    def book_hotel(self):
        '''book a hotel by changing availability to no'''
        df.loc[df['id'] == self.id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)  # <- нужно передать имя файла

    def available(self):
        '''checks if the hotel is available'''
        availability = df.loc[df['id'] == self.id, 'available'].squeeze()

        if availability == 'yes':
            return True
        else:
            return False


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


print(df)

while True:
    hotel_id = input("Enter hotel id: ")

    # Проверка существует ли отель
    if hotel_id not in df['id'].values:  # <- проверка
        print("This hotel does not exist")
    else:
        hotel = Hotel(hotel_id)

        if hotel.available():
            hotel.book_hotel()

            name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("hotel is not free")