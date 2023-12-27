import re


def parse(s):
    url = re.search(
        r'^(?:.+)?src="https://www\.youtube\.com/embed/([a-zA-Z0-9]+)"(?:.+)?', s)
    if url:
        return f'https://youtu.be/{url.group(1)}'
    else:
        return None


def main():
    print(parse(input('HTML: ')))


if __name__ == "__main__":
    main()
