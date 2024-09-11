#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked."""
    if not boxes:
        return True  # No boxes to unlock, return True

    n = len(boxes)  # Total number of boxes
    unlocked = set([0])  # Start with box 0 unlocked
    stack = [0]  # Start checking from box 0

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:  # Check all keys in current_box
            if 0 <= key < n and key not in unlocked:  # Key must be valid
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n  # Return True if all boxes are unlocked
