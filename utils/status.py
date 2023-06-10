from enum import Enum


class InsertStatus(Enum):
    UPDATE_NOT_ALLOWED = -5
    INCOMPLETE_INFO = -4
    BAD_ID = -3
    DUPLICATE_ENTRY = -2
    DUPLICATE_ID = -1
    UNEXPECTED_ERROR = 0
    INSERTED_SUCCESSFULLY = 1
    UPDATED_SUCCESSFULLY = 2


class FindStatus(Enum):
    INSUFFICIENT_INFO = -2
    NO_RECORDS = -1
    UNEXPECTED_ERROR = 0
    RECORD_FOUND = 1
