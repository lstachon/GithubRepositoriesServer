# GithubRepositoriesServer

# Przygotowanie do uruchomienia

Wymagane jest posiadanie zainstalowanego pythona3 i pakietu requests, pakiet ten mozna zainstalować za pomocą komendy:  
`pip install requests`

# Obsługa
Serwer obłusguje zapytania GET w postaci http://localhost:8000/github_username/command gdzie github_username zastępujemy nazwą dowolnego użytkownika githuba,
a command należy zastąpić jedną z następujących komend:  
repositories - by wylistować repozytoria danego użytkownika wraz z ilością gwiazdek dla danego repozytorium.   
total_stars - by uzyskać łączną ilość gwiazdek dla wszystkich repozytoriów danego użytkownika. 

przykład1: http://localhost:8000/lstachon/repositories.   
przykład2: http://localhost:8000/lstachon/total_stars

Zapytania były testowane na przeglądarkach internetowych Google Chrome i Firefox.

# Możliwe ulepszenia

Ulepszenie requesta listowania repozytoriów o dodanie współtwórców.   

Obsługa wyjątku gdy API githuba odmawia dostępu.  

Wypisywanie repozytoriów dla danego uzytkownika które były pisane w większości w podanym przez nas języku.  
