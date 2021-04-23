from time import sleep

import grpc
from termcolor import colored

import branch_pb2_grpc
from branch_pb2 import MsgRequest


class Customer:
    def __init__(self, id, events):
        self.id = id
        self.events = events
        self.recvMsg = list()
        self.writeset = list()

    # Send gRPC request for each event
    def executeEvents(self):
        for event in self.events:
            # Sleep 3 seconds for 'query' events
            if event["interface"] == "query":
                sleep(3)

            # Setup gRPC channel & client stub for branch
            port = str(50000 + event["dest"])
            channel = grpc.insecure_channel("localhost:" + port)
            stub = branch_pb2_grpc.BranchStub(channel)

            print(
                colored(
                    "Customer #" + str(self.id) + "\tto Branch #" + str(event["dest"]) + "\t" + str(event), "magenta"
                )
            )

            # Set MsgRequest.money = 0 for query events
            money = event["money"] if event["interface"] != "query" else 0

            # Send request to Branch server
            response = stub.MsgDelivery(MsgRequest(interface=event["interface"], money=money, writeset=self.writeset))

            # Append to self.recvMsg list
            self.recvMsg.append({"interface": response.interface, "dest": event["dest"]})

    # Generate output msg
    def output(self):
        return {"id": self.id, "recv": self.recvMsg}
