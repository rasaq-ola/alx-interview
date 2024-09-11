#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked."""
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])  # We can always unlock the first box
    stack = [0]  # Use a stack to keep track of boxes to check

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
