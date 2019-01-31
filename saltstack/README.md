##### 本脚本用于自动安装saltstack服务端与客户端，支持CentOS6.x/7.x。

* ##### 安装方法

```bash

# curl -sSLf https://raw.githubusercontent.com/Eivll0m/Ops_Scripts/master/saltstack/install_saltstack.sh -o install_saltstack.sh

# bash install_saltstack.sh

```

* ##### 需要手动修改的地方 

```bash
salt_master_name="salt-master"
salt_master_ip="10.2.1.11"
```
