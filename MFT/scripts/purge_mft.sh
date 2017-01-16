#!/bin/sh

export ORACLE_HOME=/home/oracle/Oracle/Middleware/Oracle_Home
export WLST_SCRIPT=/home/oracle/purge_mft.py

${ORACLE_HOME}/mft/common/bin/wlst.sh ${WLST_SCRIPT}

exit $?

# test
