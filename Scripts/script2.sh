#!/bin/bash
clear                                # clear terminal window

echo "Hello, $USER"                  # dollar sign is used to get content of
echo                                 # variable

echo "Your homedirectory is: $HOME"  # show homedirectory
echo

echo "Your terminal type is: $TERM"
echo

echo "These is all the services started up in runlevel 3 on your system:"
ls /etc/rc3.d/S*
echo

echo "That's all..."
