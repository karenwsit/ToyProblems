#Implementation of Building a Parse Tree


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")

#Evaluating a Parse Tree via postorder traversal

def postordereval(parseTree):

    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if parseTree:
        res1 = postordereval(parseTree.getLeftChild())
        res2 = postordereval(parseTree.getRightChild())
        if res1 and res2:
            return opers[parseTree.getRootVal()](res1, res2)
        else:
            return parseTree.getRootVal()
