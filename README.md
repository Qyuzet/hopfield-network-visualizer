# Hopfield Network Visualizer: Exploring Associative Memory and Neural Computations

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

## 📄 License
[Add your license here]

## 🙏 Acknowledgments
- [List any inspirations, libraries, or resources]
