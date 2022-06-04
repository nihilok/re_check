from argparse import ArgumentParser
import sys

parser = ArgumentParser(description="Check Regex Syntax (Python)")

parser.add_argument('-t', '--text', nargs=1, metavar='<TEXT>')

parser.add_argument('pattern', nargs=1, metavar='<PATTERN>')


def parse_args():
    namespace = parser.parse_args(sys.argv[1:])
    pattern = namespace.pattern[0]
    text = namespace.text[0] or "The quick brown fox jumped over the lazy dog."
    return pattern, text


if __name__ == "__main__":
    parser.print_help()