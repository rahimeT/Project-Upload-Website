
import aspose.words as aw
import docx2txt


def readAlgorithm(path):
# load the PDF file
    doc = aw.Document("media/" + str(path))

    # convert PDF to Word DOCX format
    doc.save("abcWord.docx")

    text = docx2txt.process("abcWord.docx")

    with open("abcText.txt", "w", encoding="utf-8") as text_file:
        print(text, file=text_file)
        text_file.close()

    fileRead = open("abcText.txt", "r", encoding="utf-8")

    bilgilerF = open("bilgiler.txt", "w", encoding="utf-8")

    liste = open("abcText.txt", encoding="utf-8").readlines()

 # Üniversite Adı ve Fakülteyi Çekme
    for i in range(len(liste)):
        uniBulundu = False
        bolunmus = liste[i].split(" ")
        for j in range(len(bolunmus)):
            if bolunmus[j] == "ÜNİVERSİTESİ":
                cumleUniFak = bolunmus
                uniBulundu = True
                break
        if uniBulundu:
            universiteAdi = ""
            fakulteAdi = ""
            for j in range(len(cumleUniFak)):
                if cumleUniFak[j] == "ÜNİVERSİTESİ":
                    for k in range(j + 1):
                        if cumleUniFak[k] != "":
                            universiteAdi += cumleUniFak[k] + " "
                    for k in range(j + 1, len(cumleUniFak) - 1):
                        if cumleUniFak[k] != "":
                            fakulteAdi += cumleUniFak[k] + " "
            universiteAdi = universiteAdi[:-1]
            fakulteAdi = fakulteAdi[:-1]

 # Bölüm bilgisi çekme
    for i in range(len(liste)):
        bolunmus = liste[i].split(" ")
        bolumBulundu = False
        for j in range(len(bolunmus)):
            if bolunmus[j] == "BÖLÜMÜ":
                cumleBolum = bolunmus
                bolumBulundu = True
                bolumInd = i
                break
        if bolumBulundu:
            bolumAdi = ""
            for j in range(len(cumleBolum)):
                if cumleBolum[j] != "":
                    bolumAdi += cumleBolum[j] + " "
            bolumAdi = bolumAdi[:-3]
            break

    universiteStr = "Üniversite: " + universiteAdi
    fakulteStr = "Fakülte: " + fakulteAdi
    #bolumStr = "Bölüm: " + bolumAdi

    konu = liste[bolumInd + 4][:-2]
    konuStr = "Konu: " + konu

    adSoyad = liste[bolumInd + 6][:-2]
    adSoyadStr = "Ad Soyad: " + adSoyad

 # Hoca isimlerini çekme
    hocaUnvanlari = ["Ord.Prof.Dr.", "Prof.Dr.", "Prof.", "Doç.Dr.", "Doç.", "Dr.Öğr.Üyesi", "Dr.", "Dr.Öğr.", "Yrd.Doç.", "Arş.Gör.Dr.",
                 "Arş.Gör", "Öğr.Ü.", "Öğr.Gör.", "Okt.", "Çev.", "Öğr.Pl.", "Uz."]

    for i in range(len(liste)):
        hocaIndBulundu = False
        bolunmus = liste[i].split(" ")
        for j in range(len(bolunmus)):
            if bolunmus[j] in hocaUnvanlari:
                hocaIndex = i
                hocaIndBulundu = True
                break
        if hocaIndBulundu:
            break

    for i in range(len(liste)):
        tezIndBulundu = False
        bolunmus = liste[i].split(" ")
        for j in range(len(bolunmus)):
            if bolunmus[j] == "Tezin":
                tezIndex = i
                tezIndBulundu = True
                break
        if tezIndBulundu:
            break

    hocaAdlari = []
    for i in range(hocaIndex, tezIndex):
        hocaAdi = ""
        bolunmus = liste[i].split(" ")
        for j in range(len(bolunmus)):
            if bolunmus[j] in hocaUnvanlari:
                for k in range(j, len(bolunmus)):
                    if bolunmus[k] != "\n":
                        hocaAdi += bolunmus[k] + " "
        if hocaAdi != "":
            hocaAdlari.append(hocaAdi[:-1])


    # içerikte en çok tekrar eden 5 kelimeyi bulma
    kelimeler = []
    kelimeSayilari = []
    for i in range(len(liste)):
        icindekilerBulundu = False
        bolunmus = liste[i].split(" ")
        for j in range(len(bolunmus)):
            if bolunmus[j] == "İÇİNDEKİLER":
                icindekilerBulundu = True
                icindekilerInd = i
                break

    frequent_word = ""
    frequency = 0
    words = []

    bosKelimeler = [",", ".", ":", "the", "ve", "ayrıca", "de", "bir", "hem", "için", "ama", "fakat", "bu", "şu", "o", "iki", "üç", "(a)", "(b)"]

    for i in range(icindekilerInd-2, len(liste)):
        line_word = liste[i].lower().replace(',', '').replace('.', '').split(" ")
        for w in line_word:
            if w != "\n" and w != " " and w != "":
                if w not in bosKelimeler:
                    words.append(w)

    for i in range(0, len(words)):

        count = 1

        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                count = count + 1

        kelimeler.append(words[i])
        kelimeSayilari.append(count)

    yeniKelimeListesi = []
    yeniKelimeSayilari = []

    for i in range(len(kelimeler)):
        if kelimeler[i] not in yeniKelimeListesi:
            yeniKelimeListesi.append(kelimeler[i])
            yeniKelimeSayilari.append(kelimeSayilari[i])

    enCokTekrarEdenKelimeler = []
    enCokTekrarEdenSayilari = []

    for i in range(5):
        maxValue = max(yeniKelimeSayilari)
        maxIndex = yeniKelimeSayilari.index(maxValue)
        enCokTekrarEdenKelimeler.append(yeniKelimeListesi[maxIndex])
        enCokTekrarEdenSayilari.append(yeniKelimeSayilari[maxIndex])

        yeniKelimeListesi.pop(maxIndex)
        yeniKelimeSayilari.pop(maxIndex)

    bilgilerF.write(universiteStr + "\n")
    bilgilerF.write(fakulteStr + "\n")
   # bilgilerF.write(bolumStr + "\n")
    bilgilerF.write(konuStr + "\n")
    bilgilerF.write(adSoyadStr + "\n")
    bilgilerF.write("Hocalar: ")
    for i in range(len(hocaAdlari)):
        if i != len(hocaAdlari)-1:
            bilgilerF.write(hocaAdlari[i] + ", ")
        else:
            bilgilerF.write(hocaAdlari[i])
    bilgilerF.write("\n")
    bilgilerF.write("Anahtar Kelimeler: ")
    for i in range(len(enCokTekrarEdenKelimeler)):
        if i != len(enCokTekrarEdenKelimeler)-1:
            bilgilerF.write(enCokTekrarEdenKelimeler[i] + ", ")
        else:
            bilgilerF.write(enCokTekrarEdenKelimeler[i])

    
    bilgilerF.close()
