# def get_mask_card_number(card_number: str) -> str | None:
#    """Bank card number masking function"""
#    if card_number.isdigit() and len(card_number) == 16:
#        return f"{card_number[:5]}{card_number[4:6]}{'*' * 2}{'*' * 4}{card_number[12:]}"
#    else:
#        return None


# def get_mask_account(account_number: str) -> str | None:
#    """Bank account number masking function"""
#    if account_number.isdigit() and len(account_number) == 20:
#        return f"{'*' * 2}{account_number[-4:]}"
#    else:
#        return None
class ValidationError(Exception):
    pass


def get_mask_card_number(card_number: str) -> str:
    """Bank card number masking function"""
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("неверный номер карты")

    return f"{card_number[:4]}{" "}{card_number[4:6]}{'*' * 2}{" "}{'*' * 4}{" "}{card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Bank account number masking function"""
    if not account_number.isdigit() or len(account_number) != 20:
        raise ValidationError("неверный номер счета")

    return "**" + account_number[-4:]
