# Red-Black Tree Visualizer

A Streamlit web application that implements and visualizes Red-Black Tree operations in Python. The application allows users to interactively insert and delete nodes while showing the balancing process step-by-step, including rotations and recoloring.

## 🌐 Streamlit Web-App Address

**Deployed Application URL:** https://red-black-tree-operations-am9themcmsoq7bqtvbouzu.streamlit.app

*Note: To deploy this application on Streamlit Cloud, follow the deployment instructions below.*

## 📋 Project Description

This project implements a complete Red-Black Tree data structure with interactive visualization capabilities. Red-Black Trees are self-balancing binary search trees that maintain balance through a set of properties and operations.

### Algorithm Explanation

**Red-Black Tree Properties:**
1. Every node is either red or black
2. The root is always black
3. Red nodes cannot have red children (no two red nodes can be adjacent)
4. Every path from root to leaf has the same number of black nodes
5. All leaves (TNULL nodes) are considered black

**Key Operations:**
- **Insertion:** New nodes are inserted as red leaves, then the tree is rebalanced using rotations and recoloring
- **Deletion:** Nodes are removed and the tree is rebalanced to maintain properties
- **Rotations:** Left and right rotations are used to restructure the tree during balancing

## 🚀 Installation and Usage Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd rbt_visualizer
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

### Usage Instructions

1. **Inserting Nodes:**
   - Enter a numeric value in the "Insert Node" field
   - Click the "Insert" button
   - Watch the tree visualization update with the new node

2. **Deleting Nodes:**
   - Enter the value of the node you want to delete
   - Click the "Delete" button
   - Observe the rebalancing process

3. **Viewing History:**
   - The application maintains a history of all operations
   - Scroll down to see step-by-step changes
   - Use "Clear History" to reset the operation log

## 📸 Screenshots of the Application

### Main Interface
![Main Interface](screenshots/main_interface.png)
*The main interface showing the Red-Black Tree visualization with controls for insertion and deletion.*

### Tree Visualization
![Tree Visualization](screenshots/tree_visualization.png)
*A clear visual representation of the Red-Black Tree with red and black nodes.*

### Operation History
![Operation History](screenshots/operation_history.png)
*Step-by-step history of tree operations showing the balancing process.*

*Note: Screenshots will be added after the application is deployed and running.*

## ⚡ Complexity Analysis

### Time Complexity (Big O Notation)

| Operation | Average Case | Worst Case | Space Complexity |
|-----------|--------------|------------|------------------|
| **Search** | O(log n) | O(log n) | O(1) |
| **Insert** | O(log n) | O(log n) | O(1) |
| **Delete** | O(log n) | O(log n) | O(1) |
| **Rotation** | O(1) | O(1) | O(1) |

### Space Complexity
- **Overall:** O(n) where n is the number of nodes
- **Per Node:** O(1) for storing node data and pointers

### Why Red-Black Trees are Efficient
- **Self-balancing:** Automatically maintains balance after insertions/deletions
- **Guaranteed height:** Tree height is always O(log n)
- **Fast operations:** All basic operations (search, insert, delete) are O(log n)
- **Memory efficient:** Only requires one extra bit per node for color

## 🏗️ Project Structure

```
rbt_visualizer/
├── app.py              # Main Streamlit application
├── algorithm.py        # Red-Black Tree implementation
├── utils.py           # Visualization utilities
├── test_algorithm.py  # Unit tests
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## 🧪 Testing

Run the test suite to verify the Red-Black Tree implementation:

```bash
pytest test_algorithm.py -v
```

The test suite covers:
- Node insertion and property maintenance
- Node deletion and rebalancing
- Red-Black Tree property validation

## 🚀 Deployment Instructions

### Deploy to Streamlit Cloud

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and set `app.py` as the main file
   - Click "Deploy"

3. **Update the README** with your deployed app URL

## 📚 References and Resources

### Academic Resources
- **Introduction to Algorithms (CLRS)** - Chapter 13: Red-Black Trees
- **Data Structures and Algorithms in Python** - Michael T. Goodrich

### Online Resources
- [Red-Black Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Graphviz Documentation](https://graphviz.org/documentation/)

### Implementation References
- **Algorithm Design:** Based on standard Red-Black Tree algorithms
- **Visualization:** Uses Graphviz for tree rendering
- **Web Framework:** Streamlit for interactive web interface

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

İbrahim Halil Siyli / ihalilsiyli@gmail.com

---

