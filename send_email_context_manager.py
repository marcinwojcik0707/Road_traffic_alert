import smtplib
import ssl

class EmailContextManager():
    def __init__(self, smtp_server, port, ssl_enable, credentials):
        self.smtp_server = smtp_server
        self.port = port
        self.ssl_enable = ssl_enable
        self.my_server = None
        self.credentials = credentials
    def __enter__(self):
        if not self.ssl_enable:
            self.my_server = smtplib.SMTP(self.smtp_server, self.port)
        else:
            context = ssl.create_default_context()
            self.my_server = smtplib.SMTP_SSL(self.smtp_server, self.port, context=context)
        return self
    def login(self, username, password):
        self.my_server.login(username, password)
    def sendmail(self, sender, reciver, message):
        self.my_server.sendmail(sender, reciver, message)
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.my_server.close()