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
    try:
        if request.method == "GET":
            return JsonResponse({"Ayuda": "HelloWorld!"})
        else:
            response = {"Respuesta":"Esta Funcionando el post"}
            # print("RESPONSE: ", response)
            return JsonResponse(response)
    except SympifyError as e:
        return JsonResponse({"error": "Verifique los datos de entrada"})

@csrf_exempt
def body2dict(request):
    """
    Metodo que recibe un request y devuelve el JSON del body como diccionario
    """

    return json.loads(request.body.decode("UTF-8"))

def agregarBD(request):

    client = MongoClient()
    db = client[databaseName]
    coll = db[collectionName]
    result = coll.insert_one(request)
