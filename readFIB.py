#!/usr/local/bin/python3
import argparse
import sys
import pyttsx3


class PrintColors:
    RED = '\033[1;31m'
    GREEN = '\033[0;32m'
    RESET = '\033[0;0m'


__UN_MASTERED_TAG__ = '</meijizhu>'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        dest='fib_file',
        type=argparse.FileType('r'),
        default='../FIB.md',
        help=
        'The dictation file you want to use. Default value is \'../FIB.md\'')
    parser.add_argument(
        '-s',
        '--startline',
        dest='start_line',
        type=int,
        default=0,
        help='The line you want to start from. Default value is 1')
    parser.add_argument(
        '-o',
        '--onlyum',
        dest='only_unmastered',
        action='store_true',
        help=
        'Only dictate the words you haven\'t mastered, which lines contain <meijizhu> tag. Default ignored.'
    )
    args = parser.parse_args()
    args.start_line -= 1

    engine = pyttsx3.init()
    input('Press Enter to start...')
    for index, line in enumerate(args.fib_file.readlines()):
        if index >= args.start_line:
            if line and line[0].isalpha():
                if not args.only_unmastered or __UN_MASTERED_TAG__ in line:
                    __process_line(line, engine)


def __process_line(line, engine):
    word = line.split(' ')[0]
    engine.say(word)
    engine.runAndWait()
    answer = input('Your answer: ')
    if word == answer:
        print(f'{PrintColors.GREEN}Nice work~{PrintColors.RESET}  {line}',
              end='')
    else:
        print(
            f'Correct answer is: {PrintColors.RED}{word}{PrintColors.RESET}  {line}',
            end='')


if __name__ == "__main__":
    main()