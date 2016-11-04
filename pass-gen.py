import sys
import generator

passphrase = generator
def main():
    i = "error"
    while (i == "error"):
        i = passphrase.generate()
        if i != "error":
            print(i)

main()
