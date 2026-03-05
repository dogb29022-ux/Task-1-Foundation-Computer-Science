import socket
import base64
import os
import time

# SMTP configuration
SMTP_SERVER = "localhost"
SMTP_PORT = 1025

sender = "sujanbyanju0@gmail.com"
receiver = "dogb29022@gmail.com"
Data = "iVBORw0KGgoAAAANSUhEUgAABLcAAAL"
message = "This email demonstrates Base64 encoding with attachments."

# File to attach
file_path = "Diagrams/base64_one.png"   # change to your file (image/pdf/txt/etc)

# Generate MIME boundary
boundary = "----BOUNDARY123456789"

# Encode text message
encoded_message = base64.b64encode(message.encode()).decode()

# Read and encode attachment
filename = os.path.basename(file_path)

with open(file_path, "rb") as f:
    file_data = f.read()

encoded_file = base64.b64encode(file_data).decode()

# Create MIME message
mime_message = f"""Data: {Data}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

--{boundary}
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: base64

{encoded_message}

--{boundary}
Content-Type: application/octet-stream; name="{filename}"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="{filename}"

{encoded_file}

--{boundary}--
"""

smtp_commands = f"""EHLO localhost
MAIL FROM:<{sender}>
RCPT TO:<{receiver}>
DATA
{mime_message}
.
QUIT
"""

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SMTP_SERVER, SMTP_PORT))

    print(client.recv(1024).decode())

    for line in smtp_commands.split("\n"):
        client.send((line + "\r\n").encode())
        time.sleep(0.3)

        try:
            response = client.recv(1024).decode()
            print(response)
        except:
            pass

    client.close()
    print("\nEmail with attachment sent successfully.")

except Exception as e:
    print("Error:", e)