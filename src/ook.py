#!/usr/bin/python
import os
import sys
import subprocess

HELP = """
Usage: ook COMMAND 
   start [args]
       Start the Odoo server on port 8069
       with a db named with the current git
       branch. It will create a database 
       with demo data if it doesn't exist.

       [args] will be passed to the odoo 
       server command line.

   reset [args]
       Restart the server with a new database
       
       [args] will be passed to the odoo
       server command line at restart.

   stop
       Stops the current server.

   log 
       Prints the last 20 commits.
"""
   
def pexec(cmd):
    os.system(cmd)

def rexec(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    return process.communicate()[0]


def log():
    pexec("git log --oneline -n 20")

def main():
    args = sys.argv[1:]
    if len(args) == 0 :
        print "Ook!"
        print HELP
    elif args[0] == "log":
        log()
    else:
        print "Unknown command", args[0]
        print HELP

if __name__ == "__main__":
    main()

