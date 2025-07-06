from Znode import Node
import time
# create a client node and connects to a publisher server
client  = Node(node_type="SUB", verbose=True)

# subscribe to a topic or subtopic
client.subscribe("msg/mango")

# receive message from the subscribed topics
while True:
    packet, success =  client.receive()
    topic, msg = packet
    if success:
        print(f"topic: {topic} | message : {msg}", success)
    
