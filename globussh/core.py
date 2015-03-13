from subprocess import call, check_output


def globus_exists(path):
    foo = check_output(args=["/usr/bin/ssh", "globus", "ls {:s}".format(path)])
    return not len(foo) == 0


def transfer_sync(transfer, label="globussh_sync"):
    with open("tmp.transfer", "w") as f:
        f.write(transfer)
    taskid = check_output(args=["/usr/bin/ssh",
                                "globus",
                                "transfer --generate-id"]
                          ).decode("utf-8")
    with open("tmp.transfer", "r") as f:
        call(args=["/usr/bin/ssh",
                   "globus",
                   "transfer",
                   "-s 3 ",
                   "--label={:s}".format(label),
                   "--taskid={:s}".format(taskid)],
             stdin=f)
    call(args=["/usr/bin/ssh", "globus", "wait -q {:s}".format(taskid)])


def transfer_async(transfer, label="globussh_async"):
    with open("tmp.transfer", "w") as f:
        f.write(transfer)
    with open("tmp.transfer", "r") as f:
        call(args=["/usr/bin/ssh",
                   "globus",
                   "transfer",
                   "-s 3",
                   "--label={:s}".format(label)],
             stdin=f)
