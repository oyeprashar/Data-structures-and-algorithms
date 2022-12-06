str1 = "4(2(3)(1))(6(5))"
root = generateTree(0,len(str1)-1,str1)

preorder(root)