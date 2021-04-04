import hashlib
import os
import json

path = os.getcwd()

def gethash(path, row_index):
    for row in open('countries.json', "r", encoding='utf-8'):

        yield (hashlib.md5(row.encode()))



