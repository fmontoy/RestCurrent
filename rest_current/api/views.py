
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from sympy import SympifyError
import json

@csrf_exempt
def index(request):
    try:
        if request.method == "GET":
            return JsonResponse({"Ayuda": "HelloWorld!"})
        else:
            params = body2dict(request)
            print("PARAMS ", params)
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
