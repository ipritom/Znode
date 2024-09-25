from znode import ZNode
import time

# create a publisher node
publisher  = ZNode(node_type="PUB")

while True:
    publisher.publish(topic="msg/mango", msg=f"{str(time.time())[-1]}")
    publisher.publish(topic="msg/apple", msg=f"")
    # time.sleep(1)
  