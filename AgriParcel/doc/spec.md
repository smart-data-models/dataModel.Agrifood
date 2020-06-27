# Agri Parcel
This entity contains a harmonised description of a generic parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.

| Attribute Name | Attribute Type | Description | Constraint |
|:--- |:--- |:--- |:---:|
| id | @id | Provides a unique identifier for an instance of the entity either in the form of a URI (i.e. either a publicly accessible URL or a URN). | Mandatory |
| type | @type | Defines the type of the entity. | Mandatory |
| createdAt | TemporalProperty | Indicates the date/ time that the instance of the entity was created in ISO 8601 format. The value of this will be set by the server when the entity was created. | Mandatory |
| modifiedAt | TemporalProperty | Indicates the date/ time when the entity was last modified in ISO 8601 format. The value of this will be set by the server when the entity was modified, if the entity has not been modified it may have a null value. | Optional |
| source | Property | Specifies the URL to the source of this data (either organisation or where relevant more specific source) | Recommended |
| dataProvider | Property | Specifies the URL to information about the provider of this information | Recommended |
| entityVersion | Property | The entity specification version as a number. A version number of 2.0 or later denotes the entity is represented using NGSI-LD | Recommended |
| location | GeoProperty | The geo:json encoded polygon / multi-polygon describing this parcel. | Mandatory |
| area | Property | The area of the parcel nominally in square meters. | Mandatory |
| description | Property | Home Farm - North West field. | Recommended |
| category | Property | The category of the parcel of land e.g.: **arable, grassland, vineyard, orchard, mixed crop, lowland, upland, set-aside, forestry, wetland.** | Recommended |
| hasAgriParcelParent | Relationship | An optional reference to a higher level (parent) AgriParcel entity to which this entity relates. | Optional |
| hasAgriParcelChildren | Relationship | An optional reference to lower level (child) AgriParcel records to which this entity relates. | Optional |
| hasAgriCrop | Relationship | Reference to the crop associated with this parcel | Mandatory |
| cropStatus | Property | A choice from an enumerated list describing the crop planting status One of: **seeded, justBorn, growing, maturing, readyForHarvesting.** | Recommended |
| lastPlantedAt | DateTime | Indicates the date when the crop was last planted. | Recommended |
| hasAgriSoil | Relationship | Reference to the soil associated with this parcel of land. | Optional |
| hasDevice | Relationship | Reference to the IoT devices associated with this parcel i.e. sensors, controls. | Recommended |
| <em>dateLastPlanted</em> | <em>DateTime</em> | <em>Indicates the date when the crop was last planted.<br/><br/>Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **lastPlantedAt**</em> | <em>Deprecated</em> |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Parcel** entity

[Download context definition.](../examples/Agri-Parcel-context.jsonld)

```JavaScript
{
    "@context": {
        "description": "https://schema.org/description",
        "lastPlantedAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/lastplantedat"
        },
        "dateLastPlanted": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/datelastplanted"
        }
    }
}
```
## Example of Agri Parcel Entity
The following is an example instance of the **Agri Parcel** entity

[Download example entity definition.](../examples/Agri-Parcel.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Parcel-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriParcel:72d9fb43-53f8-4ec8-a33c-fa931360259a",
    "type": "AgriParcel",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
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
    "area": {
        "type": "Property",
        "value": 200,
        "unitCode": "MTK"
    },
    "description": {
        "type": "Property",
        "value": "Spring wheat"
    },
    "category": {
        "type": "Property",
        "value": "arable"
    },
    "hasAgriParcelParent": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"
    },
    "hasAgriParcelChildren": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",
            "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"
        ]
    },
    "hasAgriCrop": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriCrop:36021150-4474-11e8-a721-af07c5fae7c8"
    },
    "cropStatus": {
        "type": "Property",
        "value": "seeded"
    },
    "lastPlantedAt": {
        "type": "Property",
        "value": "2016-08-23T10:18:16Z"
    },
    "hasAgriSoil": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriSoil:429d1338-4474-11e8-b90a-d3e34ceb73df"
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
