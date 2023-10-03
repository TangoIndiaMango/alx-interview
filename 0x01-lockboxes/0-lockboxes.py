#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing locked boxes and their keys.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False
    
    n = len(boxes)
    keys = set([0])  # Start with the key for the first box.
    stack = [0]  # Start with the first box in the stack.

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in keys:
                keys.add(key)
                stack.append(key)

    return len(keys) == n
