test_dic= {'codingal':2, 'is':2, 'best':2, 'for':2, 'coding':1}
print("The original dictionary is: " + str(test_dic))
K=2
res = 0
for key in test_dic:
    if test_dic[key] == K:
        res += 1
print ("The number of keys with value 2 are: " + str(res))