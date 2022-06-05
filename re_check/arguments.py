from argparse import ArgumentParser
import sys

from re_check.constants import DEFAULT_TEXT, LOREM

parser = ArgumentParser(description="Check Regex Syntax (Python)")

parser.add_argument('-t', '--text', nargs=1, metavar='<TEXT>')

parser.add_argument('-l', '--lorem', action="store_true")

parser.add_argument('pattern', nargs=1, metavar='<PATTERN>')


def parse_args():
    namespace = parser.parse_args(sys.argv[1:])
    pattern = namespace.pattern[0] if namespace.pattern is not None else None
    text = namespace.text[0] if namespace.text is not None else LOREM if namespace.lorem else DEFAULT_TEXT
    return pattern, text


if __name__ == "__main__":
    parser.print_help()
