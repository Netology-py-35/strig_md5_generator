import hashlib


def string_md5(file_path):
    with open(file_path, 'r') as file:
        for line in file.readline():
            result = hashlib.md5(line.encode("utf-8")).hexdigest()
            yield result


if __name__ == '__main__':
    for md5 in string_md5('test.txt'):
        print(md5)
