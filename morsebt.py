import binary_tree
def morseEncode(tree, character, code):
    if tree==None:
        return False
    elif tree.value==character:
        return True
    else:  
        if morseEncode(tree.left,character,code)==True:
            code.append(".")
            return True
        elif morseEncode(tree.right,character,code)==True:
            code.append("-")
            return True
def morseDecode(tree,code,i):
    if i == len(code):
        return tree.value
    elif code[i]=='.':
        i+=1
        if tree.left:
            return morseDecode(tree.left,code,i)
    elif code[i]=='-':
        i+=1
        if tree.right:
            return morseDecode(tree.right,code,i)


def initMorseBT():
    #initialize morse binary tree manually
    #we cannot use insert function because morse only has dot and dashes
    binarytree = binary_tree.BinaryTree("START") #root node
    binarytree.left = binary_tree.BinaryTree("E")
    binarytree.right = binary_tree.BinaryTree("T")
    binarytree.left.left = binary_tree.BinaryTree("I")
    binarytree.left.right = binary_tree.BinaryTree("A")
    binarytree.right.left = binary_tree.BinaryTree("N")
    binarytree.right.right = binary_tree.BinaryTree("M")
    binarytree.left.left.left = binary_tree.BinaryTree("S")
    binarytree.left.left.right = binary_tree.BinaryTree("U")
    binarytree.left.right.left = binary_tree.BinaryTree("R")
    binarytree.left.right.right = binary_tree.BinaryTree("W")
    binarytree.right.left.left = binary_tree.BinaryTree("D")
    binarytree.right.left.right = binary_tree.BinaryTree("K")
    binarytree.right.right.left = binary_tree.BinaryTree("G")
    binarytree.right.right.right = binary_tree.BinaryTree("O")

    binarytree.left.left.left.left = binary_tree.BinaryTree("H")
    binarytree.left.left.left.right = binary_tree.BinaryTree("V")
    binarytree.left.left.right.left = binary_tree.BinaryTree("F")
    binarytree.left.left.right.right = binary_tree.BinaryTree("")
    binarytree.left.right.left.left = binary_tree.BinaryTree("L")
    binarytree.left.right.left.right = binary_tree.BinaryTree("")
    binarytree.left.right.right.left = binary_tree.BinaryTree("P")
    binarytree.left.right.right.right = binary_tree.BinaryTree("J")
    binarytree.right.left.left.left = binary_tree.BinaryTree("B")
    binarytree.right.left.left.right = binary_tree.BinaryTree("X")
    binarytree.right.left.right.left = binary_tree.BinaryTree("C")
    binarytree.right.left.right.right = binary_tree.BinaryTree("Y")
    binarytree.right.right.left.left = binary_tree.BinaryTree("Z")
    binarytree.right.right.left.right = binary_tree.BinaryTree("Q")
    binarytree.right.right.right.left = binary_tree.BinaryTree("")
    binarytree.right.right.right.right = binary_tree.BinaryTree("")

    #special characters insertion
    binarytree.left.left.left.left.left = binary_tree.BinaryTree("")
    binarytree.left.left.left.left.right = binary_tree.BinaryTree("")
    binarytree.left.left.left.right.left = binary_tree.BinaryTree("")
    binarytree.left.left.left.right.right = binary_tree.BinaryTree("")
    binarytree.left.left.right.left.left = binary_tree.BinaryTree("")
    binarytree.left.left.right.left.right = binary_tree.BinaryTree("¿")
    binarytree.left.left.right.right.left = binary_tree.BinaryTree("?")
    binarytree.left.left.right.right.right = binary_tree.BinaryTree("")
    binarytree.left.right.left.left.left = binary_tree.BinaryTree("&")
    binarytree.left.right.left.left.right = binary_tree.BinaryTree("")
    binarytree.left.right.left.right.left = binary_tree.BinaryTree("+")
    binarytree.left.right.left.right.right = binary_tree.BinaryTree("")
    binarytree.left.right.right.left.left = binary_tree.BinaryTree("")
    binarytree.left.right.right.left.right = binary_tree.BinaryTree("")
    binarytree.left.right.right.right.left = binary_tree.BinaryTree("")
    binarytree.left.right.right.right.right = binary_tree.BinaryTree("")
    binarytree.right.left.left.left.left = binary_tree.BinaryTree("")
    binarytree.right.left.left.left.right = binary_tree.BinaryTree("")
    binarytree.right.left.left.right.left = binary_tree.BinaryTree("")
    binarytree.right.left.left.right.right = binary_tree.BinaryTree("")
    binarytree.right.left.right.left.left = binary_tree.BinaryTree("")
    binarytree.right.left.right.left.right = binary_tree.BinaryTree("")
    binarytree.right.left.right.right.left = binary_tree.BinaryTree("(")
    binarytree.right.left.right.right.right = binary_tree.BinaryTree("")
    binarytree.right.right.left.left.left = binary_tree.BinaryTree("")
    binarytree.right.right.left.left.right = binary_tree.BinaryTree("")
    binarytree.right.right.left.right.left = binary_tree.BinaryTree("")
    binarytree.right.right.left.right.right = binary_tree.BinaryTree("")
    binarytree.right.right.right.left.left = binary_tree.BinaryTree("")
    binarytree.right.right.right.left.right = binary_tree.BinaryTree("")
    binarytree.right.right.right.right.left = binary_tree.BinaryTree("")
    binarytree.right.right.right.right.right = binary_tree.BinaryTree("")
    binarytree.left.right.left.right.left.right = binary_tree.BinaryTree(".")
    binarytree.right.right.left.left.right.right = binary_tree.BinaryTree(",")
    binarytree.right.left.right.right.left.right = binary_tree.BinaryTree(")")
    binarytree.right.left.left.left.left.right = binary_tree.BinaryTree("-")
    binarytree.right.right.left.left.left.right = binary_tree.BinaryTree("¡")
    binarytree.left.left.right.right.left.right = binary_tree.BinaryTree("_")
    binarytree.left.right.right.right.right.left = binary_tree.BinaryTree("'")
    binarytree.right.right.right.left.left.left = binary_tree.BinaryTree(":")
    binarytree.left.right.left.left.right.left = binary_tree.BinaryTree('"')
    binarytree.right.left.right.left.right.right = binary_tree.BinaryTree("!")
    binarytree.right.left.right.left.right.left = binary_tree.BinaryTree(";")
    binarytree.left.left.left.right.left.left = binary_tree.BinaryTree("")
    binarytree.left.left.left.right.left.left.right = binary_tree.BinaryTree("$")
    return binarytree

