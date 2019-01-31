#!/usr/bin/python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import sys

def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(to_list,subject,content):
    mail_host = 'smtp.exmail.qq.com'
    mail_user = 'xxx@xxx.com'
    mail_pass = 'password'
    #以上内容根据你的实际情况进行修改
    msg = MIMEText(content,'','utf-8')
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg['From'] = formatAddr('zabbix监控 <%s>' % mail_user).encode()
    msg['to'] = to_list

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(mail_user,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
