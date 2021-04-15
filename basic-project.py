import random # Dizinden rasgele sayı seçebilmek için 'random' modülünü kullanacağız.
dizin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # Sayılarımızı belirliyoruz.
tutulansayi = [] # 'Random' modülü sayesinde seçilecek sayıların dizini.
dongu = 0 # D'nin ne olduğunu az sonra anlaşılacak.

while len(tutulansayi) < 4: # 'D' değişkeni 3 sayısından küçük olduğu sürece devam edecek bir döngü oluşturuyoruz.
    sayi = random.randint(0, 9) # Sayı değişkenimize rasgele bir sayı atıyoruz, sayı her döngü tekrarlandığında değişecek.
    if not sayi in tutulansayi: # Türkçesi: "Eğer 'sayi' değişkeni 'tutulansayi' değişkeninde değilse, alttaki kodları çalıştır"
        tutulansayi.append(sayi) # 'tutulansayi' değişkenine 'append' methodu ile 'sayi' değişkenini ekliyoruz.
        dizin.remove(sayi) # 'dizin' dizisindne 'sayi' değişkenini kaldırıyoruz ki aynı sayıyı 2 kere eklemeyelim.
    dongu += 1 # 'D' değişkenine +1 ekliyoruz ki döngü sonsuza dek çalışmasın.
print(tutulansayi)
while True: # Dosya çalıştığı sürece alttaki kodları çalıştır.
    yanlisyer = 0 # Yanlış yer değişkenini tanımlıyoruz.
    dogruyer = 0 # Doğru yer değişkenini tanımlıyoruz.
    dongu = 0 # Döngü değişkenini tanımlıyoruz.
    tahministek = input("Tahmininiz: ") # Kullanıcıdan 'Tahmin' alıyoruz.
    tahministek = [int(tahminsayi) for tahminsayi in tahministek] # Kullanıcıdan aldığımız değişkeni 'dizin'e çeviriyoruz.   
    
    # girilen sayı rakamları birbirinden farklı mı?
    
    for i in range(0,4):
        if(tutulansayi[i]==tahministek[i]):
            dogruyer+=1

    kesisim= len(set(tutulansayi).intersection(tahministek)) 

    yanlisyer=kesisim-dogruyer
    print(f"+ {dogruyer} - {yanlisyer}")

    if(dogruyer==4):
        print("tebrikler doğru sayıyı buldunuz!")
        break
    if (tahministek==[0,0,0,0]):
        break
