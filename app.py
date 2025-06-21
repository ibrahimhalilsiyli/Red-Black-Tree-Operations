import streamlit as st
from algorithm import RedBlackTree
from utils import plot_tree, get_tree_statistics
import copy
import time
import random

def get_tree():
    if 'tree' not in st.session_state:
        st.session_state.tree = RedBlackTree()
    return st.session_state.tree

def get_operation_history():
    if 'operation_history' not in st.session_state:
        st.session_state.operation_history = []
    return st.session_state.operation_history

def add_operation_step(description, tree_state, step_type="operation"):
    history = get_operation_history()
    
    # Check if this is a duplicate of the last step
    if history and history[-1]['description'] == description:
        return  # Skip duplicate steps
    
    # Limit history size for performance
    if len(history) > 30:
        history = history[-25:]  # Keep only last 25 steps
        st.session_state.operation_history = history
    
    history.append({
        'description': description,
        'tree_state': copy.deepcopy(tree_state),
        'step_type': step_type,
        'timestamp': time.time()
    })

def get_tree_height(tree):
    """Calculate the height of the tree"""
    if tree.root == tree.TNULL:
        return 0
    
    def height_recursive(node):
        if node == tree.TNULL:
            return 0
        return 1 + max(height_recursive(node.left), height_recursive(node.right))
    
    return height_recursive(tree.root)

def main():
    st.set_page_config(page_title="Red-Black Tree Visualizer", layout="wide")
    st.title("🌳 Red-Black Tree Visualizer")
    st.markdown("Interactive visualization of Red-Black Tree operations with step-by-step explanations")

    # Sidebar for controls
    with st.sidebar:
        st.header("🎛️ Controls")
        
        # Algorithm settings
        st.subheader("Algorithm Settings")
        auto_step_delay = st.slider("Step Delay (seconds)", 0.0, 2.0, 0.5, 0.1)
        show_explanations = st.checkbox("Show Step Explanations", value=True)
        
        # Test cases
        st.subheader("📋 Test Cases")
        test_case = st.selectbox(
            "Choose Test Case:",
            ["Custom Input", "Best Case", "Average Case", "Worst Case", "Random Data"]
        )
        
        if test_case == "Best Case":
            test_data = [10, 5, 15, 3, 7, 12, 18]
            st.info("Best Case: Balanced insertion sequence")
        elif test_case == "Average Case":
            test_data = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
            st.info("Average Case: Random-like insertion sequence")
        elif test_case == "Worst Case":
            test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            st.info("Worst Case: Sequential insertion (requires many rotations)")
        elif test_case == "Random Data":
            test_data = random.sample(range(1, 100), 15)
            st.info("Random Case: 15 random numbers")
        else:
            test_data = []
        
        if test_case != "Custom Input" and st.button("Load Test Case"):
            tree = get_tree()
            tree.__init__()  # Reset tree
            st.session_state.tree = tree
            
            for value in test_data:
                add_operation_step(f"Inserting {value}", tree)
                tree.insert(value)
                add_operation_step(f"After inserting {value}", tree, "result")
            
            st.success(f"Loaded {len(test_data)} nodes from {test_case}")
        
        # Clear buttons
        if st.button("🗑️ Clear Tree"):
            tree = get_tree()
            tree.__init__()
            st.session_state.tree = tree
            st.session_state.operation_history = []
            st.success("Tree cleared!")
        
        if st.button("📝 Clear History"):
            st.session_state.operation_history = []
            st.success("History cleared!")

    # Main content area
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("🎯 Operations")
        
        # Insert operation
        st.subheader("Insert Node")
        insert_value = st.number_input("Value to insert:", value=0, step=1, key="insert_input")
        col_insert1, col_insert2 = st.columns(2)
        
        with col_insert1:
            if st.button("➕ Insert"):
                tree = get_tree()
                # Only track before and after states for better performance
                add_operation_step(f"Before inserting {insert_value}", tree)
                tree.insert(insert_value)
                add_operation_step(f"After inserting {insert_value}", tree, "result")
                st.success(f"Inserted {insert_value}")
        
        with col_insert2:
            if st.button("🔄 Insert with Steps"):
                tree = get_tree()
                # Clear previous operation history
                tree.operation_history = []
                
                # Perform insertion with detailed steps
                tree.insert(insert_value)
                
                # Only add the final result to avoid overwhelming the history
                if tree.operation_history:
                    # Take only the last few meaningful steps
                    meaningful_steps = []
                    for step in tree.operation_history:
                        if step['operation_type'] in ['start', 'rotation', 'recolor']:
                            meaningful_steps.append(step)
                    
                    # Add only the most important steps (max 3)
                    for step in meaningful_steps[-3:]:
                        add_operation_step(step['description'], step['tree_state'], step['operation_type'])
                
                st.success(f"Inserted {insert_value} with detailed Red-Black Tree operations")

        # Delete operation
        st.subheader("Delete Node")
        delete_value = st.number_input("Value to delete:", value=0, step=1, key="delete_input")
        col_delete1, col_delete2 = st.columns(2)
        
        with col_delete1:
            if st.button("🗑️ Delete"):
                tree = get_tree()
                add_operation_step(f"Before deleting {delete_value}", tree)
                tree.delete_node(delete_value)
                add_operation_step(f"After deleting {delete_value}", tree, "result")
                st.success(f"Deleted {delete_value}")
        
        with col_delete2:
            if st.button("🔄 Delete with Steps"):
                tree = get_tree()
                add_operation_step(f"Starting deletion of {delete_value}", tree)
                tree.delete_node(delete_value)
                add_operation_step(f"Completed deletion of {delete_value}", tree, "result")
                st.success(f"Deleted {delete_value} with detailed steps")

        # Search operation
        st.subheader("Search Node")
        search_value = st.number_input("Value to search:", value=0, step=1, key="search_input")
        if st.button("🔍 Search"):
            tree = get_tree()
            result = tree.search(search_value)
            if result != tree.TNULL:
                st.success(f"✅ Found {search_value} in the tree")
                st.info(f"Node color: {result.color}")
            else:
                st.error(f"❌ {search_value} not found in the tree")

    with col2:
        st.header("🌳 Tree Visualization")
        tree = get_tree()
        
        if tree.root != tree.TNULL:
            # Compact visualization controls
            col_viz1, col_viz2 = st.columns(2)
            
            with col_viz1:
                show_stats = st.checkbox("Show Stats", value=True)
            with col_viz2:
                compact_mode = st.checkbox("Compact Mode", value=True)
            
            # Create and display the tree visualization
            dot = plot_tree(tree)
            if dot:
                # Use a smaller, more compact container
                if compact_mode:
                    # Create a very large container for the chart in compact mode
                    with st.container():
                        st.markdown("""
                        <style>
                        .very-large-chart {
                            max-width: 1200px;
                            margin: auto;
                        }
                        </style>
                        """, unsafe_allow_html=True)
                        st.graphviz_chart(dot, use_container_width=False)
                else:
                    # Full-width mode - balanced visualization
                    st.markdown("**Full-size visualization (use container width)**")
                    st.graphviz_chart(dot, use_container_width=True)
            else:
                st.error("❌ Visualization error")
            
            # Display compact tree statistics
            if show_stats:
                # Cache stats to avoid repeated calculations
                if 'cached_stats' not in st.session_state or st.session_state.get('last_tree_state') != id(tree):
                    stats = get_tree_statistics(tree)
                    st.session_state.cached_stats = stats
                    st.session_state.last_tree_state = id(tree)
                else:
                    stats = st.session_state.cached_stats
                
                # Compact metrics display
                col_stats1, col_stats2, col_stats3 = st.columns(3)
                
                with col_stats1:
                    st.metric("Nodes", stats['total_nodes'])
                with col_stats2:
                    st.metric("Height", stats['height'])
                with col_stats3:
                    st.metric("Black Height", stats['black_height'])
                
                # Compact validation status
                if stats['is_valid']:
                    st.success("✅ Valid Red-Black Tree")
                else:
                    st.error("❌ " + stats['validation_message'][:50] + "...")
        else:
            st.info("🌱 Empty tree - insert nodes to visualize")

    # Red-Black Tree Operations Explanation
    st.header("🔴⚫ Red-Black Tree Operations & Properties")
    
    col_rb1, col_rb2 = st.columns(2)
    
    with col_rb1:
        st.subheader("📋 Red-Black Tree Properties")
        st.markdown("""
        **1. Every node is either red or black**
        - Nodes are colored to maintain balance
        
        **2. Root is always black**
        - Ensures consistent black height
        
        **3. Red nodes cannot have red children**
        - No two red nodes can be adjacent
        
        **4. All paths from root to leaves have same number of black nodes**
        - This is the key to maintaining balance
        
        **5. All leaves (TNULL) are considered black**
        - Provides consistent termination
        """)
        
        st.subheader("🔄 Rotation Operations")
        st.markdown("""
        **Left Rotation:**
        - Moves right child up
        - Preserves BST property
        - Used to fix violations
        
        **Right Rotation:**
        - Moves left child up
        - Preserves BST property
        - Used to fix violations
        """)
    
    with col_rb2:
        st.subheader("🎨 Recoloring Operations")
        st.markdown("""
        **Case 1: Uncle is Red**
        - Recolor parent and uncle to black
        - Recolor grandparent to red
        - Move up to grandparent
        
        **Case 2: Uncle is Black (Triangle)**
        - Rotate parent in opposite direction
        - Creates a line configuration
        
        **Case 3: Uncle is Black (Line)**
        - Rotate grandparent
        - Recolor parent and grandparent
        """)
        
        st.subheader("⚡ Operation Complexity")
        st.markdown("""
        **Time Complexity:**
        - Insert: O(log n)
        - Delete: O(log n)
        - Search: O(log n)
        
        **Space Complexity:**
        - O(n) for tree structure
        - O(1) auxiliary space
        """)

    # Operation Types Legend
    st.subheader("📊 Operation Types")
    col_legend1, col_legend2, col_legend3, col_legend4 = st.columns(4)
    
    with col_legend1:
        st.markdown("**🟢 Start:** Beginning of operation")
    with col_legend2:
        st.markdown("**🔵 Insert:** Basic node insertion")
    with col_legend3:
        st.markdown("**🟡 Rotation:** Tree restructuring")
    with col_legend4:
        st.markdown("**🔴 Recolor:** Color property fixes")

    # Operation History
    st.header("📋 Operation History")
    
    history = get_operation_history()
    if history:
        # Show only the last 5 steps to improve performance
        recent_history = history[-5:] if len(history) > 5 else history
        
        for i, step in enumerate(recent_history):
            step_number = len(history) - len(recent_history) + i + 1
            
            # Color code the expander based on operation type
            if step['step_type'] == "start":
                expander_color = "🟢"
            elif step['step_type'] == "insert":
                expander_color = "🔵"
            elif step['step_type'] == "rotation":
                expander_color = "🟡"
            elif step['step_type'] == "recolor":
                expander_color = "🔴"
            else:
                expander_color = "⚪"
            
            with st.expander(f"{expander_color} Step {step_number}: {step['description']}", expanded=(i == len(recent_history)-1)):
                st.write(f"**Description:** {step['description']}")
                st.write(f"**Operation Type:** {step['step_type']}")
                
                # Add detailed algorithm explanation based on step type
                if step['step_type'] == "start":
                    st.markdown("**Operation Start:** Initialize insertion process")
                elif step['step_type'] == "insert":
                    st.markdown("**Basic Insertion:** Insert node as red leaf")
                elif step['step_type'] == "rotation":
                    st.markdown("**Rotation Operation:** Restructures tree to fix violations")
                elif step['step_type'] == "recolor":
                    st.markdown("**Recoloring Operation:** Changes node colors to fix violations")
                
                # Only show tree visualization for the last step to improve performance
                if i == len(recent_history) - 1:
                    if step['tree_state'].root != step['tree_state'].TNULL:
                        dot = plot_tree(step['tree_state'])
                        if dot:
                            st.graphviz_chart(dot, use_container_width=False)
                    else:
                        st.write("Empty tree")
        
        # Show total steps info
        if len(history) > 5:
            st.info(f"Showing last 5 of {len(history)} total steps. Use 'Clear History' to reset.")
    else:
        st.info("No operations performed yet. Try 'Insert with Steps' to see detailed Red-Black Tree operations!")

    # Complexity Analysis
    st.header("⚡ Complexity Analysis")
    
    col_comp1, col_comp2 = st.columns(2)
    
    with col_comp1:
        st.subheader("Time Complexity")
        st.markdown("""
        | Operation | Average Case | Worst Case | Best Case |
        |-----------|--------------|------------|-----------|
        | **Search** | O(log n) | O(log n) | O(1) |
        | **Insert** | O(log n) | O(log n) | O(log n) |
        | **Delete** | O(log n) | O(log n) | O(log n) |
        | **Rotation** | O(1) | O(1) | O(1) |
        """)
        
        st.markdown("""
        **Why O(log n)?**
        - Red-Black Trees maintain balance
        - Height is always O(log n)
        - Each operation traverses at most the tree height
        """)
    
    with col_comp2:
        st.subheader("Space Complexity")
        st.markdown("""
        | Component | Space Usage |
        |-----------|-------------|
        | **Per Node** | O(1) |
        | **Tree Structure** | O(n) |
        | **Auxiliary Space** | O(1) |
        | **Total** | O(n) |
        """)
        
        st.markdown("""
        **Memory Breakdown:**
        - Each node: key, color, 3 pointers
        - TNULL sentinel: shared across all leaves
        - No recursion stack needed for operations
        """)

    # Test Cases and Examples
    st.header("🧪 Test Cases & Examples")
    
    col_test1, col_test2 = st.columns(2)
    
    with col_test1:
        st.subheader("Predefined Test Cases")
        st.markdown("""
        **Best Case Scenario:**
        - Balanced insertion: [10, 5, 15, 3, 7, 12, 18]
        - Minimal rotations needed
        - Optimal tree structure
        
        **Average Case Scenario:**
        - Random-like insertion: [50, 30, 70, 20, 40, 60, 80, ...]
        - Moderate number of rotations
        - Typical real-world usage
        
        **Worst Case Scenario:**
        - Sequential insertion: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        - Maximum rotations required
        - Tests rebalancing efficiency
        """)
        
        # Edge Cases
        st.subheader("🔍 Edge Cases")
        st.markdown("""
        **Empty Tree:**
        - Insert into empty tree
        - Delete from empty tree
        - Search in empty tree
        
        **Single Node:**
        - Insert into single node tree
        - Delete single node
        - Rotations with single node
        
        **Duplicate Values:**
        - Insert duplicate keys
        - Handle repeated values
        
        **Large Numbers:**
        - Very large integer values
        - Negative numbers
        - Zero values
        """)
    
    with col_test2:
        st.subheader("Custom Test Cases")
        st.markdown("""
        **Try these custom sequences:**
        
        **Rotation Test:**
        ```
        [10, 20, 30, 40, 50]
        ```
        
        **Color Violation Test:**
        ```
        [5, 3, 7, 1, 9]
        ```
        
        **Complex Scenario:**
        ```
        [25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 42]
        ```
        
        **Edge Case Tests:**
        ```
        [0, -5, 1000, -1000]  # Mixed values
        [1, 1, 1, 1]          # Duplicates
        []                     # Empty sequence
        ```
        """)
        
        custom_input = st.text_input("Enter custom sequence (comma-separated):")
        if st.button("Load Custom Sequence"):
            try:
                values = [int(x.strip()) for x in custom_input.split(',') if x.strip()]
                tree = get_tree()
                tree.__init__()
                st.session_state.tree = tree
                
                for value in values:
                    tree.insert(value)
                
                st.success(f"Loaded {len(values)} custom values!")
            except ValueError:
                st.error("Please enter valid numbers separated by commas")

    # Performance Testing Section
    st.header("⚡ Performance Testing")
    
    col_perf1, col_perf2 = st.columns(2)
    
    with col_perf1:
        st.subheader("Performance Metrics")
        
        # Performance test controls
        test_size = st.slider("Test Size (nodes)", 10, 1000, 100, 10)
        test_type = st.selectbox("Test Type", ["Random", "Sequential", "Balanced"])
        
        if st.button("Run Performance Test"):
            # import time
            # import random
            
            tree = get_tree()
            tree.__init__()
            st.session_state.tree = tree
            
            # Generate test data
            if test_type == "Random":
                test_data = random.sample(range(1, test_size * 2), test_size)
            elif test_type == "Sequential":
                test_data = list(range(1, test_size + 1))
            else:  # Balanced
                test_data = []
                # Generate balanced sequence
                def add_balanced(start, end):
                    if start <= end:
                        mid = (start + end) // 2
                        test_data.append(mid)
                        add_balanced(start, mid - 1)
                        add_balanced(mid + 1, end)
                add_balanced(1, test_size)
            
            # Measure insertion time
            start_time = time.time()
            for value in test_data:
                tree.insert(value)
            end_time = time.time()
            
            insertion_time = end_time - start_time
            
            # Measure search time
            search_start = time.time()
            for _ in range(100):  # 100 random searches
                search_value = random.choice(test_data)
                tree.search(search_value)
            search_end = time.time()
            
            search_time = (search_end - search_start) / 100  # Average search time
            
            # Display results
            col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
            
            with col_metrics1:
                st.metric("Insertion Time", f"{insertion_time:.4f}s")
            with col_metrics2:
                st.metric("Avg Search Time", f"{search_time:.6f}s")
            with col_metrics3:
                st.metric("Tree Height", get_tree_height(tree))
            
            st.success(f"Performance test completed with {test_size} nodes ({test_type} pattern)")
    
    with col_perf2:
        st.subheader("Algorithm Validation")
        st.markdown("""
        **Red-Black Properties Check:**
        - ✅ Root is black
        - ✅ No red-red violations
        - ✅ Black height consistency
        - ✅ BST property maintained
        
        **Performance Characteristics:**
        - **Insertion:** O(log n) guaranteed
        - **Search:** O(log n) guaranteed
        - **Deletion:** O(log n) guaranteed
        - **Space:** O(n) for tree structure
        """)
        
        # Real-time validation
        current_tree = get_tree()
        if current_tree.root != current_tree.TNULL:
            stats = get_tree_statistics(current_tree)
            
            if stats['is_valid']:
                st.success("✅ Current tree satisfies all Red-Black properties")
            else:
                st.error(f"❌ Tree validation failed: {stats['validation_message']}")
            
            st.metric("Black Height", stats['black_height'])
            st.metric("Total Height", stats['height'])
        else:
            st.info("🌱 No tree to validate (empty tree)")

    # Instructions for users
    st.header("📚 How to Use")
    
    st.markdown("""
    ### Getting Started
    1. **Insert Nodes:** Use the sidebar controls to add nodes to the tree
    2. **Delete Nodes:** Remove nodes and watch the rebalancing process
    3. **View Steps:** Enable step-by-step explanations to understand the algorithm
    4. **Try Test Cases:** Use predefined test cases to see different scenarios
    
    ### Understanding the Visualization
    - **Red Nodes:** Represented in red circles
    - **Black Nodes:** Represented in black circles
    - **Edges:** Show parent-child relationships
    - **History:** Track all operations performed
    
    ### Algorithm Learning
    - Watch how the tree maintains balance after each operation
    - Observe rotations and color changes
    - Understand the Red-Black properties in action
    """)

if __name__ == "__main__":
    main()