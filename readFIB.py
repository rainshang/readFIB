#!/usr/local/bin/python3
import sys
import pyttsx3


def main():
    if len(sys.argv) > 1:
        fibFile = sys.argv[1]
    else:
        fibFile = '../FIB.md'
    engine = pyttsx3.init()
    for line in open(fibFile, 'r').readlines():
        if line and line[0].isalpha():
            input('Press any key (etc. Enter) to continue...')
            print(line)
            engine.say(line.split(' ')[0])
            engine.runAndWait()


if __name__ == "__main__":
    main()