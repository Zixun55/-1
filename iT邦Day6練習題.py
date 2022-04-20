arr=[i for i in range(1,21,1)]
arr1=[x for x in arr if x % 2 == 1]
arr2=[y for y in arr if y % 2 == 0]
for j in range(len(arr1)):
    print(arr1[j] ,'<--->', arr2[j])
