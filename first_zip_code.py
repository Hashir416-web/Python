numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("The sum of the two lists is:")
print(list(result))
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
sqaure = list(map(sq,nums))
print("The square of the numbers in the list is:")
print(sqaure)