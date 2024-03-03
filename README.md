# Wprowadzenie do projektu grupy 3

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

## Instalacja zależności

### Krok 3: Instalacja paczek z pliku `requirements.txt`
Znajdując się w głównym katalogu projektu, wykonaj poniższe polecenie, aby zainstalować wszystkie wymagane paczki.

```bash 
pip install -r requirements.txt
```
