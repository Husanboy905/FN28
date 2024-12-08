# Descriptorlar
# # 1-misol
# class LowercaseDescriptor:
#     def __get__(self, misol, egasi):
#         return self._value
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError("Qiymat qator bo'lishi kerak")
#         self._value = value.lower()
#
# class User:
#     name = LowercaseDescriptor()
#
# user = User()
# user.name = "Alice"
# print(user.name)
#
# user.name = "567890"
# print(user.name)

# 2-misol
# class PositiveDescriptor:
#     def __get__(self, instance, egasi):
#         return self._value
#
#     def __set__(self, instance, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError("Qiymat raqam bo'lishi kerak")
#         if value < 0:
#             raise ValueError("Qiymat ijobiy bo'lishi kerak")
#         self._value = value
#
# class Account:
#     balance = PositiveDescriptor()
#
# class Product:
#     price = PositiveDescriptor()
#
# account = Account()
# account.balance = 456
# print(account.balance)


# Datetime Moduli
# 1-misol
# from datetime import datetime, timedelta
#
# bugun = datetime.now()
# print("Bugungi sana:", bugun)
#
# ytti_kundan_keyin = bugun + timedelta(days=7)
# print("7 kundan keyin sana:",ytti_kundan_keyin )
#
# yeti_kundan_oldin = bugun - timedelta(days=7)
# print("7 kun oldin sana:", yeti_kundan_oldin)
#
# # 2-misol
# from datetime import datetime
#
# birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
# joriy_yil = datetime.now().year
# yosh = joriy_yil - tug'ilgan_yil
#
# if yosh < 0:
#     print("Siz kelgusi yilga kirdingiz!")
# elif yosh == 0:
#     print("Tug'ilgan kun muborak bo'lsin!")
# else:
#     print("Sizning yoshingiz:", yosh)


# 3-misol
# from datetime import datetime
#
# date_format = "%Y-%m-%d"
# start_date = input("Boshlanish sanasini kiriting (YYYY-AA-DD): ")
# end_date = input("Tugash sanasini kiriting (YYYY-AA-DD): ")
# start = datetime.strptime(start_date, date_format)
# end = datetime.strptime(end_date, date_format)
#
# difference = end - start
# total_seconds = difference.total_seconds()
# print("Ikki sana orasidagi jami soniyalar:", total_seconds)

# Math Moduli
# 1-misol
# import math
#
# diameter = float(input("Doira diametrini kiriting: "))
# radius = diameter / 2
# area = math.pi * (radius ** 2)
# print("Doira maydoni:", area)

# 2-misol
# import math
#
# raqam = float(input("Raqam kiriting: "))
#
# if raqam < 0:
#     raise ValueError("Salbiy sonning kvadrat ildizi yoki kub ildizini hisoblab bo‘lmaydi.")
#
# square_root = math.sqrt(raqam)
# cube_root = raqam ** (1/3)
#
# print("Kvadrat ildiz:", square_root)
# print("Kub ildizi:", cube_root)


# Random Module
# 1-miso
# import random
#
# random_integers = [random.randint(1, 100) for _ in range(5)]
# random_floats = [random.uniform(0, 1) for _ in range(3)]
#
# all_numbers = random_integers + random_floats
# average = sum(all_numbers) / len(all_numbers)
#
# print("Random integers:", random_integers)
# print("Random floats:", random_floats)
# print("Average of all numbers:", average)