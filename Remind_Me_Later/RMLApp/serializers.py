from rest_framework import serializers
from RMLApp.models import RemindMe

# remind_message = models.TextField()
#     remind_date = models.DateTimeField('date to Remind', null=False)
#     remind_email = models.EmailField(max_length=254,blank=True)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     remind_phone = models.CharField(max_length = 15, validators=[phone_regex], blank=True) # validators should be a list



class RemindMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemindMe
        fields = ('id', 'remind_message', 'remind_date', 'remind_email', 'remind_phone')
    # pk = serializers.IntegerField(read_only=True)
    # remind_message = serializers.CharField(style={'base_template': 'textarea.html'})
    # remind_date = serializers.DateTimeField(require=True)
    # remind_email = serializers.EmailField(required=False, allow_blank=True, max_length=254)
    # remind_phone = serializers.CharField(required=False, allow_blank=True, max_length=15)

    def create(self, validated_data):
        return RemindMe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.remind_message = validated_data.get('remind_message', instance.title)
        instance.remind_date = validated_data.get('remind_date', instance.remind_date)
        instance.remind_email = validated_data.get('remind_email', instance.remind_email)
        instance.remind_phone = validated_data.get('remind_phone', instance.remind_phone)
        instance.save()
        return instance