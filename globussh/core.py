from subprocess import call, check_output, Popen, PIPE

def globus_exists(path):
    foo = check_output(args=["/usr/bin/ssh", "globus", "ls {:s}".format(path)])
    return not len(foo) == 0


def transfer_sync(transfer, label="globussh_sync"):
    taskid = check_output(args=["/usr/bin/ssh",
                                "globus",
                                "transfer --generate-id"]
                          ).decode("utf-8")
    p = Popen(args=["/usr/bin/ssh",
                    "globus",
                    "transfer",
                    "-s 3 ",
                    #"-g",
                    "--label={:s}".format(label),
                    "--taskid={:s}".format(taskid)],
                    universal_newlines=True,
                    stdin=PIPE)
    p.communicate(input=transfer)
    p.wait()
    call(args=["/usr/bin/ssh", "globus", "wait -q {:s}".format(taskid)])


def transfer_async(transfer, label="globussh_async"):
    p = Popen(args=["/usr/bin/ssh",
                    "globus",
                    "transfer",
                    "-s 3 ",
                    "--label={:s}".format(label)],
                    universal_newlines=True,
                    stdin=PIPE)
    p.communicate(input=transfer)
    p.wait()
