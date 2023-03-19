import argparse

parser = argparse.ArgumentParser(description='Find a subclass in a file')
parser.add_argument('filename', type=str, help='the name of the file to search')
parser.add_argument('subclass', type=str, help='the subclass to find')
args = parser.parse_args()

with open(args.filename, 'r') as subclasses:
    pointer = subclasses.read()
    lst = list(pointer.split(','))
    for item in lst:
        if args.subclass in item:
            print('{0}: {1}'.format(lst.index(item), item))
