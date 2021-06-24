#Code by GUNAVARDHAN - CH18B035
n = int(input())
sum = 0
for i in range(1, n):
    if i%2 != 0 and i*i < n:	#Same as before but with additional conditon of odd numbers
        sum += i*i
    else:
        if i*i >= n:
            break
print(sum)