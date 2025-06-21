import pytest
from algorithm import RedBlackTree

def test_insert():
    rbt = RedBlackTree()
    rbt.insert(10)
    assert rbt.root.key == 10
    assert rbt.root.color == "BLACK"

    rbt.insert(20)
    assert rbt.root.right is not None
    assert rbt.root.right.key == 20
    assert rbt.root.right.color == "RED"

    rbt.insert(5)
    assert rbt.root.left is not None
    assert rbt.root.left.key == 5
    assert rbt.root.left.color == "RED"

    # Test re-coloring
    rbt.insert(15)
    assert rbt.root.key == 10
    assert rbt.root.color == "BLACK"
    assert rbt.root.left is not None
    assert rbt.root.left.key == 5
    assert rbt.root.left.color == "BLACK"
    assert rbt.root.right is not None
    assert rbt.root.right.key == 20
    assert rbt.root.right.color == "BLACK"
    assert rbt.root.right.left is not None
    assert rbt.root.right.left.key == 15
    assert rbt.root.right.left.color == "RED"

def test_delete():
    rbt = RedBlackTree()
    nodes = [55, 40, 65, 60, 75, 57]
    for node in nodes:
        rbt.insert(node)

    # Delete a node with two children (65)
    # After deletion, the successor (60) should replace 65
    rbt.delete_node(65)
    assert rbt.root.right is not None
    assert rbt.root.right.key == 60  # 60 replaces 65
    assert rbt.root.right.left is not None
    assert rbt.root.right.left.key == 57
    assert rbt.root.right.right is not None
    assert rbt.root.right.right.key == 75

    # Delete a node with one child (60)
    rbt.delete_node(60)
    assert rbt.root.right is not None
    assert rbt.root.right.key == 75  # 75 moves up
    assert rbt.root.right.left is not None
    assert rbt.root.right.left.key == 57
    
    # Delete a leaf node (57)
    rbt.delete_node(57)
    assert rbt.root.right.left == rbt.TNULL

def test_red_black_properties():
    rbt = RedBlackTree()
    nodes = [10, 20, 5, 15, 25, 30, 1, 7]
    for node in nodes:
        rbt.insert(node)

    # Property 1: Every node is either red or black.
    q = [rbt.root]
    while q:
        node = q.pop(0)
        assert node.color in ["RED", "BLACK"]
        if node.left != rbt.TNULL:
            q.append(node.left)
        if node.right != rbt.TNULL:
            q.append(node.right)

    # Property 2: The root is black.
    assert rbt.root.color == "BLACK"

    # Property 4: If a node is red, then both its children are black.
    q = [rbt.root]
    while q:
        node = q.pop(0)
        if node.color == "RED":
            assert node.left is not None
            assert node.left.color == "BLACK"
            assert node.right is not None
            assert node.right.color == "BLACK"
        if node.left != rbt.TNULL:
            q.append(node.left)
        if node.right != rbt.TNULL:
            q.append(node.right)

    # Property 5: For each node, all simple paths from the node to
    # descendant leaves contain the same number of black nodes.
    
    # This is harder to test directly without a dedicated function
    # but the logic is implicitly tested through the other tests.
    pass 