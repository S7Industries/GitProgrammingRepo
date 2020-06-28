import os
import re
from pexpect import pxssh

class gitRepo:

    def __init__(self, server, username, psw, remoteFolder):
        self.server = server
        self.username = username
        self.psw = psw
        self.dirList = None
        self.remoteFolder = remoteFolder

    def login(self):
        self.ssh = pxssh.pxssh()

        try:
            self.logout()
        except Exception:
            print('not logged')

        if not self.ssh.login(self.server, self.username, self.psw):
            print ('not logged')
            print (str(self.ssh))
        else:
            print ('logged to: '+ self.server)
            
    def logout(self):
        self.ssh.logout()
    
    def createRepo(self, nameRepo, languageRepo):
        #data
        self.nameRepo = nameRepo
        self.languageRepo = languageRepo

        #cd to git dir
        self.ssh.sendline('cd && cd ./'+self.remoteFolder)
        self.ssh.prompt()

        #list the dir available based on programming language [name folder]
        self.dirList = self.listDir()

        #enter in dir based on language
        if (self.languageRepo in self.dirList):
            self.ssh.sendline('cd ./'+self.languageRepo)
            self.ssh.prompt()

        #create dir 
        self.ssh.sendline('mkdir '+self.nameRepo+' && cd ./'+self.nameRepo+' && git init --bare')
        self.ssh.prompt()

        print ('repo: '+self.nameRepo+' created')
        
    def removeRepo(self, nameRepo, languageRepo):
        #data
        self.nameRepo = nameRepo
        self.languageRepo = languageRepo

        #return in main gitRepo dir
        self.ssh.sendline('cd && cd ./'+self.remoteFolder)
        self.ssh.prompt()

        #enter in dir based on language
        if (self.languageRepo in self.dirList):
            self.ssh.sendline('cd ./'+self.languageRepo)
            self.ssh.prompt()

        self.ssh.sendline('sudo rm -r'+self.nameRepo)
    
    def showRepo(self):
        
        #return in main gitRepo dir
        self.ssh.sendline('cd && cd ./'+self.remoteFolder)
        self.ssh.prompt()

        #ls git repo
        self.ssh.sendline('ls')
        self.ssh.prompt()
        print (self.ssh.before[5:])


    def pwd(self):
        
        self.ssh.sendline('pwd')
        self.ssh.prompt()

        self.remoteAdd = ' remote add ' + self.nameRepo +' ' + self.username +'@' + self.server +':' + self.ssh.before[5:] #delete the print command and \n [pwd \n]
        self.remoteClone = 'git clone' + self.nameRepo+ ' ' + self.username +'@' + self.server + self.ssh.before[5:]
        
        return self.remoteAdd, self.remoteClone
        


    def listDir(self):

        #cd to git dir
        self.ssh.sendline('cd && cd ./'+self.remoteFolder)
        self.ssh.prompt()

        #ls dir 
        self.ssh.sendline('ls')
        self.ssh.prompt()        
        self.listDir = self.ssh.before[5:].split(' ')
        self.listDir = re.sub(r"\[0m\\x1b\[01;34m|\\x1b\[01\;34m|\\x1b\[0m|\\r\\n", '\1', str(self.listDir))
        print(self.listDir)
        return self.listDir

    def addLocal(self, localPath):
        self.localPath = localPath
        self.remoteAdd, self.remoteClone = self.pwd()
        os.system('git init '+ self.localPath)
        os.system('git -C ' + self.localPath + self.remoteAdd)
        gitCloneFile = open(self.localPath+'/gitClone.txt', 'w')
        gitCloneFile.write(self.remoteClone)
        gitCloneFile.close()
        


        
