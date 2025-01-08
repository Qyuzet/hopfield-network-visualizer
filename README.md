
# Hopfield Network Visualizer: Exploring Associative Memory and Neural Computations [1.225 neurons & pixel]

## Overview

The Hopfield Network Visualizer is an interactive web application designed to demonstrate the principles and operations of Hopfield Neural Networks. This project bridges theoretical concepts with practical implementation, providing users with tools to train, recall, and explore patterns using a 35x35 grid-based neural network. The platform supports both manual and automated pattern input, making it a versatile tool for learning and experimentation.

![image](https://github.com/user-attachments/assets/0a66bc04-64f3-4888-91e5-1d6cecc45842)
![image](https://github.com/user-attachments/assets/60d143df-0518-4800-bfaa-9ba47d91b388)

## Features

### Neural Network Interactions
- **Train**: Memorize patterns by clicking and drawing on the grid.
- **Predict**: Recall and reconstruct patterns.
- **Noise Injection**: Add random noise to test network robustness.
- **Memory Slideshow**: Cycle through memorized patterns to visualize retrieval capabilities.

### Advanced Capture Modes
- **Webcam Integration**: Capture and train patterns from live video input.
- **Auto-Training**: Automatically memorize frames from webcam captures.
- **Configurable Speeds**: Adjust capture and slideshow intervals for flexibility.

## Tech Stack

### Frontend
- **React**: For building the interactive user interface.
- **Vite**: Ensuring fast development builds.
- **Tailwind CSS**: For responsive and modern UI design.
- **Axios**: Facilitating API requests.
- **KaTeX**: Rendering mathematical equations.

### Backend
- **Python**: Core logic for network computations.
- **Flask**: Enabling API communication.
- **NumPy**: Efficient handling of matrix operations and neural computations.

## Demo Video

<https://www.loom.com/share/04319ce5db05479c99d517913100dd78?sid=58b86e04-f114-4295-83db-753d32df006a>

*This video showcases the application’s capabilities, including pattern training, recall, noise tolerance, and webcam integration.*

## Key Components

### Grid Visualization
- 35x35 interactive drawing grid.
- Real-time pattern rendering.
- Side-by-side input and output canvases for comparison.

### Controls
- Memorize patterns.
- Recall stored patterns.
- Inject noise for robustness testing.
- Clear the grid for new inputs.
- Enable and configure webcam integration.

### Mathematical Insights
Includes formula cards explaining:

- **Network Energy**:  
  ![Energy](https://latex.codecogs.com/png.latex?E%20%3D%20-%5Cfrac%7B1%7D%7B2%7D%20%5Csum_%7Bi%20%5Cneq%20j%7D%20w_%7Bij%7D%20x_i%20x_j)

- **Neuron Update Rule**:  
  ![Neuron Update](https://latex.codecogs.com/png.latex?x_i%20%5Cgets%20%5Ctext%7Bsign%7D%5Cleft%28%5Csum_j%20w_%7Bij%7D%20x_j%5Cright%29)

- **Hebbian Learning**:  
  ![Hebbian Learning](https://latex.codecogs.com/png.latex?w_%7Bij%7D%20%3D%20%5Csum_%7Bk%3D1%7D%5EN%20x_i%5E%7B%28k%29%7D%20x_j%5E%7B%28k%29%7D)

- **Convergence Principles**:  
  Stable states and energy minimization dynamics.


## 🔧 Installation

### Prerequisites
- **Node.js**
- **Python 3.8+**
- **pip**

### Frontend Setup
```bash
# Clone the repository
git clone https://github.com/Qyuzet/hopfield-network-visualizer

# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
```

## Hopfield Network Principles

Hopfield Networks are recurrent artificial neural networks capable of storing and retrieving memories through associative mechanisms. Key characteristics include:
- **Bidirectional connections** between neurons.
- **Energy-based learning** to stabilize the network.
- **Associative memory retrieval** to reconstruct partial patterns.
- **Pattern completion** even with noise or missing inputs.

## Technical Details

### Backend API

#### 1. Pattern Memorization
**Endpoint**: `/api/memorize`

The `/api/memorize` endpoint allows the network to store patterns using Hebbian learning. Each pattern updates the weight matrix to encode the memory.

**Code Example**:
```python
@app.route("/api/memorize", methods=["POST"])
def memorize():
    global weights, memorized_patterns
    grid = request.json.get("grid")
    if grid:
        vector = [cell for row in grid for cell in row]
        memorized_patterns.append(vector)

        # Update weights using Hebbian learning
        for i in range(len(vector)):
            for j in range(len(vector)):
                if i != j:
                    weights[i][j] += vector[i] * vector[j]
        return jsonify({"message": "Pattern memorized successfully"}), 200
    return jsonify({"error": "Invalid grid data"}), 400
```

#### 2. Pattern Recall
**Endpoint**: `/api/recall`

This endpoint retrieves stored patterns by iteratively updating the grid until the network converges to a stable state.

**Code Example**:
```python
@app.route("/api/recall", methods=["POST"])
def recall():
    global weights
    noisy_grid = request.json.get("grid")

    # Convert 2D grid to flat vector
    vector = [cell for row in noisy_grid for cell in row]

    # Iteratively update the vector until convergence
    max_iterations = 50
    for _ in range(max_iterations):
        prev_vector = vector[:]
        for i in range(len(vector)):
            sum_input = sum(weights[i][j] * vector[j] for j in range(len(vector)))
            vector[i] = 1 if sum_input > 0 else -1
        if vector == prev_vector:
            break

    # Reshape the vector back into a 2D grid
    recalled_grid = [vector[i:i + num_cells] for i in range(0, len(vector), num_cells)]
    return jsonify({"grid": recalled_grid}), 200
```

#### 3. Noise Injection and Robustness Testing
Noise can be added to patterns to test the network’s ability to recall memories despite disturbances.

**Code Example**:
```python
@app.route("/api/noise", methods=["POST"])
def add_noise():
    pattern = request.json.get("grid")
    noise_level = request.json.get("noise_level", 0.1)
    noisy_pattern = pattern.copy()
    mask = np.random.random(pattern.shape) < noise_level
    noisy_pattern[mask] *= -1
    return jsonify({"grid": noisy_pattern}), 200
```

### Frontend Interactions

#### 1. Grid Visualization
The frontend renders a 35x35 grid that allows users to interactively draw patterns or view recalled memories.

**Code Example**:
```javascript
const renderCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Render grid lines and active cells
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[row].length; col++) {
            if (grid[row][col] === 1) {
                ctx.fillStyle = "#000";
                ctx.fillRect(
                    col * cellLength,
                    row * cellLength,
                    cellLength,
                    cellLength
                );
            }
        }
    }
};
```

#### 2. Webcam Integration
The application supports pattern training through live video input, enhancing usability.

**Code Example**:
```javascript
const processWebcamFrame = async () => {
    if (!isWebcamActive || !videoRef.current) return;

    const tempCanvas = document.createElement("canvas");
    const tempCtx = tempCanvas.getContext("2d");
    tempCanvas.width = 35;
    tempCanvas.height = 35;
    tempCtx.drawImage(videoRef.current, 0, 0, 35, 35);

    const imageData = tempCtx.getImageData(0, 0, 35, 35);
    const newGrid = Array.from({ length: 35 }, () => Array(35).fill(-1));

    for (let y = 0; y < 35; y++) {
        for (let x = 0; x < 35; x++) {
            const index = (y * 35 + x) * 4;
            const gray = (imageData.data[index] + imageData.data[index + 1] + imageData.data[index + 2]) / 3;
            newGrid[y][x] = gray < 128 ? 1 : -1;
        }
    }
    setGrid(newGrid);
    renderCanvas();
};
```

### Energy Minimization and Convergence
**Backend Logic for Energy Calculation**:
```python
def calculate_energy(vector, weights):
    energy = 0
    for i in range(len(vector)):
        for j in range(i + 1, len(vector)):
            energy -= weights[i][j] * vector[i] * vector[j]
    return energy
```

**Frontend Visualization of Energy**:
```javascript
<h3>Energy: {energy !== null ? energy : "Not calculated"}</h3>
```

- **Grid Size**: 35x35 neurons (1,225 pixels).
- **Neuron States**: Binary states (-1 or +1).
- **Learning Rule**

: Hebbian learning algorithm.
- **Recall Method**: Synchronous update of neuron states.

## Limitations
- Fixed grid size (35x35).
- Limited pattern storage due to the network’s capacity constraints.
- Deterministic recall process may fail in highly noisy environments.

## Contributing
We welcome contributions! Feel free to submit issues or feature requests to improve this project.

## License
This project is licensed under the MIT License.

## References

[1] J. Hopfield, "Neural networks and physical systems with emergent collective computational abilities," Proceedings of the National Academy of Sciences of the United States of America, vol. 79, no. 8, pp. 2554–2558, 1982. doi: https://doi.org/10.1073/PNAS.79.8.2554.

[2] Tailwind CSS, "Installation - Tailwind CSS Documentation," [Online]. Available: https://tailwindcss.com/docs/installation. [Accessed: 08-Nov-2024].

[3] React, "Learn React," [Online]. Available: https://react.dev/learn. [Accessed: 08-Nov-2024].

[4] Axios, "Introduction - Axios Documentation," [Online]. Available: https://axios-http.com/docs/intro. [Accessed: 08-Jan-2025].

[5] Flask, "Flask Documentation (Stable Version)," [Online]. Available: https://flask.palletsprojects.com/en/stable/. [Accessed: 08-Jan-2025].

[6] Python Software Foundation, "venv — Creation of virtual environments," [Online]. Available: https://docs.python.org/3/library/venv.html. [Accessed: 08-Jan-2025].

[7] GeeksforGeeks, "Hopfield Neural Network," [Online]. Available: https://www.geeksforgeeks.org/hopfield-neural-network/. [Accessed: 08-Jan-2025].
