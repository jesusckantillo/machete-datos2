class Node:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class Tree:

    def __init__(self, root: "Node") -> None:
        self.root = root

    @staticmethod
    def create_dummy_tree() -> "Tree":
        nodes = [Node(chr(x)) for x in range(65, 76)]

        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]

        nodes[1].left = nodes[3]
        nodes[1].right = nodes[4]

        nodes[2].right = nodes[5]

        nodes[3].left = nodes[6]
        nodes[3].right = nodes[7]

        nodes[5].left = nodes[8]
        nodes[5].right = nodes[9]

        nodes[7].left = nodes[10]

        return Tree(nodes[0])