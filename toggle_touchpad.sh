# A function for logging
safemk () {
if [ ! -d $1 ];
  then mkdir $1;
  chmod +rw $1;
fi
}
logdir=/home/$USER/.toggleTouchpad
touchpadString="TouchPad"
touchpadID=$(xinput list | grep $touchpadString | awk -F " " '{print $6}' | awk -F "=" '{print $2}')
touchpadEnabled=$(xinput list-props $touchpadID | grep "Device Enabled" | awk -F ":" '{print $2}')
sleeptime=1

# Create the logging directory
safemk $logdir
touch $logdir/errorLog.txt

# Check for arguments on the command line
if test $# -eq 1
then
        # Change the argument to lowercase
        arg1=$(echo $1 | tr [:upper:] [:lower:])
        cliArg=1
else
        # There is no argument.
        cliArg=0
fi

if [ $cliArg -eq 1 ]
then
        # If there's an argument, check to see whether it is on, off, or junk
        if [ $arg1 = 'on' ]
        then
                # The argument was 'on', so turn the touchpad on
                xinput --set-prop $touchpadID "Device Enabled" 1
                if [ $(xinput list-props $touchpadID | grep "Device Enabled" | awk -F ":" '{print $2}') -eq 0 ]
                then
                        echo "Something went wrong\n" >> $logdir/errorLog.txt
                fi
        elif [ $arg1 = 'off' ]
        then
                # Sleep for a short time to fix a bug that re-enabled the touchpad immediately after disabling it
                sleep $sleeptime
                # The argument was 'off', so turn the touchpad off
                xinput --set-prop $touchpadID "Device Enabled" 0
                if [ $(xinput list-props $touchpadID | grep "Device Enabled" | awk -F ":" '{print $2}') -eq 1 ]
                then
                        echo "Something went wrong, perhaps \$sleeptime needs to be greater than $sleeptime ?\n" >> $logdir/errorLog.txt
                fi
        else
                # The argument was junk, so log the error and go on
                echo "Invalid argument \""$arg1"\" was supplied\n" >> $logdir/errorLog.txt
        fi
else
        # There was no argument, so just toggle the touchpad to the opposite
        # of the state it has now.
        if [ $touchpadEnabled -eq 1 ]
        then
                xinput --set-prop $touchpadID "Device Enabled" 0
        else
                xinput --set-prop $touchpadID "Device Enabled" 1
        fi
fi
