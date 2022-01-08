from twilio.rest import Client

client = Client("sid", "token")


for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

#msg = client.messages.create(
#    to="+18328684797",
#    from_="+18057930079",
#    body="hello from python",
#)

#print(f"Created a new message: {msg.sid}")
