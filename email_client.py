import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(target, body, subject):

    msg = MIMEMultipart()
    msg['From'] = "doe993860@gmail.com"
    msg['To'] = target
    msg['Subject'] = subject

    # body = "Python test"
    msg.attach(MIMEText(body, 'plain'))

    pwd = read_file('/Users/Chris/PycharmProjects/read_from.txt')

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('doe993860@gmail.com', pwd)

    text = msg.as_string()
    # msg = "\nHello World 2!"
    server.sendmail('doe993860@gmail.com', target, text)


def read_file(fname):

    try:
       f = open(fname, 'r')
    except IOError:
        print("Could not read file: ", fname)
        sys.exit()
    with f:
        password = f.readline()
        # print(password)
    return password


if __name__ == "__main__":
    read_file()
