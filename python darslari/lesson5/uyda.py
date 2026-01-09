# list1 = [1,2,3]
# if list1:
#     print("Royhatda element bor")

    
# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("cho'milgani kettik! ")
# #elif kun.lower()=='yakshanba' and harorat<30:
# else:
#     print("Uyda dam olamiz")

# menyu = ['osh','qozonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yemoqchisiz?>>> ')
# if ovqat.lower() in menyu:
#     print('buyurtma qabul qilindi.')
# else:
#     print('Afsuski, bizda bunday taom yo\'q')
# car = {'model':'ferrari','rang':'qizil'}
# print(car['model'])
# print(car['rang'])

# car = {'model':'malibu 2','rangi':'qora','yili':'2024'}
# print(car['model'])
# print(car['rangi'])
# print(car['yili'])

narx=car.get('narx','Bunday kalit mavjud emas')
narx=car.get('narx')
print(narx)