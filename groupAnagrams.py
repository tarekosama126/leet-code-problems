def groupAnagrams(strs):
    cache = {}
    for i in strs:
        orginal = i
        org_ordered = str(sorted(i))
        print(org_ordered)
        if org_ordered in cache.keys():
            cache[org_ordered] = cache[org_ordered] + [orginal]
        else:
            cache[org_ordered] = [orginal]
    print(cache)
    output = []
    for key in cache:
        output.append(cache[key])
    return output