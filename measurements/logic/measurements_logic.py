
from ..models import Measurement


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.value = new_mea["value"]
    measurement.unit = new_mea["unit"]
    measurement.place = new_mea["place"]
    measurement.save()
    return measurement

def create_measurement(msr):
    measurement = Measurement(variable_id=msr["variable_id"],
                              value=msr["value"],
                              unit=msr["unit"],
                              place=msr["place"]
                              )
    measurement.save()
    return measurement