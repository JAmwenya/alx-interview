#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): List of lists, where each inner list represents keys in a box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False  # Ensure valid input format

    n = len(boxes)
    visited = set([0])  # Start with the first box unlocked
    stack = [0]  # Stack for DFS traversal

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if isinstance(key, int) and 0 <= key < n and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
