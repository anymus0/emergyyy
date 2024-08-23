from ImapClient import getMails
import os
import time

# Load environment variables
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_USERNAME = os.getenv('IMAP_USERNAME')
IMAP_PASSWORD = os.getenv('IMAP_PASSWORD')
IMAP_MAILBOX = os.getenv('IMAP_MAILBOX')


mails = getMails(IMAP_HOST, IMAP_USERNAME, IMAP_PASSWORD, IMAP_MAILBOX, 'ALL')
print(mails)