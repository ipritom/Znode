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
    
    
    def subscribe(self, topic:str=None):
        if topic is None:
            topic = self.defaul_topic
        self.socket.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))