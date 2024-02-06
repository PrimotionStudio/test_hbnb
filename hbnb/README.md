# AirBnB Clone

## Description

The AirBnB Clone project is a command-line interface (CLI) tool that replicates some functionalities of the AirBnB website. It allows users to manage objects in a database, such as creating, reading, updating, and deleting instances of various classes like User, Place, Review, etc.

## Command Interpreter

The command interpreter is a CLI tool called `hbnb`. Here's how you can start and use it:

### How to Start

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/PrimotionStudio/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnB_clone
    ```

3. Run the command interpreter:

    ```bash
    ./console.py
    ```

### Commands and Usage

Once the command interpreter is running, you can use the following commands:

- **create**: Create a new object instance.
  Example:
  (hbnb) create User

- **show**: Show details of an existing object by its ID.
Example:
(hbnb) show Place 1234

- **destroy**: Delete an existing object by its ID.
Example: 
(hbnb) destroy Review 5678

- **all**: Show all instances or instances of a specific class.
Example: 
(hbnb) all
(hbnb) all User

- **update**: Update attributes of an existing object by its ID.
Example: 
(hbnb) update State abcd name "California"

## Authors
Queendarlin Nnamani <queendarlinnnamani@gmail.com>
Martins Okanlawon <oyedelenewton@gmail.com>
