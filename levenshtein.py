# Levenshtein Mesafesi Modeli

"""
Bu model, metinler arasındaki benzerliği bulmayı hedefleyen
Vladimir Levenshtein tarafından geliştirilmiş bir algoritmanın
python modelidir. Gerçek hayat örnekleri, iki makaleyi kıyaslayarak
makalede çalıntı paragraf bulma, yazı kıyaslama gibi alanlardır.

Yapay Zeka ve Bilgisayarlı Görü projem altında geliştirdiğim ilk model.
"""

import numpy

def minimum(s1, s2, s3):
    if s1 <= s2 and s1 <= s3:
        return s1
    elif s2 <= s1 and s2 <= s3:
        return s2
    elif s3 <= s1 and s3 <= s2:
        return s3
    
def maks(s1, s2):
    if s1 > s2:
        return s1
    elif s2 > s1:
        return s2
    
def normalize(X, size):
    if len(X) < size:
        fark = size - len(X)
        for i in range(fark):
            X = X + " "
    return X

def LevenshteinMesafesi(A, B):
    K = numpy.zeros((len(A) + 1, len(B) + 1))
    A_len = len(A)
    B_len = len(B)
    
    for i in range(A_len):
        K[i][0] = i
    for i in range(B_len):
        K[0][i] = i
    
    silme = 0
    ekleme = 0
    yerdegistirme = 0
    
    for i in range(1, A_len + 1):
        for j in range(1, B_len + 1):
            if A[i-1] == B[j-1]:
                K[i][j] = K[i-1][j-1]
            else:
                silme = K[i-1][j] + 1
                ekleme = K[i][j-1] + 1
                yerdegistirme = K[i-1][j-1] + 1
                
                K[i][j] = minimum(silme,ekleme,yerdegistirme)
                
    return K[B_len-1][A_len-1]

kelime_1 = input('Birinci kelimeyi girin: ')
kelime_2 = input('İkinci kelimeyi girin: ')
max_len = max(len(kelime_1), len(kelime_2))

kelime_1 = normalize(kelime_1, max_len)
kelime_2 = normalize(kelime_2, max_len)

mesafe = LevenshteinMesafesi(kelime_1, kelime_2)
benzerlik = (max_len - mesafe) / max_len
print(f'{kelime_1} ve {kelime_2} arasındaki levenshtein mesafesi: {mesafe}')
print(f'Benzerlik Oranı: {benzerlik}')