# This code allows you to install a orion-ld broker in a linux system
# The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#
# INSTALL NGSI LD broker (OrionLD)
# sudo docker pull mongo:3.6
# sudo docker pull fiware/orion-ld
# sudo docker network create fiware_default
# sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
# sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#
# TO RELAUNCH (only if you have already installed a broker in the same machine)
# sudo docker stop fiware-orionld
# sudo docker rm fiware-orionld
# sudo docker stop mongo-db
# sudo docker rm mongo-db
# sudo docker network rm fiware_default
#
# CHECK INSTANCES
# curl -X GET 'http://localhost:1026/version'
# curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#
# now the python code you can use to insert some value in the context broker

from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
import requests
import sys

print("Searching broker...")
serverUrl = None
for _url in ["http://localhost:1026", "https://localhost:1026"]:
    try:
        if requests.get(f"{_url}/version", timeout=5).status_code == 200:
            serverUrl = _url
            print(f"Broker found at {serverUrl}")
            break
    except Exception:
        pass
if serverUrl is None:
    serverUrl = input(
        "No broker found at default locations. Enter broker URL (or press Enter to abort): "
    ).strip()
    if serverUrl:
        try:
            if requests.get(f"{serverUrl}/version", timeout=5).status_code != 200:
                print("WARNING: Cannot connect to broker. Script cannot provide results.")
                sys.exit(1)
        except Exception:
            print("WARNING: Cannot connect to broker. Script cannot provide results.")
            sys.exit(1)
    else:
        print("WARNING: No broker URL provided. Script cannot provide results.")
        sys.exit(1)

dataModel = "AgriParcelRecord"
subject = "dataModel.Agrifood"

atmosphericPressure = 1013.25
attribute = "atmosphericPressure"
value = atmosphericPressure
# Updates the attribute in the broker; creates the entity if it does not exist
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

hasAgriParcel = "urn:ngsi-ld:AgriParcel:d3676010-d815-468c-9e01-25739c5a25ed"
attribute = "hasAgriParcel"
value = hasAgriParcel
# Updates the attribute in the broker; creates the entity if it does not exist
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

hasDevice = ['urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6', 'urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b', 'urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416', 'urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551']
attribute = "hasDevice"
value = hasDevice
# Updates the attribute in the broker; creates the entity if it does not exist
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print("In case you have installed the orion-ld broker (see header comments)")
print("Execute this to check the entity was inserted:")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
