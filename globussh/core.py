from subprocess import call, check_output, Popen, PIPE

def globus_exists(path):
    foo = check_output(args=["/usr/bin/ssh", "globus", "ls {:s}".format(path)])
    return not len(foo) == 0


def transfer_sync(transfer, 
                  label="globussh_sync", 
                  activate=False, 
                  sync=3,
                  deadline=None,
                  encrypt=False,
                  verify=False,
                  delete=False):
    taskid = check_output(args=["/usr/bin/ssh",
                                "globus",
                                "transfer --generate-id"]
                          ).decode("utf-8")
    opts = []
    if sync is not None:
      opts.append("-s {:d}".format(sync))
    if activate:
      opts.append("-g")
    if deadline is not None:
      opts.append("-d {:s}".format(deadline))
    if encrypt:
      opts.append("--encrypt")
    if verify:
      opts.append("--verify-checksum")
    else:
      opts.append("--no-verify-checksum")
    if delete:
      opts.append("--delete")

    p = Popen(args=["/usr/bin/ssh", "globus", "transfer"] 
                 + opts
                 + ["--label={:s}".format(label),
                    "--taskid={:s}".format(taskid)],
                    universal_newlines=True,
                    stdin=PIPE)
    p.communicate(input=transfer)
    p.wait()
    call(args=["/usr/bin/ssh", "globus", "wait -q {:s}".format(taskid)])


def transfer_async(transfer,
                   label="globussh_async", 
                   activate=False, 
                   sync=3,
                   deadline=None,
                   encrypt=False,
                   verify=False,
                   delete=False):
    opts = []
    if sync is not None:
      opts.append("-s {:d}".format(sync))
    if activate:
      opts.append("-g")
    if deadline is not None:
      opts.append("-d {:s}".format(deadline))
    if encrypt:
      opts.append("--encrypt")
    if verify:
      opts.append("--verify-checksum")
    else:
      opts.append("--no-verify-checksum")
    if delete:
      opts.append("--delete")

    p = Popen(args=["/usr/bin/ssh", "globus", "transfer"] 
                 + opts
                 + ["--label={:s}".format(label)],
                    universal_newlines=True,
                    stdin=PIPE)
    p.communicate(input=transfer)
    p.wait()
