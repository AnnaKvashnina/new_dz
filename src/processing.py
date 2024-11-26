# from pickle import FALSE
from typing import Any

dictionary_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(dictionary_list: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:

    """ value output function """

    executed_list = []
    for key_state in dictionary_list:
        if key_state["state"] == state:
            executed_list.append(key_state)
    return executed_list


def sort_by_date(dictionary_list: list[dict[str, Any]], rev: bool) -> list[dict[str, Any]]:
    """ date sort function """
    list_by_date = sorted(dictionary_list, key=lambda x: x["date"], reverse=rev)
    return list_by_date
