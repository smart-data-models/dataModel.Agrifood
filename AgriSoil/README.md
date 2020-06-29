# Agri Soil
This entity contains a harmonised description of soil. This entity is primarily associated with the agricultural vertical and related IoT applications.

| Attribute Name | Attribute Type | Description | Constraint |
|:--- |:--- |:--- |:---:|
| id | @id | Provides a unique identifier for an instance of the entity either in the form of a URI (i.e. either a publicly accessible URL or a URN). | Mandatory |
| type | @type | Defines the type of the entity. | Mandatory |
| createdAt | TemporalProperty | Indicates the date/ time that the instance of the entity was created in ISO 8601 format. The value of this will be set by the server when the entity was created. | Mandatory |
| modifiedAt | TemporalProperty | Indicates the date/ time when the entity was last modified in ISO 8601 format. The value of this will be set by the server when the entity was modified, if the entity has not been modified it may have a null value. | Optional |
| source | Property | Specifies the URL to the source of this data (either organisation or where relevant more specific source) | Recommended |
| dataProvider | Property | Specifies the URL to information about the provider of this information | Recommended |
| entityVersion | Property | The entity specification version as a number. A version number of 2.0 or later denotes the entity is represented using NGSI-LD | Recommended |
| name | Property | The name of this soil type. | Mandatory |
| alternateName | Property | Alternative name of this soil type. | Optional |
| description | Property | A description of this soil. | Recommended |
| hasAgriProductType | Relationship | Reference to the recommended types of product (such as fertiliser) that can be used to condition this soil type. | Optional |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Soil** entity

[Download context definition.](../examples/Agri-Soil-context.jsonld)

```JavaScript
{
    "@context": {
        "name": "https://schema.org/name",
        "alternateName": "https://schema.org/alternateName",
        "description": "https://schema.org/description"
    }
}
```
## Example of Agri Soil Entity
The following is an example instance of the **Agri Soil** entity

[Download example entity definition.](../examples/Agri-Soil.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Soil-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriSoil:789363b4-c771-43d6-8505-ca582efe8fcd",
    "type": "AgriSoil",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
    "name": {
        "type": "Property",
        "value": "Clay"
    },
    "alternateName": {
        "type": "Property",
        "value": "Heavy soil"
    },
    "description": {
        "type": "Property",
        "value": "Fine grained, poor draining soil. Particle size less than 0.002mm"
    },
    "hasAgriProductType": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriProductType:ea54eedf-d5a7-4e44-bddd-50e9935237c0",
            "urn:ngsi-ld:AgriProductType:275b4c08-5e52-4bb7-8523-74ce5d0007de"
        ]
    }
}
```
