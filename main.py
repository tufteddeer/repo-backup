from github import Github
import os


g = Github(os.environ['GITHUB_API_TOKEN'])
dstDir = "repos"

for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo.clone_url)
    dst = dstDir + "/" + repo.name
    if os.path.exists(dst):
        os.system("cd " + dst + "&& git fetch")
    else:
        os.system("git clone --mirror " + repo.clone_url + " " + dst)