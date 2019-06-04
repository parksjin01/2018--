"""
    Relative
    ~~~~~~~~
"""

def relative_filter(tree):
    """
    Infer relative grammar is used in this sentence or not

    :param tree: Paresed dependency tree of sentence
    :return: True (Relative grammar is used in sentence) / False (Relative grammar is not used in sentence)
    """

    for idx in range(len(tree)):
        if "SBAR" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx]
            if "WHNP" in str(tree[idx]).split("->")[1].strip().split(" "):
                return True
            if "WHPP" in str(tree[idx]).split("->")[1].strip().split(" "):
                return True
            if "IN" in str(tree[idx]).split("->")[1].strip().split(" "):
                return True
            if "WHADVP" in str(tree[idx]).split("->")[1].strip().split(" "):
                return True
            if "WHADJP" in str(tree[idx]).split("->")[1].strip().split(" "):
                return True
    # print tree
    return False