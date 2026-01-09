# While loopi - togri 

# b = 7
# a = 7
# if a >= b:
#     print("A")
# else:
#     print("d")

# and=va
# or=yoki
# not=emas

# yosh = 40
# print(yosh != 7)
# if not(yosh <=7 or yosh > 65):
#     print("bepul")
# else:
#     print("Pullik")
    
# numbers = []
# for number in range(1, 11):
#     numbers.append(number)
# print(numbers)

# n = 5
# 12345
# n = 3
# 1234
# n = 6
# 123456
# n = 5
# num_str = ""
# for a in range(1, n+1):
#  (f"{a}")
# pass
# num_str+= str(a)
# print(num_str)

# ismlar = ["Ali","Vali","Bek","Xon","Oysha"]
# for ism in ismlar [1:4]:
#     print(f"Assalomu aleykum {ism}")

# n = 5
# b = 0
# for a in range(1,n+1):
#     print(a)

# import random
# kom_num = random.randint(1, 10)
# n = 1
# while n <6:
#     user_guess =int(input(f"{n}-taxminiy raqamni kiriting: "))
#     if user_guess == kom_num:
#         print(f"{n}-urinishda topdingiz va {(6-n)*10} bal oldingiz! ")
#         print("Siz yuttiz!!!")
#     n += 1

import random
kom_num = random.randint(5, 25)
n = 1
while n <6:
    user_guess =int(input(f"{n}-taxminiy raqamni kiriting: "))
    if user_guess == kom_num:
       print(f"{n}-urinishda topdingiz va {(6-n)*10} bal oldingiz! ")
       print("Siz yuttiz!!!")
    n += 1


    