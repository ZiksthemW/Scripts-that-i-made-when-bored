import random # Dizinden rasgele sayı seçebilmek için 'random' modülünü kullanacağız.
dizin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # Sayılarımızı belirliyoruz.
tutulansayi = [] # 'Random' modülü sayesinde seçilecek sayıların dizini.
dongu = 0 # D'nin ne olduğunu az sonra anlaşılacak.

while dongu <= 3: # 'D' değişkeni 3 sayısından küçük olduğu sürece devam edecek bir döngü oluşturuyoruz.
    sayi = random.randint(0, 9) # Sayı değişkenimize rasgele bir sayı atıyoruz, sayı her döngü tekrarlandığında değişecek.
    if not sayi in tutulansayi: # Türkçesi: "Eğer 'sayi' değişkeni 'tutulansayi' değişkeninde değilse, alttaki kodları çalıştır"
        tutulansayi.append(sayi) # 'tutulansayi' değişkenine 'append' methodu ile 'sayi' değişkenini ekliyoruz.
        dizin.remove(sayi) # 'dizin' dizisindne 'sayi' değişkenini kaldırıyoruz ki aynı sayıyı 2 kere eklemeyelim.
    dongu += 1 # 'D' değişkenine +1 ekliyoruz ki döngü sonsuza dek çalışmasın.

while True: # Dosya çalıştığı sürece alttaki kodları çalıştır.
    yanlisyer = 0 # Yanlış yer değişkenini tanımlıyoruz.
    dogruyer = 0 # Doğru yer değişkenini tanımlıyoruz.
    dongu = 0 # Döngü değişkenini tanımlıyoruz.
    tahministek = input("Tahmininiz: ") # Kullanıcıdan 'Tahmin' alıyoruz.
    tahministek = [int(tahminsayi) for tahminsayi in tahministek] # Kullanıcıdan aldığımız değişkeni 'dizin'e çeviriyoruz.
    for tahmin in tahministek: # Tahministek içindeki tahmin kadar döngü değiştiriyoruz. Daha doğrusu tahministek içindeki index kadar.
        if tahmin in tutulansayi: # Türkçesi: Eğer 'tahmin' değişkeni 'tutulansayi' içinde ise alttaki kodu çalıştır.
            if tahmin == tutulansayi[dongu]: # Türkçesi: Eğer 'tahmin' değişkeni, 'tutulansayi' daki 'dongu' indexine eşit ise, alttaki kodu çalıştır.
                dogruyer += 1 # 'dogruyer' değişkenine +1 ekliyoruz.
            else: # Değilse
                yanlisyer += 1 # 'yanlisyer' değişkenine +1 ekliyoruz.
        dongu += 1 # dongu'ye +1 ekliyoruz ki index numaramız değişsin.
    if dogruyer == 4: # Türkçesi: Eğer 'dogruyer' değişkeni 4 sayısına eşit ise alttaki kodları çalıştır.
        print("Oyunu kazandınız!") # 'Oyunu kazandınız!' çıktısı ver.
        break # Programı kapat.
    else: # Değilse
        print(f"Doğru yer: {dogruyer}\nYanlış yer: {yanlisyer}") # Çıktı verip 'While' döngüsünün başına dön.
