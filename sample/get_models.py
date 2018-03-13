from __future__ import print_function
import time
import stylelens_admin
from stylelens_admin.models import Models
from pprint import pprint
# create an instance of the API class
api_instance = Models()

try:
    api_response = api_instance.get_models('od_3s')
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_models: %s\n" % e)