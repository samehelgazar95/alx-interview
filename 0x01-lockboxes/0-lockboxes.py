#!/usr/bin/python3
"""Unlock the boxes"""


def canUnlockAll(boxes):
    """Unlock the boxes, Problem Solving"""
    if len(boxes[0]) == 0:
        return False

    keys_set = set()
    keys_map = {i: False for i in range(len(boxes))}
    keys_map[0] = True

    prev_len = len(keys_set)
    keys_set.update(boxes[0])

    while len(keys_set) > prev_len:
        prev_len = len(keys_set)
        new_keys = []
        for key in keys_set:
            keys_map[key] = True
            new_keys.extend(boxes[key])

        keys_set.update(new_keys)

    # Return True if any value meets the condition
    if any(i is False for i in keys_map.values()):
        return False
    else:
        return True
