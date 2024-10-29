
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "AgriFertilize"
subject = "dataModel.Agrifood"
subtype = {'type': 'Property', 'value': {'type': 'TypeFertilize', 'id': {'type': 'Property', 'value': 1339}, 'code': {'type': 'Property', 'value': 'F0002478/2025'}, 'name': {'type': 'Property', 'value': 'Abono Organico Npk (Ca) 1,5-1-2 (2) Mezcla De Origen Animal Y Vegetal Sirlepur'}, 'mmcm': {'type': 'Property', 'value': [{'type': 'CM', 'id': {'type': 'Property', 'value': 10000}, 'subtype': {'type': 'Property', 'value': {'type': 'TCM', 'id': {'type': 'Property', 'value': 1}, 'subtype': {'type': 'Property', 'value': {'type': 'SCM', 'id': {'type': 'Property', 'value': 1}, 'name': {'type': 'Property', 'value': 'Macronutriente principal'}}}, 'code': {'type': 'Property', 'value': 1}, 'name': {'type': 'Property', 'value': 'Nitrógeno total'}, 'symbol': {'type': 'Property', 'value': '% N total'}}}, 'value': {'type': 'Property', 'value': 1.5}}, {'type': 'CM', 'id': {'type': 'Property', 'value': 10001}, 'subtype': {'type': 'Property', 'value': {'type': 'TCM', 'id': {'type': 'Property', 'value': 6}, 'subtype': {'type': 'Property', 'value': {'type': 'SCM', 'id': {'type': 'Property', 'value': 1}, 'name': {'type': 'Property', 'value': 'Macronutriente principal'}}}, 'code': {'type': 'Property', 'value': 6}, 'name': {'type': 'Property', 'value': 'Óxido de fósforo total'}, 'symbol': {'type': 'Property', 'value': '% P2O5 total'}}}, 'value': {'type': 'Property', 'value': 1}}, {'type': 'CM', 'id': {'type': 'Property', 'value': 10002}, 'subtype': {'type': 'Property', 'value': {'type': 'TCM', 'id': {'type': 'Property', 'value': 9}, 'subtype': {'type': 'Property', 'value': {'type': 'SCM', 'id': {'type': 'Property', 'value': 1}, 'name': {'type': 'Property', 'value': 'Macronutriente principal'}}}, 'code': {'type': 'Property', 'value': 9}, 'name': {'type': 'Property', 'value': 'Óxido de potasio'}, 'symbol': {'type': 'Property', 'value': '% K2O total'}}}, 'value': {'type': 'Property', 'value': 2}}]}, 'macm': {'type': 'Property', 'value': []}, 'hecm': {'type': 'Property', 'value': []}, 'micm': {'type': 'Property', 'value': []}, 'accm': {'type': 'Property', 'value': []}, 'aacm': {'type': 'Property', 'value': []}, 'otcm': {'type': 'Property', 'value': []}, 'comp': {'type': 'Property', 'value': {'type': 'Company', 'id': {'type': 'Property', 'value': 269}, 'name': {'type': 'Property', 'value': 'Organicos Pedrin, S.l'}, 'nif': {'type': 'Property', 'value': ''}}}, 'manure': {'type': 'Property', 'value': ''}, 'material': {'type': 'Property', 'value': {'type': 'TMF', 'id': {'type': 'Property', 'value': 15}, 'name': {'type': 'Property', 'value': 'Productos fertilizantes: abonos orgánicos'}}}, 'matdet': {'type': 'Property', 'value': ''}, 'provider': {'type': 'Property', 'value': ''}, 'nif': {'type': 'Property', 'value': ''}, 'check': {'type': 'Property', 'value': 0}, 'metadata': {'type': 'Property', 'value': [{'type': 'Create', 'user': {'type': 'Property', 'value': {'type': 'UserMetadata', 'id': {'type': 'Property', 'value': '1'}, 'loginname': {'type': 'Property', 'value': 'sistema'}, 'email': {'type': 'Property', 'value': ''}, 'name': {'type': 'Property', 'value': 'Sistema'}, 'surname': {'type': 'Property', 'value': ''}, 'nif': {'type': 'Property', 'value': ''}}}, 'date': {'type': 'Property', 'value': '2024-02-09T15:48:46.000Z'}}]}, 'reviewed': {'type': 'Property', 'value': 1}}}
attribute = "subtype"
value = subtype
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

inidate = "{'type': 'Property', 'value': '2024-05-30T09:14:44.000Z'}"
attribute = "inidate"
value = inidate
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

enddate = "{'type': 'Property', 'value': ''}"
attribute = "enddate"
value = enddate
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

dose = {'type': 'Property', 'value': 10}
attribute = "dose"
value = dose
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
