from unittest.mock import patch
import send_notification

@patch('send_notification.EmailContextManager')
def test_send_mail(mock_smtp):   
    subject = 'Traffic alert!'
    message = 'Allert message'
    send_notification.send_email(message, subject)
    mock_smtp.assert_called()
    context = mock_smtp.return_value.__enter__.return_value
    context.login.assert_called()
    context.sendmail.assert_called_with('senderemail@gmail.com','reciveremail@gmail.com',b'Subject: Traffic alert!\n\nAllert message')