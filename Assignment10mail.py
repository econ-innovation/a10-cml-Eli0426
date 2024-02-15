# -*- coding: utf-8 -*-

"""
@Name: Assignment10
@Auth: 丛正龙
@Date: 2024/2/15
@Wechat: Czl15842762738
@Phone: 15842762738
@Email: congzhenglong02@163.com
"""
#!/bin/bash

# 设置收件邮箱
recipient="public@example.com"

# 设置邮件主题
subject="Assignment10congzl"

# 设置邮件正文
body="This is my Assignment10, wish you all the best.\nBest regards,\n丛正龙"

# 请求头
email_content="Subject: $subject\nFrom: congzhenglong02@163.com\nTo: $recipient\n\n$body"

# 发送邮件
echo -e "$email_content" | msmtp "$recipient"

