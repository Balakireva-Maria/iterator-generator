import hashlib
import os
import json

path = os.getcwd()


def csv_reader(path):
    for row in open('countries.json', "r"):
        yield (hashlib.md5(row.encode()))

for item in csv_reader(path):
    print(item)


