import numpy as np

# Define the transition matrix
T = np.array(
    [[0.7, 0.2, 0.1, 0], [0.3, 0.4, 0.3, 0], [0.2, 0.3, 0.4, 0.1], [0.1, 0.2, 0.2, 0.5]]
)

# Define the weather state labels
states = ["sunny", "cloudy", "rainy", "snowy"]

# Set the initial state
current_state = "sunny"

# Initialize the sequence of states
state_sequence = [current_state]

# Generate 15 states
for i in range(14):
    # Get the index of the current state
    current_index = states.index(current_state)

    # Generate the next state based on the transition matrix
    next_index = np.random.choice(range(4), p=T[current_index])
    next_state = states[next_index]

    # Append the next state to the sequence
    state_sequence.append(next_state)

    # Update the current state
    current_state = next_state

# Print the sequence of states
print(state_sequence)
