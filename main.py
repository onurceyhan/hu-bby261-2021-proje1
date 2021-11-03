dosya = ("WebSitesi.txt")
yedekdosya = ("WebSitesiYedek.txt")

def WebAdrGost():
    acilanDosya = open(dosya, "r")
    for line in acilanDosya.readlines():
        print(line)

    acilanDosya.close()
    return menu()


def WebAdresiDeg():
   WebAdres = input("Web Adresini giriniz.")
   f = open(dosya, 'w')
   d = open(yedekdosya, 'a')
   d.write(WebAdres + "\n")
   d.close()
   f.write(WebAdres)
   f.close()
   return menu()

def WebAdrsBil():
    import urllib.request
    from bs4 import BeautifulSoup
    webSite = urllib.request.urlopen(open(dosya).read())
    getBytes = webSite.read()
    webPage = getBytes.decode("utf8")
    webSite.close()
    soup = BeautifulSoup(webPage, 'html.parser')
    print(soup.title.contents)
    return menu()

def YedekWebAdrslrGost():
    acilanDosya2 = open(yedekdosya, "r")
    for line in acilanDosya2.readlines():
        print(line)

    acilanDosya2.close()
    return menu()

def menu():
    print("Web Site Bilgileri menüsüne hoşgeldiniz!")
    print("1)Web Adresi Görmek için, 2) Web Adresini değiştirmek için, 3)Web adresi bilgilerini(title) erişebilmek için, 4)Önceden sisteme girilmiş web adreslerini görmek için")
    acilis = input("Açmak istediğiniz yerin numarasını giriniz.")
    numaralar = ("1","2","3","4")
    if acilis == numaralar[0]:
        print(WebAdrGost())
    elif acilis == numaralar[1]:
        print(WebAdresiDeg())
    elif acilis == numaralar[2]:
        print(WebAdrsBil())
    elif acilis == numaralar[3]:
        print(YedekWebAdrslrGost())
    else:
        print("Geçersiz bir numara girdiniz!")

print(menu())

