
# Port Scanner

A simple port scanning tool written in Python that allows users to scan TCP and UDP ports on a specified IP address. The tool provides a command-line interface for easy interaction.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Menu Options](#menu-options)
- [Code Structure](#code-structure)
- [Limitations](#limitations)
- [Disclaimer](#disclaimer)
- [License](#license)

## Features
- **TCP Port Scanning**: Scan a range of TCP ports on a target IP address.
- **UDP Port Scanning**: Scan a range of UDP ports on a target IP address.
- **Interactive Menu**: User-friendly menu to select scanning options.
- **Input Validation**: Ensures valid IP addresses and port ranges are provided.
- **Display Open Ports**: Shows a list of open ports found during scanning.
- **Change Target IP**: Allows changing the target IP address without restarting the application.

## Requirements
- Python 3.x
- Standard Python libraries: `socket`

## Installation
### Clone the Repository
```bash
git clone https://github.com/Rskladanek/PortScanner.git
cd PortScanner
```
## Set Up the Directory Structure

### Ensure your project directory is structured as follows:
```bash
PortScanner/
├── main.py
├── menu.py
└── modules/
    └── portscanner.py
```
## Install Dependencies

No external dependencies are required beyond the Python Standard Library.
## Usage
### Running the Application

Execute the main script using Python:
```bash
python main.py
```
### Menu Options

Upon running the application, you'll be greeted with an ASCII art banner and prompted to enter the target IP address. After entering a valid IP address, the main menu will be displayed:
```bash
=== Choose an Option ===
1. TCP Port Scan
2. UDP Port Scan
3. Show Open Ports
4. Change Target IP
5. Exit
=========================
```
Option Details:

    TCP Port Scan
        Prompts for a starting and ending port number.
        Scans the specified range for open TCP ports.
        Displays progress and results.

    UDP Port Scan
        Prompts for a starting and ending port number.
        Scans the specified range for open UDP ports.
        Due to the nature of UDP, results may vary.
        Displays progress and results.

    Show Open Ports
        Displays a list of open ports found during the current session.
        Separates TCP and UDP ports for clarity.

    Change Target IP
        Allows you to change the target IP address without restarting the application.
        Validates the new IP address before accepting it.

    Exit
        Exits the application gracefully.

## Code Structure
### main.py

The entry point of the application. It imports the Menu class from menu.py and starts the menu loop.
```python
from menu import Menu

if __name__ == "__main__":
    m = Menu()
    m.run()
```
### menu.py

Contains the Menu class, which handles user interaction, displays options, and processes user input.

from modules.portscanner import PortScanner

class Menu:
    # Class implementation...

### modules/portscanner.py

Contains the PortScanner class, which performs the actual scanning of TCP and UDP ports.

import socket

class PortScanner:
    # Class implementation...

## Limitations

    UDP Scanning Reliability
        UDP scanning is inherently less reliable due to the protocol's connectionless nature.
        Many UDP services do not respond to unsolicited packets, making it difficult to determine if a port is open or filtered.
        Scanning UDP ports may produce false negatives.

    Performance
        Scanning large port ranges can be time-consuming, especially for UDP scans.
        The tool currently scans ports sequentially without multithreading.

    Permission Requirements
        Scanning certain ports or running on specific systems may require administrative privileges.
        Ensure you have the necessary permissions to execute the scans.

## Disclaimer
### Legal and Ethical Considerations

    This tool is intended for educational purposes and authorized network testing only.
    Scanning ports on networks or devices without explicit permission from the owner is illegal and unethical.
    The author is not responsible for any misuse of this tool.

## License

This project is licensed under the MIT License.
