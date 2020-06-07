#!/usr/bin/env python3

from urllib.parse import urlparse
from subprocess import call
from sys import argv
import csv

__version__ = "1.0"


class Csv2Keychain:
    def addkey(self, account_data, update: bool, displayrow: bool):
        url = urlparse(account_data["url"])
        domain = url.netloc
        path = url.path

        syscall = [
            "security",
            "add-internet-password",
            "-l",
            account_data["name"],
            "-s",
            domain,
            "-p",
            path,
            "-a",
            account_data["username"],
            "-t",
            "form",
            "-r",
            "{:<4}".format(url.scheme[0:4]),
            "-T",
            "/Applications/Safari.app",
            "-w",
            account_data["password"],
        ]
        if update:
            syscall.append("-U")
        if displayrow:
            print(account_data)

        call(syscall)

    def __init__(self):
        csvpath = argv[1]
        params = argv[2:]

        overwrite = "-u" in params
        displayrow = "-s" in params

        with open(csvpath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            print("File opened")
            counter = 1
            for row in reader:
                print(f"Copying item #{str(counter)}...")
                self.addkey(row, overwrite, displayrow)
                print(f"#{str(counter)} complete")
                counter += 1


usage = """
csv2keychain [path.csv] [-u] [-s]
    -u    update existing password for every account in keychain, if any
    -s    display credentials on the screen during the process
"""

if __name__ == "__main__":
    print(f"Executing csv2keychain version {__version__}")
    print(f"List of argument strings: {argv[1:]}")
    if len(argv) == 1 or "-h" in argv or "--help" in argv:
        print(usage)
        exit()
    Csv2Keychain()
