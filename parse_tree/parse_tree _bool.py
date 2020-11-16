from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator


def buildParseTree(fpexp):
    fplist = split_expression(fpexp)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['and', 'or', 'not']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['and', 'or', 'not', ')']:
            try:
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree


def split_expression(fpexp):
    a_list = fpexp.split()
    for i in range(len(a_list) - 1):
        if a_list[i] == 'True':
            a_list[i] = True
        elif a_list[i] == 'False':
            a_list[i] = False
        elif a_list[i] not in 'andornot()':
            raise NameError("Only True, False and logic operators allowed")
    return a_list


def evaluate(parseTree):
    opers = {'and': operator.and_, 'or': operator.or_,
             'not': operator.not_}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    result = None
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        result = fn(evaluate(leftC), evaluate(rightC))
    elif leftC or rightC:
        fn = opers[parseTree.getRootVal()]
        if leftC and rightC is None: # Not Operator
            result = fn(evaluate(leftC))
        elif rightC and leftC is None: # Not Operator
            result = fn(evaluate(rightC))
    else:
        result = parseTree.getRootVal()

    return result


def main():
    pt = buildParseTree('( False and False )')  #False
    pt1 = buildParseTree('( False and True )')  # False
    pt2 = buildParseTree('( False or True )')  # True
    #  pt3 = buildParseTree('( not False )') # True
    #  pt.postorder()
    print(evaluate(pt))
    print(evaluate(pt1))
    print(evaluate(pt2))
    #  print(evaluate(pt3))



if __name__ == '__main__':
    main()
