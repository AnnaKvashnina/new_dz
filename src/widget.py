from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_information:str) -> str:
    """ Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""

    letter_result = ""
    number_result = ""
    number_count = 0
    for symbol in user_information:
        if symbol.isalpha():
            letter_result += symbol
        elif symbol.isdigit():
            number_result += symbol
            number_count += 1
    if number_count > 16:
        return f"{letter_result} {get_mask_account(number_result)}"
    else:
        return f"{letter_result} {get_mask_card_number(number_result)}"


def get_date(date:str) -> str:
    """ Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
