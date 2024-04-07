<h1 align="center">TBH Creatures</h1>
<div align="center">
<h2 align="center">Fireplace</h2>
<img src="app/static/img/logoxd.svg" width="100px">
</div>

## W ramach hackathonu Hacknarok 2024

### Opis projektu

Aplikacja stworzona z myślą o pomaganiu użytkownikom w utrzymywaniu skupienia podczas wykonywania zadań. Utrzymana w klimacie nordyckim, pozwala przenieść się do świata wikingów, gdzie zasiadając przy wspólnym ognisku wojownicy mogą w pełni poświęcić się planowaniu bitew, nie rozpraszając się mediami społecznościowymi.

### Instrukcja użytkowania
#### Strona logowania i rejestracji

Strona główna umożliwia uzytkownikom założenie własnego konta w oparciu o nazwę użytkownika i hasło. Użytkownikom już posiadającym konto, aplikacja umożliwia logowanie z wykorzystaniem zarejestrowanych danych.

<p align="center">
    <img src="screenshots/rejestracja.png" width="70%">
</p>

<p align="center">
    <img src="screenshots/logowanie.png" width="70%">
</p>

#### Strona główna

Po zalogowaniu do swojego konta, użytkownik ma możliwość stworzenia nowego spotkania (ogniska), lub dołączenia do już istniejącego ogniska. 

<p align="center">
    <img src="screenshots/oknoglowne.png" width="70%">
</p>

#### Ranking
W oknie głównym dostępny jest również ranking. Zawiera on informacje z nazwą użytkownia, punktami przyznawanymi za odwiedziny przy ognisku, oraz ilością wizyt.

<p align="center">
    <img src="screenshots/ranking.png" width="70%">
</p>

#### Rozpal ognisko
Do utworzenia, potrzebne jest podanie jego nazwy. Będzie ona później widoczna w oknie ogniska.\
Po rozpaleniu ogniska, użytkownik hostujący przenoszony jest do jego okna.

<p align="center">
    <img src="screenshots/ogniskohost.png" width="70%">
</p>

Osoba tworząca ognisko widzi kod dostępu do ogniska, którego inni użytkownicy będą potrzebować, aby do niego dołączyć. Widoczna jest również lista osób uczestniczących w spotkaniu. W przypadku, kiedy członek spotkania zminimalizuje okno ogniska, jego nazwa podświetlni się na czerwono.

<p align="center">
    <img src="screenshots/usernotactive.png" width="30%">
</p>

#### Dołącz do ogniska

Dołączając do ogniska należy wpisać kod udostępniony przez gospodarza ogniska. Po dołączeniu, ukazuje się informacja o osobie hostującej ognisko, nazwie spotkania, oraz o panujących na ognisku zasadach.

<p align="center">
    <img src="screenshots/ogniskoguest.png" width="70%">
</p>

Opuszczając ognisko, użytkownik powraca do strony głównej.

### Instrukcja uruchomienia
1. Sklonuj repozytorium
```bash
git clone https://github.com/N0wakowsky/hacknarok
cd hacknarok
```

2. Zainstaluj zależności używając poetry lub pip
```bash
# z poetry
poetry install
```
```bash
# z pip
pip install -r requirements.txt
```

3. Uruchom serwer w środowisku lokalnym
```bash
# z poetry
poetry run python run.py
```
```bash
# z pip
python run.py
```

4. W środowisku lokalnym wejdź do aplikacji poprzez przeglądarkę internetową. Znajduje się pod adresem `localhost:5000`

5. Użytkownicy podłączeni do tej samej sieci będą wstanie dostać się do aplikacji poprzez adres wyświetlony w terminalu po wykonaniu kroku #3.