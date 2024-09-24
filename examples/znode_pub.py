from znode import ZNode
import time

server  = ZNode(node_type="PUB")

while True:
    server.publish("msg/comp", "HELLL NO")
    server.publish("msg/inv", "HELLL YES")
    time.sleep(1)
    print(time.time())