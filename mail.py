import smtplib

to = 'bentolima100@gmail.com'
gmail_user = 'secretaria@bento.cv'
gmail_pwd = 'bento123.'
smtpserver = smtplib.SMTP("mail.bento.cv",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()
