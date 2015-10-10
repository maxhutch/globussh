from subprocess import call, check_output, Popen, PIPE, STDOUT, check_call

def exists(path):
    foo = check_output(args=["/usr/bin/ssh", "globus", "ls {:s}".format(path)])
    return not len(foo) == 0


def wait(taskid):
  ret = check_output(args=["/usr/bin/ssh", "globus", "wait -q {:s}".format(taskid)],
                     stderr=STDOUT)
  if ret == "Error: No such task id '{:s}'".format(taskid):
    raise RuntimeError("Tried to wait on a task that doesn't exist")
  return

def cancel(taskid):
  return check_call(args=["/usr/bin/ssh", "globus", "cancel {:s}".format(taskid)])


def transfer(transfer, 
             label="globussh_transfer", 
             activate=False, 
             sync=3,
             deadline=None,
             encrypt=False,
             verify=False,
             delete=False,
             block=True):
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

    if block:
      wait(taskid)
    return taskid


def scp(source,
        dest,
        label="globussh_scp", 
        activate=False, 
        sync=3,
        deadline=None,
        encrypt=False,
        verify=False,
        delete=False,
        recursive=False,
        block=True):

    opts = []
    if recursive:
      opts.append("-r")
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
    if not block:
      opts.append("-D")

    return check_call(args=["/usr/bin/ssh", "globus", "scp"] 
                 + opts
                 + [source, dest]) 

def rm(path,
       label="globussh_rm", 
       activate=False, 
       ignore=False,
       deadline=None,
       recursive=False,
       block=True):

    opts = []
    if recursive:
      opts.append("-r")
    if ignore:
      opts.append("-f")
    if activate:
      opts.append("-g")
    if deadline is not None:
      opts.append("-d {:s}".format(deadline))
    if not block:
      opts.append("-D")

    return check_call(args=["/usr/bin/ssh", "globus", "rm"] 
                 + opts
                 + [path]) 


def rename(old, new):
    return check_call(args=["/usr/bin/ssh", "globus", "rename"] 
                 + [old, new])
