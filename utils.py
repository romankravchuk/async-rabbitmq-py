from enum import Enum


class Commands(Enum):
    GET_BOOK_LIST=0
    ADD_BOOK=1
    GET_BOOK_BY_ID=2
    FIND_BOOK_BY_AUTHOR=3
    FIND_BOOK_BY_NAME=4
    DELETE_BOOK=5
    DISCONNECT_FROM_SERVER=6
    TURN_OF_SERVER=7