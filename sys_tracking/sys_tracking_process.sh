#!/bin/bash

# script variables

DIR=/home/jsw65/Documents/utils/python-snippets/sys_tracking
SCRIPT=$DIR/sys_tracking_append.py
SCRIPT_NAME=sys_tracking_append
SCRIPT_OPTS=$DIR
SCRIPT_PIDFILE=$DIR/$SCRIPT_NAME.pid

# custom functions

do_start () {
    echo "Starting $SCRIPT_NAME in background ..."
    $SCRIPT $SCRIPT_OPTS &
    PID=$!
    echo "$SCRIPT_NAME started with pid $PID"
    touch $SCRIPT_PIDFILE
    echo $PID > $SCRIPT_PIDFILE
}

do_stop () {
    PID=$(<"$SCRIPT_PIDFILE")
    echo "Killing $SCRIPT_NAME using pid $PID ..."
    sudo kill -15 $PID
    echo "$SCRIPT_NAME killed"
}

do_clean () {
    echo "Cleaning $SCRIPT_NAME ..."
    echo "rm -f $DIR/*.LOG $DIR/*.pid"
    rm -f $DIR/*.LOG $DIR/*.pid
}

# control structure to handle command line argument (start|stop|retart|reload|force-reload|status|*)

case "$1" in
    
    start|stop)
        do_${1}
        ;;
    
    restart|reload|force-reload)
        do_stop
        do_start
        ;;
    
    status)
        ps -p $(<"$SCRIPT_PIDFILE")
        ;;
    
    clean|clear)
        do_stop &>/dev/null # this is hacky
        do_clean
        ;;
        
    *)
        echo "Usage: /etc/init.d/$SCRIPT_NAME {start|stop|restart|status|clear}"
        exit 1
        ;;
    
esac

exit 0