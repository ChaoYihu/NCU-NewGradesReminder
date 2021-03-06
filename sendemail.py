import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

host_name = ''
username = ''
token = ''


def emailsend(body, receiver, host=host_name, user=username, email_token=token):
    # 第三方 SMTP 服务
    mail_host = host  # 设置服务器
    mail_user = user  # 用户名(这里填写你的QQ邮箱,确保你的QQ邮箱开启了SMTP服务!)
    mail_pass = email_token  # 口令

    sender = mail_user
    receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("南昌大学分数更新提示系统")
    message['To'] = Header('您' + receivers[0])
    subject = '您有新的成绩更新!'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        server = smtplib.SMTP(mail_host, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        print('[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end='')
        print('正在登录smtp发信服务器...')
        server.login(mail_user, mail_pass)
        text = message.as_string()
        server.sendmail(sender, receivers, text)
        server.close()
        print('[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end='')
        print('邮件发送成功!')
    except:
        if mail_user == "" or mail_pass == '':
            print('[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end='')
            print('邮件发送失败,原因是没有填写第三方SMTP服务器的用户名和口令,请在emailsend.py文件中填写好!')
            print('[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end='')
            print('程序将在10秒钟后自动退出!')
            time.sleep(10)
            exit()
        print('[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end='')
        print('邮件发送失败!(发生了未知的错误)')


def buildtext(username, grades):
    gradestext = ''
    for i in grades.keys():
        gradestext = gradestext + i + "  " + grades[i] + "\n"
    grate = "亲爱的学号为" + username + "的同学:\n\n您的新成绩如下所示:\n"
    textbody = grate + gradestext
    return textbody
