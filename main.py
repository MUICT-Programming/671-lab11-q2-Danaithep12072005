lst1 = []
lst2 = []
updated_list = []
def summation(n):
    for i in range(n):
        x = int(input())
        lst1.append(x)
    for i in range(n):
        z = int(input())
        lst2.append(z)
        updated_list.append(lst1[i]+lst2[i])
    return updated_list
def find_min_max(updated_list):
    nummin = min(updated_list)
    nummax = max(updated_list)
    return nummin,nummax
print(summation(n))
print(find_min_max(updated_list))UR CODE HERE
