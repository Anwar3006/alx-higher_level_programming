#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    from sys import argv

    Quant = len(argv) - 1
    Result = 0
    for i in range(Quant):
        Result += int(argv[i + 1])
    print("{}".format(Result))
