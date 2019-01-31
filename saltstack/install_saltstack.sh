#!/bin/bash
# @Time     : 2019/1/31 14:01
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : install_saltstack.sh

salt_master_name="salt-master"
salt_master_ip="10.2.1.11"

which wget
[ $? -eq 0 ] || ( set -x;yum -y install wget )

modify_repo(){
    sed -i 's/gpgcheck=1/gpgcheck=0/' /etc/yum.repos.d/saltstack-rhel6.repo
}

install_salt(){
    if [ x$1 == x"master" ];then
        ( set -x
        yum -y install salt-master
        if [ $? -ne 0 ];then
            modify_repo
            yum -y install salt-master
        else
            echo 'Salt-master installation completed!' 
        fi )
    else
        ( set -x
        yum -y install salt-minion
        if [ $? -ne 0 ];then
            modify_repo
            yum -y install salt-minion
        else
            echo 'Salt-minion installation completed!'
        fi )
        if [ $? -eq 0 ];then
            echo "master: ${salt_master_name}" > /etc/salt/minion
            echo "id: `hostname`" >> /etc/salt/minion
            echo "${salt_master_ip}    ${salt_master_name}" >>/etc/hosts
        else
            exit 1
        fi
    fi
}

configure_salt_master(){
cat > /etc/salt/master <<EOF
default_include: master.d/*.conf
interface: ${salt_master_ip}
ipv6: False
publish_port: 4505
user: root
ret_port: 4506
pidfile: /var/run/salt-master.pid
root_dir: /
conf_file: /etc/salt/master
pki_dir: /etc/salt/pki/master
cachedir: /var/cache/salt/master
show_timeout: True
color: True
job_cache: True
minion_data_cache: True
cache: localfs
auto_accept: False
file_roots:
  base:
    - /srv/salt
pillar_roots:
  base:
    - /srv/pillar
EOF
}

centos6(){
    wget -O /etc/yum.repos.d/saltstack-rhel6.repo http://repo.saltstack.com/yum/redhat/6.9/x86_64/saltstack-rhel6.repo 
    install_salt
    if [ x$1 == x"master" ];then
        configure_salt_master
        /etc/init.d/salt-master start
        chkconfig --add salt-master
        chkconfig salt-master on
    else
        /etc/init.d/salt-minion start
        chkconfig --add salt-minion
        chkconfig salt-minion on
    fi
}

centos7(){
    wget -O /etc/yum.repos.d/saltstack-rhel7.repo http://repo.saltstack.com/yum/redhat/7.4/x86_64/saltstack-rhel7.repo
    install_salt
    if [ x$1 == x"master" ];then
        configure_salt_master    
        systemctl start salt-master
        systemctl enable salt-master
    else
        systemctl start salt-minion
        systemctl enable salt-minion
    fi
}

main(){
    if [[ `cat /etc/redhat-release` =~ "6." ]];then
        centos6
    elif [[ `cat /etc/redhat-release` =~ "7." ]];then
        centos7
    fi
}

main
