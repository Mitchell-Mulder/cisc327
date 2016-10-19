import datetime


def write_summary_file(records):
    """
    Write the stored list of records from the current session to a timestamped transaction summary file.
    """
    time = datetime.datetime.now().isoformat()
    time = time.replace(":", "_")
    logfile = open("TSF{}.txt".format(time), "w")
    for i in range(0, len(records)):
        transaction = records[i][0]
        if transaction == "transfer":
            logfile.write("TR {} {} {} ***\n".format(records[i][2],
                                                     records[i][1], records[i][3]))
        elif transaction == "deposit":
            logfile.write("DE {} 00000000 {} ***\n".format(records[i][1],
                                                           records[i][2]))
        elif transaction == "withdraw":
            logfile.write("WD 00000000 {} {} ***\n".format(records[i][1],
                                                           records[i][2]))
        elif transaction == "create":
            logfile.write("CR {} 00000000 000 {}\n".format(records[i][1],
                                                           records[i][2]))
        else:
            logfile.write("DL {} 00000000 000 {}\n".format(records[i][1],
                                                           records[i][2]))
    logfile.write('ES\n')
    logfile.close()
    return
