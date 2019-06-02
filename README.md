# repo-backup

_Disclaimer: This is just quickly hacked together, i have no idea how well it works._

Simple script that backups your github reositories.

Uses PyGithub to speak to the github.com api.

# Usage

## Backup:

`export GITHUB_API_TOKEN=mytoken`

`python backup-repos.py /path/to/backup/directory`

## Restore

`git clone /path/to/backup/directory/myrepository`