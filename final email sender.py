import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Attaching CV to the file and encoding it so it is properly sent
def attach_file_to_email(message, file_path):
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(file_path, "rb").read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={file_path.split('\\')[-1]}")
    message.attach(part)

sender_email = "hello@gmail.com" #Your Email Adress
sender_password = "123456789qwerty" #Your Temporary Password

server = smtplib.SMTP("smtp.gmail.com", 25,timeout=120)
server.starttls()

server.login(sender_email, sender_password)

#Extracting the Names and Email from CSV file
file = open("Email list.csv", 'r')
lines = file.readlines()

header = lines[0].strip().split(',')
updated_lines = [lines[0]]

for line in lines[1:]:
    row = line.strip().split(',') 
    if row[3] == 'FALSE':
        name = row[0]
        prof_email = row[1]
        pers_email = row[2]
        #Your Cold Email
        text = f"""Hello Professor {name}  

My name is Muhammad Ibrahim Goreja and I am currently enrolled ---------a researcher

To provide some background on my qualifications,---------- I have also attached my CV to this file.

I have always been extremely interested in this --------thing

Eagerly looking forward to your reply and working with you.
Regards,
Muhammad Ibrahim Goreja""" 
        
        message = MIMEMultipart()
        message["From"] = sender_email
        filename = "C:\\Users\\DELL\\Documents\\Me\\Muhammad Ibrahim Goreja - CV.pdf"
        attach_file_to_email(message, filename)

        #Sending email to Professsional email if that is not available then Personal or to both
        if pers_email == "":
            message["To"] = prof_email
            message["Subject"] = "Research Opportunity"
            message.attach(MIMEText(text, "plain"))
            server.sendmail(sender_email, prof_email, message.as_string())
        elif prof_email == "":
            message["To"] = pers_email
            message["Subject"] = "Research Opportunity"
            message.attach(MIMEText(text, "plain"))
            server.sendmail(sender_email, pers_email, message.as_string())
        else:
             message["To"] = prof_email+ ","+pers_email
             message["Subject"] = "Research Opportunity"
             message.attach(MIMEText(text, "plain"))
             server.sendmail(sender_email, message["To"].split(","), message.as_string())
        row[3] = 'TRUE'
    updated_lines.append(','.join(row) + '\n')
            
server.quit()

#Editing the CSV about those who have been sent a mail to
file = open("Email list.csv", 'w')
file.writelines(updated_lines)
        