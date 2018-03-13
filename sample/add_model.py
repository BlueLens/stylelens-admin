from __future__ import print_function
import time
import stylelens_admin
from stylelens_admin.models import Models
from pprint import pprint
# create an instance of the API class
api_instance = Models()

url = 'https://xxx.sss.zzz'
try:
    api_response = api_instance.add_model('od_1s', url, '0.0.1')
    pprint(api_response)
except Exception as e:
    print("Exception when calling add_model: %s\n" % e)