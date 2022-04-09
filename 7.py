n = input()

def specialNum(n, count=0):
    if int(n) == 1:
        return count
    elif count>=50:
        return -1    
    else:
        sum = 0
        for i in range(len(n)):
            sum += int(n[i]) * int(n[i])
        count+=1 
        return specialNum(str(sum),count)

d = specialNum(n)
print(d)





def findAnagrams(list1):
    list2 = []
    nums = [''.join(sorted(i)) for i in list1]
    dict1 = {}
    for i, e in enumerate(nums):
        dict1.setdefault(e,[]).append(i)
    for index in dict1.values():
        col = list(list1[i] for i in index)
        print(col)
        list2.append(col)
    print(list2)
    return list2

    

findAnagrams(["aniket", "niaket"])
             

