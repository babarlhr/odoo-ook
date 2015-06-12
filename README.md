# Ook!

Ook is a command line interface for Odoo developpers.
It automates away the complex and boring parts of the
work.

## Install

    sudo pip install odoo-ook

## Usage Examples
    
    ook start

Typing this command will automatically start the odoo server. 
It will creates a database for the current branch, kill
a previously launched server, etc. This command works anywhere, ook will
find the path to the odoo install automatically. 

    ook reset

Relaunch the server with a fresh database

    ook try branchname

Typing this command will automatically download the branch from
the Odoo git repository and create a server / database for 
this branch on a new port. 

    ook find stuff

Find matching files in the odoo repository

    ook help

Will show you the list of available helper commands

    
