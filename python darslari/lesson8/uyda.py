fanlar = {
     "banana":20000,
     "cherry":10000,
     "grapes":30000,
     "pineapple":25000,
}
fanlar['apple']=10000
fanlar['banana']=50000
print(fanlar)
print(fanlar['apple'])
print(fanlar.get("apple", "topilmadi!"))

arzon_mevalar = []
for k,v in fanlar.items():
    if v < 20000:
        arzon_mevalar.append(k)
print(arzon_mevalar)
print(list(fanlar.keys()))
print(list(fanlar.values()))
