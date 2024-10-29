
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
dataModel = "AgriPhytosanitary"
subject = "dataModel.Agrifood"
subtype = {'type': 'Property', 'value': {'type': 'TypePhytosanitary', 'id': {'type': 'Property', 'value': '183'}, 'idpdf': {'type': 'Property', 'value': '88013'}, 'code': {'type': 'Property', 'value': '11179'}, 'name': {'type': 'Property', 'value': 'Microthiol Special Disperss'}, 'names': {'type': 'Property', 'value': [{'type': 'Property', 'value': 'Colpenn'}, {'type': 'Property', 'value': 'Microthiol Special Disperss'}, {'type': 'Property', 'value': 'Sulf 80 Wg'}]}, 'idate': {'type': 'Property', 'value': '1970-01-01T00:00:00.000Z'}, 'rdate': {'type': 'Property', 'value': ''}, 'edate': {'type': 'Property', 'value': '2025-04-15T00:00:00.000Z'}, 'cdate': {'type': 'Property', 'value': ''}, 'ldate': {'type': 'Property', 'value': ''}, 'mix': {'type': 'Property', 'value': 1}, 'idtf': {'type': 'Property', 'value': [{'type': 'Property', 'value': 11}, {'type': 'Property', 'value': 1}]}, 'comp': {'type': 'Property', 'value': {'type': 'Company', 'id': {'type': 'Property', 'value': 1}, 'name': {'type': 'Property', 'value': 'Upl Iberia S.a.'}, 'nif': {'type': 'Property', 'value': 'A08103343'}}}, 'subs': {'type': 'Property', 'value': {'type': 'Substance', 'id': {'type': 'Property', 'value': '1'}, 'name': {'type': 'Property', 'value': 'Azufre 80% [Wg] P/P'}}}, 'prod': {'type': 'Property', 'value': {'type': 'TypeProduct', 'id': {'type': 'Property', 'value': 1}, 'name': {'type': 'Property', 'value': 'Producto fitosanitario registrado'}}}, 'ci': {'type': 'Property', 'value': []}}}
attribute = "subtype"
value = subtype
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

dose = "{'type': 'Property', 'value': '1'}"
attribute = "dose"
value = dose
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

measure = "{'type': 'Property', 'value': '1'}"
attribute = "measure"
value = measure
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

efficacy = {'type': 'Property', 'value': {'type': 'TypeEfficacy', 'id': {'type': 'Property', 'value': '1'}, 'name': {'type': 'Property', 'value': 'Buena'}, 'detail': {'type': 'Property', 'value': ''}}}
attribute = "efficacy"
value = efficacy
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
