# Agri Greenhouse
This entity contains a harmonised description of the conditions recorded within a generic greenhouse, a type of AgriParcel. This entity is primarily associated with the agricultural vertical and related IoT applications.

| Attribute Name | Attribute Type | Description | Constraint |
|:--- |:--- |:--- |:---:|
| id | @id | Provides a unique identifier for an instance of the entity either in the form of a URI (i.e. either a publicly accessible URL or a URN). | Mandatory |
| type | @type | Defines the type of the entity. | Mandatory |
| createdAt | TemporalProperty | Indicates the date/ time that the instance of the entity was created in ISO 8601 format. The value of this will be set by the server when the entity was created. | Mandatory |
| modifiedAt | TemporalProperty | Indicates the date/ time when the entity was last modified in ISO 8601 format. The value of this will be set by the server when the entity was modified, if the entity has not been modified it may have a null value. | Optional |
| source | Property | Specifies the URL to the source of this data (either organisation or where relevant more specific source) | Recommended |
| dataProvider | Property | Specifies the URL to information about the provider of this information | Recommended |
| hasAgriParcelParent | Relationship | Reference to the AgriParcel entity to which this entity relates. | Mandatory |
| hasAgriParcelChildren | Relationship | Related sub AgriParcel records to which this entity relates. | Optional |
| hasWeatherObserved | Relationship | Reference to the weather observation record current for this entity. | Recommended |
| hasWaterQualityObserved | Relationship | Reference to one or more water quality observation records current for this entity. | Recommended |
| relativeHumidity | Property | The inside relative humidity expressed as a number between 0 and 1 representing the range 0% to 100 (%).<br/><br/>0 ≤ relativeHumidity ≤ 1 | Recommended |
| leafTemperature | Property | The average greenhouse air temperature nominally in degrees centigrade. | Recommended |
| co2 | Property | The measured interior C02 concentration nominally in mg/L. | Optional |
| dailyLight | Property | Daily Accumulated light measured in kW per square metre | Optional |
| drainFlow | Property | The observed drain flow rate in litres per second | Optional |
| hasDevice | Relationship | Reference to the IoT devices associated with this greenhouse i.e. sensors, controls. | Recommended |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Greenhouse** entity

[Download context definition.](../examples/Agri-Greenhouse-context.jsonld)

```JavaScript
{
    "@context": {}
}
```
## Example of Agri Greenhouse Entity
The following is an example instance of the **Agri Greenhouse** entity

[Download example entity definition.](../examples/Agri-Greenhouse.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Greenhouse-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
    "type": "AgriGreenhouse",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
    "hasAgriParcelParent": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b"
    },
    "hasAgriParcelChildren": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",
            "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"
        ]
    },
    "hasWeatherObserved": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d"
    },
    "hasWaterQualityObserved": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",
            "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"
        ]
    },
    "relativeHumidity": {
        "type": "Property",
        "value": 0.4,
        "unitCode": "C62",
        "observedAt": "2016-08-22T19:20Z"
    },
    "leafTemperature": {
        "type": "Property",
        "value": 22,
        "unitCode": "CEL",
        "observedAt": "2016-08-22T19:20Z"
    },
    "co2": {
        "type": "Property",
        "value": 28,
        "unitCode": "M1",
        "observedAt": "2016-08-22T19:20Z"
    },
    "dailyLight": {
        "type": "Property",
        "value": 24,
        "unitCode": "N78",
        "observedAt": "2016-08-22T19:20Z"
    },
    "drainFlow": {
        "type": "Property",
        "value": {
            "value": 33,
            "maxValue": 50,
            "minValue": 25,
            "unitText": "Litre per second"
        },
        "unitCode": "G51",
        "observedAt": "2016-08-22T19:20Z"
    },
    "hasDevice": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",
            "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",
            "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",
            "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"
        ]
    }
}
```
