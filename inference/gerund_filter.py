"""
    Gerund
    ~~~~~~
"""

def gerund_filter(tree):
    """
    Infer gerund grammar is used or not in the sentence

    :param tree: Paresed dependency tree of sentence
    :return: True (Gerund grammar is used in sentence) / False (Gerund grammar is not used in sentence)
    """

    # print tree
    for idx in range(len(tree)):
        if "VBG" in str(tree[idx]).split("->")[1].strip():
            if "VBN" in str(tree[idx - 1]).split("->")[0].strip() or "VBZ" in str(tree[idx - 1]).split("->")[0].strip() or "VBP" in str(tree[idx - 1]).split("->")[0].strip() or "VBD" in str(tree[idx - 1]).split("->")[0].strip():
                return False
            for tmp_idx in range(idx, -1, -1):
                if str(tree[idx]).split("->")[0].strip() in str(tree[tmp_idx]).split("->")[1].strip():
                    if "VBN" in str(tree[tmp_idx]).split("->")[1].strip() or "VBZ" in str(tree[tmp_idx]).split("->")[1].strip() or "VBP" in str(tree[tmp_idx]).split("->")[1].strip() or "VBD" in str(tree[tmp_idx]).split("->")[1].strip() or "VB" in str(tree[tmp_idx]).split("->")[1].strip():
                        return False
                    break

        if "VBG" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx]
            # if "IN" in str(tree[idx]).split("->")[1].strip().split(" "):
            return True
    return False