import requests

GITHUB_API = 'https://api.github.com/users/'
GITHUB_API_REQUESTS = '/repos?per_page=100&page='


class GitRepositoryHandler:
    def __init__(self, name):
        self.username = name

    def list_repositories(self):
        page_number = 1

        repositories_info = self.get_repository_info(page_number)

        result = []

        if len(repositories_info) == 0:
            result.append("the chosen user does not exist or has no repositories")
            return result

        while len(repositories_info) > 0:
            for repository in repositories_info:
                result.append(
                    "repository name: " + repository['name'] + " stars: " + str(repository['stargazers_count']))
            page_number += 1
            repositories_info = self.get_repository_info(page_number)

        return result

    def get_total_stars(self):
        page_number = 1

        repositories_info = self.get_repository_info(page_number)

        if len(repositories_info) == 0:
            return "the chosen user does not exist or has no repositories"

        stars_sum = 0
        while len(repositories_info) > 0:
            for repository in repositories_info:
                stars_sum += repository['stargazers_count']
            page_number += 1
            repositories_info = self.get_repository_info(page_number)

        return str(stars_sum)

    def get_repository_info(self, i):
        repository_info = requests.get(GITHUB_API + self.username + GITHUB_API_REQUESTS + str(i))
        return repository_info.json()
