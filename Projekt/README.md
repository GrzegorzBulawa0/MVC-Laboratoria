Wybrany projekt:

Zadanie 12 – Katalog kolekcji filmów 

Projekt ma formę wykazu filmów, pozwalającego na dyskusję i ocenianie filmów. 

------------

Opis i funkcjonalność projektu:

Wykaz filmów zawiera startową stronę główną index, na której znajduje się krótkie podsumowanie jego zawartości.

W projekcie zaimplementowany jest User z Django, który wraz z implementacją aplikacji account, pozwala na zarejestrowanie prostego konta.

Na utworzone konto można się zalogować, co daje użytkownikowi dostęp do zakładki "Lista Filmów".

W powyższej zakładce znajduje się obecny wykaz filmów dodanych do dyskusji przez admina, bądź innych użytkowników.

Lista umożliwia wyszukiwanie filmu po nazwie, zawiera paginacje (5 na strone) i możliwość filtrowania filmów na bazie najgorsze, najlepsze (według ocen), bądź też najnowsze/najstarsze (wedle tego kiedy zostały dodane).

Na liście użytkownik może wejść w istniejący już tytuł, bądź dodać nowy.

Dodając nowy, musi podać jego nazwę oraz reżysera. 

Wchodząc w dany tytuł, użytkownik może podejrzeć dodane komentarze i oceny, pozwalając mu zobaczyć jak inni odebrali dany film.

Komentarze można filtrować Najlepsze/Najgorsze/Najstarsze/Najnowsze.

Użytkownik może także zostawić komentarz samemu, podając jego treść i ocenę w skali 1-10.

Każdy zalogowany użytkownik może zostawić pod konkretnym filmem tylko jeden komentarz w tym samym czasie.

Zamieszczony komentarz, użytkownik może usunąć, bądź edytować.

Po zakończeniu użytkowania, użytkownik może się wylogować, przyciskiem u dołu strony.

---------------

Wykorzystane technologie:

Python
Django
SQLite
HTML
CSS
Git
Github

---------------
Instalacja i uruchomienie:
Sklonuj repozytorium git clone https://github.com/GrzegorzBulawa0/MVC-Laboratoria/tree/main/Projekt

Przejdź do folderu projektu /Projekt

Zainstaluj Django pip install django

Wykonaj migracje bazy danych py manage.py migrate

Uruchom serwer py manage.py runserver

Otwórz aplikację w przeglądarce http://127.0.0.1:8000/

Panel administratora: http://127.0.0.1:8000/admin/