"""
1-100  arasında rastgele üretilecek bi sayıyı aşağı yukarı ifadeler ile buldurmaya çalışın.
** "random modülü"
** 100 üzerinden planlama yapın . her soru 20 puan
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın

"""

import random

sayi = random.randint(1,10) # Belirtilen iki sayı arasında bir tam sayı üretir (1 ve 100 dahil)
can = int(input('kaç hak kullanmak istersiniz : '))
hak = can
sayac = 0 

while hak > 0 :
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin : '))

    if sayi == tahmin :
        print(f'Tebrikler {sayac}. defada  bildiniz. Toplam puanınız : {100 - (100/can) * (sayac - 1)}')
        break
    elif sayi > tahmin:
        print(f'Yukarı . Kalan hakkınız : {hak}')

    else:
        print(f'Aşağı . Kalan hakkınız : {hak}')

    if hak == 0 :
        print(f'Sayıyı bilemediniz. Hakkınız bitmiştir. Sayi : {sayi}')

