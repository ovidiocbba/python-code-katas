"""
Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

Link: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
"""


def abbrev_name(name):
    first = name[0].upper()
    second = name.split(" ")[1][0].upper()
    return f'{first}.{second}'
