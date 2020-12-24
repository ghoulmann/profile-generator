from log_generator.ApacheLog import ApacheLog
class AuthLog(ApacheLog):
    def __init__(self):
        super().generate()


    def __str__(self):
        print(self.logline)
