from django.http import HttpResponse



from RMLApp.models import RemindMe
from RMLApp.serializers import RemindMeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Remind_Me_Later.tasks import sendEmail
@api_view(['GET', 'POST'])
def remindme_list(request, format=None):
    if request.method == 'GET':
        remindme = RemindMe.objects.all()
        serializer = RemindMeSerializer(remindme, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RemindMeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            #print(serializer.data['id'])
            modelid = serializer.data['id']

            time = serializer.validated_data['remind_date']
            #print()
            #time = datetime(time)
            sendEmail.apply_async( eta=time, kwargs={'id': modelid})

            return Response({'status':'ok'},status=status.HTTP_201_CREATED)
        return Response({'status':'error','error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def remindme_detail(request, pk, format=None):
    try:
        remindme = RemindMe.objects.get(pk=pk)
    except remindme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RemindMeSerializer(remindme)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RemindMeSerializer(remindme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        remindme.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)