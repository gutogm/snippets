import smtplib

def send(_user, _pwd, _from, _to, _subject, _text, _address, _port):
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (_from, ", ".join(_to), _subject, _text)
    server = smtplib.SMTP(_address, _port)
    server.ehlo()
    server.starttls()
    server.login(_user, _pwd)
    server.sendmail(_from, _to, message)
    server.close()
