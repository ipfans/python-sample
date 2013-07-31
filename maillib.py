#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

# 邮件帐户用户名&密码
usernm = "jet@google-inc.com"
passwd = "Ufuck0ff!!"

# 邮件服务器地址和端口
server_host = "smtp.google-inc.com"
server_port = "465"


def send_mail(to_list, Subject, content):
    msg = MIMEText(content, _subtype='html', _charset='UTF-8')
    msg['Subject'] = Subject
    msg['From'] = usernm
    msg['To'] = to_list
    smtp = smtplib.SMTP_SSL()
    smtp.connect(server_host, server_port)
    smtp.login(usernm, passwd)
    smtp.sendmail(usernm, to_list, msg.as_string())
    smtp.quit()


def main():
    content = "<a href='http://www.baidu.com'>百度首页</a>"
    msg = MIMEText(content, _subtype='html', _charset='UTF-8')
    msg['Subject'] = "this is a email from python demo"
    msg['From'] = usernm
    msg['To'] = usernm
    smtp = smtplib.SMTP_SSL()
    smtp.connect(server_host, server_port)
    smtp.login(usernm, passwd)
    smtp.sendmail(usernm, usernm, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    main()
