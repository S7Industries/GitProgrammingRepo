from gitHandle import gitRepo
from data import *

ssh = gitRepo(server[1],username[1], psw[1], remoteFolder[0]) #if you use array 
#ssh = gitRepo(server, username ,psw, remoteFolder) #if not use array 

repoData = raw_input('insert repo name and language: ').split(' ')
repoName = repoData[0]
repoLanguage = repoData[1]

localRepo = raw_input('insert local repo path: ')

ssh.login()
ssh.createRepo(repoName, repoLanguage)
ssh.addLocal(localRepo)
# ssh.listDir()
ssh.logout()
