def grouping_clause(tree, pivot, res):
    end = ""
    start_idx = 0
    for idx in range(len(tree)):
        if pivot == str(tree[idx]).split("->")[0].strip():
            res.append([])
            for item in tree[start_idx:idx + 1]:
                if "'" in str(item).split("->")[1]:
                    if '"' in str(item).split("->")[1]:
                        res[-1][-1] += str(item).split("->")[1].strip().strip('"')
                    else:
                        res[-1].append(str(item).split("->")[1].strip().strip("'"))
            start_idx = idx
            end = str(tree[idx]).split("->")[1].strip().split(" ")[-1]
        if end == str(tree[idx]).split("->")[0].strip():
            if "'" != str(tree[idx]).split("->")[1].strip().split(" ")[-1][0]:
                end = str(tree[idx]).split("->")[1].strip().split(" ")[-1]
                # print str(tree[idx]).split("->")
            elif "'" == str(tree[idx]).split("->")[1].strip().split(" ")[-1][0] or "'" == str(tree[idx]).split("->")[1].strip().split(" ")[-1][0]:
                res.append([])
                for item in tree[start_idx:idx+1]:
                    # print item
                    if "'" in str(item).split("->")[1]:
                        if '"' in str(item).split("->")[1]:
                            res[-1][-1] += str(item).split("->")[1].strip().strip('"')
                        else:
                            res[-1].append(str(item).split("->")[1].strip().strip("'"))
                start_idx = idx + 1
                if idx < len(tree) - 1:
                    end = str(tree[idx + 1]).split("->")[1].strip().split(" ")[-1]
    res.append([])
    for item in tree[start_idx:len(tree) + 1]:
        # print item
        if "'" in str(item).split("->")[1]:
            if '"' in str(item).split("->")[1]:
                res[-1][-1] += str(item).split("->")[1].strip().strip('"')
            else:
                res[-1].append(str(item).split("->")[1].strip().strip("'"))