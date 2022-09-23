#!/usr/bin/python3

if __name__ == "__main__":
   from sys import argv

Quant = len(argv) - 1
if Quant == 0:
    print("0 arguments.")
elif Quant == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(Quant))
    for i in range(Quant):
        print("{}: {}".format(i + 1, argv[i + 1]))