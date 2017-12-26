def combinationSum(candidates, target):
    result = []
    if not candidates:
        return []
    generateCombine(candidates, target, [], result)
    return result

def generateCombine(candidates, target, s, result):
    if target == 0:
        result.append(s[:])
        return

    if target<0:
        return

    for i in xrange(len(candidates)):
        s.append(candidates[i])
        generateCombine(candidates[i:], target-candidates[i], s, result)
        s.pop()
    return
        
