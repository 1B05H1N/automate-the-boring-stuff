import imapclient
conn = imapclient.IMAPClient('imap.email.com', ssl = True)
conn.login('email@email.com', 'password')
conn.select_folder('INBOX', readonly = True)

UIDs = conn.search(['SINCE 20-AUG-2015'])
UIDs

conn.fetch([47474], ['BODY[]','FLAGS'])#UID I want
import pyzmail
pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
message.get_address('from')
message.get_address('to')
message.get_address('bcc')
message.html_part
message.html_part == None

message.text_part.get_payload().decode('UTF-8')
message.text_part.charset == None

conn.list_folders()

conn.select_folder('INBOX', readonly=False)

UIDs = conn.search(['ON 24-AUG-2015'])
UIDs
conn.logout()