from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")

num_cells = 35
weights = [[0 for _ in range(num_cells * num_cells)] for _ in range(num_cells * num_cells)]
memorized_patterns = []  # Store the memorized patterns

@app.route("/api/memorize", methods=["POST"])
def memorize():
    global weights, memorized_patterns
    grid = request.json.get("grid")
    if grid:
        vector = [cell for row in grid for cell in row]
        memorized_patterns.append(vector)

        # Update weights w' Hebbian learning
        for i in range(len(vector)):
            for j in range(len(vector)):
                if i != j:
                    weights[i][j] += vector[i] * vector[j]
        return jsonify({"message": "Pattern memorized successfully"}), 200
    return jsonify({"error": "Invalid grid data"}), 400

# @app.route("/api/recall", methods=["POST"])
# def recall():
#     global weights
#     noisy_grid = request.json.get("grid")
    
#     # Log the received data for debugging
#     print("Received grid:", noisy_grid)

#     if not noisy_grid:
#         return jsonify({"error": "No grid data received"}), 400

#     # Validate the input structure
#     if not isinstance(noisy_grid, list):
#         return jsonify({"error": "Invalid grid format"}), 400
    
#     # Handle both 2D grid and flat list inputs
#     if isinstance(noisy_grid[0], list):  # If it is a 2D grid
#         vector = [cell for row in noisy_grid for cell in row]
#     elif isinstance(noisy_grid[0], int):  # If it is a flat list
#         vector = noisy_grid
#     else:
#         return jsonify({"error": "Invalid grid format"}), 400

#     # Process the vector for recall
#     max_iterations = 50
#     for _ in range(max_iterations):
#         prev_vector = vector[:]
#         for i in range(len(vector)):
#             sum_input = sum(weights[i][j] * vector[j] for j in range(len(vector)))
#             vector[i] = 1 if sum_input > 0 else -1
#         if vector == prev_vector:
#             break

#     # Reshape the vector back into a 2D grid
#     recalled_grid = [vector[i:i + num_cells] for i in range(0, len(vector), num_cells)]
#     return jsonify({"grid": recalled_grid}), 200

@app.route("/api/recall", methods=["POST"])
def recall():
    global weights
    noisy_grid = request.json.get("grid")
    
    if not noisy_grid:
        return jsonify({"error": "No grid data received"}), 400

    # Convert 2D grid to flat vector
    vector = [cell for row in noisy_grid for cell in row]

    # Calculate the energy of the initial state
    energy = 0
    for i in range(len(vector)):
        for j in range(i + 1, len(vector)):
            energy -= weights[i][j] * vector[i] * vector[j]
    
    # Iteratively update the vector until convergence
    max_iterations = 50
    for _ in range(max_iterations):
        prev_vector = vector[:]
        for i in range(len(vector)):
            sum_input = sum(weights[i][j] * vector[j] for j in range(len(vector)))
            vector[i] = 1 if sum_input > 0 else -1
        
        # Recalculate energy after each update
        new_energy = 0
        for i in range(len(vector)):
            for j in range(i + 1, len(vector)):
                new_energy -= weights[i][j] * vector[i] * vector[j]

        # If energy converges, break the loop
        if new_energy == energy:
            break
        
        energy = new_energy  # Update the energy

    # Reshape the vector back into a 2D grid
    recalled_grid = [vector[i:i + num_cells] for i in range(0, len(vector), num_cells)]
    return jsonify({"grid": recalled_grid, "energy": energy}), 200



@app.route("/api/recallAll", methods=["POST"])
def recallAll():
    global memorized_patterns
    if not memorized_patterns:
        return jsonify({"error": "No patterns memorized"}), 400

    # Convert flat vectors into 2D grids
    grids = [[pattern[i:i + num_cells] for i in range(0, len(pattern), num_cells)] for pattern in memorized_patterns]
    return jsonify({"grids": grids}), 200



@app.route("/api/get-patterns", methods=["GET"])
def get_patterns():
    global memorized_patterns
    # Return the count of memorized patterns
    return jsonify({"patterns": len(memorized_patterns)}), 200


@app.route("/api/clear", methods=["POST"])
def clear():
    global weights, memorized_patterns
    weights = [[0 for _ in range(num_cells * num_cells)] for _ in range(num_cells * num_cells)]
    memorized_patterns = []
    return jsonify({"message": "Memory cleared successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)
