
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
subtype = {'type': 'TypePhytosanitary', 'id': '183', 'idpdf': '88013', 'code': '11179', 'name': 'Microthiol Special Disperss', 'names': ['Colpenn', 'Microthiol Special Disperss', 'Sulf 80 Wg'], 'idate': '01-01-1970', 'rdate': '', 'edate': '15-04-2025', 'cdate': '', 'ldate': '', 'mix': 1, 'idtf': [11, 1], 'comp': {'type': 'Company', 'id': 1, 'name': 'Upl Iberia S.a.', 'nif': 'A08103343'}, 'subs': {'type': 'Substance', 'id': '1', 'name': 'Azufre 80% [Wg] P/P'}, 'prod': {'type': 'TypeProduct', 'id': 1, 'name': 'Producto fitosanitario registrado'}, 'ci': []}
attribute = "subtype"
value = subtype
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

dose = "1"
attribute = "dose"
value = dose
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

measure = "1"
attribute = "measure"
value = measure
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

efficacy = {'type': 'TypeEfficacy', 'id': '1', 'name': 'Buena', 'detail': ''}
attribute = "efficacy"
value = efficacy
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
