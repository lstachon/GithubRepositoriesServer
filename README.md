# GithubRepositoriesServer

# Obsługa
Serwer obłusguje zapytania GET w postaci http://localhost:8000/github_username/command gdzie github_username zastępujemy nazwą dowolnego użytkownika githuba,
a command należy zastąpić jedną z następujących komend:  
repositories - by wylistować repozytoria danego użytkownika wraz z ilością gwiazdek dla danego repozytorium.   
total_stars - by uzyskać łączną ilość gwiazdek dla wszystkich repozytoriów danego użytkownika. 

przykład1: http://localhost:8000/lstachon/repositories.   
przykład2: http://localhost:8000/lstachon/total_stars

jeżeli "import request" z klasy gitRepositoryHandler podklreśla się na czerwono należy w projekcie w terminalu napisać następujacą komendę:  
pip install requests

# Możliwe ulepszenia

Ulepszenie requesta listowania repozytoriów o dodanie współtwórców.   

Obsługa wyjątku gdy API githuba odmawia dostępu.
