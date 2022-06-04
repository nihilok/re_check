import re

from re_check.arguments import parse_args

if __name__ == "__main__":
    pattern, text = parse_args()
    regex = re.compile(pattern)

    result = regex.findall(text)

    if result is not None:
        print(f'{pattern=}')
        print(f'{text=}')
        print(f'found {len(result)} matches')
        print(result)
    else:
        print('No matches found')
