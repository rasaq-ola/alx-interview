# 0x01. Lockboxes

## Description

This project is designed to solve the "Lockboxes" problem, where you are given a set of locked boxes, each containing keys to other boxes. The objective is to determine if all boxes can be unlocked starting from the first box.

## Requirements

- **Python Version:** The project is implemented in Python 3 and is tested on Ubuntu 20.04 LTS using Python 3.8.
- **PEP 8:** All code follows the PEP 8 style guide.
- **Executable:** All Python scripts must be executable.
- **Documentation:** All functions are properly documented.

## Files

- `0-lockboxes.py`: Contains the implementation of the `canUnlockAll` function.
- `main_0.py`: A test script provided to check the functionality of the `canUnlockAll` method.

## Usage

To use the `canUnlockAll` function, ensure that the script is executable and run it with a test script like `main_0.py`.

### Example

```bash
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$

