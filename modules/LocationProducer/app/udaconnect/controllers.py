from datetime import datetime


from flask import request, Response
from flask_restx import Namespace, Resource

from app.udaconnect.services import LocationProducer


DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling


@api.route("/send_loc")
class LocationResource(Resource):
    def post(self):
        location = request.get_json()
        LocationProducer.create_location(location)
        return Response(status=202)
