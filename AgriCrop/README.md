# Agri Crop
This entity contains a harmonised description of a generic crop. This entity is primarily associated with the agricultural vertical and related IoT applications.

| Attribute Name | Attribute Type | Description | Constraint |
|:--- |:--- |:--- |:---:|
| id | @id | Provides a unique identifier for an instance of the entity either in the form of a URI (i.e. either a publicly accessible URL or a URN). | Mandatory |
| type | @type | Defines the type of the entity. | Mandatory |
| createdAt | TemporalProperty | Indicates the date/ time that the instance of the entity was created in ISO 8601 format. The value of this will be set by the server when the entity was created. | Mandatory |
| modifiedAt | TemporalProperty | Indicates the date/ time when the entity was last modified in ISO 8601 format. The value of this will be set by the server when the entity was modified, if the entity has not been modified it may have a null value. | Optional |
| source | Property | Specifies the URL to the source of this data (either organisation or where relevant more specific source) | Recommended |
| dataProvider | Property | Specifies the URL to information about the provider of this information | Recommended |
| entityVersion | Property | The entity specification version as a number. A version number of 2.0 or later denotes the entity is represented using NGSI-LD | Recommended |
| name | Property | The name of this crop. | Mandatory |
| alternateName | Property | An alternative name for this crop. | Optional |
| description | Property | A description of this crop. | Recommended |
| hasAgriSoil | Relationship | Reference to the recommended types of soil suitable for growing this crop. | Optional |
| hasAgriFertiliser | Relationship | Reference to the recommended types of fertiliser suitable for growing this crop. | Optional |
| hasAgriPest | Relationship | Reference to the pests known to attack this crop. | Optional |
| plantingFrom | Property | A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date. | Optional |
| harvestingInterval | Property | A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date. | Optional |
| wateringFrequency | Property | A description of the recommended watering schedule. A choice from an enumerated list. One of: **daily, weekly, biweekly, monthly, onDemand, other** | Optional |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Crop** entity

[Download context definition.](../examples/Agri-Crop-context.jsonld)

```JavaScript
{
    "@context": {
        "name": "https://schema.org/name",
        "alternateName": "https://schema.org/alternateName",
        "description": "https://schema.org/description"
    }
}
```
## Example of Agri Crop Entity
The following is an example instance of the **Agri Crop** entity

[Download example entity definition.](../examples/Agri-Crop.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Crop-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
    "type": "AgriCrop",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
    "name": {
        "type": "Property",
        "value": "Wheat"
    },
    "alternateName": {
        "type": "Property",
        "value": "Triticum aestivum"
    },
    "description": {
        "type": "Property",
        "value": "Spring wheat"
    },
    "hasAgriSoil": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",
            "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"
        ]
    },
    "hasAgriFertiliser": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
            "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"
        ]
    },
    "hasAgriPest": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
            "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"
        ]
    },
    "plantingFrom": {
        "type": "Property",
        "value": [
            {
                "dateRange": "-09-28/-10-12",
                "description": "Best Season"
            },
            {
                "dateRange": "-10-11/-10-18",
                "description": "Season OK"
            }
        ]
    },
    "harvestingInterval": {
        "type": "Property",
        "value": [
            {
                "dateRange": "-03-21/-04-01",
                "description": "Best Season"
            },
            {
                "dateRange": "-04-02/-04-15",
                "description": "Season OK"
            }
        ]
    },
    "wateringFrequency": {
        "type": "Property",
        "value": "daily"
    }
}
```
