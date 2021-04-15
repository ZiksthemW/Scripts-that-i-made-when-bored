import random # Dizinden rasgele sayı seçebilmek için 'random' modülünü kullanacağız.
dizin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # Sayılarımızı belirliyoruz.
tutulansayi = [] # 'Random' modülü sayesinde seçilecek sayıların dizini.

while len(tutulansayi) < 4: # 'D' değişkeni 3 sayısından küçük olduğu sürece devam edecek bir döngü oluşturuyoruz.
    sayi = random.randint(0, len(dizin)) # Sayı değişkenimize rasgele bir sayı atıyoruz, sayı her döngü tekrarlandığında değişecek.
    if not sayi in tutulansayi:
            tutulansayi.append(sayi) # 'tutulansayi' değişkenine 'append' methodu ile 'sayi' değişkenini ekliyoruz.
            dizin.remove(sayi) # 'dizin' dizisindne 'sayi' değişkenini kaldırıyoruz ki aynı sayıyı 2 kere eklemeyelim.
            if tutulansayi[0] == 0:
                tutulansayi.remove(tutulansayi[0])

print(tutulansayi)
while True: # Dosya çalıştığı sürece alttaki kodları çalıştır.
    yanlisyer = 0 # Yanlış yer değişkenini tanımlıyoruz.
    dogruyer = 0 # Doğru yer değişkenini tanımlıyoruz.
    dongu = 0 # Döngü değişkenini tanımlıyoruz.
    try:
        tahministek = input("Tahmininiz: ") # Kullanıcıdan 'Tahmin' alıyoruz.
        tahministek = [int(tahminsayi) for tahminsayi in tahministek] # Kullanıcıdan aldığımız değişkeni 'dizin'e çeviriyoruz.
    except:
        print("lütfen rakam giriniz!")
    if (len(tahministek)==4):
        # girilen sayı rakamları birbirinden farklı mı?
        b=[]
        for sayi in tahministek:
                if sayi in b:
                    print("rakamlar sadece bir kez kullanılmalıdır")
                    break
                b.append(sayi)

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
    else:
        print("eksik yada fazla giriş yaptınız")

