from github import Github
import os
import subprocess

check = subprocess.Popen("git --version", shell=True)
check.wait()
if check.returncode != 0:
    print("looks like the git executable is not in your path!")
    exit(1)

try:
    githubToken = os.environ['GITHUB_API_TOKEN']
except KeyError:
    print("Please set GITHUB_API_TOKEN environment variable!")
    exit(1)

g = Github(githubToken)

dstDir = "repos"

for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo.clone_url)
    dst = dstDir + "/" + repo.name
    if os.path.exists(dst):
        fetch = subprocess.Popen("cd " + dst + "&& git fetch", shell=True)
        fetch.wait()
        if fetch.returncode != 0:
            print("Failed to fetch " + repo.name)
    else:
        clone = subprocess.Popen("git clone --mirror " + repo.clone_url + " " + dst, shell=True)
        clone.wait()
        if clone.returncode != 0:
            print("Failed to clone " + repo.name)