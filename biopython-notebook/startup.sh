#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m'

if ! id -u $JUPYTER_USER > /dev/null 2>&1; then
  echo -e "use local user: " ${BLUE}$JUPYTER_USER${NC}
  addgroup --gid $JUPYTER_UID $JUPYTER_USER
  adduser --uid  $JUPYTER_UID  -s /bin/bash --disabled-password --home $JUPYTER_HOME $JUPYTER_USER
fi

if [ -e $JUPYTER_HOME ];
  then
    echo -e ${GREEN}$JUPYTER_HOME${NC} exists
    chown -R $JUPYTER_UID $JUPYTER_HOME
    chgrp -R $JUPYTER_UID $JUPYTER_HOME
else
  mkdir -p $JUPYTER_HOME
  chown -R $JUPYTER_UID $JUPYTER_HOME
fi

exec jupyter notebook --no-browser --ip=* --port=9803
