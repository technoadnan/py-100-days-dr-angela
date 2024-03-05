num = 1023
reverse_number,n = 0,1000

while num != 0:
   new_num = num % 10
   num = num // 10
   reverse_number = reverse_number + new_num * n
   n = n / 10

print(reverse_number)