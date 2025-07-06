# Znode 
Znode, or Zero Node, is a messaging module built on the ØMQ framework. It facilitates communication between scripts within your programs. Very lightweight and lightning fast Pub/Sub tools.

# How to Install
You can install the module with pip in the following way. 
```
pip install git+https://github.com/ipritom/Znode 
```
# How to Use
Import Znode module
```py
from Znode import Node
```
## Create a Publisher Node

```py
publisher  = Node(node_type="PUB")
```
Now you can send message with a topic name with following code.
```py
publisher.publish(topic="abc", msg="your msg here!")
```
You can create a loop to publish continuous messages. 

## Create a Subscriber Node
In following way you can create a subscriber node and subscribe to a topic.

```py
# create a client node and connects to a publisher server
client  = Node(node_type="SUB", verbose=True)

# subscribe to a topic or subtopic
client.subscribe("abc")
```
Following example show how to receive message publised by the publisher.

```py
packet, success =  client.receive()
```
`packet` contains a list of topic and a message. You can unpack it in following way. 

```
topic, msg = packet
```

You can also subscribe to the multiple topic. 

Check ***example*** directory. 

## Subscription Mode
There are two subscription mode. 
* Blocking
* Non-blocking (default)

To activate the blocking mode just set `blocking=True`
```py
client  = Node(node_type="SUB", verbose=True, blocking=True)
```
In this mode, client will halt while receiving untill receive a message. 

If you keep, `verbose=True` while creating a `Node` you will see the following message if the client node does not receive any message.
```
Resource temporarily unavailable
```
