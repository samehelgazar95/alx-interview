#!/usr/bin/python3
"""Unlock the boxes"""


#  This solution does not work for some cases
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
    if any(i is False for i in keys_map.values()):
        return False
    else:
        return True
#  The right solution for all cases
# def canUnlockAll(boxes):
#     """
#     Function that checks with boolean value if the list type and
#     length to invoke two for iterations one to traverse the list
#     and the other to compaer if key is idx or not in order to open
#     """
#     if type(boxes) is not list:
#         return False
#     elif (len(boxes)) == 0:
#         return False
#     for k in range(1, len(boxes) - 1):
#         boxes_checked = False
#         for idx in range(len(boxes)):
#             boxes_checked = k in boxes[idx] and k != idx
#             if boxes_checked:
#                 break
#         if boxes_checked is False:
#             return boxes_checked
#     return True