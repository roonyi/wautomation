from twilio.rest import Client

account_sid = 'AC6156524fb3848c6d808143475c74ff64'
auth_token = '4bc1ec16743cfd126ad1a8ff739e4a90'
client = Client(account_sid, auth_token)
def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+51920893272'
    )

    print(message.sid)