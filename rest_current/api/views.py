from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pymongo import MongoClient

databaseName = "ceiba_data"
collectionName = "current"

client = None
db     = None
coll   = None


@csrf_exempt
def index(request):
        if request.method == "GET":
            return JsonResponse({"Ayuda": "HelloWorld!"})
        else:
            response = {"Respuesta":"Esta Funcionando el post"}

            result = body2dict(request)
            agregarBD(result)
            return JsonResponse(response)

@csrf_exempt
def body2dict(request):
    """
    Metodo que recibe un request y devuelve el JSON del body como diccionario
    """

    return json.loads(request.body.decode("UTF-8"))

def agregarBD(result):
    current = result['current']
    client = MongoClient()
    db = client[databaseName]
    coll = db[collectionName]
    res = db.coll.find({"clave":1})
    print res
