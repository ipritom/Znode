from znode import Node
import time

# create a publisher node
publisher  = Node(node_type="PUB")

while True:
    publisher.publish(topic="msg/mango", msg=f"{str(time.time())[-1]}")
    publisher.publish(topic="msg/apple", msg=f"")
  