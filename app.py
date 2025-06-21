import streamlit as st
from algorithm import RedBlackTree
from utils import plot_tree
import copy

def get_tree():
    if 'tree' not in st.session_state:
        st.session_state.tree = RedBlackTree()
    return st.session_state.tree

def main():
    st.set_page_config(page_title="Red-Black Tree Visualizer", layout="wide")
    st.title("Red-Black Tree Visualizer")

    tree = get_tree()

    col1, col2 = st.columns(2)

    with col1:
        st.header("Controls")
        
        insert_value = st.number_input("Insert Node", value=0, step=1, key="insert_input")
        if st.button("Insert"):
            if 'history' not in st.session_state:
                st.session_state.history = []
            
            # Create a deep copy of the tree before insertion
            tree_copy = copy.deepcopy(tree)
            st.session_state.history.append(tree_copy)
            
            tree.insert(insert_value)
            st.session_state.tree = tree

            # Create another deep copy after insertion to show the final state
            tree_copy = copy.deepcopy(tree)
            st.session_state.history.append(tree_copy)
            
            st.success(f"Inserted {insert_value}")

        delete_value = st.number_input("Delete Node", value=0, step=1, key="delete_input")
        if st.button("Delete"):
            if 'history' not in st.session_state:
                st.session_state.history = []
            
            # Create a deep copy of the tree before deletion
            tree_copy = copy.deepcopy(tree)
            st.session_state.history.append(tree_copy)

            tree.delete_node(delete_value)
            st.session_state.tree = tree
            
            # Create another deep copy after deletion
            tree_copy = copy.deepcopy(tree)
            st.session_state.history.append(tree_copy)

            st.success(f"Deleted {delete_value}")
        
        if st.button("Clear History"):
            st.session_state.history = []


    with col2:
        st.header("Red-Black Tree")
        if tree.root != tree.TNULL:
            dot = plot_tree(tree)
            st.graphviz_chart(dot)
        else:
            st.write("The tree is empty.")

    if 'history' in st.session_state and st.session_state.history:
        st.header("Operation History")
        for i, old_tree in enumerate(st.session_state.history):
            st.subheader(f"Step {i+1}")
            dot = plot_tree(old_tree)
            if dot:
                st.graphviz_chart(dot)
            else:
                st.write("Tree was empty at this step.")
    
    st.header("Complexity Analysis")
    st.markdown("""
    | Operation | Average Case | Worst Case |
    |-----------|--------------|------------|
    | Space     | O(n)         | O(n)       |
    | Search    | O(log n)     | O(log n)   |
    | Insert    | O(log n)     | O(log n)   |
    | Delete    | O(log n)     | O(log n)   |
    """)

if __name__ == "__main__":
    main() 