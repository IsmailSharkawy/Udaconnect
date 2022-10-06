
import time
from concurrent import futures

import grpc
import person_pb2
import person_pb2_grpc
import requests
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api")

class PersonServicer(person_pb2_grpc.PersonRequestServicer):
    def Retrieve(self, request, context):
        rest_people = requests.get('http://10.43.80.52:5000/' + "api/persons").json()
        logging.info('len of people',len(rest_people))
        for person in rest_people:
            response = person_pb2.Person(
                id=person['id'],
                first_name=person['first_name'],
                last_name=person['last_name'],
                company_name=person['company_name'],
            )
            yield response
def run():
    logger.info(f"running")
    print('running')
    # people_list = []
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    person_pb2_grpc.add_PersonRequestServicer_to_server(PersonServicer(), server)


    server.add_insecure_port("[::]:30005")
    server.start()
    logger.info("Server starting on port 30005...")


    # Keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    run()
