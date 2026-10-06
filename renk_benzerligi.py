def arrange(item, dim, min, max):
    item_count = len(item)
    sonuc = []

    for i in range(dim):
        if i < item_count:
            sonuc.append(item[i] / ((max - min) / 100))
        else:
            sonuc.append(50 / ((max - min) / 100))

    return sonuc


def usal(x, derece=2):
    return x ** derece


def kokal(sayi, derece=2):
    if sayi < 0 and derece % 2 == 0:
        return None

    return sayi ** (1 / derece)


print(kokal(16))
print(kokal(27, 3))
print(kokal(81, 4))

# RENK UZAYI
kirmizi = [255, 0, 0]
koyuKirmizi = [181, 25, 25]
kahverengi = [48, 34, 15]
siyah = [0, 0, 0]
beyaz = [255, 255, 255]
gri = [82, 82, 82]

kirmizi_normalized = arrange(kirmizi, 3, 0, 255)
koyuKirmizi_normalized = arrange(koyuKirmizi, 3, 0, 255)
kahverengi_normalized = arrange(kahverengi, 3, 0, 255)
siyah_normalized = arrange(siyah, 3, 0, 255)
beyaz_normalized = arrange(beyaz, 3, 0, 255)
gri_normalized = arrange(gri, 3, 0, 255)


def vectorSimilarity(A, B):
    if len(A) != len(B):
        return -1

    len_ = len(A)
    total = 0
    for i in range(len_):
        total += usal(B[i] - A[i], 2)

    distance = kokal(total)

    max_dist = 0
    for i in range(len_):
        max_dist += usal(100, 2)

    max_dist = kokal(max_dist)

    return 1 - (distance / max_dist)


benzerlik_orani = vectorSimilarity(beyaz_normalized, gri_normalized)
print(benzerlik_orani)