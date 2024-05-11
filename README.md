
Prosty Serwer HTTP, FTP i SSH

## Autor
Imię i Nazwisko: Radosław Stawiszynski
Rok Akademicki: 2022/2023
Kierunek Studiów: Informatyka

## Opis Programu
# Cel Programu
Program jest prostym serwerem obsługującym protokoły HTTP, FTP i SSH. Zapewnia podstawową funkcjonalność każdego z tych serwerów, a także dodatkowe logowanie zdarzeń.

## Opis Kodu
# Serwer HTTP
Serwer HTTP działa na porcie 8000.
Obsługuje podstawowe zapytania HTTP GET i loguje zdarzenia, takie jak zapytania klientów.

# Serwer FTP
Serwer FTP działa na porcie 2121.
Umożliwia dostęp do folderu FTP z uprawnieniami do odczytu, zapisu i wykonania.
Loguje zdarzenia, takie jak połączenia i operacje na plikach.

# Serwer SSH
Serwer SSH działa na porcie 2222.
Pozwala na bezpieczne zdalne połączenie i uruchomienie polecenia SFTP.
Loguje zdarzenia, takie jak połączenia klientów.

## Instrukcje Uruchomienia
Instalacja zależności:
Upewnij się, że masz zainstalowane wymagane biblioteki, użyj poniższej komendy:

## Uruchomienie Programu:
Uruchom program poprzez uruchomienie pliku main.py. Po uruchomieniu, serwery HTTP, FTP i SSH będą działały na odpowiednich portach.

## Testowanie:
Aby przetestować serwer HTTP, otwórz przeglądarkę i odwiedź http://localhost:8000.
Aby przetestować serwer FTP, użyj dowolnego klienta FTP i połącz się z localhost:2121, używając nazwy użytkownika user i hasła password.
Aby przetestować serwer SSH, użyj klienta SSH i połącz się z localhost:2222, używając klucza prywatnego.

## Zabezpieczenia
# Ograniczenia Dostępu FTP:
Dostęp do serwera FTP wymaga uwierzytelnienia poprzez nazwę użytkownika i hasło. Użytkownicy anonimowi mają ograniczone uprawnienia.

# Bezpieczne Połączenia SSH:
Serwer SSH wymaga klucza prywatnego do uwierzytelnienia. Połączenia są zabezpieczone protokołem SSL/TLS.

## Logowanie Zdarzeń:
Program loguje zdarzenia dla każdego serwera, co ułatwia monitorowanie aktywności i identyfikację ewentualnych problemów.

## Zamykanie Programu
Program może zostać zakończony poprzez naciśnięcie klawisza Ctrl+C w terminalu.

## Uwagi
Program ten służy wyłącznie celom edukacyjnym i demonstracyjnym. W rzeczywistych środowiskach produkcyjnych konieczne jest wprowadzenie dodatkowych zabezpieczeń i funkcji, aby zapewnić stabilność i bezpieczeństwo usług sieciowych.