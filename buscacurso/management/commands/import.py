from django.core.management.base import BaseCommand, CommandError
from buscacurso.models import Curso_Faculdade



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count =Curso_Faculdade.objects.from_csv('buscacurso/csv/DB-TCC.csv')
        print ("records inserted".format(insert_count))