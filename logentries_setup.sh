#!/bin/bash

set -e

echo -e "[Main]
pull-server-side-config = False

[ApacheError]
path = /var/log/apache2/error.log
token = $(cat /etc/le/token)

[ApacheHostAccess]
path = /var/log/apache2/other_vhosts_access.log
token = $(cat /etc/le/token)

[ApacheAccess]
path = /var/log/apache2/access.log
token = $(cat /etc/le/token)

" > /etc/le/config
chmod -R 777 /var/log/
service logentries restart
