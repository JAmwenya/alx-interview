#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): List of lists, where each inner list represents keys in a box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set([0])  # Start with the first box unlocked
    stack = [0]  # Stack for DFS or BFS traversal

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in visited and 0 <= key < n:  # Valid key
                visited.add(key)
                stack.append(key)

    return len(visited) == n
