#!/bin/bash
# @Time     : 2019/1/13 12:01
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : install_shadowsocks_client.sh

set -e

install_shadowsocks(){
    ( set -x;yum -y install epel-release )
    ( set -x;yum -y install python-pip )
    ( set -x;pip install shadowsocks )
    if [ $? -ne 0 ];then
        echo 'shadowsocks installation failed !'
        exit 100
    fi
    [ -d /etc/shadowsocks ] || mkdir /etc/shadowsocks
cat > /etc/shadowsocks/shadowsocks.json <<-'EOF'
{
        "server":"x.x.x.x",
        "server_port":1035,
        "local_address":"127.0.0.1",
        "local_port":1080,
        "password":"password",
        "timeout":300,
        "method":"aes-256-cfb",
        "fast_open": false,
        "workers": 1
}
EOF
cat > /etc/systemd/system/shadowsocks.service <<-'EOF'
[Unit]
Description=Shadowsocks
[Service]
TimeoutStartSec=0
ExecStart=/usr/bin/sslocal -c /etc/shadowsocks/shadowsocks.json
[Install]
WantedBy=multi-user.target
EOF
    echo -e "\033[32mPlease enter shadowsocks server IP: \033[0m"
    read ssip
    echo -e "\033[32mPlease enter shadowsocks server port: \033[0m"
    read ssport
    echo -e "\033[32mPlease enter the shadowsocks connection password: \033[0m"
    read sspasswd
    sed -i "/server\"/s/:.\(.*\).,/:\"${ssip}\",/" /etc/shadowsocks/shadowsocks.json
    sed -i "/server_port/s/:.\(.*\).,/:${ssport},/" /etc/shadowsocks/shadowsocks.json 
    sed -i "/password/s/:.\(.*\).,/:\"${sspasswd}\",/" /etc/shadowsocks/shadowsocks.json 
    systemctl enable shadowsocks.service
    systemctl start shadowsocks.service
    if timeout 3 curl -s --socks5 127.0.0.1:1080 http://httpbin.org/ip|grep -q "${ssip}";then
        echo 'Shadowsocks client service ran successfully !'
    fi
}

install_privoxy(){
    ( set -x;yum -y install privoxy )
    sed -i '\#forward-socks5t   /#{s/^#\s\+//;s#:[^ ]\+#:1080#}' /etc/privoxy/config
    systemctl enable privoxy
    systemctl start privoxy
cat >> /etc/profile <<-'EOF'
PROXY_HOST=127.0.0.1
export all_proxy=http://$PROXY_HOST:8118
export ftp_proxy=http://$PROXY_HOST:8118
export http_proxy=http://$PROXY_HOST:8118
export https_proxy=http://$PROXY_HOST:8118
export no_proxy=localhost,172.16.0.0/16,192.168.0.0/16,127.0.0.1,10.10.0.0/16
EOF
    source /etc/profile
    if curl -Is www.google.com |grep -q 'HTTP/1.1 200 OK';then
	echo -e '\033[32mThe agent has been successfully configured !\033[0m'
    fi
}

main(){
    install_shadowsocks
    install_privoxy
}

main
