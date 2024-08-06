from github import Github
from github import Auth
from dotenv import load_dotenv
import os

load_dotenv(".env")

auth = Auth.Token(os.getenv("TOKEN"))



g = Github(auth=auth)

Repo = "" # Which repo do you want to add Topics to
Topics = ["html","python"] #What do you want to add
Auto_Topic = True



if Auto_Topic:
    for repo in g.get_user().get_repos():
        topics = []
        for lan in repo.get_languages().keys():
            topics.append(lan.lower())
        repo.replace_topics(topics)
else:
    repo = g.get_user().get_repo(Repo)
    repo.replace_topics(Topics)
        

g.close()