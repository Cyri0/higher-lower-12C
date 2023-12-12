from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PersonSerializer
from .models import Person

import random

@api_view(['GET'])
def getAllPersons(request):

    persons = Person.objects.all()
    serialized_persons = PersonSerializer(persons, many = True)

    return Response(serialized_persons.data)


@api_view(['GET'])
def getTwoPersons(request):

    persons = Person.objects.all()
    
    rnd = random.randint(0,len(persons)-1)

    choosenPersons = []
    choosenPersons.append(persons[rnd])

    while True:
        rnd = random.randint(0,len(persons)-1)
        if(persons[rnd] not in choosenPersons):
            choosenPersons.append(persons[rnd])
            break

    serialized_persons = PersonSerializer(choosenPersons, many = True)
    return Response(serialized_persons.data)