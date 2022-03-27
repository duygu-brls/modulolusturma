def sansur(cumleListesi, yasakliKelime, yeniKelime):
    yasakliKelime = ['şişman', 'kötü']
    yeniKelime = ['kilolu', 'uygunsuz']
    cumleListesi = input("Lütfen cümlenizi giriniz: ")
    cumleKelimeler = list(cumleListesi.split())
    for kelime in cumleKelimeler:
        if kelime in yasakliKelime:
            print("Yasaklı kelime mevcut: ", kelime)
            indx = yasakliKelime.index(kelime)
            karakter = yeniKelime[indx]
            cumleListesi = cumleListesi.replace(kelime, karakter)
            print("Cümleniz {} şeklinde düzeltilmiştir".format(cumleListesi))
print("Merhaba ! Ben cümle modülüyüm. Cümlenizin kullanıma uygun olup olmadığını kontrol ederim. ")