'''sum_until_0: Continuously read integers from standard input until
 you receive a zero. 
Print the sum of these integers.'''
n=int(input())
sum=0
while n!=0:
    sum+=n
    n=int(input())
print(sum)

'''total_price: Continuously read pairs of integers from standard input,
      representing the quantity and price of items, 
    until you receive the string "END". Print the total price of all items.'''
total_price = 0
while True:
    line = input()
    if line == "END":
        break
    quantity, price = map(int, line.split())
    total_price += quantity * price
print(total_price)
