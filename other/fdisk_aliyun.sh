#!/bin/bash


if [ -z $1 ];then
    echo "Usage:./hostinit.sh hostname"
    exit 1
fi

hostname=$1
ip=192.168.100.${hostname##*-}


Fdisk (){
ssh $ip "[ -d /data ] && exit 1 || mkdir /data"
ssh $ip "cat >/tmp/fdisk.txt <<EOF
n
p
1


w
EOF"
ssh $ip 'fdisk /dev/vdb < /tmp/fdisk.txt'
ssh $ip 'mkfs.ext4 /dev/vdb1'
ssh $ip "echo '/dev/vdb1		/data			ext4	defaults	0 0' >> /etc/fstab"
ssh $ip 'mount -a'
ssh $ip "rm -f /tmp/fdisk.txt"
}


Fdisk
