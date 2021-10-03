def swap(item1, item2):
    tmp = item1
    item1 = item2
    item2 = tmp
    return item1, item2

def reverseString(s):
    end_index = len(s) - 1 
    for i in range(0,end_index):
        if i >= end_index:
            break;
        s[i],s[end_index] = swap(s[i], s[end_index])
        end_index-=1
    return s

s = ["H","a","n","n","a","h"]
print(reverseString(s))