import smtplib, ssl

class Mailer:

    def __init__(self):
        self.EMAIL = "socialdistancingmonitorproject@gmail.com" #This email will be used to send alert mail, so this hould be logged in your laptop
        self.PASS = "hyrv jagv ulgt tsoq"  # Here change this to your app password from your gamil's app password
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        SUBJECT = 'ALERT!'
        TEXT = f'Social Distancing Violations Exceeded! Need Urgent Supervision'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()