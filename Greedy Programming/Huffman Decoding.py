def decodeHuffmanData(root, binaryString):
    res = ""
    currRoot = root

    for bit in binaryString:
        if currRoot.left is None and currRoot.right is None:
            res += currRoot.data
            currRoot = root

        if bit == '0':
            currRoot = currRoot.left

        if bit == '1':
            currRoot = currRoot.right

    res += currRoot.data

    return res