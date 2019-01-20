##### 本脚本用于自动安装及配置shadowsocks客户端，在CentOS7.x下测试通过。安装过程中需要输入shadowsocks服务器IP、端口及连接密码。

* ##### 安装方法

```bash

# curl -sSLf https://raw.githubusercontent.com/Eivll0m/Ops_Scripts/master/shadowsocks/install_shadowsocks_client.sh -o install_shadowsocks_client.sh

# bash install_shadowsocks_client.sh

```

* ##### 临时取消代理方法

```bash

# while read var; do unset $var; done < <(env | grep -i proxy | awk -F= '{print $1}')

```
