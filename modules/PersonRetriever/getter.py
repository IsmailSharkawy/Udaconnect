
import grpc
import person_pb2
import person_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = person_pb2_grpc.PersonRequestStub(channel)

response = stub.Retrieve(person_pb2.Empty())
for person in list(response):
    print(person.id)

