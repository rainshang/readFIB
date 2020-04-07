#!/usr/local/bin/python3
import sys
import pyttsx3


class PrintColors:
    RED = '\033[1;31m'
    GREEN = '\033[0;32m'
    RESET = '\033[0;0m'


def main():
    if len(sys.argv) > 1:
        fibFile = sys.argv[1]
    else:
        fibFile = '../FIB.md'
    engine = pyttsx3.init()
    input('Press any key (etc. Enter) to start...')
    for line in open(fibFile, 'r').readlines():
        if line and line[0].isalpha():
            word = line.split(' ')[0]
            engine.say(word)
            engine.runAndWait()
            answer = input('Your answer: ')
            if word == answer:
                print(f'{PrintColors.GREEN}Nice work~{PrintColors.RESET}')
            else:
                print(
                    f'Correct answer is: {PrintColors.RED}{word}{PrintColors.RESET}'
                )


if __name__ == "__main__":
    main()