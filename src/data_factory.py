from faker import Faker
from datetime import timedelta

fake = Faker()
def create_booking_payload() -> dict:
    checkin_date = fake.date_between(start_date = 'today', end_date = '+30d')
    checkout_date = checkin_date + timedelta(days = fake.random_int(min = 1, max = 10))
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": checkin_date.strftime("%Y-%m-%d"),
            "checkout": checkout_date.strftime("%Y-%m-%d"),
        }
    }

