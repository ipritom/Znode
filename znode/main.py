import zmq
import time
import datetime

class Node:
    def __init__(self, 
                 host:str="127.0.0.1", 
                 port:int=5353, 
                 node_type:str="PUB",
                 default_topic:str=None,
                 blocking=False,
                 verbose=False) -> None:
        
        self.host = host 
        self.port = port
        self.defaul_topic = default_topic
        self.connection_point = f"tcp://{self.host}:{self.port}"
        self.blocking = blocking
        self.verbose = verbose
        # node configuration here
        self.context = zmq.Context()
        self.node_type = node_type.upper()
        
        if node_type=="PUB":
            self.socket = self.context.socket(zmq.PUB)
            self.__bind()
        elif node_type=="SUB":
            self.socket = self.context.socket(zmq.SUB)
            self.__connect()
            
            if self.defaul_topic is not None: 
                self.subscribe(self.defaul_topic)
        else:
            raise ValueError("node_type can be PUB or SUB")
        

    def __connect(self):
        """Connects to a 0MQ socket as a subscriber"""
        self.socket.connect(self.connection_point)

    def __bind(self):
        """Connects to a 0MQ socket as a publisher"""
        self.socket.bind(self.connection_point)
        
    def __debug(self, e):
        if self.verbose:
            print(f"{datetime.datetime.now()} | {e}")
            
    def publish(self, topic:str=None, msg:str=""):
        # need to check the type
        if topic is None:
            topic = self.defaul_topic
        
        if isinstance(msg, bytes):
            self.socket.send_multipart([topic.encode("utf-8"), msg])
        else:
            self.socket.send_multipart([topic.encode("utf-8"), msg.encode("utf-8")])

    def receive(self):
        packet = [None, None]

        # handling blocking rx
        if self.blocking:
            packet = self.socket.recv_multipart()
            return packet, True
        # handling non-blocking rx
        else:
            try:
                packet = self.socket.recv_multipart(flags=zmq.NOBLOCK)
                return packet, True
            except Exception as e:
                self.__debug(e)
                return packet, False
    

    def get_stream(self):
        """Get a stream of messages from the socket.
            This method will empty the socket and return all messages
            received until the socket is empty.
        """
        if self.node_type != "SUB":
            raise Warning("get_stream is only available for SUB nodes")
        
        if self.blocking:
            raise AttributeError("get_stream is not available for blocking SUB nodes")
        
        stream = []
        while True:
            packet, success = self.receive()
            if not success:
                break
            stream.append(packet)

        return stream
    
    def subscribe(self, topic:str=None):
        if topic is None:
            topic = self.defaul_topic
        self.socket.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))