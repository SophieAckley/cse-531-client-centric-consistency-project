from concurrent import futures

import grpc
from termcolor import colored

import branch_pb2_grpc
from branch_pb2 import MsgRequest, MsgResponse


class Branch(branch_pb2_grpc.BranchServicer):
    def __init__(self, id, balance, branches):
        self.id = id
        self.balance = balance
        self.branches = branches
        self.stubList = list()
        self.writeset = list()

    # Setup gRPC channel & client stub for each branch
    def createStubs(self):
        for branchId in self.branches:
            if branchId != self.id:
                port = str(50000 + branchId)
                channel = grpc.insecure_channel("localhost:" + port)
                self.stubList.append(branch_pb2_grpc.BranchStub(channel))

    # Incoming MsgRequest from Customer transaction
    def MsgDelivery(self, request, context):
        return self.ProcessMsg(request, False)

    # Incoming MsgRequest from Branch propagation
    def MsgPropagation(self, request, context):
        return self.ProcessMsg(request, True)

    # Handle received Msg, generate and return a MsgResponse
    def ProcessMsg(self, request, isPropagation):
        if request.interface == "query":
            pass
        elif request.interface == "deposit":
            self.balance += request.money
        elif request.interface == "withdraw":
            if self.balance >= request.money:
                self.balance -= request.money

        if not isPropagation and request.interface != "query":
            self.Propagate_Transaction(request)

        return MsgResponse(interface=request.interface, money=self.balance, writeset=self.writeset)

    # Propagate Customer transactions to other Branches
    def Propagate_Transaction(self, request):
        for stub in self.stubList:
            stub.MsgPropagation(MsgRequest(interface=request.interface, money=request.money, writeset=request.writeset))
