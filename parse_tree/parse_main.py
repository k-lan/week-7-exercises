from parse_tree import *


def main():
    pt = buildParseTree("( (10 + 5) *3 )")
    pt.postorder()
    print(split_expression("( (100 + 5) *3 )"))


if __name__ == '__main__':
    main()
