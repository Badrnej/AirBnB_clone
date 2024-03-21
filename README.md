# HBNB - The Console

Welcome to HBNB, a student project aiming to build a clone of the AirBnB website. In this initial stage, we've implemented a backend interface, known as the console, allowing users to manage program data. The console supports commands for creating, updating, and destroying objects, as well as managing file storage through JSON serialization/deserialization, ensuring persistent data between sessions.

## Project Structure

The repository is organized based on different tasks related to the project. Each task is associated with specific files, providing a structured approach to the development process.

### Project Tasks and Files
1. **Authors**
    - **AUTHORS**: Lists project authors
        - NEJAA BADREDDINE
        - 
2. **Pep8**
    - All code is PEP8 compliant.
3. **Unit Testing**
    - **/tests**: Contains unit tests for all class-defining modules.
4. **Make BaseModel**
    - **/models/base_model.py**: Defines a parent class to be inherited by all model classes.
5. **Update BaseModel w/ kwargs**
    - **/models/base_model.py**: Adds functionality to recreate an instance from a dictionary representation.
6. **Create FileStorage class**
    - **/models/engine/file_storage.py, /models/__init__.py, /models/base_model.py**: Defines a class to manage persistent file storage.
7. **Console 0.0.1**
    - **console.py**: Adds basic functionality to the console program, allowing it to quit, handle empty lines, and ^D.
8. **Console 0.1**
    - **console.py**: Updates the console with methods allowing the user to create, destroy, show, and update stored data.
9. **Create User class**
    - **console.py, /models/engine/file_storage.py, /models/user.py**: Dynamically implements a user class.
10. **More Classes**
    - **/models/user.py, /models/place.py, /models/city.py, /models/amenity.py, /models/state.py, /models/review.py**: Dynamically implements more classes.
11. **Console 1.0**
    - **console.py, /models/engine/file_storage.py**: Updates the console and file storage system to work dynamically with all classes.

## General Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/Amineafilal/AirBnB_clone.git
    ```

2. Navigate to the "console.py" file and run it:

    ```bash
    ./console.py
    ```

    This command will open the HBNB console, indicated by the prompt `(hbnb)`.

## Console Commands

The HBNB console supports various commands for managing objects and file storage. Here are some key commands:

- **create**: Creates an instance based on a given class.
- **destroy**: Destroys an object based on class and UUID.
- **show**: Shows an object based on class and UUID.
- **all**: Shows all objects the program has access to, or all objects of a given class.
- **update**: Updates existing attributes of an object based on class name and UUID.
- **quit**: Exits the program (EOF will as well).

### Alternative Syntax

Users can issue commands using an alternative syntax:

- **Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])**

Advanced syntax is implemented for specific commands:

- **all**: Shows all objects the program has access to, or all objects of a given class.
- **count**: Returns the number of object instances by class.
- **show**: Shows an object based on class and UUID.
- **destroy**: Destroys an object based on class and UUID.
- **update**: Updates existing attributes of an object based on class name and UUID.

## Examples

### Primary Command Syntax

#### Example 1: Create an Object
```bash
(hbnb) create BaseModel
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
