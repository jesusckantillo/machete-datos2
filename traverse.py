from __future__ import annotations
from typing import Optional
from trees import Tree, Node

def preorder(node: Optional["Node"]) -> None:
    if node is not None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

preorder(Tree.root)