n = int(input())
a = 2

while a<n:
    if n%a == 0:
        print(n,'is not prime number')
        break
    a = a+1

if n == a:
    print(n,'is prime number')