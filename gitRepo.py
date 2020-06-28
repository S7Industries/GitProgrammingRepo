from gitHandle import gitRepo
from dataServer import *
import getpass

print ('Server address registered: \n')
for i in server:
    print(str(server.index(i))+')'+i)

print('Username registered: \n')
for i in username:
    print(str(username.index(i))+')'+i)

print('Remote folder registered: \n')
for i in remoteFolder:
    print(str(remoteFolder.index(i))+')'+i)


serverNumber = int(raw_input('Insert number of server to connect: '))
usernameNumber = int(raw_input('Insert number of username to connect: '))
remoteFolderNumber = int(raw_input('Insert number of remote folder to connect: '))
password = getpass.getpass('Insert password: ')

ssh = gitRepo(server[serverNumber],username[usernameNumber], psw[password], remoteFolder[remoteFolderNumber]) #if you use array 
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
