#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing locked boxes and their keys.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if len(boxes[0]) == 0:
        return (False)
    keys = {0}
    size = len(boxes)
    visited = {0}
    keys = keys.union(boxes[0])
    while size > 0:
        for i in keys:
            if i in visited:
                continue
            keys = keys.union(boxes[i])
            visited.add(i)
        size -= 1
    return len(keys) == len(boxes)

    # n = len(boxes)
    # visited_boxes = [False] * n
    # visited_boxes[0] = True
    # stack = [0]

    # while stack:
    #     current_box = stack.pop()
    #     for key in boxes[current_box]:
    #         if not visited_boxes[key]:
    #             visited_boxes[key] = True
    #             stack.append(key)

    # return all(visited_boxes)
