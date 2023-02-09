# file with external func

import random

from basic_word import BasicWord
import urllib, urllib.request, json


# import certifi
# import ssl

def load_random_word() -> BasicWord:
    """ create one BasicWord fill it from external data and return it
        request data from jsonkeeper
        be careful with kaspersky and other useless firewalls !
        alternatively use npoint.io resurse
    """
    # external_adr: str = "https://jsonkeeper.com/b/P3L7"  # it doesn't work =(
    external_adr: str = "https://api.npoint.io/8e92a5832c382022b229"  # it worked!!

    # don't delete this codes - it will be needed if I win against "VERIFY_SERTIFICATE" error
    # external_adr = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
    # response = urllib.request.urlopen(external_adr,  context=ssl.create_default_context(cafile=certifi.where()))
    # ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

    response = urllib.request.urlopen(external_adr)
    data = json.loads(response.read())
    random_num_from_data: int = random.randint(0, len(data) - 1)

    # fill word for return
    new_word4created: BasicWord = BasicWord(data[random_num_from_data]['word'], data[random_num_from_data]['subwords'])
    return new_word4created

# need write exeption handler, but it not describe in SOW
