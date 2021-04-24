import requests

GITHUB_API = 'https://api.github.com/users/'
GITHUB_API_REQUESTS = '/repos?per_page=100&page='


class GitUser:
    def __init__(self, name):
        self.username = name

    def listRepositories(self):
        i = 1

        repositories_info = self.getRepositoryInfo(i)

        result = []

        if len(repositories_info) == 0:
            result.append("the chosen user not exists or has no repositories")
            return result

        while len(repositories_info) > 0:
            for repository in repositories_info:
                result.append(
                    "repository name: " + repository['name'] + " stars: " + str(repository['stargazers_count']))
            i = i + 1
            repositories_info = self.getRepositoryInfo(i)

        return result

    def getTotalStars(self):
        i = 1

        repositories_info = self.getRepositoryInfo(i)

        if len(repositories_info) == 0:
            return "the chosen user not exists or has no repositories"

        stars_sum = 0
        while len(repositories_info) > 0:
            for repository in repositories_info:
                stars_sum += repository['stargazers_count']
            i += 1
            repositories_info = self.getRepositoryInfo(i)

        return str(stars_sum)

    def getRepositoryInfo(self, i):
        r = requests.get(GITHUB_API + self.username + GITHUB_API_REQUESTS + str(i))
        return r.json()
