# -*- coding=utf-8 -*-
import sys
import random

def main(argv):
    if not (len(sys.argv)==2 and sys.argv[1].isdigit()):
        print("usage:\n\tmkdate <interger>\n")
        exit(1)
    wall = 10000 * int(sys.argv[1])
    for c in range(wall):
        print("{}-{}-{} {}:{}:{}".format(
            random.randint(0,20)+2000,
            random.randint(0,12)+1,
            random.randint(0,31)+1,
            random.randint(0,24)+1,
            random.randint(0,60)+1,
            random.randint(0,60)+1
            ))

if __name__ == '__main__':
    main(sys.argv)
