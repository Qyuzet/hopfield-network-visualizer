# Hopfield Network Visualizer: Exploring Associative Memory and Neural Computations [1.225 neurons & pixel]

## Overview

This project is an interactive web application for visualizing Hopfield Neural Networks, featuring a React frontend with Vite and Tailwind CSS, and a Python Flask backend. The application allows users to train, recall, and explore patterns using a 35x35 grid-based neural network.

![image](https://github.com/user-attachments/assets/0a66bc04-64f3-4888-91e5-1d6cecc45842)
![image](https://github.com/user-attachments/assets/60d143df-0518-4800-bfaa-9ba47d91b388)



## Features

### Neural Network Interactions
- **Train**: Memorize patterns by clicking and drawing on the grid
- **Predict**: Recall and reconstruct patterns
- **Noise Injection**: Add random noise to test network robustness
- **Memory Slideshow**: Cycle through memorized patterns

### Advanced Capture Modes
- **Webcam Integration**: Capture and train patterns from live video
- **Auto-Training**: Automatically memorize frames from webcam
- **Configurable Speeds**: Adjust capture and slideshow intervals

## Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Axios (API requests)
- KaTeX (Mathematical notation rendering)

### Backend
- Python
- Flask
- Numpy (Neural network computations)

## Demo Video

https://www.loom.com/share/04319ce5db05479c99d517913100dd78?sid=523a56c7-4e73-4d2d-88b0-2b5f249718cf

## Key Components

### Grid Visualization
- 35x35 interactive drawing grid
- Real-time pattern rendering
- Side-by-side input and output canvases

### Controls
- Pattern memorization
- Pattern recall
- Noise addition
- Grid clearing
- Webcam integration
- Auto-training modes

### Mathematical Insights
Includes formula cards explaining:
- Network Energy
- Neuron Update Rule
- Hebbian Learning
- Convergence Principles

## 🔧 Installation

### Prerequisites
- Node.js
- Python 3.8+
- pip

### Frontend Setup
```bash
# Clone the repository
git clone <your-repo-url>

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

Hopfield Networks are a type of recurrent artificial neural network that can store and retrieve memories. Key characteristics:
- Bidirectional connections between neurons
- Energy-based learning
- Associative memory retrieval
- Ability to complete partial patterns

## Technical Details

- **Grid Size**: 35x35 neurons
- **Neuron States**: Binary (-1/+1)
- **Learning Rule**: Hebbian learning
- **Recall Method**: Synchronous update

## Limitations
- Fixed grid size
- Limited pattern storage capacity
- Deterministic recall process

## Contributing
Contributions, issues, and feature requests are welcome!

## License
MIT




Initial Grid: You start with a noisy grid (a version of a grid that is similar but not exactly the same as the memorized one).

Energy Calculation: At the start, the code calculates the "energy" of the current grid. Energy is a measure of how well the grid matches the stored patterns. The goal is to reduce the energy to a minimum (which means the grid is as close as possible to a memorized pattern).

Update the Grid: The grid is then updated in a series of steps. Each element of the grid is updated based on the sum of its interactions with all the other elements in the grid. If the sum is positive, the element is set to +1; if it's negative, it's set to -1. These updates are designed to bring the grid closer to a stored pattern.

Recalculate Energy: After each update, the energy is recalculated. If the energy doesn't change from one iteration to the next, that means the grid has stabilized and no further changes are needed.

Break on Convergence: When the energy no longer changes between iterations, the system is considered to have converged. At this point, the grid is assumed to have settled into the closest pattern that was previously stored, even though it started from a noisy or incomplete version.
##  Acknowledgments
Inspiration:
Hopfield, J. (1982). Neural networks and physical systems with emergent collective computational abilities.. Proceedings of the National Academy of Sciences of the United States of America, 79 8, 2554-8 . https://doi.org/10.1073/PNAS.79.8.2554.
