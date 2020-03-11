from haystack import indexes
from registration.models import BirthRegistration, DeathRegistration, RegistrationCentre


class BirthCertificateIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    middle_name = indexes.CharField(model_attr='middle_name')
    surname = indexes.CharField(model_attr='surname')
    reference_number = indexes.CharField(model_attr='reference_number')
    date_of_birth = indexes.DateTimeField(model_attr='date_of_birth')

    def get_model(self):
        return BirthRegistration

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class DeathCertificateIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    person = indexes.CharField(model_attr='person')
    date_of_death = indexes.DateField(model_attr='date_of_death')

    def get_model(self):
        return DeathRegistration

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

#  	/usr/local/lib/python3.5/dist-packages/haystack/backends/solr_backend.py
#    app_label, model_name = raw_result[DJANGO_CT].split('.')