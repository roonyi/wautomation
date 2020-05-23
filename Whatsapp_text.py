from twilio.rest import Client

account_sid = 'AC6156524fb3848c6d808143475c74ff64'
auth_token = 'e10eab24722d17b7fa1f144ea1e4fb4f'
client = Client(account_sid, auth_token)
def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hola Anita!!! Llena por favor esta encuesta.. gracias',
        to='whatsapp:+51920893272'
    )

    print(message.sid)