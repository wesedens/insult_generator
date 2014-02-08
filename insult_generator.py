#!/usr/bin/python

import csv
from random import choice

if __name__ == '__main__':
    insults = []
    with open('insults', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            insults.append(row)
    adj1 = choice(insults)[0].strip()
    adj2 = choice(insults)[1].strip()
    noun = choice(insults)[2].strip()
    print adj1 +' ' +adj2 +' ' +noun
