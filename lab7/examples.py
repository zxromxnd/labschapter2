from event_emitter import EventEmitter


print("Example 1: Multiple independent listeners\n")

events = EventEmitter()

def logger(message):
    print(f"Logger: {message}")

def notifier(message):
    print(f"Notifier: {message}")

def analyzer(message):
    print(f"Analyzer: {message}")

events.on('message', logger)
events.on('message', notifier)
events.on('message', analyzer)

events.emit('message', 'Hello World')
print()


print("Example 2: Chat system with user entities\n")

class User:
    def __init__(self, name, chat_emitter):
        self.name = name
        self.chat = chat_emitter
        self.chat.on('message', self.on_message)
    
    def on_message(self, sender, text):
        if sender != self.name:
            print(f"{self.name} received: '{text}' from {sender}")
    
    def send_message(self, text):
        print(f"{self.name} sends: '{text}'")
        self.chat.emit('message', self.name, text)


chat = EventEmitter()

alice = User('Alice', chat)
bob = User('Bob', chat)
charlie = User('Charlie', chat)

alice.send_message('Hi everyone!')
bob.send_message('Hello Alice!')
charlie.send_message('Hey there!')