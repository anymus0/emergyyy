import email
from imaplib import IMAP4 as imap

def getMails(host: str, username: str, password: str, mailboxName: str, imapFilters: str):
    # create empty email list (this will be returned)
    mails = []
    # create IMAP4 connection
    with imap(host=host) as imapConn:
        # login to the account
        imapConn.login(username, password)
        imapConn.select(mailboxName)
        # set filters
        status, data = imapConn.search(None, imapFilters)
        
        if status == 'OK':
            emailIDs = data[0].split()
            
            for emailID in emailIDs:
              status, data = imapConn.uid('fetch', emailID,'(RFC822)')
              
              if status == 'OK':
                # get raw message
                msg = email.message_from_bytes(data[0][1])
                # If the message is not multipart, get the payload directly
                body = msg.get_payload(decode=True)
                # Decode the body if it's encoded
                body = body.decode(msg.get_content_charset() or 'utf-8')
                # construct and push object to mails
                mail = {
                  'date': msg['Date'],
                  'to': msg['To'],
                  'fromSender': msg['From'],
                  'subject': msg['Subject'],
                  'body': body
                }
                mails.append(mail)

    return mails
