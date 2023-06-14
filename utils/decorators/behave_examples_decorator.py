import os.path
from os import getcwd, listdir
from behave.model import Row
import csv


def insert_examples():
    csv_path = os.path.join(getcwd(), "statics", "behave_files")
    filenames = [
        os.path.join(csv_path, item)
        for item in listdir(csv_path)
        if item.endswith(".csv")
    ]

    def inner(func):
        def wrapper(*args, **kwargs):
            for file in filenames:
                with open(file) as f:
                    content = csv.reader(f, delimiter=",", skipinitialspace=True)
                    mlist = []
                    for i, item in enumerate(content):
                        if i == 0:
                            mlist = item
                        else:
                            for j in args[1]:
                                for i in j.examples:
                                    print("mlist : ", mlist)
                                    print(i.table.headings, " | ", i.table.headings == mlist)
                                    if i.table.headings == mlist:
                                        i.table.rows.append(
                                            Row(
                                                headings=mlist,
                                                cells=[
                                                    str(m.replace("\n", ""))
                                                    for m in item
                                                ],
                                            )
                                        )
                f.close()
            func(*args, **kwargs)

        return wrapper

    return inner
