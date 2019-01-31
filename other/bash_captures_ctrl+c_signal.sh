#!/bin/bash
# Capture signal

trap 'onCtrlC' SIGINT
function onCtrlC () {
    echo "Do you want to exit the current shell script? yes/no"
    read var
    case "$var" in
        YES|yes)
            echo 'exit now !'
            exit 100
            ;;
        NO|no)
            echo 'no...'
            ;;
        *)
            exit 1
            ;;
    esac
}
# Specific script content
while true; do
    echo 'I am working!'
    sleep 1
done
