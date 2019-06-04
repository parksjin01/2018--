"""
    Present-Perfect
    ~~~~~~~~~~~~~~~
"""

def present_perfect_filter(tree):
    """
    Infer present-perfect is used in sentence or not

    :param tree: Paresed dependency tree of sentence
    :return: True (Present-Perfect grammar is used in sentence) / False (Present-Perfect grammar is not used in sentence)
    """

    # print tree
    for idx in range(len(tree)):
        if "VBZ" in str(tree[idx]).split("->")[0].strip() or "VBP" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx], tree[idx+1]
            if "VP" == str(tree[idx + 1]).split("->")[0].strip():
                if "VBN" in str(tree[idx + 1]).split("->")[1].split(" ") or "VBD" in str(tree[idx + 1]).split("->")[1].split(" "):
                    return True

            if "VP" in str(tree[idx - 1]).split("->")[1].strip().split(" "):
                return True
    # print tree
    return False