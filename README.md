# Tic-Tac-Toe Project

This project implements a Tic-Tac-Toe game in Python. It includes:
- **Interactive Version**: Allows users to play interactively.
- **Testable Version**: Designed for automated testing with predefined moves.

## Features
- Play against the computer.
- Supports automated testing.
- Includes Continuous Integration (CI) with GitHub Actions.

## How to Run
1. Clone the repository.
2. Install the required dependencies from `requirements.txt`.
3. Run the game or test the code.

## Repository Structure
The project files and their purposes are as follows:
- `Tic-Tac-Toe/`
  - `.github/`
    - `workflows/`
      - `main.yml` - GitHub Actions CI workflow file
  - `InteractiveTicTacToe.py` - Interactive Tic-Tac-Toe game with user inputs
  - `TestableTicTacToe.py` - Testable Tic-Tac-Toe game for unit testing
  - `requirements.txt` - List of dependencies required for the project
  - `test_tictactoe.py` - Unit test suite for the Tic-Tac-Toe game
  - `tictactoe.py` - Core game logic
  - `README.md` - Project documentation (this file)
## License
Licensed under MIT License.
