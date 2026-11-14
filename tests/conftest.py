import pytest
#from src.data_factory import BookerClient
from src.client import BookerClient
from src.data_factory import create_booking_payload

@pytest.fixture(scope = "session")
def client() -> BookerClient:
    return BookerClient()

@pytest.fixture(scope = "session")
def auth_token(client: BookerClient) -> str:
    response = client.create_token()
    return response.json()["token"]

@pytest.fixture
def created_booking(client: BookerClient, auth_token: str) -> int:
    payload = create_booking_payload()
    response = client.create_booking(payload)
    assert response.status_code == 200, f"Error al crear reserva: {response.status_code} - {response.text}"
    booking_id = response.json()["bookingid"]
    yield booking_id
    client.delete_booking(booking_id, auth_token)