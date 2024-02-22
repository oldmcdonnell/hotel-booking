import pandas as pd
import pyarrow

df = pd.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """book a hotel by changing availability"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """check if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
        Thank you for your reservation
        Here are your booking details:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content

#main look
print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("hotel is not free")