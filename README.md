# Ook!

Ook is a command line interface for Odoo developpers.
It automates away the most annoying and boring parts 
of the workflow. 

Ook assumes that you have one directory with Odoo installed
as a git repository and that you periodically change the
branch to do stuff. If you have a different workflow,
ook may not be as helpful. 

## Install

    sudo pip install odoo-ook
    sudo ook install

## Usage Examples
    
    ook start

This command will start the odoo server in the current terminal.
It will create a database for the current branch, kill
a previously launched server, etc. Ook command works from anywhere,
Ook will select the Odoo server with the following heuristic.

  - If you are in a subdirectory of an odoo install, it will use that one.
  - Otherwise it will use the previously used odoo install.
  - Otherwise it will try to find odoo in the usual install directories.

<b></b>

    ook reset

Relaunch the server with a fresh database

    ook try branchname

Typing this command will automatically download the branch from
the right Odoo git repository and create a temporary 
server / database for this branch on a new port.

All of this is done in a way such that your odoo repository is 
not modified. (Useful when you want to try a new branch in the
middle of your work)

    ook find stuff

Find matching files in the odoo repository

    ook help

Will show you the list of commands

