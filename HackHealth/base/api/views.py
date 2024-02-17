from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import UploadedFile
from .serializers import RoomSerializer
from .serializers import NLPResultSerializer, DIPResultSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = UploadedFile.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = UploadedFile.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


def get_results(request):
    nlp_input = request.data.get('nlp_input')
    dip_input = request.data.get('dip_input')

    # Assuming NLPModel and DIPModel are your models and they have methods to process input
    # nlp_result = NLPModel.process(nlp_input)
    # dip_result = DIPModel.process(dip_input)
    nlp_result = "Super dead brother"
    dip_result = 1
    nlp_serializer = NLPResultSerializer({'result': nlp_result})
    dip_serializer = DIPResultSerializer({'result': dip_result})

    return Response({'nlp_result': nlp_serializer.data, 'dip_result': dip_serializer.data})