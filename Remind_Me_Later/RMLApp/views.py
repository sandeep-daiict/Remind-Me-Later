from RMLApp.models import RemindMe
from RMLApp.serializers import RemindMeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Remind_Me_Later.tasks import sendEmail, sendSMS
@api_view(['GET'])
def remindme_list(request, format=None):
    if request.method == 'GET':
        remindme = RemindMe.objects.all()
        serializer = RemindMeSerializer(remindme, many=True)
        return Response(serializer.data)

    return Response({'status':'error'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def remindme_add(request, format=None):
    if request.method == 'POST':
        serializer = RemindMeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            #print(serializer.data['id'])
            modelid = serializer.data['id']
            email = serializer.validated_data['remind_email']
            phone = serializer.validated_data['remind_phone']
            time = serializer.validated_data['remind_date']

            if email:
                sendEmail.apply_async( eta=time, kwargs={'id': modelid})
            if phone:
                sendSMS.apply_async( eta=time, kwargs={'id': modelid})
            #print()
            #time = datetime(time)


            return Response({'status':'ok'},status=status.HTTP_201_CREATED)
        return Response({'status':'error','error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'status':'error'}, status=status.HTTP_400_BAD_REQUEST)
