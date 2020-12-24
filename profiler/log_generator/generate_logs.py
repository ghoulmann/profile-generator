from log_generator import AccessLog

def generate_access_log(entries, time):
    timestamp = time
    print(timestamp)
    log_entries = []
    for i in range(0,int(entries)):
        logline = AccessLog(timestamp)
        log_entries.append(logline.__str__())
        timestamp = logline._logtime
        print(timestamp)
    return log_entries


    #with open(outfile, 'a') as fh:
    #        fh.write(logline.__str__()+"\r")