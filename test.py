total = 0
def rob(digits):
    index = len(digits)
    global total
    total += max(digits[index-1]+digits[index-3],digits[index-2])
    return total

digits = [2,1,1,2]

print(rob(digits))