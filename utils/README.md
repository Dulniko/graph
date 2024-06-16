# Graham
Algorytm Grahama służy do znajdowania otoczki wypukłej zbioru punktów na płaszczyźnie. 

Za pomocą tego algorytmu wyznaczamy granicę krainy płaszczaków w sposób najbardziej optymalny, dzięki czemu zostaje zaoszczędzona ilość płotów.

## dane wejściowe: 
Lista punktów jako obiekty klasy Point (plik graham.py)

```python
points = [Point(x1, y1), Point(x2, y2), ...]
```

## dane wyjściowe: 
Lista punktów tworzących otoczkę wypukłą w porządku przeciwnym do ruchu wskazówek zegara. 

```python
result = [Point(x1, y1), Point(x2, y2), ...]
```

## złożoność obliczeniowa: 
### O(n * log(n))
* n - ilość punktów

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