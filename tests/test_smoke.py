import pytest

@pytest.mark.smoke
def test_health_check(client):
    response = client.ping()
    assert response.status_code == 201

@pytest.mark.smoke
def test_booking_fixture_works(created_booking):
    assert isinstance(created_booking, int)
    assert created_booking > 0

