#!/usr/bin/python3
def to_subtract(list_num):
    toSub = 0
    maxList = max(list_num)

    for i in list_num:
        if maxList > i:
            toSub += i

    return (maxList - toSub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listKeys = list(romNum.keys())

    num = 0
    lastRom = 0
    listNum = [0]

    for c in roman_string:
        for rNum in list_keys:
            if rNum == c:
                if rom_n.get(c) <= lastRom:
                    num += to_subtract(listNum)
                    listNum = [rom_n.get(c)]
                else:
                    listNum.append(rom_n.get(c))

                lastRom = rom_n.get(c)

    num += to_subtract(listNum)

    return (num)
