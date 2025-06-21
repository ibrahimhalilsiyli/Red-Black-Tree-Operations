import graphviz
from algorithm import RedBlackTree, Node

def plot_tree(tree):
    """Create a compact and efficient visualization of the Red-Black Tree"""
    if tree.root == tree.TNULL:
        return None
    
    try:
        # Create the graph with minimal settings
        dot = graphviz.Digraph(comment='Red-Black Tree')
        
        # Use very compact settings for better performance
        dot.attr(rankdir='TB', dpi='72', concentrate='false')
        
        # Calculate tree size for ultra-compact sizing
        node_count = count_nodes(tree)
        
        # Optimize for performance - use smaller sizes for large trees
        if node_count <= 10:
            # Small tree - medium nodes
            node_size = '0.5'
            font_size = '10'
            graph_size = '6,5'
            node_sep = '0.3'
            rank_sep = '0.3'
        elif node_count <= 25:
            # Medium tree - small nodes
            node_size = '0.4'
            font_size = '8'
            graph_size = '7,6'
            node_sep = '0.2'
            rank_sep = '0.2'
        else:
            # Large tree - very small nodes for performance
            node_size = '0.3'
            font_size = '7'
            graph_size = '10,8'
            node_sep = '0.1'
            rank_sep = '0.1'
        
        # Set minimal node attributes for better performance
        dot.attr('node', 
                shape='circle',
                style='filled',
                fontcolor='white',
                width=node_size,
                height=node_size,
                fontsize=font_size,
                margin='0.01',
                penwidth='0.5')
        
        # Set minimal graph size and spacing
        dot.attr(size=graph_size,
                nodesep=node_sep,
                ranksep=rank_sep)
        
        # Traverse tree and add nodes and edges
        _add_nodes_and_edges_compact(dot, tree)
        
        return dot
        
    except Exception as e:
        print(f"Error in tree visualization: {e}")
        return None

def _add_nodes_and_edges_compact(dot, tree):
    """Helper function to add nodes and edges with minimal overhead"""
    if tree.root == tree.TNULL:
        return
    
    # Use breadth-first traversal
    queue = [tree.root]
    
    while queue:
        current_node = queue.pop(0)
        
        if current_node != tree.TNULL:
            # Create node with minimal styling
            node_color = 'red' if current_node.color == "RED" else 'black'
            dot.node(str(current_node.key), fillcolor=node_color)
            
            # Add edges to children
            if current_node.left != tree.TNULL:
                dot.edge(str(current_node.key), str(current_node.left.key))
                queue.append(current_node.left)
            
            if current_node.right != tree.TNULL:
                dot.edge(str(current_node.key), str(current_node.right.key))
                queue.append(current_node.right)

def count_nodes(tree):
    """Count total number of nodes in the tree"""
    if tree.root == tree.TNULL:
        return 0
    
    def count_recursive(node):
        if node == tree.TNULL:
            return 0
        return 1 + count_recursive(node.left) + count_recursive(node.right)
    
    return count_recursive(tree.root)

def get_tree_height(tree):
    """Get the height of the tree"""
    if tree.root == tree.TNULL:
        return 0
    
    def height_recursive(node):
        if node == tree.TNULL:
            return -1
        return 1 + max(height_recursive(node.left), height_recursive(node.right))
    
    return height_recursive(tree.root)

def get_black_height(tree):
    """Get the black height of the tree (number of black nodes from root to any leaf)"""
    if tree.root == tree.TNULL:
        return 0
    
    def black_height_recursive(node):
        if node == tree.TNULL:
            return 0
        
        # Count black nodes on the path
        black_count = 1 if node.color == "BLACK" else 0
        
        # All paths should have the same black height
        left_height = black_height_recursive(node.left)
        right_height = black_height_recursive(node.right)
        
        # Return the black height plus current node if it's black
        return black_count + left_height
    
    return black_height_recursive(tree.root)

def validate_red_black_properties(tree):
    """Validate that the tree satisfies all Red-Black Tree properties"""
    if tree.root == tree.TNULL:
        return True, "Empty tree is valid"
    
    violations = []
    
    # Property 1: Every node is either red or black
    def check_colors(node):
        if node == tree.TNULL:
            return
        if node.color not in ["RED", "BLACK"]:
            violations.append(f"Node {node.key} has invalid color: {node.color}")
        check_colors(node.left)
        check_colors(node.right)
    
    # Property 2: Root is black
    if tree.root.color != "BLACK":
        violations.append("Root is not black")
    
    # Property 4: Red nodes cannot have red children
    def check_red_children(node):
        if node == tree.TNULL:
            return
        if node.color == "RED":
            if node.left != tree.TNULL and node.left.color == "RED":
                violations.append(f"Red node {node.key} has red left child {node.left.key}")
            if node.right != tree.TNULL and node.right.color == "RED":
                violations.append(f"Red node {node.key} has red right child {node.right.key}")
        check_red_children(node.left)
        check_red_children(node.right)
    
    # Property 5: All paths from root to leaves have same number of black nodes
    def get_black_height_path(node):
        if node == tree.TNULL:
            return 0
        black_count = 1 if node.color == "BLACK" else 0
        return black_count + get_black_height_path(node.left)
    
    def check_black_height_consistency(node, expected_height, current_height):
        if node == tree.TNULL:
            if current_height != expected_height:
                violations.append(f"Path to leaf has black height {current_height}, expected {expected_height}")
            return
        
        new_height = current_height + (1 if node.color == "BLACK" else 0)
        check_black_height_consistency(node.left, expected_height, new_height)
        check_black_height_consistency(node.right, expected_height, new_height)
    
    # Run all checks
    check_colors(tree.root)
    check_red_children(tree.root)
    
    expected_black_height = get_black_height_path(tree.root)
    check_black_height_consistency(tree.root, expected_black_height, 0)
    
    if violations:
        return False, f"Violations found: {'; '.join(violations)}"
    else:
        return True, "All Red-Black Tree properties are satisfied"

def get_tree_statistics(tree):
    """Get comprehensive statistics about the tree"""
    stats = {
        'total_nodes': count_nodes(tree),
        'height': get_tree_height(tree),
        'black_height': get_black_height(tree),
        'is_valid': validate_red_black_properties(tree)[0],
        'validation_message': validate_red_black_properties(tree)[1]
    }
    return stats

def measure_operation_time(operation_func, *args, **kwargs):
    """Measure the execution time of a tree operation"""
    import time
    start_time = time.time()
    result = operation_func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time 