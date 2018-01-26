#!/usr/bin/env python
# coding:utf-8
# author:Eivll0m
# date:2017/03/07

from fabric.api import *
from fabric.colors import *
from time import sleep
import sys

env.roledefs = {
    'server1' : ['admin@10.39.54.159:4399'],
    'server2' : ['admin@10.39.88.58:4399'],
    'server3' : ['admin@10.39.52.217:4399'],
    'server4' : ['admin@10.39.65.68:4399'],
    'server5' : ['admin@10.39.158.136:4399'],
    'server6' : ['admin@10.39.158.143:4399'],
    'server7' : ['admin@10.39.154.153:4399'],
    'server8' : ['admin@10.39.139.90:4399'],
    'server9' : ['admin@10.39.138.12:4399'],
    'server10' : ['admin@10.39.149.78:4399'],
    'server11' : ['admin@10.39.151.150:4399'],
    'server12' : ['admin@10.13.150.25:4399'],
    'server13' : ['admin@10.13.151.68:4399'],
    'server14' : ['admin@10.138.154.50:4399'],
    'server15' : ['admin@10.39.42.125:4399'],
    'server16' : ['admin@10.139.132.186:4399']
    }

@roles('server1')
def wxcontroller_1():
    '部署wxcontroller_1'
    print blue('您正在部署wxcontroller_1')
    local('cd /app/admin/data;rm -rf wxcontroller')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信/workspace/target/wxcontroller /app/admin/data/ &> /app/admin/logs/wxcontroller_rsync.log')
    local('cp /app/admin/config/wxcontroller/jdbc.properties /app/admin/data/wxcontroller/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf wxcontroller_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wxcontroller &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wxcontroller admin@10.39.54.159:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/wxcontroller_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.54.159 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server2')
def wxcontroller_2():
    '部署wxcontroller_2'
    print blue('您正在部署wxcontroller_2')
    local('cd /app/admin/data;rm -rf wxcontroller')
    local('rsync -avz --delete -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信/workspace/target/wxcontroller /app/admin/data/ &> /app/admin/logs/wxcontroller_rsync.log')
    local('cp /app/admin/config/wxcontroller/jdbc.properties /app/admin/data/wxcontroller/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf wxcontroller_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wxcontroller &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wxcontroller admin@10.39.88.58:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/wxcontroller_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.88.58 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')

def wxcontroller():
    '部署所有的wxcontroller'
    execute(wxcontroller_1)
    execute(wxcontroller_2)
	
	
@roles('server6')
def channelmanage_1():
    '部署channelmanage_1'
    print blue('您正在部署channelmanage_1')
    local('cd /app/admin/data;rm -rf channelmanage')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/渠道管理/workspace/target/channelmanage /app/admin/data/ &> /app/admin/logs/channelmanage_rsync.log')
    local('cp /app/admin/config/channelmanage/jdbc.properties /app/admin/data/channelmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf channelmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz channelmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/channelmanage admin@10.39.158.143:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/channelmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.158.143 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		
@roles('server7')
def channelmanage_2():
    '部署channelmanage_2'
    print blue('您正在部署channelmanage_2')
    local('cd /app/admin/data;rm -rf channelmanage')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/渠道管理/workspace/target/channelmanage /app/admin/data/ &> /app/admin/logs/channelmanage_rsync.log')
    local('cp /app/admin/config/channelmanage/jdbc.properties /app/admin/data/channelmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf channelmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz channelmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/channelmanage admin@10.39.154.153:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/channelmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.154.153 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		

def channelmanage():
    '部署所有的channelmanage'
    execute(channelmanage_1)
    execute(channelmanage_2)
	

@roles('server3')
def usermanage_1():
    '部署usermanage_1'
    print blue('您正在部署usermanage_1')
    local('cd /app/admin/data;rm -rf usermanage')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/用户管理/workspace/target/usermanage /app/admin/data/ &> /app/admin/logs/usermanage_rsync.log')
    local('cp /app/admin/config/usermanage/jdbc.properties /app/admin/data/usermanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf usermanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz usermanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/usermanage admin@10.39.52.217:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/usermanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.52.217 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		

@roles('server4')
def usermanage_2():
    '部署usermanage_2'
    print blue('您正在部署usermanage_2')
    local('cd /app/admin/data;rm -rf usermanage')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/用户管理/workspace/target/usermanage /app/admin/data/ &> /app/admin/logs/usermanage_rsync.log')
    local('cp /app/admin/config/usermanage/jdbc.properties /app/admin/data/usermanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf usermanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz usermanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/usermanage admin@10.39.65.68:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/usermanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.65.68 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		
def usermanage():
    '部署所有的usermanage'
    execute(usermanage_1)
    execute(usermanage_2)
	
	
@roles('server3')
def openplatform_1():
    '部署openplatform_1'
    print blue('您正在部署openplatform_1')
    local('cd /app/admin/data;rm -rf openplatform')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/开放平台/workspace/target/openplatform /app/admin/data/ &> /app/admin/logs/openplatform_rsync.log')
    local('cp /app/admin/config/openplatform/jdbc.properties /app/admin/data/openplatform/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf openplatform_`date "+%Y%m%d-%H-%M-%S"`.tar.gz openplatform &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/openplatform admin@10.39.52.217:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/channelmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.52.217 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		

@roles('server4')
def openplatform_2():
    '部署openplatform_2'
    print blue('您正在部署openplatform_2')
    local('cd /app/admin/data;rm -rf openplatform')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/开放平台/workspace/target/openplatform /app/admin/data/ &> /app/admin/logs/openplatform_rsync.log')
    local('cp /app/admin/config/openplatform/jdbc.properties /app/admin/data/openplatform/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf openplatform_`date "+%Y%m%d-%H-%M-%S"`.tar.gz openplatform &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/openplatform admin@10.39.65.68:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/channelmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.65.68 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		
def openplatform():
    '部署所有的openplatform'
    execute(openplatform_1)
    execute(openplatform_2)
	
	
@roles('server5')
def assetmanage_1():
    '部署assetmanage_1'
    print blue('您正在部署assetmanage_1')
    local('cd /app/admin/data;rm -rf assetmanage')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/资产管理/workspace/target/assetmanage /app/admin/data/ &> /app/admin/logs/assetmanage_rsync.log')
    local('cp /app/admin/config/assetmanage/jdbc.properties /app/admin/data/assetmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf assetmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz assetmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/assetmanage admin@10.39.158.136:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/assetmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.158.136 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		
		
@roles('server6')
def assetmanage_2():
    '部署assetmanage_2'
    print blue('您正在部署assetmanage_2')
    local('cd /app/admin/data;rm -rf assetmanage')
    local('rsync -avz -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/资产管理/workspace/target/assetmanage /app/admin/data/ &> /app/admin/logs/assetmanage_rsync.log')
    local('cp /app/admin/config/assetmanage/jdbc.properties /app/admin/data/assetmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf assetmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz assetmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
	print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/assetmanage admin@10.39.158.143:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/assetmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.158.143 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')
		
	
def assetmanage():
    '部署所有的assetmanage'
    execute(assetmanage_1)
    execute(assetmanage_2)


@roles('server1')
def wx_bsmanage_1():
    '部署wx_bsmanage_1'
    print blue('您正在部署wx_bsmanage_1')
    local('cd /app/admin/data;rm -rf wx_bsmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信业务员公众号/workspace/target/wx_bsmanage /app/admin/data/ &> /app/admin/logs/wx_bsmanage_rsync.log')
    local('cp /app/admin/config/wx_bsmanage/jdbc.properties /app/admin/data/wx_bsmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf wx_bsmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_bsmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_bsmanage admin@10.39.54.159:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/wx_bsmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.54.159 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server2')
def wx_bsmanage_2():
    '部署wx_bsmanage_2'
    print blue('您正在部署wx_bsmanage_2')
    local('cd /app/admin/data;rm -rf wx_bsmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信业务员公众号/workspace/target/wx_bsmanage /app/admin/data/ &> /app/admin/logs/wx_bsmanage_rsync.log')
    local('cp /app/admin/config/wx_bsmanage/jdbc.properties /app/admin/data/wx_bsmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf wx_bsmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_bsmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_bsmanage admin@10.39.88.58:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/wx_bsmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.88.58 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


def wx_bsmanage():
    '部署所有的wx_bsmanage'
    execute(wx_bsmanage_1)
    execute(wx_bsmanage_2)


@roles('server8')
def wx_channelmanage_1():
    '部署wx_channelmanage_1'
    print blue('您正在部署wx_channelmanage_1')
    local('cd /app/admin/data;rm -rf wx_channelmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信渠道公众号/workspace/target/wx_channelmanage /app/admin/data/ &> /app/admin/logs/wx_channelmanage_rsync.log')
    local('cp /app/admin/config/wx_channelmanage/jdbc.properties /app/admin/data/wx_channelmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf wx_channelmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_channelmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_channelmanage admin@10.39.139.90:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/wx_channelmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.139.90 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server9')
def wx_channelmanage_2():
    '部署wx_channelmanage_2'
    print blue('您正在部署wx_channelmanage_2')
    local('cd /app/admin/data;rm -rf wx_channelmanage')    
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信渠道公众号/workspace/target/wx_channelmanage /app/admin/data/ &> /app/admin/logs/wx_channelmanage_rsync.log')
    local('cp /app/admin/config/wx_channelmanage/jdbc.properties /app/admin/data/wx_channelmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf wx_channelmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_channelmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_channelmanage admin@10.39.138.12:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/wx_channelmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.138.12 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


def wx_channelmanage():
    '部署所有的wx_channelmanage'
    execute(wx_channelmanage_1)
    execute(wx_channelmanage_2)


@roles('server8')
def postloanmanage_1():
    '部署postloanmanage_1'
    print blue('您正在部署postloanmanage_1')
    local('cd /app/admin/data;rm -rf postloanmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/货后管理/workspace/target/postloanmanage /app/admin/data/ &> /app/admin/logs/postloanmanage_rsync.log')
    local('cp /app/admin/config/postloanmanage/jdbc.properties /app/admin/data/postloanmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf postloanmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz postloanmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/postloanmanage admin@10.39.139.90:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/postloanmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.139.90 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server9')
def postloanmanage_2():
    '部署postloanmanage_2'
    print blue('您正在部署postloanmanage_2')
    local('cd /app/admin/data;rm -rf postloanmanage')    
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/货后管理/workspace/target/postloanmanage /app/admin/data/ &> /app/admin/logs/postloanmanage_rsync.log')
    local('cp /app/admin/config/postloanmanage/jdbc.properties /app/admin/data/postloanmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf postloanmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz postloanmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/postloanmanage admin@10.39.138.12:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/postloanmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.138.12 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


def postloanmanage():
    '部署所有的postloanmanage'
    execute(postloanmanage_1)
    execute(postloanmanage_2)

@roles('server10')
def easytools():
    '部署easytools'
    print blue('您正在部署easytools')
    local('cd /app/admin/3line-data;rm -rf easytools')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/三线业务城市系统/workspace/target/easytools /app/admin/3line-data/ &> /app/admin/logs/easytools_rsync.log')
    local('cp /app/admin/config/easytools/jdbc.properties /app/admin/3line-data/easytools/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf easytools_`date "+%Y%m%d-%H-%M-%S"`.tar.gz easytools &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/3line-data/easytools admin@10.39.149.78:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/easytools_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.149.78 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
	print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server10')
def line3_usermanage():
    '部署3line_usermanage'
    print blue('您正在部署3line_usermanage')
    local('cd /app/admin/3line-data;rm -rf usermanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/三线用户管理系统/workspace/target/usermanage /app/admin/3line-data/ &> /app/admin/logs/3line_usermanage_rsync.log')
    local('cp /app/admin/config/3line-usermanage/jdbc.properties /app/admin/3line-data/usermanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf usermanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz usermanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/3line-data/usermanage admin@10.39.149.78:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/3line_usermanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.149.78 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server11')
def wx_xhmanage_1():
    '部署wx_xhmanage_1'
    print blue('您正在部署wx_xhmanage_1')
    local('cd /app/admin/data;rm -rf wx_xhmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信下户公众号/workspace/target/wx_xhmanage /app/admin/data/ &> /app/admin/logs/wx_xhmanage_rsync.log')
    local('cp /app/admin/config/wx_xhmanage/jdbc.properties /app/admin/data/wx_xhmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf wx_xhmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_xhmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_xhmanage admin@10.39.151.150:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/wx_xhmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.151.150 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server12')
def wx_xhmanage_2():
    '部署wx_xhmanage_2'
    print blue('您正在部署wx_xhmanage_2')
    local('cd /app/admin/data;rm -rf wx_xhmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信下户公众号/workspace/target/wx_xhmanage /app/admin/data/ &> /app/admin/logs/wx_xhmanage_rsync.log')
    local('cp /app/admin/config/wx_xhmanage/jdbc.properties /app/admin/data/wx_xhmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf wx_xhmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_xhmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_xhmanage admin@10.13.150.25:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/wx_xhmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.13.150.25 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


def wx_xhmanage():
    '部署所有的wx_xhmanage'
    execute(wx_xhmanage_1)
    execute(wx_xhmanage_2)


@roles('server11')
def wx_taskmanage_1():
    '部署wx_taskmanage_1'
    print blue('您正在部署wx_taskmanage_1')
    local('cd /app/admin/data;rm -rf wx_taskmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信任务公众号/workspace/target/wx_taskmanage /app/admin/data/ &> /app/admin/logs/wx_taskmanage_rsync.log')
    local('cp /app/admin/config/wx_taskmanage/jdbc.properties /app/admin/data/wx_taskmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf wx_taskmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_taskmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_taskmanage admin@10.39.151.150:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/wx_taskmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.39.151.150 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server12')
def wx_taskmanage_2():
    '部署wx_taskmanage_2'
    print blue('您正在部署wx_taskmanage_2')
    local('cd /app/admin/data;rm -rf wx_taskmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信任务公众号/workspace/target/wx_taskmanage /app/admin/data/ &> /app/admin/logs/wx_taskmanage_rsync.log')
    local('cp /app/admin/config/wx_taskmanage/jdbc.properties /app/admin/data/wx_taskmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf wx_taskmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_taskmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_taskmanage admin@10.13.150.25:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/wx_taskmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.13.150.25 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


def wx_taskmanage():
    '部署所有的wx_taskmanage'
    execute(wx_taskmanage_1)
    execute(wx_taskmanage_2)

@roles('server13')
def reportmanage_1():
    '部署reportmanage_1'
    print blue('您正在部署reportmanage_1')
    local('cd /app/admin/data;rm -rf reportmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/报表管理/workspace/target/reportmanage /app/admin/data/ &> /app/admin/logs/reportmanage_rsync.log')
    local('cp /app/admin/config/reportmanage/jdbc.properties /app/admin/data/reportmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf reportmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz reportmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/reportmanage admin@10.13.151.68:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/reportmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.13.151.68 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')

@roles('server14')
def reportmanage_2():
    '部署reportmanage_2'
    print blue('您正在部署reportmanage_2')
    local('cd /app/admin/data;rm -rf reportmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/报表管理/workspace/target/reportmanage /app/admin/data/ &> /app/admin/logs/reportmanage_rsync.log')
    local('cp /app/admin/config/reportmanage/jdbc.properties /app/admin/data/reportmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf reportmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz reportmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/reportmanage admin@10.138.154.50:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/reportmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.138.154.50 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')

def reportmanage():
    '部署所有的reportmanage'
    execute(reportmanage_1)
    execute(reportmanage_2)

@roles('server13')
def wx_borrower_1():
    '部署wx_borrower_1'
    print blue('您正在部署wx_borrower_1')
    local('cd /app/admin/data;rm -rf wx_borrower')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信借款人公众号/workspace/target/wx_borrower /app/admin/data/ &> /app/admin/logs/wx_borrower_rsync.log')
    local('cp /app/admin/config/wx_borrower/jdbc.properties /app/admin/data/wx_borrower/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf wx_borrower_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_borrower &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_borrower admin@10.13.151.68:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/wx_borrower_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.13.151.68 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')

@roles('server14')
def wx_borrower_2():
    '部署wx_borrower_2'
    print blue('您正在部署wx_borrower_2')
    local('cd /app/admin/data;rm -rf wx_borrower')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/微信借款人公众号/workspace/target/wx_borrower /app/admin/data/ &> /app/admin/logs/wx_borrower_rsync.log')
    local('cp /app/admin/config/wx_borrower/jdbc.properties /app/admin/data/wx_borrower/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf wx_borrower_`date "+%Y%m%d-%H-%M-%S"`.tar.gz wx_borrower &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/wx_borrower admin@10.138.154.50:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/wx_borrower_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.138.154.50 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')

def wx_borrower():
    '部署所有的wx_borrower'
    execute(wx_borrower_1)
    execute(wx_borrower_2)

@roles('server15')
def confluent():
    '部署confluent'
    print blue('您正在部署confluent')
    local('cd /app/admin/data;rm -rf confluent')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/数据仓库/workspace/* /app/admin/data/confluent/ &> /app/admin/logs/confluent_rsync.log')
    local('sed -i "/connection.url.*report/{s#//[^:]\+:#//xxx.xxx.xxx.xxx:#;n;n;s/=.*/BAwXNP#aA/}" /app/admin/data/confluent/kafka-connect-jdbc/*')
    local('sed -i "/connection.url.*channelmanage/{s#//[^:]\+:#//xxx.xxx.xxx.xxx:#;n;n;s/=.*/BAwXNP#aA/}" /app/admin/data/confluent/kafka-connect-jdbc/*')
    local('sed -i "/connection.url.*assetmanage/{s#//[^:]\+:#//xxx.xxx.xxx.xxx:#;n;n;s/=.*/BAwXNP#aA/}" /app/admin/data/confluent/kafka-connect-jdbc/*')
    local('sed -i "/connection.url.*postloanmanage/{s#//[^:]\+:#//xx.xxx.xxx.xxx:#;n;n;s/=.*/BAwXNP#aA/}" /app/admin/data/confluent/kafka-connect-jdbc/*')
    local('sed -i "/connection.url.*openplatform/{s#//[^:]\+:#//xxx.xxx.xxx.xxx:#;n;n;s/=.*/BAwXNP#aA/}" /app/admin/data/confluent/kafka-connect-jdbc/*')
    local('sed -i "s#/app/zhangxin/#/app/admin/#" /app/admin/data/confluent/schema-registry/*')
    #写sed修改配置
    with cd('/app/admin/confluent'):
	run('cp restartAll.sh /app/admin/backup/restartAll.sh_`date "+%Y%m%d-%H-%M-%S"`')
    with cd('/app/admin/confluent/etc'):
        bak_status = run('tar -czf /app/admin/backup/kafka-connect-jdbc_`date "+%Y%m%d-%H-%M-%S"`.tar.gz kafka-connect-jdbc &>/dev/null;tar -czf /app/admin/backup/schema-registry_`date "+%Y%m%d-%H-%M-%S"`.tar.gz schema-registry &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz -e "ssh -p 4399" --exclude="restartAll.sh" /app/admin/data/confluent/* admin@10.39.42.125:/app/admin/confluent/etc/ &> /app/admin/logs/confluent_rsync.log')
	    local('rsync -avz -e "ssh -p 4399" /app/admin/data/confluent/*.sh admin@10.39.42.125:/app/admin/confluent/ &> /app/admin/logs/confluent_rsync.log;chmod +x /app/admin/confluent/*.sh')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启confluent')
    run("source /app/admin/.bash_profile;/app/admin/confluen/restartAll.sh")
    restart_status = run('ps -ef|grep java|grep -v root|grep -v grep|wc -l')
    if int(restart_status) > 15:
        print green('confluent重启完成，请查看日志!')
    else:
        print red('confluent重启失败，请检查日志后手动重启!')

@roles('server13')
def fundingmanage_1():
    '部署fundingmanage_1'
    print blue('您正在部署fundingmanage_1')
    local('cd /app/admin/data;rm -rf fundingmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/资金方管理/workspace/target/fundingmanage /app/admin/data/ &> /app/admin/logs/fundingmanage_rsync.log')
    local('cp /app/admin/config/fundingmanage/jdbc.properties /app/admin/data/fundingmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf fundingmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz fundingmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/fundingmanage admin@10.13.151.68:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/fundingmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.13.151.68 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')


@roles('server14')
def fundingmanage_2():
    '部署fundingmanage_2'
    print blue('您正在部署fundingmanage_2')
    local('cd /app/admin/data;rm -rf fundingmanage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/资金方管理/workspace/target/fundingmanage /app/admin/data/ &> /app/admin/logs/fundingmanage_rsync.log')
    local('cp /app/admin/config/fundingmanage/jdbc.properties /app/admin/data/fundingmanage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8090/webapps'):
        bak_status = run('tar -czf fundingmanage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz fundingmanage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/fundingmanage admin@10.138.154.50:/app/admin/tomcat-8090/webapps/ &> /app/admin/logs/fundingmanage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.138.154.50 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8090/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8090|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
        print red('tomcat重启失败，请检查日志后手动重启!')

def fundingmanage():
    '部署所有的fundingmanage'
    execute(fundingmanage_1)
    execute(fundingmanage_2)


@roles('server10')
def sso():
    '部署sso'
    print blue('您正在部署sso')
    local('cd /app/admin/data;rm -rf sso')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/单点登录/workspace/target/sso.jar /app/admin/data/sso/ &> /app/admin/logs/sso_rsync.log')
    local('cp /app/admin/config/sso/application.properties /app/admin/data/sso/')
    with cd('/app/admin/sso'):
        bak_status = run('tar -czf sso_`date "+%Y%m%d-%H-%M-%S"`.tar.gz sso.jar &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz -e "ssh -p 4399" /app/admin/data/sso/ admin@10.39.149.78:/app/admin/sso/ &> /app/admin/logs/sso_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启sso')
    #run("ps -ef|awk '/java/ && /[t]omcat-8090/{print $2}'|xargs kill -9")
    #sleep(5)
    local('ssh admin@10.39.149.78 -p 4399 "source /app/admin/.bash_profile;/app/admin/sbin/deploy_sso.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [s]so|wc -l')
    if int(restart_status) == 1:
        print green('sso重启完成，请查看日志!')
    else:
        print red('sso重启失败，请检查日志后手动重启!')


@roles('server16')
def TemplateSchemeManage():
    '部署TemplateSchemeManage'
    print blue('您正在部署TemplateSchemeManage')
    local('cd /app/admin/data;rm -rf TemplateSchemeManage')
    local('rsync -avz  -e "ssh -p 4399" admin@103.38.224.58:/app/jenkins/.jenkins/jobs/模板方案/workspace/target/TemplateSchemeManage /app/admin/data/ &> /app/admin/logs/TemplateSchemeManage_rsync.log')
    local('cp /app/admin/config/TemplateSchemeManage/jdbc.properties /app/admin/data/TemplateSchemeManage/WEB-INF/classes/properties/')
    with cd('/app/admin/tomcat-8080/webapps'):
        bak_status = run('tar -czf TemplateSchemeManage_`date "+%Y%m%d-%H-%M-%S"`.tar.gz TemplateSchemeManage &>/dev/null;echo $?')
    if int(bak_status) == 0:
        print green('备份成功!')
        try:
            local('rsync -avz --delete -e "ssh -p 4399" /app/admin/data/TemplateSchemeManage admin@10.139.132.186:/app/admin/tomcat-8080/webapps/ &> /app/admin/logs/TemplateSchemeManage_rsync.log')
            """上面的原目录要改一下"""
            print green('同步成功!')
        except:
            print red('同步失败，请检查!')
            sys.exit()
    else:
        print red('备份不成功，请检查!')
        sys.exit()
    sleep(2)
    print red('准备重启tomcat')
    run("ps -ef|awk '/java/ && /[t]omcat-8080/{print $2}'|xargs kill -9")
    sleep(5)
    local('ssh admin@10.139.132.186 -p 4399 "source /app/admin/.bash_profile;/app/admin/tomcat-8080/bin/startup.sh &> /dev/null"')
    restart_status = run('ps -ef|grep java|grep [t]omcat-8080|wc -l')
    if int(restart_status) == 1:
        print green('tomcat重启完成，请查看日志!')
    else:
	print red('tomcat重启失败，请检查日志后手动重启!')
