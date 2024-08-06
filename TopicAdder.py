from github import Github
from github import Auth

Repo = "" # Which repo do you want to add Topics to
Topics = ["html","python"] #What do you want to add
Auto_Topic = True

def Get_Repos(key):
    try:
        auth = Auth.Token(key)
        g = Github(auth=auth)
        repos = list(g.get_user().get_repos())
        g.close()
        repos = [repo.name for repo in repos]
        return repos
    except:
        return None

def Auto_Topic(key,repos):
    auth = Auth.Token(key)
    g = Github(auth=auth)
    for repo in g.get_user().get_repos():
        topics = []
        if repo.name in repos:
            for lan in repo.get_languages().keys():
                topics.append(lan.lower())
            repo.replace_topics(topics)
    g.close()
    
def Manual_Topic():
    pass # TODO
        
