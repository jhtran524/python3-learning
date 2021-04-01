# Reversing a list using reversed() function.
def Reverse(numberList):
    return [ele for ele in reversed(numberList)]
      
# Hard-coded numbers
numberList = [21, 13, 18, 11, 31, 44]
print(Reverse(numberList))