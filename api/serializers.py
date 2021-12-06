from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['body', 'updated', 'created']  # or take all from models field paste: fields = '__all__'

