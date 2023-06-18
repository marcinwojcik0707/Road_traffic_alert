import smtplib
import ssl

class EmailContextManager():
    """Context manager for email sending
    """    
    def __init__(self, smtp_server, port, ssl_enable, credentials):
        """Create object attributes for server connection.

        Args:
            smtp_server (str): addres of smtp server
            port (str): server port 
            ssl_enable (str): If ssl required. "True" or "False"
            credentials (str): Credentials of email account
        """        
        self.smtp_server = smtp_server
        self.port = port
        self.ssl_enable = ssl_enable
        self.my_server = None
        self.credentials = credentials
    def __enter__(self):
        """Method to enter the context manager and create server connection

        """        
        if not self.ssl_enable:
            self.my_server = smtplib.SMTP(self.smtp_server, self.port)
        else:
            context = ssl.create_default_context()
            self.my_server = smtplib.SMTP_SSL(self.smtp_server, self.port, context=context)
        return self
    def login(self, username, password):
        """login to user account

        Args:
            username (str): username to email
            password (str): password or email code to login into account
        """        
        self.my_server.login(username, password)
    def sendmail(self, sender, reciver, message):
        """Send email to selected reciver

        Args:
            sender (str): sender email address
            reciver (str): reciver email address
            message (str): content to send
        """        
        self.my_server.sendmail(sender, reciver, message)
    def __exit__(self, exc_type, exc_value, exc_trace):
        """Close server connection when exiting context manager
        """     
        self.my_server.close()