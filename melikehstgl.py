1.HAFTA
#vucut kilo endeksi hesaplama
boy=float(input("boyunuzu metre cinsinden giriniz:"))
kilo=int(input("kilonuzu giriniz:"))
vki=kilo/(boy**2)
print(f"vücut kitle endeksi:{vki}")
if vki<=18:
    print("zayıfsınız")
elif 18<vki<25:
    print("normal kilodasınız")
elif 25<vki<30:
    print("fazla kilolusunuz")
elif vki>30:
    print("malsef obez olmussunuz:(")
    
    





#listeye eklenen sayıların karekokunu bulma 
import math
rakamlar=[]
while True:
    giris=input("0 ile 9 arasında bır sayı gırınız(sonlandırmak icin q tusuna basın)")
    if giris=="q":
        break
    if giris.isdigit() and 0<=int(giris)<=9:
        rakamlar.append(giris)
    else:
        print("gecersız gırıs yaptın cnm")
if rakamlar:
    sayi = int("".join(rakamlar))
    print("Sayının karekökü:", math.sqrt(sayi))
else:
    print("Hiç rakam girilmedikine")








#2.HAFTA
#topun aldıgı mesafe
def topun_yolunu_hesapla(ilk_yukseklik):
   yukseklik=ilk_yukseklik
   toplam_yol=0
   while yukseklik>0.1:
       toplam_yol+=yukseklik
       yukseklik*=0.9#her sıcramada yuzde onunu kaybedıyor
       if yukseklik>0.1:
           toplam_yol+=yukseklik#eger sıcrama yukseklıgı 0.1 metreden fazlaysa cıkıs mesafesını de ekle
   return toplam_yol
 
ilk_yukseklik=float(input("topun bırakıldıgı mesafeyı metre cınsınden gırınız:"))
toplam_yol=topun_yolunu_hesapla(ilk_yukseklik)
print(f"topun aldıgı toplam mesafe{toplam_yol}")






#not ortalaması ve harf notu hesaplama
def harf_notu_hesapla(vize,final):
    not_ortalaması=(vize*0.4)+(final*0.6)#ortalamayı belırle
    if 70<=not_ortalaması<=100:
        harf_notu="A"
    elif 50<=not_ortalaması<=69:
        harf_notu="B"
    elif 30<=not_ortalaması<=49:
        harf_notu="C"
    elif 0<=not_ortalaması<=29:
        harf_notu="D"
    else:
        harf_notu="gecersız"
    return not_ortalaması,harf_notu
 
vize = float(input("Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))
not_ortalaması,harf_notu=harf_notu_hesapla(vize, final)
print(f"not ortalamanız:{not_ortalaması}")
print(f"harf notunuz:{harf_notu}")





#lısteyı 5 kere kaydırma
liste=list(range(1,11))
k=5
print(liste)
for i in range(k):
    liste=[liste[-1]]+liste[:-1]#listenın son elamnını al daha sonra lıstenın gerı kalanını yazdır
    print(liste)






#sayıyı 16lık tabana cevırme
def onaltılık_tabana_cevir(sayi):
    karakterler="0123456789ABCDEF"
    onaltilik_sayi=""
    if sayi==0:
        return 0
    while sayi>0:
        x=sayi%16
        karakter=karakterler[x]
        onaltilik_sayi=karakter+onaltilik_sayi
        sayi=sayi//16
    return onaltilik_sayi

sayi=int(input("16lık tabana cevırmek ıstedıgınız sayıyı gırın:"))
onaltılık_sayi=onaltılık_tabana_cevir(sayi)
print(f"{sayi}sayısının 16lık tabandakı karsılıgı:{onaltılık_sayi}")






#metındekı kelımelerı lısteye ekleme
metin="Proglamlama uzmanlaşmak isteyen bir kişinin çok sayida soru çözmesi gerekir Bu aşamayi sadece sebatkar öğrenciler geçer İkinci problem sorunun anlaşilmasidir Dikkatini verenler bu aşamayi rahatlikla geçer Üçüncü aşamada anlaşilan sorunun çözüm basamaklarinin ortaya çikarilmasidir Bir kağıt ve bir kalem bu güçlüğü aşmak için yeterlidir Belirlenen çözüm basamaklarinin kod bloklarina dönüşümü en kolay aşama olarak görülür"
kelime_listesi=[]#kelımelerı tutacak lıste 
kelime=""#kelımelerı gecıcı olarak saklıycak
for karakter in metin:
    if karakter!=" ":
       kelime+=karakter
    else:
        if kelime!="":
            kelime_listesi.append(kelime)
            kelime=""
if kelime != "":
    kelime_listesi.append(kelime)  #son kelımeyı eklemeyı unutmaaa          
print(kelime_listesi)







#3.HAFTA
#seklın alan hesabı
x=int(input("kısa kenar uzunlugunu belirleyin(cm):"))
n=int(input("kac adet kagıdın alt alta konulacagını belirleyin:"))
uzun_kenar=x+2#ilk uzun kenar degeri
alan_toplam=0
for i in range(1,n+1):#bu dongu kagıt sayısı kadar dönücek
    alan=x*uzun_kenar
    alan_toplam+=alan#hesaplanan alanları topluyorum
    uzun_kenar+=2#uzun kenar degerını her seferınde arttırıyorum
print(f"olusan seklım alanı:{alan_toplam}")





#depolanacak en fazla su mıktarını hesaplama
def en_cok_su_hesapla(yükseklikler):
    sol=0
    sag=len(yükseklikler)-1
    en_cok_su=0
    while sol<sag:#sol ve sag cubuk bırbırlerını gecene kadar devam et
        sol_yükseklik=yükseklikler[sol]
        sag_yükseklik=yükseklikler[sag]
        genişlik=sag-sol#ıkı cubuk arasındakı mesafeyı bul
        su_miktari=min(sol_yükseklik,sag_yükseklik)*genişlik#kısa cubugun hangısı oldugunu bul ve genıslıkle carp
        if su_miktari>en_cok_su:
            en_cok_su=su_miktari#eger buldugumuz su mıktarı en fazladan coksa guncelleme yap
        if sol_yükseklik<sag_yükseklik:#hangısının degerı daha kısaysa onu kaydırıyoruz
                sol+=1
        else:
                sag-=1
    return en_cok_su

yükseklikler=[1,8,6,2,5,4,8,3,7]
sonuc=en_cok_su_hesapla(yükseklikler)
print(f"en fazla su miktarı:{sonuc}")



#paket uretımsss
t = int(input("Kaç adet paket üretilecegini belirle"))

k_sure = 12  # K bandı 12 saniyede üretir
l_sure = 15  # L bandı 15 saniyede üretir

zaman = 0  # saniye cinsinden zaman
paket_sayisi = 0  # toplam üretilen paket sayısı
ayni_anda_uretimler = []

while paket_sayisi < t:
    zaman += 1  # zamanı saniye saniye artır
    k_uretti = (zaman % k_sure == 0)
    l_uretti = (zaman % l_sure == 0)

    if k_uretti:
        paket_sayisi += 1
    if l_uretti:
        paket_sayisi += 1

    if k_uretti and l_uretti:#her ıkısı de paket urettıyse
        ayni_anda_uretimler.append(zaman)

print("\nAynı anda üretim yapılan zamanlar:")
for z in ayni_anda_uretimler:
    saat = z // 3600
    dakika = (z % 3600) // 60
    saniye = z % 60
    print(f"{saat} saat, {dakika} dakika, {saniye} saniye")
