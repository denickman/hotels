import pandas
from numpy.ma.core import squeeze

# С dtype={"id": str} pandas прочитает id как текст (строка):
df = pandas.read_csv('hotels.csv', dtype={"id": str})
df_cards = pandas.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pandas.read_csv('card_security.csv', dtype=str)


#  dtype={"id": str} - читать столбец 'id' как текст, не как число.
# df.loc[] возвращает результат в виде таблицы (Series), даже если это одна ячейка:
# .squeeze() извлекает значение из таблицы и превращает его в обычное значение /  обычную строку:.

class Hotel:
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expDate, holder, cvv):
        for card in df_cards:
            if (card['number'] == self.number and
                    card['expiration'] == expDate and
                    card['holder'] == holder and
                    card['cvc'] == cvv):
                return True
        return False


class SecureCreditCard(CreditCard):

    def authenticate(self, given_password):
        row = df_cards_security.loc[df_cards_security['number'] == self.number]

        if row.empty:  # если карта не найдена
            return False

        password = row['password'].values[0]  # извлеки первое значение

        if password == given_password:
            return True
        else:
            return False






print(df)


while True:
    hotel_id = input("Enter hotel id: ")

    # Проверка существует ли отель
    if hotel_id not in df['id'].values:  # <- проверка
        print("This hotel does not exist")
    else:
        hotel = Hotel(hotel_id)

        if hotel.available():

            # card_number = input("Enter card number: ")

            credit_card = SecureCreditCard(number='1234')

            if credit_card.validate(expDate = '12/26', holder = 'JOHN SMITH', cvv='123'):
                if credit_card.authenticate(given_password = 'mypass'):

                    hotel.book_hotel()

                    name = input('Enter your name: ')
                    reservation_ticket = ReservationTicket(name, hotel)
                    print(reservation_ticket.generate())
                else:
                    print("Credit card auth failed")
            else:
                print("there was a problem with your method")
        else:
            print("hotel is not free")