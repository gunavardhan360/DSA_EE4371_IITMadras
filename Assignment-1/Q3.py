#Code by GUNAVARDHAN - CH18B035
def fun(arr):           #Function name "fun"
    odd = 0             #logic: product is odd if both numbers are odd
    for i in arr:
        if i%2 == 1 :   #counting odd numbers 
            odd += 1
        if odd == 2:    #we just need to know there are 2 numbers or not-
            break       #not required to go through complete loop we can exit as soon we find 2 numbers
    if odd == 2:
        return True
    return False

arr = list(map(int, input().split())) #inputing the sequence
arr = set(arr)                        #question specifies the numbers to be distinct so we convert it to set
print(fun(arr))