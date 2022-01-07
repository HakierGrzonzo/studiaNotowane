Wymaga pythona 3.10

Uruchamiamy przez plik `test.py`

Wyniki z mojego komputera:

    Testing <function heapsort at 0x7f0b81246a70>
    10	->	2.5e-05	True
    1024	->	0.002348	True
    8192	->	0.025722	True
    524288	->	2.775035	True
    Nobody got time for that!
    Testing <function mergesort at 0x7f0b8137e5f0>
    10	->	0.002455	True
    1024	->	0.002106	True
    8192	->	0.019959	True
    524288	->	2.029737	True
    Nobody got time for that!
    Testing <function quicksort at 0x7f0b8125c040>
    10	->	0.003123	True
    1024	->	0.001285	True
    8192	->	0.013404	True
    524288	->	1.218742	True
    Nobody got time for that!
    Testing <function bubbleSort at 0x7f0b81247eb0>
    10	->	0.002918	True
    1024	->	0.077351	True
    8192	->	5.442486	True
    Nobody got time for that!
    Testing <function insertsort at 0x7f0b81247f40>
    10	->	1.6e-05	True
    1024	->	0.018657	True
    8192	->	1.411479	True
    Nobody got time for that!

Linijka ,,Nobody got time for that'' oznacza że algorytm był trwał 1,1 sekundy,
więc nie będziemy testować większych zbiorów.
