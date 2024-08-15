#!/usr/bin/python3

def canUnlockAll(boxes):
    """ Determines if all boxes can be unlocked. """
    n = len(boxes)
    unlocked = set([0])  # Start with box 0 unlocked
    stack = [0]  # Use a stack (LIFO) to explore boxes

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
