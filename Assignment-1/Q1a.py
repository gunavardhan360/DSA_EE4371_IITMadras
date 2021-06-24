#Code by GUNAVARDHAN REDDY - CH18B035
n = int(input())   		#Taking the given input
sum = 0					#Declaring a variable to store the result
for i in range(1, n):	#Loop from 1 to n to add if the squares are less than n
    if i*i < n:
        sum += i*i
    else:				#break as if a small number square is more than n then any
        break			#number greater than that will be more than n
print(sum)				#print result