# Scena 1
*Grzes czyta karteczki z nazwami swoich projektów, wyrzuca je na podłogę po kolei*

- Trzykrotny udział w Ludum Dare, tylko 700 miejsca na jakieś 3 tysiące gier…
- Czytnik ebooków w konsoli z własnym renderowaniem html i css, nudy…
- Cross-compiler na commodore 64, już było na programowanie…
- Aplikacja webowa do estymacji zadań do jiry? Nie ma jak pokazać…

- A dobra robimy o restreamerze z praktyk:

# Scena 2

Na praktykach które odbywałem sobie w zeszłoroczne wakacje dostałem pewien problem do rozwiązania:

Otóż kamery IP na budynku mają pewien problem. Nie lubią mieć więcej niż dwóch, trzech klientów naraz.
Dodajmy do tego iż implementacja protokołu RTSP do streamowania obrazu, no cóż… bywa ciekawa.

Więc musiałem zrobić pewne narzędzie, które było by swojego rodzaju proxy, dające możliwość retransmisji obrazu
(w tym po http), trwożenia nowych strumieni z plików oraz możliwość transkodowania.

# Scena 3

*Grzes wyciąga taśmę klejącą*

Po zobaczeniu co mam zrobić, zostało tylko jedno, rozpocząć klejenie.

# Scena 4

*Kamera na ścianę*

Zacznijmy od tego co łatwo znaleźć w google w parę minut.

*nakleja ffmpeg na ścianę*

FFMPEG - jeśli chcesz coś zrobić z video, on to robi. Film do tysięcy plików .png z wypalonymi napisami?

*Kod na ekranie*
```bash
ffmpeg -i video.mp4 napisy.srt && \
ffmpeg -i video.mp4 -filter:v "fps=10, scale=1024:576, subtitles=napisy.srt" klatka%05d.png
```

Zrobione!

*koniec kodu na ekranie*

Może również łączyć się z tymi kamerami, i nawet można mu wybrać czy to ma być tcp, udp lub

*screen z https://ffmpeg.org/ffmpeg-protocols.html#rtsp, zbliżenie*

http?!?

*koniec screena*

Ale ffmpeg ma jeden problem, on może odbierać streamy oraz stremować na serwer który mu się poda, ale
nie jest serwerem sam w sobie. Zatem potrzebujemy

*nakleja rtsp-simple-server*

rtsp-simple-server. Znaleziony na githubie, działa dobrze.

*grzes z greenscreena*

Tylko teraz mamy problem, gdyż dla każdej kamery musimy uruchomić jednego ffmpega z dobrymi parametrami oraz uruchomić serwer.
Musimy to skleić w całość.

*nakleja na wszystko python*

Jakiś skrypt który czyta wszystko z configa w formacie json da radę.

*nakleja obok sklejony bash-streameye-ffmpeg*

Dorzucimy jeszcze jakąś opcję streamowania po http poprzez streameye, też z githuba.



