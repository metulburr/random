import smtplib

class Email():
    def __init__(self, **d):
        self.server = d['server']
        self.port = d['port']
        self.sender = d['send']
        self.password = d['pass']
        self.receiver = d['recv']
        self.subject = d['subject']
        self.body = d['body']
      
    def format_it(self):
        self.body = "" + self.body + ""
        self.headers = [
            "From: " + self.sender,
            "Subject: " + self.subject,
            "To: " + self.receiver,
            "MIME-Version: 1.0",
            "Content-Type: text/html"
        ]
        self.headers = "\r\n".join(self.headers)

    def send(self):
        self.session = smtplib.SMTP(self.server, self.port)
        self.format_it()
        self.session.starttls()
        self.session.login(self.sender, self.password)
        self.session.sendmail(self.sender, self.receiver, self.headers + "\r\n\r\n" + self.body)
        self.session.quit()

if __name__ == '__main__':
    config = {
        'server' :'smtp.gmail.com',
        'port'   :587,
        'send'   :'SENDER@gmail.com',
        'pass'   :'SENDERS_PASSWORD',
        'recv'   :'RECIEVER@gmail.com',
        'subject':'This is the subject',
        'body'   :'This is the body of the message'
    }
    email = Email(**config)
    email.send()
    print('Mail Sent Successfully')
