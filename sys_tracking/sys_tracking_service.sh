#!/bin/bash

# daemon variables

DIR=/home/jsw65/Documents/utils/python-snippets/sys_tracking
DAEMON=$DIR/sys_tracking_append.py
DAEMON_NAME=sys_tracking_append
DAEMON_OPTS=$DIR
DAEMON_USER=root
DAEMON_PIDFILE=$DIR/$DAEMON_NAME.pid

# useful daemon functions

. /lib/lsb/init-functions

# custom functions

do_start () {
    log_daemon_msg "Starting system $DAEMON_NAME daemon ..."
    start-stop-daemon --start --background --pidfile $DAEMON_PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON -- $DAEMON_OPTS
    log_end_msg $?
}

do_stop () {
    log_daemon_msg "Stopping system $DAEMON_NAME daemon ..."
    start-stop-daemon --stop --pidfile $DAEMON_PIDFILE --retry 10
    log_end_msg $?
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
        status_of_proc -p $DAEMON_PIDFILE $DAEMON && exit 0 || exit $?
        ;;
    
    clean|clear)
        do_stop &>/dev/null # this is hacky
        do_clean
        ;;
    
    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status|clear}"
        exit 1
        ;;
    
esac

exit 0