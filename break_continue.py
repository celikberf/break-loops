# name = 'Berfin Celik'

# # for ile tum elemanları ekrana yazdırdık . if letter 'e' break dersek ifadee 'e'ye geldiğinde yazmayı keser.
# # if letter 'e' continue dersek 3 harfini atlar diğer ifadeleri ekrana yazdırır.

# for letter in name:
#     if letter == 'e' :
#         continue 
#     print(letter)
"""
x = 0

while x < 5:
    x += 1
    if x == 2:
        continue # 2 'yi atladı 
    print(x)
  """

# 1 - 100 arası tek sayıların toplamı 

x = 1
result = 0
while x <= 100 :
    x+=1
    if x % 2 == 1:
        continue
    result += x
   
    print(f"toplam : {result}")