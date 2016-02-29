from smtplib import SMTP_SSL as SMTP
import logging
import logging.handlers
import sys
from email.mime.text import MIMEText


def send_confirmation():
    text= """This is a small python module to send mail. This text will be the body of the message.""" 
    msg = MIMEText(text, 'plain')
    msg['Subject'] = "The Subject" 
    me ='from@gmail.com'
    msg['To'] = 'to@domain.com'
    try:
        conn = SMTP('smtp.gmail.com')
        conn.set_debuglevel(True)
        conn.login('login (no @domain.com)', 'password')
        try:
            conn.sendmail(me, me, msg.as_string())
        finally:
            conn.close()
#?
    except Exception as exc:
        logger.error("ERROR!!!")
        logger.critical(exc)
        sys.exit("Mail failed: {}".format(exc))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    random_condition = True

    if random_condition:
        send_confirmation()
