#!/usr/bin/env python3
# prog.py

from icecream import ic

def main(argv):
    print("main func")
    print(argv)

if __name__ == '__main__':
    import sys
    main(sys.argv)