from models.booking import CreateBookingResponse
from src.constant import BookingData


def test_create_booking(created_booking):
    try:
        parsed = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f"Структура ответа не соотвествует данным: {e}")

    assert parsed.booking.bookingdates.checkin == "2026-01-01"

    assert created_booking["booking"]["firstname"] == BookingData.FIRSTNAME.value, (
        "Вернулось не корректное имя\n"
        f"Respopnse:\n{created_booking}\n"
        f"Ожидаемое имя: {BookingData.FIRSTNAME}"
    )
    assert created_booking["booking"]["lastname"] == BookingData.LASTNAME.value, (
        "Вернулось не корректная фамилия\n"
        f"Respopnse:\n{created_booking}\n"
        f"Ожидаемое имя: {BookingData.LASTNAME}"
    )
