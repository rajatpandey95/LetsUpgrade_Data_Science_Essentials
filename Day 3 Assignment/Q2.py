import numpy as np

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

list1 = np.array(list1)
list2 = np.array(list2)

l = np.append(list1, list2)
l.sort()
print(l)
