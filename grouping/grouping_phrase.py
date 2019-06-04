"""
    grouping_phrase
    ~~~~~~~~~~~~~~~
"""

def grouping_phrase(tree, pivot, res):
    """

    Provide grouping of leaf node from dependency parsed tree.
    This service is used for grouping the leaf node phrase.

    :param tree: Paresed dependency tree of sentence
    :param res: Result of grouping

    """
    for node in tree[0]:
        res.append(str(u" ".join(node.leaves())).split(" "))
    return res