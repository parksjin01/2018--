"""
    Infinitive
    ~~~~~~~~~~
"""

def infinitive_filter(tree):
    """
    Infer infinitive grammar is used in this sentence or not

    :param tree: Paresed dependency tree of sentence
    :return: True (Infinitive grammar is used in sentence) / False (Infinitive grammar is not used in sentence)
    """

    # print tree
    for idx in range(len(tree)):
        if "TO" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx], tree[idx+1]
            if "VP" == str(tree[idx + 1]).split("->")[0].strip():
                return True
    return False