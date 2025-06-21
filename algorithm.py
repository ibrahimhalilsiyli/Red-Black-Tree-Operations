import sys
import copy
import time

class Node:
    def __init__(self, key, color="RED", parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
    
    def __copy__(self):
        return Node(self.key, self.color, self.parent, self.left, self.right)
    
    def __deepcopy__(self, memo):
        if self in memo:
            return memo[self]
        
        new_node = Node(self.key, self.color)
        memo[self] = new_node
        
        # Don't deepcopy parent to avoid circular references
        # Parent will be set by the tree structure
        if self.left is not None and self.left != self:  # Avoid self-reference
            new_node.left = copy.deepcopy(self.left, memo)
        if self.right is not None and self.right != self:  # Avoid self-reference
            new_node.right = copy.deepcopy(self.right, memo)
        
        return new_node

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, "BLACK")
        self.root = self.TNULL
        self.operation_history = []  # Track operations for visualization

    def add_operation_step(self, description, operation_type="operation"):
        """Add a step to the operation history for visualization"""
        # Create deep copy for all operations to ensure accurate visualization
        tree_copy = copy.deepcopy(self)
        
        self.operation_history.append({
            'description': description,
            'tree_state': tree_copy,
            'step_type': operation_type,  # Use 'step_type' to match app.py
            'timestamp': time.time()
        })

    def insert(self, key):
        # Add initial step for all operations
        self.add_operation_step(f"Starting insertion of {key}", "start")
        
        node = Node(key, "RED", left=self.TNULL, right=self.TNULL)
        
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Add step after basic insertion
        self.add_operation_step(f"Inserted {key} as red node", "insert")

        if node.parent is None:
            node.color = "BLACK"
            self.add_operation_step(f"Root node {key} colored black", "recolor")
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    # Case 1: Uncle is red - recoloring
                    self.add_operation_step(f"Case 1: Uncle is red - recoloring nodes", "recolor")
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: Uncle is black, node is left child - right rotation
                        self.add_operation_step(f"Case 2: Right rotation on parent", "rotation")
                        k = k.parent
                        self.right_rotate(k)
                    # Case 3: Uncle is black, node is right child - left rotation
                    self.add_operation_step(f"Case 3: Left rotation on grandparent", "rotation")
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == "RED":
                    # Case 1: Uncle is red - recoloring
                    self.add_operation_step(f"Case 1: Uncle is red - recoloring nodes", "recolor")
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Case 2: Uncle is black, node is right child - left rotation
                        self.add_operation_step(f"Case 2: Left rotation on parent", "rotation")
                        k = k.parent
                        self.left_rotate(k)
                    # Case 3: Uncle is black, node is left child - right rotation
                    self.add_operation_step(f"Case 3: Right rotation on grandparent", "rotation")
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"
        self.add_operation_step("Final step: Root colored black", "recolor")

    def delete_node(self, key):
        z = self.TNULL
        node = self.root
        while node != self.TNULL:
            if node.key == key:
                z = node
            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Key not found in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == "BLACK":
            self.fix_delete(x)
    
    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    s = x.parent.right
                
                if s.left.color == "BLACK" and s.right.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.right.color == "BLACK":
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.right_rotate(s)
                        s = x.parent.right
                    
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    s = x.parent.left
                
                if s.right.color == "BLACK" and s.left.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.left.color == "BLACK":
                        s.right.color = "RED"
                        s.color = "BLACK"
                        self.left_rotate(s)
                        s = x.parent.left
                    
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"
    
    def rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    
    def search(self, key):
        """Search for a key in the tree"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """Recursive search helper"""
        if node == self.TNULL or key == node.key:
            return node
        
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key) 