from flask import Flask
from flask import request as data
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


load_dotenv()
app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)
sender_email = os.environ.get("sender")
password = os.environ.get("password")


@app.route("/hook/", methods=["POST"])
@limiter.limit("1 per day")
def main():
    msg = data.form.get("message")

    receiver_email = data.form.get("sender")
    recep = os.environ.get("recep")
    message = MIMEMultipart("alternative")
    message["Subject"] = "dev email "
    message["From"] = sender_email
    message["To"] = recep
    html = """\
<html>
  <head>
    <style>
      html body{{
        margin: 0;
        padding: 0;
        background-color: rgb(69,69,69);
        color: white;
        font-family: Comic Sans MS;
        
        
      }}
      .st{{
        background-color: rgb(117, 66, 245);
        text-align: center;
        border-radius: 2px;
        width: 500px;
        align-items: center;
        
      }}
      .ft{{
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: large;
      }}
    </style>
  </head>
  <body>
    <h1 class="st">You got mail from {sender}</h1>
    <div class="ft">
      {msg}
    </div>
    
  </body>
</html>
"""
    e_ms = msg
    s_m = receiver_email
    html = html.format(sender=s_m, msg=e_ms)
    part = MIMEText(html, "html")
    message.attach(part)
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recep, message.as_string())

    return "email sent"


if __name__ == "__main__":
    app.run(port=5000)
