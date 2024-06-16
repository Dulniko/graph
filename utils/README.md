# Algorytmy

## Graham

Algorytm Grahama służy do znajdowania otoczki wypukłej zbioru punktów na płaszczyźnie. 

### dane wejściowe: 
Lista punktów jako obiekty klasy Point (plik graham.py)

[Point(x1, y1), Point(x2, y2), ...]

### dane wyjściowe: 
Lista punktów tworzących otoczkę wypukłą w porządku przeciwnym do ruchu wskazówek zegara. 

[Point(x1, y1), Point(x2, y2), ...]

### złożoność obliczeniowa: 
O(n*log(n))

##
## Ford-Fulkerson

Algorytm Forda-Fulkersona służy do znajdowania maksymalnego przepływu w sieci przepływowej. 

### dane wejściowe: 
Graf w postaci listy list liczb

[ [x1, y1, z1, ...], [x2, y2, z2, ...], ... ]

### dane wyjściowe: 

Liczba opisująca maksymalny przepływ

### złożoność obliczeniowa: 
O(E*|f|), gdzie E to ilość krawędzi, |f| to wartość maksymalnego przepływu

##
## Edmonds-Karp

Algorytm Edmondsa-Karpa jest implementacją algorytmu Forda-Fulkersona z użyciem przeszukiwania wszerz (BFS) do znajdowania ścieżek powiększających. Służy do znajdowania maksymalnego przepływu w sieci przepływowej. 

### dane wejściowe: 
Graf w postaci listy list liczb

[ [x1, y1, z1, ...], [x2, y2, z2, ...], ... ]

### dane wyjściowe: 

Liczba opisująca maksymalny przepływ

### złożoność obliczeniowa: 
O(V*E^2), gdzie V to liczba wierzchołkow, E to ilość krawędzi

##
## Huffman

Algorytm Huffmana jest stosowany do kompresji danych przez tworzenie drzewa kodowego o minimalnej sumarycznej długości kodów

### dane wejściowe: 
Tekst typu string

### dane wyjściowe: 

Zakodowany tekst w postaci ciągu liczb 0, 1

### złożoność obliczeniowa: 
O(n*log(n)), gdzie n to liczba symboli

##
## Knuth-Morris-Pratt (KMP)

Algorytm Knutha-Morrisa-Pratta służy do efektywnego wyszukiwania wzorca w tekście

### dane wejściowe: 
* tekst typu string
* wzorzec typu string

### dane wyjściowe: 

Lista indeksów opisujących miejsce wystąpienie danego wzorca

### złożoność obliczeniowa: 
O(n + m), gdzie n to długość tekstu, m to długość wzorca

##
## Drzewo przedziałowe

Drzewo przedziałowe (segmentowe) służy do efektywnego wykonywania operacji na przedziałach.

### dane wejściowe:
* List[Guard] - lista obiektów klasy Guard
* Guard - obiekt klasy Guard
* Przedział [a, b]

### dane wyjściowe:
* maksymalna wartość w przedziale

### złożoność obliczeniowa:
* budowanie drzewa: O(n)
* zapytanie: O(log(n))
* aktualizacja: O(log(n))

##
## Algorytm zachłanny do ustalenia patrolu

Algorytm zachłanny do ustalenia patrolu polega na wybraniu miejsc odpoczynku dla strażnika. Strażnik zatrzymuję się po maksymalnej ilosći kroków lub gdy napotyka punkt ciemniejszy od poprzedniego.

### dane wejściowe:
* List[Point] - lista obiektów klasy Point
* max_steps - maksymalna ilość kroków

### dane wyjściowe:
* Lista punktów, w których strażnik się zatrzymał i czy zrobił to z własnej woli.

### złożoność obliczeniowa:
* O(n)