from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor, protocol

class ChatProtocol(LineReceiver, protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state = "REGISTER"
    
    def connectionMade(self):
        self.sendLine("What's your name?")
    
    def connectionLost(self, reason):
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage("{} has left the channel. There are {} users online now!".format(self.name, self.count_users()))
    
    def lineReceived(self, line):
        if self.state == "REGISTER":
            self.handle_REGISTER(line)
        else:
            self.handle_CHAT(line)
            
    def handle_REGISTER(self, name):
        if name in self.factory.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.name = name
        self.factory.users[name] = self
        self.state = "CHAT"
        self.sendLine("Welcome, {}, There are {} users online now!".format(name, self.count_users()))
        self.broadcastMessage("{} has joined the channel. There are {} users online now!".format(name, self.count_users()))
    def handle_CHAT(self, message):
        message = "<{}> {}".format(self.name, message)
        self.broadcastMessage(message)
        
    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)
    
    def count_users(self):
        return len(list(self.factory.users.keys()))


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}
    def buildProtocol(self, addr):
        return ChatProtocol(self)
reactor.listenTCP(7777, ChatFactory())
reactor.run()
