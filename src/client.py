import requests

class BookerClient:
    def __init__(self, base_url: str = "https://restful-booker.herokuapp.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })


    def ping(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/ping")

    def create_token(self, username: str = "admin", password: str = "password123") -> requests.Response:
        payload = {"username": username, "password": password}
        return self.session.post(f"{self.base_url}/auth", json = payload)

    def create_booking(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/booking", json=payload)

    def get_booking(self, booking_id: int ) -> requests.Response:
        return self.session.get(f"{self.base_url}/booking/{booking_id}")

    def delete_booking(self, booking_id: int, token: str) -> requests.Response:
        headers = {"Cookie": f"token={token}"}
        return self.session.delete(f"{self.base_url}/booking/{booking_id}", headers=headers)

    def update_booking(self, booking_id: int, token: str) -> requests.Response:
        headers = {"Cookie": f"token={token}"}
        return self.session.put(f"{self.base_url}/booking/{booking_id}", headers=headers)

