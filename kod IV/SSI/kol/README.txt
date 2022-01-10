Jako zastępstwo zrzutów ekranu bo nie ustawiłem sobie
tego jeszcze na linuxie:

Analiza zbioru:

          variance  skewness  curtosis  entropy  class
    0      3.62160   8.66610   -2.8073 -0.44699      0
    1      4.54590   8.16740   -2.4586 -1.46210      0
    2      3.86600  -2.63830    1.9242  0.10645      0
    3      3.45660   9.52280   -4.0112 -3.59440      0
    4      0.32924  -4.45520    4.5718 -0.98880      0
    ...        ...       ...       ...      ...    ...
    1367   0.40614   1.34920   -1.4501 -0.55949      1
    1368  -1.38870  -4.87730    6.4774  0.34179      1
    1369  -3.75030 -13.45860   17.5932 -2.77710      1
    1370  -3.56370  -8.38270   12.3930 -1.28230      1
    1371  -2.54190  -0.65804    2.6842  1.19520      1

    [1372 rows x 5 columns]
              variance     skewness     curtosis      entropy        class
    count  1372.000000  1372.000000  1372.000000  1372.000000  1372.000000
    mean      0.433735     1.922353     1.397627    -1.191657     0.444606
    std       2.842763     5.869047     4.310030     2.101013     0.497103
    min      -7.042100   -13.773100    -5.286100    -8.548200     0.000000
    25%      -1.773000    -1.708200    -1.574975    -2.413450     0.000000
    50%       0.496180     2.319650     0.616630    -0.586650     0.000000
    75%       2.821475     6.814625     3.179250     0.394810     1.000000
    max       6.824800    12.951600    17.927400     2.449500     1.000000

    Data columns (total 5 columns):
     #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   variance  1372 non-null   float64
     1   skewness  1372 non-null   float64
     2   curtosis  1372 non-null   float64
     3   entropy   1372 non-null   float64
     4   class     1372 non-null   int64  
    dtypes: float64(4), int64(1)
    memory usage: 53.7 KB

    Z wykresów wynika iż duża korelacja występuje między `class` a
    `varience`



Dane Znormalizowane:

    Dla proporcji 60:40:

        Klasyfikator miękki:	53.73%
        Naiwny Bayess:      	38.98%
        KNN:                    100%

    Dla proporcji 80:20:

        Klasyfikator miękki:	53.82%
        Naiwny Bayess:	        38.91%

    Brak większych zmian

Dane nieznormalizowane:

    Tabela ważona zbioru miękkiego dla danych nieznormalizowanych:

        Klasa   wagi...
         0      'curtosis': 1, 'entropy': -1, 'skewness': 4, 'variance': 2
         1      'curtosis': 2, 'entropy': -1, 'skewness': -1, 'variance': -2

    Dla proporcji 60:40:

        Klasyfikator miękki:	69.22%
        Naiwny Bayess:	        0.0%
        KNN:                    100%
        
    Dla proporcji 80:20:

        Klasyfikator miękki:	74.55%
        Naiwny Bayess:	        0.0%

    Dla bazy nieznormalizowanej program poradził sobie o 
    wiele lepiej w klasyfikatorze Miękkim, ale Bayess
    przestał działać (chociaż 0% dokładności sugeruje że 
    po zanegowaniu dla 2 klas ma 100% dokładności)


