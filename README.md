🐦 Flappy Bird – Python (Pygame)

A simplified recreation of the classic Flappy Bird game built with Python and Pygame.

This project was developed as part of the INF1007 – Programming I course.
The graphical interface and overall structure were provided, and the core game logic was implemented from scratch.

⸻

🎮 Game Overview

In this arcade-style game:
	•	The bird automatically moves forward
	•	The player presses SPACE to make the bird jump
	•	The goal is to pass between pairs of pipes
	•	The player starts with 3 lives
	•	A life is lost if:
	•	The bird hits a pipe
	•	The bird touches the ground
	•	The bird exits the screen from the top
	•	The game ends when all lives are lost
	•	Press R to restart after Game Over

Each pair of pipes gives 1 point (0.5 per pipe).

⸻

🧠 What I Implemented

The following mechanics were fully implemented:
	•	Gravity system
	•	Jump impulse logic
	•	Dynamic pipe generation with random gap
	•	Continuous pipe spawning
	•	Pipe movement & cleanup
	•	Collision detection using pygame.Rect
	•	Score system
	•	Life management
	•	Game restart logic
	•	Game Over state handling

⸻

🗂 Project Structure
flappy_bird/
├── assets/
├── bird.py
├── pipes.py
├── config.py
├── window.py
├── game.py
└── main.py

	•	bird.py → Bird state & initialization
	•	pipes.py → Pipe images & configuration
	•	game.py → Core game mechanics
	•	window.py → Rendering & display
	•	main.py → Game loop & input handling


⚙️ Installation

Make sure Python is installed.

Install Pygame:  

pip install -U pygame


Run the game:

python main.py



📚 Technical Concepts Used
	•	Game loop architecture
	•	Event-driven programming
	•	Physics simulation (gravity & velocity)
	•	Collision detection
	•	State management
	•	Object representation using dictionaries
	•	Modular file structure

⸻

🚀 Purpose of the Project

This project was built for learning purposes to:
	•	Understand game architecture in Python
	•	Practice structuring a multi-file project
	•	Apply physics concepts in code
	•	Improve debugging and logical reasoning skills


© 2026 Mehdi Azaiez. All rights reserved.

This project was developed for academic purposes (INF1007).
Copying, redistribution, or reuse of this code is not permitted.
