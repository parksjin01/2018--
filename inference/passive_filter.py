def passive_filter(tree):
    # print tree
    for idx in range(len(tree)):
        if "VBZ" in str(tree[idx]).split("->")[0].strip() or "VBP" in str(tree[idx]).split("->")[0].strip() or "VBD" in str(tree[idx]).split("->")[0].strip() or "VB" in str(tree[idx]).split("->")[0].strip():
            # print tree[idx], tree[idx+1]
            if "VP" == str(tree[idx + 1]).split("->")[0].strip():
                return True
            if "UCP" == str(tree[idx + 1]).split("->")[0].strip():
                if "VP" in str(tree[idx + 1]).split("->")[1].strip().split(" "):
                    return True
            if "VP" in str(tree[idx - 1]).split("->")[1].strip().split(" "):
                return True
    # print tree
    return False