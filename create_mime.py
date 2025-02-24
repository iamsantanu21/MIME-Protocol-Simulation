from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Create the MIME message
msg = MIMEMultipart()
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Test MIME Message'

# Add body to the email
body = "This is a test email with an attachment."
msg.attach(MIMEText(body, 'plain'))

# Add attachment
filename = "example.txt"
with open(filename, "w") as f:
    f.write("This is an example attachment.")  # Create a sample file
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')
    msg.attach(part)

# Convert the message to a string
text = msg.as_string()

# Print the MIME message
print(text)