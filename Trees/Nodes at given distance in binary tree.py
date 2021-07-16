from collections import defaultdict

class solver:

    def makeGraph(self, root):
        vertList = defaultdict(list)
        visited = set()
        queue = []
        queue.append(root)

        while len(queue) > 0:
            curr = queue.pop(0)
            visited.add(curr)

            if curr.left is not None and curr.left not in visited:
                vertList[curr.data].append(curr.left.data)
                vertList[curr.left.data].append(curr.data)

                queue.append(curr.left)

            if curr.right is not None and curr.right not in visited:
                vertList[curr.data].append(curr.right.data)
                vertList[curr.right.data].append(curr.data)

                queue.append(curr.right)
        return vertList
