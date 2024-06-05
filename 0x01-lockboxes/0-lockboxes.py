#!/usr/bin/python3
"""Unlock the boxes"""


def canUnlockAll(boxes):
    """Unlock the boxes, Problem Solving"""
    if len(boxes[0]) == 0 or type(boxes) is not list:
        return True

    keys_set = set()
    keys_map = {i: False for i in range(len(boxes))}
    keys_map[0] = True

    prev_len = len(keys_set)
    keys_set.update(boxes[0])

    while len(keys_set) > prev_len:
        prev_len = len(keys_set)
        for key in keys_set.copy():
            keys_map[key] = True
            keys_set.update(boxes[key])

    # Return True if any value meets the condition
    return all(keys_map.values())
