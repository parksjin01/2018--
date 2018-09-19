def grouping_phrase(tree, pivot, res):
    for node in tree[0]:
        res.append(str(u" ".join(node.leaves())).split(" "))
    return res