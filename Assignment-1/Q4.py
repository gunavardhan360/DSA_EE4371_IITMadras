#Code by GUNAVARDHAN - CH18B035
s = input()
count = 0                          #variable to stroe the vowels count
vowels = {'a', 'e', 'i', 'o', 'u'} #Declaring the vowels in a list
for i in s:
    if i in vowels:                #Checking whether the character is vowel
        count += 1
print(count)                       #printing back the vowels
