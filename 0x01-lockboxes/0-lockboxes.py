#!/usr/bin/env python3
"""Unlock the boxes"""


def canUnlockAll(boxes):
    """Unlock the boxes, Problem Solving"""
    if len(boxes[0]) == 0:
        return False

    keysSet = set()
    keysMap = {i: False for i in range(len(boxes))}
    keysMap[0] = True

    prevLen = len(keysSet)
    keysSet.update(boxes[0])

    while len(keysSet) > prevLen:
        prevLen = len(keysSet)
        new_keys = []
        for key in keysSet:
            keysMap[key] = True
            new_keys.extend(boxes[key])

        keysSet.update(new_keys)

    # Return True if any value meets the condition
    if any(i is False for i in keysMap.values()):
        return False
    else:
        return True
