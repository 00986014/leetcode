def letterCombinations(self, digits):
    d = {
        '0':' ',
        '1':'',
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
         }
    result = []
    def findCombination(digits, index, s):
        if index == len(digits):
            result.append(s)
            return
        c = digits[index]
        for i in d[c]:
            findCombination(digits, index+1, s+i)
        return
    if not digits:
        return result
    findCombination(digits, 0, '')
    return result
