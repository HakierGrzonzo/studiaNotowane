# Do zrobienia
#ToDo 

Kodowanie JPEG

- Demo Dyskretnej transformaty Cosinusowej 
	- Implementacja w GLSL
	- Pokazanie jak kolejne piksele pokazują kolejne częstotliwości
	- Wejście w dwa wymiary
	- Kwantyzacja
	- wyjściowe dane do skompresowania innym algorytmem
	- Dekwantyzacja
	- Transformata odwrotna
- Transformacja koloru do przestrzeni barw $YC_bC_r$

# Notatki:
----
## Podstawy

- Zaproponowana w 1972 przez Nasira Achmed'a
- Przekształca skończony zakres danych na sumę funkcji cosinus różnych częstotliwości
- Nie jest jedną konkretną transformatą, lecz rodziną wielu transformat.
- Będziemy rozmawiać o **DCT-II** (aka DCT) oraz o **DCT-III** (aka IDCT aka transformata odwrotna) w kontekście standardu JPEG

----

## Przykład


