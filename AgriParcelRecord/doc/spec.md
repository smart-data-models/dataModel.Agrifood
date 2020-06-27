# Agri Parcel Record
This entity contains a harmonised description of the conditions recorded on a generic parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.

| Attribute Name | Attribute Type | Description | Constraint |
|:--- |:--- |:--- |:---:|
| id | @id | Provides a unique identifier for an instance of the entity either in the form of a URI (i.e. either a publicly accessible URL or a URN). | Mandatory |
| type | @type | Defines the type of the entity. | Mandatory |
| createdAt | TemporalProperty | Indicates the date/ time that the instance of the entity was created in ISO 8601 format. The value of this will be set by the server when the entity was created. | Mandatory |
| modifiedAt | TemporalProperty | Indicates the date/ time when the entity was last modified in ISO 8601 format. The value of this will be set by the server when the entity was modified, if the entity has not been modified it may have a null value. | Optional |
| source | Property | Specifies the URL to the source of this data (either organisation or where relevant more specific source) | Recommended |
| dataProvider | Property | Specifies the URL to information about the provider of this information | Recommended |
| entityVersion | Property | The entity specification version as a number. A version number of 2.0 or later denotes the entity is represented using NGSI-LD | Recommended |
| hasAgriParcel | Relationship | Reference to the AgriParcel to which this entity relates. | Mandatory |
| location | GeoProperty | The geo:json encoded polygon / multi-polygon describing the parcel which this record relates to. | Mandatory |
| soilTemperature | Property | The observed soil temperature nominally in degrees centigrade. | Optional |
| soilMoistureVwc | Property | Measured as Volumetric Water Content, VWC as a percentage.<br/><br/>0 ≤soilMoistureVwc ≤ 1 | Optional |
| soilMoistureEc | Property | Measured as Electrical Conductivity, EC nominally in units of Siemens per meter (S/m). | Optional |
| airTemperature | Property | The observed air temperature (in the shade) nominally in degrees centigrade. | Recommended |
| solarRadiation | Property | Instantaneous solar radiation measured in kW/m2. | Optional |
| relativeHumidity | Property | Relative Humidity a number between 0 and 1 representing the range of 0% to 100%.<br/><br/>0 ≤ relativeHumidity ≤ 1  | Optional |
| atmosphericPressure | Property | Atmospheric Pressure nominally in units of hecto Pascals. | Recommended |
| description | Property | A description of this record | Recommended |
| hasDevice | Relationship | Reference to the IoT devices associated with this greenhouse i.e. sensors, controls. | Recommended |
| observedAt | DateTime | Indicates the date/time the record was observed/ last observed. | Recommended |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Parcel Record** entity

[Download context definition.](../examples/Agri-Parcel-Record-context.jsonld)

```JavaScript
{
    "@context": {
        "description": "https://schema.org/description",
        "observedAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/observedat"
        }
    }
}
```
## Example of Agri Parcel Record Entity
The following is an example instance of the **Agri Parcel Record** entity

[Download example entity definition.](../examples/Agri-Parcel-Record.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Parcel-Record-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriParcelRecord:8f5445e6-f49b-496e-833b-e65fc97fcab7",
    "type": "AgriParcelRecord",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
    "hasAgriParcel": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriParcel:d3676010-d815-468c-9e01-25739c5a25ed"
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Polygon",
            "coordinates": [
                [
                    100,
                    0
                ],
                [
                    101,
                    0
                ],
                [
                    101,
                    1
                ],
                [
                    100,
                    1
                ],
                [
                    100,
                    0
                ]
            ]
        }
    },
    "soilTemperature": {
        "type": "Property",
        "value": 27,
        "unitCode": "CEL",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "soilMoistureVwc": {
        "type": "Property",
        "value": 0.08,
        "unitCode": "C62",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "soilMoistureEc": {
        "type": "Property",
        "value": 17,
        "unitCode": "D10",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "airTemperature": {
        "type": "Property",
        "value": 20,
        "unitCode": "CEL",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "solarRadiation": {
        "type": "Property",
        "value": 15,
        "unitCode": "N78",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "relativeHumidity": {
        "type": "Property",
        "value": 0.15,
        "unitCode": "C62",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "atmosphericPressure": {
        "type": "Property",
        "value": 1013.25,
        "unitCode": "A97",
        "observedAt": "2017-05-04T12:30:00Z"
    },
    "description": {
        "type": "Property",
        "value": "Monthly fertiliser application"
    },
    "hasDevice": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",
            "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",
            "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",
            "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"
        ]
    },
    "observedAt": {
        "type": "Property",
        "value": "2017-05-04T10:18:16Z"
    }
}
```
