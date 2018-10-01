def gerund_filter(tree):
    # print tree
    for idx in range(len(tree)):
        if "VBG" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx]
            # if "IN" in str(tree[idx]).split("->")[1].strip().split(" "):
            return True
    return False