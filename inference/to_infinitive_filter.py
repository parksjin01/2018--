def infinitive_filter(tree):
    # print tree
    for idx in range(len(tree)):
        if "TO" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx], tree[idx+1]
            if "VP" == str(tree[idx + 1]).split("->")[0].strip():
                return True
    return False