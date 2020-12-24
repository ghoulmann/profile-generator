from log_generator.ApacheLog import ApacheLog
from random import randint
from datetime import timedelta
class AccessLog(ApacheLog):
    def __init__(self, timestamp):
        ApacheLog.__init__(self, timestamp)
        #self._user = ApacheLog.makeUser(ApacheLog._user)

        self.out = self._ipv4
        self.out += " - "
        self.out += self._user
        self.out += " [" + timestamp.strftime("%d/%b/%Y:%H:%M:%S") + " " + self._timezone + "] ".upper()
        self.out += "\"GET " + self._endpoint + " HTTP/1.1\"" + " 200 "
        self.out += str(randint(3, 300000))
        #print(self.out, end="\n")


        self._logtime = timestamp + timedelta(seconds=randint(0, 360))
	#LogLine.faketime = logdate
    def __str__(self):
        return self.out
