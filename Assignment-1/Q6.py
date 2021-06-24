#Code by GUNAVARDHAN - CH18B035
import random           #Importing the random module
nvalues = range(5, 201, 5)  # arr = {5, 10, 15, ... 200} the vlaue of n to which we need to check the hypothesis
for n in nvalues:     
    count = 0               # count variable to check how many succefull experiments
    for i in range(0, 100000):  #number of random experiments we plan to do 100000
        arr = [0]*366           #An array of 366 zeros corresponding to a day in year 
        for i in range(0, n):   #relating each day of year to a number in 365 and randomly generating the birthdays
            temp = random.randrange(1, 366)
            arr[temp] += 1      #increasing the counter on that day to count the birthdays 
            if arr[temp] > 1:   #if at any point 2 birthdays occur at same day sufficient to say expt succes and break
                count += 1
                break
    p = count/1000              #variable p gives us the probability sense of the experiment
    print(n, p)                 #printing the result or probalibity for each n after conducting these random experiments

    #the result obtained matches with the values in wiki page had checked manually but can be hardcoded if required