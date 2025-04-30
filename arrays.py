import array as arr
array_num = arr.array('i', [1, 3, 5, 6, 7,9,3])
print ("The original array is:" + str(array_num))
print ("The number of occurrences of 3 in the said array is: " + str(array_num.count(3)))
array_num.reverse()
print ("The reversed array is:")
print (str(array_num))