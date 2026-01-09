# kitoblar = []

# while True:
#     kitob = input("Yaxshi ko‘rgan kitobingiz (stop — tugatish): ")
#     if kitob.lower() == "stop":
#         break
#     kitoblar.append(kitob)

# print("Sevimli kitoblar:")
# print(kitoblar)

# while True:
#     yosh = input("Yoshingizni kiriting (exit/quit — chiqish): ")

#     if yosh.lower() == "exit" or yosh.lower() == "quit":
#         print("Dastur to‘xtadi.")
#         break

#     yosh = int(yosh)

#     if yosh < 7:
#         print("Chipta narxi: 2000 so‘m")
#     elif yosh < 18:
#         print("Chipta narxi: 3000 so‘m")
#     elif yosh < 65:
#         print("Chipta narxi: 10000 so‘m")
#     else:
#         print("Chipta bepul")

# buyurtmalar = []

# while True:
#     mahsulot = input("Mahsulot nomini kiriting (stop — tugatish): ")
#     if mahsulot.lower() == "stop":
#         break
#     buyurtmalar.append(mahsulot)

# print("Buyurtmalar ro‘yxati:")
# print(buyurtmalar)

# bozor = {}

# while True:
#     nom = input("Mahsulot nomi (stop — tugatish): ")
#     if nom.lower() == "stop":
#         break
#     narx = int(input("Mahsulot narxi: "))
#     bozor[nom] = narx

# print("E-bozor mahsulotlari:")
# print(bozor)

# # Buyurtmalar ro‘yxati



# buyurtmalar = []

# while True:
#     mahsulot = input("Buyurtma kiriting (stop — tugatish): ")
#     if mahsulot.lower() == "stop":
#         break
#     buyurtmalar.append(mahsulot)

# # E-bozor lug‘ati (tayyor)
# bozor = {
#     "non": 3000,
#     "sut": 8000,
#     "shakar": 12000
# }

# # Solishtirish
# for mahsulot in buyurtmalar:
#     if mahsulot in bozor:
#         print(f"{mahsulot} narxi: {bozor[mahsulot]} so‘m")
#     else:
#         print(f"{mahsulot} — Bizda bu mahsulot yo‘q")

