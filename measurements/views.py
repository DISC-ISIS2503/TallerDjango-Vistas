from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            msr_dto = ml.get_measurement(id)
            msr = serializers.serialize('json', [msr_dto,])
            return HttpResponse(msr, 'application/json')
        else:
            msrs_dto = ml.get_measurements()
            msrs = serializers.serialize('json', msrs_dto)
            return HttpResponse(msrs, 'application/json')

    if request.method == 'POST':
        msr_dto = ml.create_measurement(json.loads(request.body))
        msr = serializers.serialize('json', [msr_dto,])
        return HttpResponse(msr, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        msr_dto = ml.get_measurement(pk)
        msr = serializers.serialize('json', [msr_dto,])
        return HttpResponse(msr, 'application/json')

    if request.method == 'PUT':
        msr_dto = ml.update_measurement(pk, json.loads(request.body))
        msr = serializers.serialize('json', [msr_dto,])
        return HttpResponse(msr, 'application/json')