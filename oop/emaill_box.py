class Email:
    def __init__(self,sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    command = input()
    if command == 'Stop':
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)

sent_emails = [emails[int(index)].send() for index in input().split(', ')]

for current_mail in emails:
    print(current_mail.get_info())

