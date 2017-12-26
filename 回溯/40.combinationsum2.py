def combinationSum2(self, candidates, target):
    self.result = []
    if not candidates:
        return []
    candidates.sort()
    self.generateCombine(candidates, target, [])
    return self.result

def generateCombine(self, candidates, target, s):
    if target == 0:
        self.result.append(s[:])
        return

    if target<0 or not candidates:
        return

    for i in xrange(len(candidates)):
        if i == 0 or candidates[i] != candidates[i-1]:
            s.append(candidates[i])
            self.generateCombine(candidates[i+1:], target-candidates[i], s)
            s.pop()
    return
