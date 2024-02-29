import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    #class variable
    watermark = "The real estate company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

hotel1 = Hotel(hotel_id="420")
hotel2 = Hotel(hotel_id="188")

#name is an instanse cariable
print(hotel1.name)
print(hotel2.name)


print(Hotel.watermark)
print(hotel1.available())
print(hotel1.book())

print(Hotel.get_hotel_count(data=df))

print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="donal mcgee", hotel_object=hotel1)
print(ticket.the_customer_name)

print(ticket.generate())