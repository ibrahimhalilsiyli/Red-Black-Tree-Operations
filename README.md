# 🌳 Red-Black Tree Visualizer

An interactive Streamlit web application that implements and visualizes Red-Black Tree operations with step-by-step balancing, rotations, and recoloring. This project provides a comprehensive learning tool for understanding Red-Black Tree algorithms through interactive visualization and detailed explanations.

## 🎯 Project Requirements

### Core Components

This project includes all of the following required components:

#### 1. **Algorithm Implementation** ✅
- **Correct and efficient implementation** of Red-Black Tree in Python (`algorithm.py`)
- **Complete operations**: Insert, Delete, Search with proper balancing
- **Red-Black properties maintained**: Root is black, no red-red violations, black height consistency
- **Efficient data structures**: Uses sentinel nodes and proper pointer management

#### 2. **Interactive Interface** ✅
- **User controls** in sidebar for manipulating inputs and parameters
- **Real-time tree manipulation**: Insert, delete, and search operations
- **Test case selection**: Predefined scenarios (Best Case, Average Case, Worst Case, Random)
- **Custom input support**: Manual value entry and custom sequences
- **Performance testing controls**: Configurable test sizes and patterns

#### 3. **Visualization** ✅
- **Clear visual representations** using Graphviz for tree structure
- **Color-coded nodes**: Red and black nodes with distinct visual representation
- **Dynamic sizing**: Adaptive node sizes and compact/full-width modes
- **Real-time updates**: Tree visualization updates after each operation
- **Step-by-step visualizations**: Each operation step shows tree state

#### 4. **Step-by-Step Explanation** ✅
- **Detailed walkthrough** of each algorithm stage
- **Operation history**: Complete log of all operations performed
- **Color-coded steps**: Different icons for different operation types
- **Educational explanations**: Detailed descriptions of rotations and recoloring
- **Auto-step delay**: Configurable timing for step-by-step viewing

#### 5. **Complexity Analysis** ✅
- **Time complexity documentation** using Big O notation
- **Space complexity analysis** with detailed breakdown
- **Performance characteristics** for all operations
- **Real-world implications** of complexity measures
- **Performance testing tools** to validate theoretical analysis

#### 6. **Test Cases** ✅
- **Variety of examples** demonstrating different scenarios
- **Edge cases**: Empty tree, single node, duplicates, large numbers
- **Best/Average/Worst case scenarios** with explanations
- **Custom test sequences** for user experimentation
- **Performance validation** with real-time testing

## 🚀 Features

### Interactive Operations
- **Insert Nodes**: Add values with step-by-step visualization
- **Delete Nodes**: Remove values with rebalancing visualization
- **Search Nodes**: Find values with color information
- **Clear Operations**: Reset tree or clear operation history

### Visualization Features
- **Adaptive Layout**: Compact and full-width visualization modes
- **Color Coding**: Red and black nodes with clear visual distinction
- **Tree Statistics**: Real-time display of tree properties
- **Operation Tracking**: Complete history of all operations

### Educational Features
- **Red-Black Properties**: Detailed explanation of tree properties
- **Rotation Types**: Visual and textual explanation of rotations
- **Recoloring Process**: Step-by-step color change explanations
- **Algorithm Complexity**: Comprehensive complexity analysis

### Performance Features
- **Performance Testing**: Configurable test scenarios
- **Real-time Metrics**: Insertion time, search time, tree height
- **Algorithm Validation**: Automatic verification of Red-Black properties
- **Statistics Display**: Black height, total height, node count

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rbt_visualizer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## 🎮 Usage

### Getting Started
1. **Open the application** in your web browser
2. **Use the sidebar controls** to perform operations
3. **Try predefined test cases** to see different scenarios
4. **Enable step-by-step explanations** to understand the algorithm

### Interactive Controls
- **Insert Node**: Add values to the tree
- **Delete Node**: Remove values from the tree
- **Search Node**: Find values in the tree
- **Test Cases**: Load predefined scenarios
- **Performance Testing**: Run performance benchmarks

### Understanding the Visualization
- **Red Nodes**: Represented in red circles
- **Black Nodes**: Represented in black circles
- **Edges**: Show parent-child relationships
- **History**: Track all operations performed

## 🔬 Algorithm Details

### Red-Black Tree Properties
1. **Root Property**: The root is black
2. **Red Property**: Red nodes cannot have red children
3. **Black Property**: Every path from root to leaves has same black height
4. **Leaf Property**: All leaves (TNULL) are black

### Operations Complexity
| Operation | Time Complexity | Space Complexity | Description |
|-----------|----------------|------------------|-------------|
| **Search** | O(log n) | O(1) | Binary search through tree |
| **Insert** | O(log n) | O(1) | Insert and rebalance |
| **Delete** | O(log n) | O(1) | Delete and rebalance |
| **Rotation** | O(1) | O(1) | Restructure tree locally |

### Balancing Operations
- **Left Rotation**: Restructures tree to fix violations
- **Right Rotation**: Mirror operation of left rotation
- **Recoloring**: Changes node colors to maintain properties
- **Case Analysis**: Handles different violation scenarios

## 🧪 Test Cases

### Predefined Scenarios
- **Best Case**: Balanced insertion sequence `[10, 5, 15, 3, 7, 12, 18]`
- **Average Case**: Random-like sequence `[50, 30, 70, 20, 40, 60, 80, ...]`
- **Worst Case**: Sequential insertion `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- **Random Data**: 15 random numbers for testing

### Edge Cases
- **Empty Tree**: Operations on empty tree
- **Single Node**: Operations with single node
- **Duplicate Values**: Handling repeated keys
- **Large Numbers**: Very large integer values
- **Negative Numbers**: Negative value handling

### Custom Test Cases
Users can input custom sequences to test specific scenarios:
```
[0, -5, 1000, -1000]  # Mixed values
[1, 1, 1, 1]          # Duplicates
[]                     # Empty sequence
```

## 📊 Performance Analysis

### Theoretical Complexity
- **Time Complexity**: All operations are O(log n) guaranteed
- **Space Complexity**: O(n) for tree structure
- **Height Bound**: Tree height is at most 2*log(n+1)

### Performance Testing
- **Configurable Test Sizes**: 10 to 1000 nodes
- **Multiple Test Patterns**: Random, Sequential, Balanced
- **Real-time Metrics**: Insertion time, search time, tree height
- **Algorithm Validation**: Automatic property verification

## 🏗️ Project Structure

```
rbt_visualizer/
├── algorithm.py          # Red-Black Tree implementation
├── app.py               # Streamlit web application
├── utils.py             # Visualization utilities
├── test_algorithm.py    # Unit tests
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

### File Descriptions
- **`algorithm.py`**: Complete Red-Black Tree implementation with all operations
- **`app.py`**: Interactive Streamlit interface with visualization and controls
- **`utils.py`**: Tree visualization and statistics utilities
- **`test_algorithm.py`**: Comprehensive unit tests for all operations
- **`requirements.txt`**: All necessary Python packages

## 🧪 Testing

Run the test suite to verify algorithm correctness:
```bash
python test_algorithm.py
```

The test suite includes:
- **Basic operations**: Insert, delete, search
- **Edge cases**: Empty tree, single node, duplicates
- **Red-Black properties**: Validation of all tree properties
- **Performance tests**: Large-scale operation testing

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Production Deployment
1. **Install dependencies**: `pip install -r requirements.txt`
2. **Set environment variables** (if needed)
3. **Deploy to Streamlit Cloud** or other hosting platforms

## 📚 Educational Value

This project serves as an excellent learning tool for:
- **Data Structures**: Understanding tree-based data structures
- **Algorithms**: Learning balancing algorithms and complexity analysis
- **Visualization**: Seeing abstract concepts in concrete form
- **Interactive Learning**: Hands-on experimentation with algorithms


# In-App Screenshots
## Main Menu
![image](https://github.com/user-attachments/assets/6746f153-40e8-4a41-96d4-5b917399e47a)


## Visualization
![image](https://github.com/user-attachments/assets/bab85fa1-41cc-4736-967b-04716eb1b5d1)



## Steps and Complexity Analysis
![image](https://github.com/user-attachments/assets/725ea691-3b06-448e-9bd8-caf9c6ee6e7e)

## 🔗 References

- **Red-Black Trees**: Introduction to Algorithms (CLRS)
- **Streamlit**: https://streamlit.io/
- **Graphviz**: https://graphviz.org/
- **Python**: https://python.org/

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

---

**Note**: This project fulfills all core requirements for algorithm visualization and education, providing a comprehensive tool for learning Red-Black Tree operations through interactive visualization and detailed explanations. 
