#Code by GUNAVARDHAN - CH18B035
arr = list(map(int, input().split())) #inputing the 3 numbers
arr.sort()              #creative solution, sort to obtain relation as there are just 2 possibilites
if arr[0] + arr[1] == arr[2]:   # 1 - small numbers sum can be large number
    print("Possible")
elif arr[0]*arr[1] == arr[2]:   # 2 - small numbers product can be large number
    print("Possible")
else:                           # better solution to check the give "a+b=c" && "a=b-c" && "a*b=c" and many other relations if possible
    print("Not Possible")