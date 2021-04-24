import requests

APIGITHUB = 'https://api.github.com/users/'
APIGITHUB_RECORDS = '/repos?per_page=100&page='

class TooManyRequestsError(Exception):
    pass

class gitRepo:
    def __init__(self,name):
        self.username = name

    def listRepos(self):
        i = 1
        r = requests.get(APIGITHUB + self.username + APIGITHUB_RECORDS + str(i))
        dict_list = r.json()

        result = []
        while(len(dict_list)!=0):
            for dict in dict_list:
                result.append("repository name: "+dict['name']+" stars: "+str(dict['stargazers_count']))
            i= i+ 1
            r = requests.get(APIGITHUB + self.username + APIGITHUB_RECORDS + str(i))
            dict_list = r.json()

        return result


    def getStars(self):
        i = 1
        r = requests.get(APIGITHUB + self.username + APIGITHUB_RECORDS + str(i))
        dict_list = r.json()

        stars_ctr = 0
        while(len(dict_list)!=0):
            for dict in dict_list:
                stars_ctr+=dict['stargazers_count']
            i+=1
            r = requests.get(APIGITHUB + self.username + APIGITHUB_RECORDS + str(i))
            dict_list = r.json()

        return str(stars_ctr)


