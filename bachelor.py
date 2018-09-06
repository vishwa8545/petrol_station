l =[7,7,6,5,6]
l1 =[]
for i in l:
    if i in l1:
        l1.remove(i)
    else:
        l1.append(i)
print("the bachelorin the list is :",l1)

### the second one u can use collections
from collections import Counter
l1 = [7,7,6,5,6]
l =Counter(l)

        
