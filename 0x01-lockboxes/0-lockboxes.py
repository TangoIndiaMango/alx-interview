#!/usr/bin/python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing locked boxes and their keys.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    visited_boxes = [False] * n
    visited_boxes[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited_boxes[key]:
                visited_boxes[key] = True
                stack.append(key)

    return all(visited_boxes)
