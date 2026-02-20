print("=== Number Analyzer Tool ===")
num=int(input("Enter a number till you want analyzation: ")) #number is inputed from here
#printing all number till that via for loop
print(f"---Priting number from 1 to {num}---")
for i in range(1,num+1):
    print(i)
#Total sum:
total=0
print(f"---Total sum from 1 to {num}---")
for i in range(1,num+1):
    total+=i
print(f"Sum is: {total}")

#couting even numbers:
even_counter=0
print(f"---Counting Even number from 1 to {num}---")
for i in range(1,num+1):
    if(i%2==0):
        even_counter+=1
print(f"Total even numbers are: {even_counter}")

#counting odd numbers:
print(f"---Counting odd number from 1 to {num}---")
odd_counter=0
for i in range(1,num+1):
    if(i%2!=0):
        odd_counter+=1
print(f"Total odd numbers are: {odd_counter}")

#Factorial of that input number:
factorail=1
print(f"---Factorial of {num}---")
for i in range (1,num+1):
    factorail=factorail*i
print(f"{num}!= {factorail}")

#multiples of 5 till inputted number
multiples_of_5=0
print(f"---Multiples of 5---")
for i in range(1,num+1):
    if(i%5==0):
        multiples_of_5+=1
print(f"Multiples of 5 count: {multiples_of_5}")

#pattern output:
for i in range(1,5):
    print("*"*(i+1))


#prime numbers:
print("---Prime counter---")
prime_counter=0
for i in range(2,num+1):
    for u in range(2,i):
        if i%u==0:
            break
    else:
            prime_counter+=1

print(f"The total prime number are: {prime_counter}")



 