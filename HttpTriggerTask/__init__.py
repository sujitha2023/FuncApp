import logging
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a Get request.')
    base_url = 'http://fhir.hl7fundamentals.org/r4/'
    resource = 'Task'
    res = requests.get(f'{base_url}/{resource}?status=requested')
    content=res.json()
    print(content)
    for i in content['entry']:
         id=i['resource']['id']
         body = {
              'id': id,
              'resourceType': resource,
              'status': 'completed'             
         }
         resPut = json.dumps(requests.put(f'{base_url}/{resource}/{id}', json.dumps(body)).json())
         print(resPut)
    
    
    return func.HttpResponse(resPut)

