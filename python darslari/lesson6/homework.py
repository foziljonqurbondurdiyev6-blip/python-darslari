# # telefonlar = {
# #      'ali':'iphone 11',
# #      'vali':'galaxy s11',
# #       'olim':'mi 10',
# #       'orif':'nokia 3310', 
# #      }
# # print(telefonlar.values())

# # print('Foydalanuvchilarning telefonlari;')
# # for tel in set(telefonlar.values()):
# #     print(tel)

# # while True:
# #     age = input("yoshingizni kiriting: ")
# #     if age.lower|() =="exit" or age.lower()=="quit":
# #         break
# #     age = int(age)
# #     if age< 7:
# #         print(2000)
# #     elif 7 <= age <=18:
# #         print(3000)
# #     else:
# #         print("Bepul")

# python_lugat = {
#     "integer": "Butun son",
#     "float": "O‘nli kasr son",
#     "string": "Matn turi",
#     "if": "Shart operatori",
#     "else": "Aks holda",
#     "for": "Takrorlash operatori",
#     "while": "Shartli takrorlash",
#     "list": "Ro‘yxat",
#     "tuple": "O‘zgarmas ro‘yxat",
#     "dictionary": "Kalit-qiymat juftligi"
# }

# for kalit, qiymat in python_lugat.items():
#     print(f"{kalit} — {qiymat}")

# sevimli_taomlar = {
#     "otam": "osh",
#     "onam": "manti",
#     "akam": "kabob",
#     "ukam": "burger",
#     "singlim": "pizza"
# }

# print("Otamning sevimli taomi:", sevimli_taomlar["otam"])
# print("Onamning sevimli taomi:", sevimli_taomlar["onam"])
# print("Akamning sevimli taomi:", sevimli_taomlar["akam"])

# otam = {
#     "ismi": "Abdulloh",
#     "tugilgan_yili": 1975,
#     "shahri": "Qarshi",
#     "manzili": "Qashqadaryo viloyati"
# }

# print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan_yili']}-yilda tug‘ilgan. "
#       f"{otam['shahri']} shahrida yashaydi.")

# python_lugat = {
#     "boolean": "Mantiqiy qiymat (True yoki False)",
#     "dictionary": "Kalit-qiymat juftligi",
#     "float": "O‘nli kasr son",
#     "for": "Takrorlash operatori",
#     "if": "Shart operatori",
#     "integer": "Butun son",
#     "list": "Ro‘yxat",
#     "string": "Matn turi",
#     "tuple": "O‘zgarmas ro‘yxat",
#     "while": "Shartli takrorlash"
# }

# for kalit in sorted(python_lugat):
#     print(f"{kalit} — {python_lugat[kalit]}")

# davlatlar = {
#     "O‘zbekiston": "Toshkent",
#     "Rossiya": "Moskva",
#     "AQSH": "Vashington",
#     "Fransiya": "Parij",
#     "Yaponiya": "Tokio"
# }

# print("Davlatlar:")
# for davlat in sorted(davlatlar):
#     print(davlat)

# print("\nPoytaxtlar:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)

# davlat = input("Davlat nomini kiriting: ")

# if davlat in davlatlar:
#     print(f"{davlat} poytaxti — {davlatlar[davlat]}")
# else:
#     print("Bizda bunday ma'lumot yo‘q")

# menu = {
#     "osh": 25000,
#     "manti": 22000,
#     "lagmon": 20000,
#     "shashlik": 18000,
#     "somsa": 8000,
#     "sho‘rva": 15000,
#     "burger": 30000,
#     "pizza": 45000,
#     "lavash": 28000,
#     "norin": 27000
# }

# print("3 ta taom buyurtma qiling:")
# for i in range(3):
#     taom = input(f"{i+1}-taom: ").lower()

#     if taom in menu:
#         print(f"{taom.title()} narxi: {menu[taom]} so‘m")
#     else:
#         print("Bizda bunday taom yo‘q")

# print("set1 - set2:", set1.difference(set2))
# print("set2 - set1:", set2.difference(set1))

# simmetrik_farf = set1.symmetric_difference(set2)
# print("Simmetrik farq:", simmetrik_farf)

# bozorlik = ['choy', 'non', 'kartoshka', 'tuxum', 'sut']
# mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']

# bozorlik_set = set(bozorlik)
# mahsulotlar_set = set(mahsulotlar)

# bor = bozorlik_set.intersection(mahsulotlar_set)
# bor_royxat = list(bor)
# print("Do‘konda bor mahsulotlar:", bor_royxat)

# yoq = bozorlik_set.difference(mahsulotlar_set)
# yoq_royxat = list(yoq)
# print("Do‘konda yo‘q mahsulotlar:", yoq_royxat)

# mahsulotlar_set.update(yoq)
# mahsulotlar = list(mahsulotlar_set)

# print("Yangilangan mahsulotlar ro‘yxati:", mahsulotlar)

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