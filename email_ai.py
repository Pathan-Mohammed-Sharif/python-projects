import smtplib
from email.mime.text import MIMEText
from google import genai

# GEMINI API SETUP

API_KEY = "your api key"

client = genai.Client(api_key=API_KEY)

# GMAIL DETAILS

sender_email = "sender's mail"
app_password = "your app password"

# USER INPUT

receiver_email = input("Enter receiver email: ")
subject = input("Enter email subject: ")
prompt = input("Describe the email you want AI to write:\n")

# GENERATE EMAIL USING AI

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Write a professional email based on this request:
{prompt}

Return only the email body.
"""
)

email_body = response.text

# SHOW GENERATED EMAIL

print("\n" + "=" * 50)
print("GENERATED EMAIL")
print("=" * 50)
print(f"\nSubject: {subject}\n")
print(email_body)
print("=" * 50)

# REVIEW BEFORE SENDING

choice = input("\nDo you want to send this email? (yes/no): ").strip().lower()

if choice == "yes":

    message = MIMEText(email_body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, app_password)

        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        print("\n Email sent successfully!")

    except Exception as e:
        print("\n Error:", e)

    finally:
        try:
            server.quit()
        except:
            pass

else:
    print("\n Email sending cancelled.")
