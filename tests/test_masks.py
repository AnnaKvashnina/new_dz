import pytest

from src.masks import get_mask_account, get_mask_card_number, ValidationError


"""Тестирование правильности маскирования номера карты."""
@pytest.mark.parametrize(
    "value, expected",
     [("7000792289606361", "7000 79** **** 6361"),
     ("9876543210987654", "9876 54** **** 7654")
     ]
   )

def test_get_mask_card_number(value,expected):
    assert get_mask_card_number(value) == expected

def test_Len_get_mask_card_number():
   """Проверка работы функции на различных входных форматах номеров карт,
    включая граничные случаи и нестандартные длины номеров."""
   with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('700079228960636')
   assert str(exc_info.value) ==  "неверный номер карты"


#@pytest.mark.parametrize("number_account", ["7000792289606361", "9876543210987654"])
#def test_masks_card_number(number_account):
#    assert len(number_account) == 16


"""Проверка, что функция корректно обрабатывает входные строки, 
   где отсутствует номер карты."""
def test_dig_get_mask_card_number():

   with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('700079228960636k')
   assert str(exc_info.value) ==  "неверный номер карты"


def test_get_mask_account():
    """Тестирование правильности маскирования номера счета."""

    assert get_mask_account("73654108430135874305") == "**4305"




def test_len_get_mask_account():
    """Проверка, что функция корректно обрабатывает входные данные,
       где номер счета меньше ожидаемой длины."""


    with pytest.raises(ValidationError) as exc_info:
        get_mask_account('700079228960636')
    assert str(exc_info.value) == "неверный номер счета"


def test_dig_get_mask_account() -> None:
    """Проверка работы функции с различными форматами и длинами номеров счетов."""

    with pytest.raises(ValidationError) as exc_info:
        get_mask_account('7000792289606gh6')
    assert str(exc_info.value) == "неверный номер счета"




