import os
import configparser, argparse
import smtplib, ssl

# Settings file full path definition
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'settings.conf')

# Setup command line args
argparser = argparse.ArgumentParser(description='Quickly send a mail to an SMTP server')
argparser.add_argument('-r','--receiver', type=str, help='Email address to receive this message')
argparser.add_argument('-m','--message', type=str, help='Subject and body to the email message.')

# Read parameters from settings file
parser = configparser.ConfigParser()
parser.read(initfile)

smtp_server = parser.get('default', 'smtp_server')
port = parser.getint('default', 'port', fallback=587)
sender_mail = parser.get('default', 'sender_mail')
user = parser.get('default', 'user')
password = parser.get('default', 'password')

# Read parameters from command line arguments
args = argparser.parse_args()
receiver_mail = args.receiver #"target@example.com"
message = args.message #"Subject: Test Mail \n Sending mail for test purposes. \n Do not reply."

# Simple SMTP is currently disabled
"""
with smtplib.SMTP(smtp_server, port) as sserver:
    print('Login...')
    sserver.login(user, password)
    sserver.sendmail(sender_mail, receiver_mail, message)
    print('Mail sent.')
"""

# Create a secure SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)

try:
    print('Handshaking...')
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() # or ehlo() for ESMTP -- Can be ommited
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(user, password)
    print('Connection secured...')
    server.sendmail(sender_mail, receiver_mail, message)
    print('Mail sent.')
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()