from twilio.rest import Client

"""recovery code : GWQ5LQPZMY243DELE17QVM31"""
account_sid = 'AC07b799d2256341d06db6847da07add3b'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12513133128',
  body='Hi, we are testing',
  to='+918360238249'
)

print(message.sid)
