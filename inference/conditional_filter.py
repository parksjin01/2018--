"""
    Conditional
    ~~~~~~~~~~~
"""

def conditional_filter(tree):
    """
    Infer conditional grammar is used or not

    :param tree: Paresed dependency tree of sentence
    :return: True (Conditional grammar is used in sentence) / False (Conditional grammar is not used in sentence)
    """
    for idx in range(len(tree)):
        if "SBAR" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx]
            if "IN" in str(tree[idx]).split("->")[1].strip().split(" "):
                return True
    return False