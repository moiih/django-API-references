from rest_framework import serializers
from .models import Language


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')   
        
        ## This "fields" can be "list" also like ['name', 'paradigm'], instead of 'tuples'.
        
        ## The "Hyper_linlked_Model_Serializer" is used when many models are connected to ...
        ## each other with some (Foreign Key or Many-to-Many Relationship) concept, ...
        ## i.e., when relationship between the Models a bit complex.

        ## And the "Model_Serializer" is used when there is a simple model(s) following ...
        ## only Primary Key concept.