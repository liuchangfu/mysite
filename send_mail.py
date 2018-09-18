# _*_ coding:utf-8 _*_
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    subject, from_email, to = '测试邮件', 'liuchangfu0822@sina.com', '172667104@qq.com'
    text_content = '欢迎你!!'
    html_content = '<h1>欢迎你</h1>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
