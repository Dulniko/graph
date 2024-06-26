# Wprowadzenie do projektu grupy 3

- Jakub Dulnikowski
- Kamil Szpechciński
- Julian Pryczkowski

Witaj w naszym projekcie! Aby zapewnić płynne działanie i izolację od pozostałych projektów, korzystamy ze środowiska wirtualnego. Poniżej znajdziesz instrukcje, jak skonfigurować środowisko i zainstalować wszystkie potrzebne zależności.

## Instalacja środowiska wirtualnego

Zanim zainstalujesz zależności, musisz mieć zainstalowany Python oraz `pip`. Jeśli już to zrobiłeś, możesz przejść do kroku tworzenia środowiska wirtualnego.

### Krok 1: Tworzenie środowiska wirtualnego

Otwórz terminal i przejdź do głównego katalogu projektu. Następnie wykonaj poniższe polecenie, aby utworzyć środowisko wirtualne. Nazwijmy je `venv`.

```bash
python3 -m venv venv
```
### Krok 2: Aktywacja środowiska wirtualnego
Po utworzeniu środowiska wirtualnego, musisz je aktywować. Sposób aktywacji zależy od systemu operacyjnego.

#### Dla użytkowników unix 
```bash 
source venv/bin/activate
```

#### Dla użytkowników windows
```bash 
venv\Scripts\activate
```

### Krok 3: Instalacja paczek z pliku `requirements.txt`
Znajdując się w głównym katalogu projektu, wykonaj poniższe polecenie, aby zainstalować wszystkie wymagane paczki.

```bash 
pip install -r requirements.txt
```

### Krok 4: Zainstaluj aplikacje w trybie edytowalnym
Aby zainstalować aplikacje w trybie edytowalnym, wykonaj poniższe polecenie w głównym katalogu projektu.

```bash
pip install -e .
```

### Krok 5: Odpalanie aplikacji
Aby uruchomić aplikację, wykonaj poniższe polecenie w głównym katalogu projektu.

```bash
uvicorn main:app --reload
```

Aplikacja będzie dostępna pod adresem `http://127.0.0.1:8000`.


## UWAGA! Tailwind CSS
Do projektu dodano Tailwind CSS za pomocą CDN, co pozwala na szybkie prototypowanie i stylizację bez konieczności konfiguracji złożonych narzędzi. Tailwind jest ładowany bezpośrednio w przeglądarce, co eliminuje potrzebę lokalnej kompilacji stylów.


## Uruchomienie testów
Aby uruchomić testy, wykonaj poniższe polecenie w głównym katalogu projektu.

```bash
pytest
```

## Formatowanie kodu
Formatowanie kodu odbywa się za pomocą narzędzia black. Jakość kodu
kontrolowana jest przez narzędzie ruff.

1. Aby sformatować kod, wykonaj poniższe polecenie w głównym katalogu projektu.

```bash
black .
```

2. Aby sprawdzić jakość kodu, wykonaj poniższe polecenie w głównym katalogu projektu.

```bash
ruff check --fix .
```

## Użyte technologie
- FastAPI
- Tailwind CSS
- Pytest
- Black
- Ruff
- jinja2
- networkx
- matplotlib
- htmx