import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
#assword = input("Type your password and press enter: ")

sender_email = "Yes@no.maybe"
receiver_email = "dirkblacklord@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
text = """\
  Hi,
  How are you?
  You Gay Lol"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="https://www.youtube.com/watch?v=sM7J-CnM5T4&ab_channel=Enchandted">You Gay Lol</a> 
    </p>
  </body>
</html>
"""
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("TimesPopRoman@gmail.com", "u4TSC7oh5#R%")

    server.sendmail(sender_email, receiver_email, message.as_string())