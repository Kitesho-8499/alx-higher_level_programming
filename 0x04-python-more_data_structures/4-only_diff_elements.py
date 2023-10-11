#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1_only = set_1.difference(set_2)
    set2_only = set_2.difference(set_1)

    result_set = set1_only.union(set2_only)

    return result_set
