list = [1,2,3,3,3,4,4,5]
list.sort()
count = 0
pre = 0
for i in list:
    if list.count(i) > count:
        count = list.count(i)
        pre = i
print(pre)