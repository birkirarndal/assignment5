n = int(input("Enter the length of the sequence: ")) # Do not change this line

oldest_nr = 1
middle_nr = 2
newest_nr = 3
temp_nr = 0
print(oldest_nr)
print(middle_nr)
print(newest_nr)
for i in range(n-3):
    temp_nr = newest_nr
    newest_nr = oldest_nr + middle_nr + newest_nr
    oldest_nr = middle_nr
    middle_nr = temp_nr
    print(newest_nr)

   
   
    