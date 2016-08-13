def send_email(mail_context):
	from email.mime.text import MIMEText
	msg=MIMEText(mail_context,'plain','utf-8')
	from_addr="rmqlife@163.com"
	to_addr="rmqlife@gmail.com"

	import smtplib
	server = smtplib.SMTP("smtp.163.com",25)
	server.set_debuglevel(1)
	server.login(from_addr,"911911")
	server.sendmail(from_addr,[to_addr],msg.as_string())
	server.quit()

if __name__ == '__main__':
	send_email('hello,send by Python...')
	
