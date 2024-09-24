from znode import ZNode


client  = ZNode(node_type="SUB")
client.subscribe("msg/inv")
# client.subscribe("inv")

while True:
    topic, msg =  client.receive("msg")
    print(msg)
