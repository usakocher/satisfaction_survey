import smtplib
from email.mime.text import MIMEText

def send_mail(colleague, role, helpful, commitment, skills, overall, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '52785bdaa85638'
    password = 'ed21a43b76d752'
    message = f"<h3>New Feedback Submission</h3><ul><li>Colleague: {colleague}</li><li>Role: {role}</li><li>Helpful: {helpful}</li><li>Skills: {skills}</li><li>Commitment: {commitment}</li><li>Overall: {overall}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Satisfaction Survey'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())