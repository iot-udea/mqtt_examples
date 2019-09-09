import paho.mqtt.client as paho


class Thing:
    def __init__(self, ID = None, base_topic = None, topics = [], commands = {}):
        self.ID = ID
        self.base_topic = base_topic
        self.topics = topics
        self.commands = commands

    def setID(self,ID):
        self.ID = ID

    def getID(self,ID):
        return self.ID

    def setBaseTopic(self,bTopic):
        self.base_topic = bTopic

    def returnBaseTopic(self):
        return self.base_topic
    
    def addTopic(self, topic):
        self.topics.append(self.base_topic + "/" + topic + "/")

    def getTopics(self):
        return self.topics

    def addCommand(self, topic, command):
        if self.commands.get(topic) == None:
            self.commands[topic] = []
        self.commands[topic].append(command)

    def printInfo(self):
        print("En construccion")
        print(self.base_topic)
        print(self.topics)
        print(self.commands)

class Light(Thing):
    def __init__(self, ID, initialState = "OFF"):
        Thing.__init__(self, ID = ID)
        self.state = initialState

    def lightOn(self,topic):
        return self.commands[topic]

def test():
    print("Hola mundo")
    t1 = Thing(base_topic = "Home")
    t1.addTopic("alcoba")
    t1.addTopic("comedor")
    t1.addCommand("mundo/alcoba/","commando1")
    t1.addCommand("mundo/alcoba/","commando2")
    t1.printInfo()


test()

"""
Client(client_id="", 
     clean_session=True, 
     userdata=None, 
     protocol=MQTTv311, 
     transport="tcp")


connect(host, 
     port=1883, 
     keepalive=60, 
     bind_address="")


subscribe(topic, qos=0)
"""