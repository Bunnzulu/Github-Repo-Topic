from github import Github,Auth

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

def Auto_Topic(key):
    auth = Auth.Token(key)
    g = Github(auth=auth)
    for repo in g.get_user().get_repos():
        topics = []
        for lan in repo.get_languages().keys():
            topics.append(lan.lower())
        repo.replace_topics(topics)
    g.close()
    
def Manual_Topic(data,key):
    auth = Auth.Token(key)
    g = Github(auth=auth)
    Dict_keys = [i for i in data.keys()]
    for repo in g.get_user().get_repos():
        if repo.name in Dict_keys: 
            topics = data.get(repo.name)
            topics = topics.split(",")
            if type(topics) == list:
                topics = [t.lower().replace(" ","-") for t in topics]
                repo.replace_topics(topics)
    g.close()
        
