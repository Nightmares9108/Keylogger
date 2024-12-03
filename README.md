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
   ```

Navigate to the project directory:

```sh
	cd keylogger```

Install the required Python libraries:
```sh
pip install pynput socket threading
```
Usage
Ensure the output.txt file exists or will be created automatically.
Run the main script:
```sh
python3 main.py
```

# Project Structure
detector.py: Module to detect keystrokes and record them into a file.

send.py: Module to send the recorded data to a remote server.

main.py: Main script to run the detector and send modules in parallel.

README.md: This file.

#  Contributing
## Contributions are welcome!

# License
This project is licensed under the MIT License. See the LICENSE file for details.


