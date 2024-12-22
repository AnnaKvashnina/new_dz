import pytest
from tomlkit import value

from src import widget
from src.widget import mask_account_card, get_date

"""Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции."""
@pytest.mark.parametrize(
    "user_information, result",
     [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("VisaPlatinum 7000792289606361", "VisaPlatinum 7000 79** **** 6361")
]
)
def test1_mask_account_card(user_information, result):
    assert mask_account_card(user_information) == result

"""Тесты для проверки, что функция корректно распознает
 и применяет нужный тип маскировки в зависимости 
 от типа входных данных (карта или счет)."""

"""Тестирование функции на обработку некорректных входных данных 
и проверка ее устойчивости к ошибкам."""

def test_get_date():
    """Тестирование правильности преобразования даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_invalid():
    """Проверка работы функции на различных входных форматах даты,
     включая граничные случаи и нестандартные строки с датами."""
    with pytest.raises(ValueError):
       widget.get_date("Не верный формат даты")

"""Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата."""