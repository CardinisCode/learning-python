
import smtplib
import socket
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


MY_ADDRESS = "youremail@gmail.com"
PASSWORD = "Enter your password here"

# set up the SMTP server
server = smtplib.SMTP(host= "smtp.gmail.com", port=587)
server.starttls()
server.login(MY_ADDRESS, PASSWORD)
print("Successfully logged in!")

names, emails = get_contacts('contacts.txt')  # read contacts
print("names:", names, "emails:", emails)
message_template = read_template('message.txt')

# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    server.send_message(msg)
    
    del msg














