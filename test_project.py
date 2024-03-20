from unittest.mock import patch, mock_open
from project import check_if_eurozone, get_currency_code, get_big_mac_price, get_exchange_rate, convert_currency

def test_check_if_eurozone():
    with patch("builtins.open", mock_open(read_data="United States\nCanada\nJapan")):
        assert check_if_eurozone("Brazil") is False

def test_get_currency_code():
    with patch("project.check_if_eurozone", return_value=True):
        assert get_currency_code("Germany") == "EUR"

def test_get_big_mac_price():
    mock_data = "date,iso_a3,currency_code,name,local_price\n2023,United States,USD,Brazil,5.00\n2023,JPN,JPY,Japan,650"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        assert get_big_mac_price("Brazil") == 5.00

def test_get_exchange_rate():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": "success",
            "rates": {"BRL": 3.5}
        }
        assert get_exchange_rate("USD", "BRL") == 3.5

def test_convert_currency():
    with patch("project.get_exchange_rate", return_value=3.5):
        assert convert_currency(10, "USD", "BRL") == 35.0
