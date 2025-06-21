import graphviz
from algorithm import RedBlackTree, Node

def plot_tree(tree):
    if tree.root == tree.TNULL:
        return None
    
    dot = graphviz.Digraph(comment='Red-Black Tree')
    dot.attr('node', shape='circle', style='filled', fontcolor='white')
    
    q = [tree.root]
    
    while q:
        node = q.pop(0)
        
        if node != tree.TNULL:
            dot.node(str(node.key), fillcolor=node.color.lower())
            
            if node.left != tree.TNULL:
                dot.edge(str(node.key), str(node.left.key))
                q.append(node.left)
            
            if node.right != tree.TNULL:
                dot.edge(str(node.key), str(node.right.key))
                q.append(node.right)
                
    return dot 