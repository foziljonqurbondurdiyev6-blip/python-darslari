# shaxslar = [
#     {
#         "ism": "Alisher Navoiy",
#         "soha": "Adabiyot",
#         "tugilgan_yil": 1441,
#         "asarlar": ["Xamsa", "Lison ut-tayr", "Mahbub ul-qulub"]
#     },
#     {
#         "ism": "Albert Einstein",
#         "soha": "Ilm-fan",
#         "tugilgan_yil": 1879,
#         "asarlar": ["Nisbiylik nazariyasi", "Ilmiy maqolalar"]
#     },
#     {
#         "ism": "Leonardo da Vinci",
#         "soha": "San’at",
#         "tugilgan_yil": 1452,
#         "asarlar": ["Mona Liza", "So‘nggi oqshom"]
#     },
#     {
#         "ism": "Mark Zuckerberg",
#         "soha": "Internet",
#         "tugilgan_yil": 1984,
#         "asarlar": ["Facebook"]
#     }
# ]

# for shaxs in shaxslar:
#     print(f"\nIsm: {shaxs['ism']}")
#     print(f"Soha: {shaxs['soha']}")
#     print("Asarlari:")
#     for asar in shaxs["asarlar"]:
#         print("-", asar)

# dost_kino = {
#     "Ali": ["Breaking Bad", "Prison Break", "Dark"]
# }

# for ism, kinolar in dost_kino.items():
#     print(f"\n{ism}ning sevimli kinolari:")
#     for kino in kinolar:
#         print("-", kino)

# davlatlar = {
#     "O‘zbekiston": {
#         "poytaxt": "Toshkent",
#         "aholi": "36 mln",
#         "til": "O‘zbek"
#     },
#     "AQSh": {
#         "poytaxt": "Washington",
#         "aholi": "331 mln",
#         "til": "Ingliz"
#     },
#     "Yaponiya": {
#         "poytaxt": "Tokio",
#         "aholi": "125 mln",
#         "til": "Yapon"
#     }
# }

# for davlat, info in davlatlar.items():
#     print(f"\nDavlat: {davlat}")
#     for kalit, qiymat in info.items():
#         print(f"{kalit}: {qiymat}")

# sorov = input("\nDavlat nomini kiriting: ")

# if sorov in davlatlar:
#     print(f"\n{sorov} haqida ma’lumot:")
#     for kalit, qiymat in davlatlar[sorov].items():
#         print(f"{kalit}: {qiymat}")
# else:
#     print("Bizda bu davlat haqida ma’lumot yo‘q")



# son = float(input("Juft son kiriting: "))
# if son%3==0:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# son = float(input("Toq son kiriting: "))
# if son%2==0:
#     print("Bu son toq emas.")
# else:
#     print("Rahmat!")


yosh = (input("Yoshingiz nechida?"))

if yosh<=5 or yosh>=70:
    narx = 0



