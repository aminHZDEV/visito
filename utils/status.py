from enum import Enum


class InsertStatus(Enum):
    BAD_ID = -3
    DUPLICATE_ENTRY = -2
    DUPLICATE_ID = -1
    UNEXPECTED_ERROR = 0
    INSERTED_SUCCESSFULLY = 1
    UPDATED_SUCCESSFULLY = 2


class FindStatus(Enum):
    NO_RECORDS = -1
    UNEXPECTED_ERROR = 0
    RECORD_FOUND = 1
