#!/usr/bin/python3
"""Unlock boxes by collecting keys from each accessible box."""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    Start with the key to box 0,
    then collect keys from accessible boxes.
    Continue unlocking boxes with the collected`
    keys until no more boxes can be unlocked.
    Return True if all boxes are unlocked, otherwise False.
    """
    boxes_tot = len(boxes)
    keys_set = [0]
    opened_boxes = 0
    idx = 0

    while idx < len(keys_set):
        current_key = keys_set[idx]
        for key in boxes[current_key]:
            if 0 < key < boxes_tot and key not in keys_set:
                keys_set.append(key)
                opened_boxes += 1
        idx += 1

    return opened_boxes == boxes_tot - 1
