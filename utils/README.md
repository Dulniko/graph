# Jarvis
Algorytm Jarvisa służy do znajdowania otoczki wypukłej zbioru punktów na płaszczyźnie. 

Za pomocą tego algorytmu wyznaczamy granicę krainy płaszczaków w sposób najbardziej optymalny, dzięki czemu zostaje zaoszczędzona ilość płotów.

## dane wejściowe: 
Lista punktów jako obiekty klasy Point (plik jarvis.py)

```python
points = [Point(x1, y1), Point(x2, y2), ...]
```

## dane wyjściowe: 
Lista punktów tworzących otoczkę wypukłą w porządku przeciwnym do ruchu wskazówek zegara. 

```python
result = [Point(x1, y1), Point(x2, y2), ...]
```

## złożoność obliczeniowa: 
### O(n * h)
* n - ilość punktów
* h - ilość punktów otoczki wypukłej

## niezmiennik pętli:
Niezmiennikiem w algorytmie Jarvisa jest fakt, że w każdym kroku pętli lista *hull* zawiera indeksy punktów, które są częścią otoczki wypukłej przetwarzanych do tej pory punktów, zaczynając od punktu o najniższej wartości *y* (i najniższej wartości *x* w przypadku remisu). Punkt *p* zawsze wskazuje na bieżący punkt otoczki wypukłej, a zmienna *q* wskazuje na potencjalny kolejny punkt, który jest najbardziej zewnętrzny względem wszystkich przetworzonych punktów.

#
# Ford-Fulkerson
Algorytm Forda-Fulkersona służy do znajdowania maksymalnego przepływu w sieci przepływowej. 

W krainie pomaga to płaszczakom w problemie związanym z dostawami płotów do punktu odbioru. Chcą oni jak najbardziej zredukować ilość płaszczaków potrzebnych do noszenia płotów (tragarzy) a zarazem zmaksymalizować ilość dostarczonych płotów w pojedynczej dostawie. Problemem jest to, iż każda droga ma określoną maksymalną ilość płotów, którą można przez tą drogę przetransportować. Zatem ten algorytm idealnie się sprawdzi do tego - uwzględniając warunki dróg (maksymalna ilość płotów na daną drogę) wskaże nam, ile jesteśmy w stanie przetransportować płotów od fabryki do punktu odbioru przez daną sieć dróg.

## dane wejściowe: 
Graf w postaci listy list liczb typu float

```python
graph = [ 
           [x1, y1, z1, ...], 
           [x2, y2, z2, ...], 
           ..., 
        ]
```

## dane wyjściowe: 
Liczba typu float opisująca maksymalny przepływ
```python
max_flow = (float)result
```

## złożoność obliczeniowa: 
### O(E * |f|)
* E - ilość krawędzi 
* |f| - wartość maksymalnego przepływu

## niezmiennik pętli:
Niezmiennikiem w algorytmie Forda-Fulkersona jest fakt, że w każdej iteracji pętli while, wartość *max_flow* odpowiada maksymalnemu przepływowi znalezionemu do tej pory, a macierz *self.flow* reprezentuje aktualny przepływ w sieci, spełniając warunki równowagi przepływu i ograniczenia przepustowości.

##
# Edmonds-Karp
Algorytm Edmondsa-Karpa jest implementacją algorytmu Forda-Fulkersona z użyciem przeszukiwania wszerz (BFS) do znajdowania ścieżek powiększających. Służy do znajdowania maksymalnego przepływu w sieci przepływowej. 

W krainie pomaga to płaszczakom w problemie związanym z dostawami płotów do punktu odbioru. Chcą oni jak najbardziej zredukować ilość płaszczaków potrzebnych do noszenia płotów (tragarzy) a zarazem zmaksymalizować ilość dostarczonych płotów w pojedynczej dostawie. Problemem jest to, iż każda droga ma określoną maksymalną ilość płotów, którą można przez tą drogę przetransportować. Zatem ten algorytm idealnie się sprawdzi do tego - uwzględniając warunki dróg (maksymalna ilość płotów na daną drogę) wskaże nam, ile jesteśmy w stanie przetransportować płotów od fabryki do punktu odbioru przez daną sieć dróg.

## dane wejściowe: 
Graf w postaci listy list liczb typu float

```python
graph = [ 
           [x1, y1, z1, ...], 
           [x2, y2, z2, ...], 
           ..., 
        ]
```

## dane wyjściowe: 
Liczba typu float opisująca maksymalny przepływ
```python
max_flow = (float)result
```

## złożoność obliczeniowa: 
### O(V * E^2) 
* V - liczba wierzchołkow 
* E to ilość krawędzi

## niezmiennik pętli:
Niezmiennikiem w algorytmie Edmondsa-Karpa jest fakt, że w każdej iteracji pętli while, wartość *max_flow* odpowiada maksymalnemu przepływowi znalezionemu do tej pory, a macierz *self.flow* reprezentuje aktualny przepływ w sieci, który spełnia warunki równowagi przepływu i ograniczenia przepustowości.

##
# Huffman
Algorytm Huffmana jest stosowany do kompresji danych przez tworzenie drzewa kodowego o minimalnej sumarycznej długości kodów.

Płaszczaki, a szczególnie informatyk na zlecenie Heretyka, stosuje ten algorytm do zapisania melodii na komputerze, który to ma ograniczone miejsce. Bez tego algorytmu informatyk nie byłby w stanie zapisać całej melodii.

## dane wejściowe: 
Tekst typu string
```python
text = (string)txt
```

## dane wyjściowe: 

Zakodowany tekst w postaci ciągu liczb 0, 1

```python
result = "0110010010..."
```

## złożoność obliczeniowa: 
### O(n * log(n))
* n - liczba symboli

## niezmiennik pętli:
Niezmiennikiem w algorytmie Huffmana, w kontekście budowy drzewa Huffmana, jest fakt, że w każdej iteracji pętli while, kolejka priorytetowa zawiera węzły, które reprezentują drzewa poddrzew, a każdy węzeł jest korzeniem poddrzewa Huffmana dla przetworzonych do tej pory znaków i ich częstotliwości. 
* **Drzewa poddrzew Huffmana**: Kolejka priorytetowa zawsze zawiera węzły, które są korzeniami drzew poddrzew Huffmana. Po każdej iteracji pętli while, drzewa te są łączone w większe drzewa, aż do momentu, gdy pozostanie jedno drzewo, które będzie pełnym drzewem Huffmana.

* **Kolejność węzłów**: Kolejka priorytetowa jest utrzymywana w taki sposób, że węzły z najniższymi częstotliwościami są przetwarzane jako pierwsze. To gwarantuje, że najrzadziej występujące znaki znajdują się bliżej liści drzewa Huffmana, co prowadzi do krótszych kodów dla bardziej popularnych znaków.

* **Korektywa drzewa**: Po każdej iteracji pętli while, nowe węzły tworzone przez połączenie dwóch węzłów o najniższych częstotliwościach są ponownie dodawane do kolejki priorytetowej, co zapewnia, że drzewo Huffmana jest budowane poprawnie i zgodnie z zasadą minimalnej redundancji.

##
# Knuth-Morris-Pratt (KMP)
Algorytm Knutha-Morrisa-Pratta służy do efektywnego wyszukiwania wzorca w tekście

Płaszczaki strasznie nienawidzą dźwięku "poli". Zatem z pomocą przychodzi ten algorytm, który to w efektywny sposób znajdzie ten dźwięk i pozwoli zamienić go na ulubiony przez płaszczaków "boli".

## dane wejściowe: 
* tekst typu string
* wzorzec typu string
```python
text = (string)txt
pattern = (string)pttrn
```

## dane wyjściowe: 
Lista indeksów opisujących miejsce wystąpienie danego wzorca
```python
result = [idx1, idx2, idx3, ...]
```

## złożoność obliczeniowa: 
### O(n + m) 
* n - długość tekstu
* m - długość wzorca

## niezmiennik pętli:
Niezmiennikiem w algorytmie KMP jest fakt, że w każdej iteracji odpowiedniej pętli, bieżący stan tablicy prefiksów prefix lub wskaźników *i* i *j* odzwierciedla aktualne dopasowanie prefiksu wzorca do podciągu w tekście. W budowie tablicy prefiksów *prefix[i]* reprezentuje długość najdłuższego prefiksu będącego jednocześnie sufiksem podciągu wzorca kończącego się na pozycji *i*. Podczas wyszukiwania wzorca w tekście, wskaźnik *j* śledzi bieżącą długość dopasowania wzorca, zapewniając poprawne i efektywne znajdowanie wszystkich wystąpień wzorca w tekście.

##
# Drzewo przedziałowe

Drzewo przedziałowe (segmentowe) służy do efektywnego wykonywania operacji na przedziałach.

## dane wejściowe:
* List[Guard] - lista obiektów klasy Guard
* Guard - obiekt klasy Guard
* Przedział [a, b]

## dane wyjściowe:
* maksymalna wartość w przedziale

## złożoność obliczeniowa:
* budowanie drzewa: O(n)
* zapytanie: O(log(n))
* aktualizacja: O(log(n))

##
## Algorytm zachłanny do ustalenia patrolu

Algorytm zachłanny do ustalenia patrolu polega na wybraniu miejsc odpoczynku dla strażnika. Strażnik zatrzymuję się po maksymalnej ilosći kroków lub gdy napotyka punkt ciemniejszy od poprzedniego.

## dane wejściowe:
* List[Point] - lista obiektów klasy Point
* max_steps - maksymalna ilość kroków

## dane wyjściowe:
* Lista punktów, w których strażnik się zatrzymał i czy zrobił to z własnej woli.

## złożoność obliczeniowa:
### O(n)
* n - ilość strażników

## niezmiennik pętli:
Niezmiennikiem w algorytmie **patrol_route** jest fakt, że w każdej iteracji pętli for, lista *stops* zawiera poprawnie zidentyfikowane przystanki na trasie patrolu zgodnie z warunkami jasności punktów i maksymalnej liczby kroków. Każdy przystanek jest dodawany do *stops* tylko wtedy, gdy jasność punktu spada w porównaniu do poprzedniego punktu lub liczba kroków osiągnęła wartość *max_steps*. Wskaźnik *steps* jest zawsze poprawnie resetowany po dodaniu przystanku, co zapewnia, że trasa patrolu spełnia wymagane warunki przystanków.