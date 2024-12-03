 # Simple Keylogger

## Description

This is a simple keylogger project that records keystrokes into a file named `output.txt` and sends the recorded data to a remote server. The project consists of three main modules: `detector`, `send`, and `main`.

## Features

- Records keystrokes into a file.
- Sends the recorded data to a remote server.
- Runs detection and sending tasks in parallel.

## Prerequisites

- Python 3.x
- Python libraries: `pynput`, `socket`, `threading`

## Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:Nightmares9108/keylogger.git
Navigate to the project directory:


cd keylogger
Install the required Python libraries:


pip install pynput
Usage
Ensure the output.txt file exists or will be created automatically.
Run the main script:

python main.py
Project Structure
detector.py: Module to detect keystrokes and record them into a file.
send.py: Module to send the recorded data to a remote server.
main.py: Main script to run the detector and send modules in parallel.
.gitignore: File to ignore unnecessary files and directories for the Git repository.
README.md: This file.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a branch for your feature (git checkout -b feature/my-feature).
Commit your changes (git commit -m 'Add my feature').
Push to the branch (git push origin feature/my-feature).
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.


