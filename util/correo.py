from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from datetime import datetime
from email.utils import formatdate
import smtplib

class Correo:

    current_date = datetime.today().strftime('%Y-%m-%d')

    def send_mail(self,script):

        server = smtplib.SMTP(host='correo.mct.com.co',port=25)
        msg = MIMEMultipart()
        password = "temporal_2015"
        msg['From'] = "notificaciones@mct.com.co"
        msg['To'] = "david.restrepo@mct.com.co"
        msg['Cc'] = ""
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = "PRUEBA - SANTIAGO "
      
				
        mail_body = self.set_mail_body(script)
        server.starttls()
        server.login(msg['From'], password)
        msg.attach(mail_body)
        server.sendmail(msg['From'], "david.restrepo@mct.com.co", msg.as_string())
        server.quit()



    def set_mail_body(sef,script):
        body_html = f"""\
					<!DOCTYPE html>
						<html>
							<head>
									<title>TODO supply a title</title>
									<meta charset="UTF-8">
									<meta name="viewport" content="width=device-width, initial-scale=1.0">
									<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.js"></script>
							</head>
							<body>
									<h1>SANTIAGO RESTREPO</h1>
									<canvas id="myChart" width="400" height="400"></canvas>
							</body>
							<script>
								{script}
							</script>
						</html>
          """
        part = MIMEText(body_html, 'html')
        return part
