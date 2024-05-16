# Remote Command Execution Client

This is a Python script for a remote command execution client. It connects to a specified server and port, receives commands from the server, executes them, and sends the output back to the server. Using this script, you can control a UEFI system remotely by sending commands from a remote server.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)


## Description

This script establishes a connection to a remote server using a socket. Once connected, it waits for commands from the server, executes the received commands on the local machine, and sends the output back to the server. This connection is maintained until a quit command is received. 

With this script, you can remotely control a UEFI system by sending commands from the server. This allows for remote management and execution of commands on the UEFI system, which can be useful for system administrators and developers who need to manage UEFI systems remotely and ))))))))))))).

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    
    ```
2. Navigate to the project directory:
    ```bash
    cd remote-command-execution-client
    ```

## Usage

1. Update the `SERVER` and `PORT` variables in the script to match the server's IP address and port.
    ```python
    SERVER = "192.168.0.136"
    PORT = 4444
    ```
2. Run the script:
    ```bash
    python3 client.py
    ```


https://github.com/nova-master/UEFI-Reverse-shell/assets/129145316/4687f795-05d2-4304-ba36-67a162255bbc


