#!/usr/bin/python3defcanUnlockAll(boxes):
    """ Determines if all boxes can be unlocked. """ifnot boxes:
        returnFalse
    
    n = len(boxes)
    unlocked = set([0])
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key notin unlocked:
                unlocked.add(key)
                stack.append(key)
    
    returnlen(unlocked) == n
