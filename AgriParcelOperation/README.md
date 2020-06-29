# Agri Parcel Operation
This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.

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
| operationType | Property | A choice from an enumerated list describing the operation performed on the parcel. One of: **fertiliser, inspection, pesticide, water, other.** | Recommended |
| description | Property | A description of the operation. | Recommended |
| result | Property | A description of the results of the operation. One of: **ok, aborted, failed.** | Recommended |
| plannedStartAt | DateTime | The planned start date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation starts may be before or after the planned start. | Mandatory |
| plannedEndAt | DateTime | The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end. | Mandatory |
| status | Property | A choice from an enumerated list describing the status. One of: **planned, ongoing, finished, scheduled, cancelled.** | Recommended |
| hasOperator | Relationship | Reference to the operator conducting the operation | Recommended |
| startedAt | DateTime | Timestamp when the operation actually started to be performed. | Recommended |
| endedAt | DateTime | Timestamp when the operation actually finished. | Recommended |
| reportedAt | DateTime | Timestamp when the event/ fault was reported. | Recommended |
| hasAgriProductType | Relationship | Reference to the AgriProductType used/ applied. | Optional |
| quantity | Property | The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids. | Optional |
| waterSource | Property | If water was applied/ use this specifies the source. One of: **borehole, rainfall, river, rainwater capture, water dam, commercial supply.** | Recommended |
| <em>startDate</em> | <em>DateTime</em> | <em>The planned start date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation starts may be before or after the planned start.<br/><br/>Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **plannedStartAt**</em> | <em>Deprecated</em> |
| <em>endDate</em> | <em>DateTime</em> | <em>The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end.<br/><br/>Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **plannedEndAt**</em> | <em>Deprecated</em> |
| <em>dateStarted</em> | <em>DateTime</em> | <em>Timestamp when the operation actually started to be performed.<br/><br/>Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **startedAt**</em> | <em>Deprecated</em> |
| <em>dateFinished</em> | <em>DateTime</em> | <em>Timestamp when the operation actually finished.<br/><br/>Note this field was defined for use with NGSIv2 and is now deprecated. For new entities and applications replace with **endedAt**</em> | <em>Deprecated</em> |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Parcel Operation** entity

[Download context definition.](../examples/Agri-Parcel-Operation-context.jsonld)

```JavaScript
{
    "@context": {
        "description": "https://schema.org/description",
        "plannedStartAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/plannedstartat"
        },
        "plannedEndAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/plannedendat"
        },
        "startedAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/startedat"
        },
        "endedAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/endedat"
        },
        "reportedAt": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/reportedat"
        },
        "startDate": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/startdate"
        },
        "endDate": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/enddate"
        },
        "dateStarted": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/datestarted"
        },
        "dateFinished": {
            "@type": "DateTime",
            "@id": "https://www.gsma.com/iot/iot-big-data/ngsi-ld/datefinished"
        }
    }
}
```
## Example of Agri Parcel Operation Entity
The following is an example instance of the **Agri Parcel Operation** entity

[Download example entity definition.](../examples/Agri-Parcel-Operation.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Parcel-Operation-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",
    "type": "AgriParcelOperation",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
    "hasAgriParcel": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"
    },
    "operationType": {
        "type": "Property",
        "value": "fertiliser"
    },
    "description": {
        "type": "Property",
        "value": "Monthly fertiliser application"
    },
    "result": {
        "type": "Property",
        "value": "ok"
    },
    "plannedStartAt": {
        "type": "Property",
        "value": "2016-08-22T10:18:16Z"
    },
    "plannedEndAt": {
        "type": "Property",
        "value": "2016-08-28T10:18:16Z"
    },
    "status": {
        "type": "Property",
        "value": "finished"
    },
    "hasOperator": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"
    },
    "startedAt": {
        "type": "Property",
        "value": "2016-08-22T10:18:16Z"
    },
    "endedAt": {
        "type": "Property",
        "value": "2016-08-28T10:18:16Z"
    },
    "reportedAt": {
        "type": "Property",
        "value": "2016-08-28T10:18:16Z"
    },
    "hasAgriProductType": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"
    },
    "quantity": {
        "type": "Property",
        "value": 40,
        "unitCode": "KGM"
    },
    "waterSource": {
        "type": "Property",
        "value": "rainwater capture"
    }
}
```
