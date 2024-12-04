#!/usr/bin/python

import os
import sys
import re


disk_regex = re.compile(r".*\(Disc.*\.chd$")
game_name_regex = re.compile(r"(.*)\(Disc.*\.chd$")


def find_multidisk(roms):
    return list(filter(lambda rom: disk_regex.match(rom), roms))


def make_disk_unions(multidisks):
    unions = dict()

    for disk in multidisks:
        game_name_match = game_name_regex.match(disk)
        file = game_name_match[0]
        game = game_name_match[1].strip()

        if game not in unions:
            unions[game] = [file]
        else:
            unions[game].append(file)

    return unions


def create_m3u(unions):
    hidden_path = where + '/.hidden'
    os.mkdir(hidden_path)

    for game, files in unions.items():
        files = sorted(files)
        filename = game + ".m3u"
        path = where + '/' + filename

        with open(path, 'w') as f:
            for file in files:
                f.write('.hidden/' + file + '\n')

        for file in files:
            oldpath = where + '/' + file
            newpath = hidden_path + '/' + file

            os.rename(oldpath, newpath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./multidisk.py <WHERE>")
        exit(1)

    where = sys.argv[1]
    roms = os.listdir(where)

    multidisks = find_multidisk(roms)
    unions = make_disk_unions(multidisks)
    create_m3u(unions)
