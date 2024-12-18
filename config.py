import password
################################################################################
# SMTP configuration settings.
################################################################################
smtp = {
    'username': '82124a001@smtp-brevo.com',
    'password': password.smtp_password,
    'host': 'smtp-relay.brevo.com',
    'port': 587,
    'from_email': 'vsparikh1996@gmail.com',
}

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################

mail_address = "1002-1335 Howe street, Vancouver, BC, V6Z1R7"

email_template = {
    'from_name': 'Secret Santa',
    'from_email': smtp['from_email'],
    'subject': 'Family Christmas',
    'body': """
Ho Ho Ho!
        {santa}, It's time to spread some holiday cheer! You’ve been chosen to be {recipient}'s Secret Santa. 
        Please remember to keep it a surprise and stick to the budget of 30 CAD.
        Send it to {mail_address} in packag to be opened with you or bring it along with you
Happy gifting and Merry Christmas! 🎄🎁
"""
}

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = {
    'Viken': 'vsparikh1996@gmail.com',
    'Viken2': 'vsparikh1996@gmail.com',
}

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    # Do not allow James to be santa for Mary
    # 'James': ('Mary',),
}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
secret_santa_record_file = 'secret-santa-record-file.txt'
