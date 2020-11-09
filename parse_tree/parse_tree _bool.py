from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator


def buildParseTree(fpexp):
    fplist = split_expression(fpexp)  # Exercise question
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


def split_expression(a_string):
    """
    Split the expression, will ignore spaces.
    This assumes digits are not larger than 3.
    This is exercise 1 in runestone
    :return: list of the split expression
    """
    final = [i for i in a_string if i != ' ']
    final_rng = len(final) - 1
    i = 0
    while i < final_rng:
        if final[i] in '0123456789':
            next_idx = i + 1
            while final[next_idx] in '0123456789' and next_idx < final_rng:
                final[i] += final[next_idx]
                final.pop(next_idx)
                final_rng = final_rng - 1

        i += 1

    return final


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv,
             '<': operator.lt, '>': operator.gt}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()
