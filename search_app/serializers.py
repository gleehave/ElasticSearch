from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search_app.documents import NewsDocument
from search_app.models import ElasticDemo


class NewsDocumentSerializer(DocumentSerializer):
    class Meta(object):
        model = ElasticDemo
        document = NewsDocument
        fields = ('title', 'content',)
    def get_location(self, obj):
        try:
            return obj.location.to_dict()
        except:
            return {}