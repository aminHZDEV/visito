import os.path
from os import getcwd
import ast
import csv


def insert_testcases(source: str = "") -> tuple[str, list]:
    """
    this function is used to add testcase to pytest parametaraize
    :param source:
    :return:
    """
    csv_path = os.path.join(getcwd(), "statics", "pytest_files", source)

    with open(csv_path) as f:
        content = csv.reader(f, delimiter=",", skipinitialspace=True)
        titles = ","
        test_cases = []
        for i, item in enumerate(content):
            if i == 0:
                titles = titles.join(item)
            else:
                test_cases.append(tuple([ast.literal_eval(it) for it in item]))
        f.close()
        return titles, test_cases
