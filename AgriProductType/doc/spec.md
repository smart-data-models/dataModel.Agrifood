# Agri Product Type
This entity contains a harmonised description of a generic agricultural product type. This entity is primarily associated with the agricultural vertical and related IoT applications. The AgriProductType includes a hierarchical structure that allows product types to be grouped in a flexible way.

| Attribute Name | Attribute Type | Description | Constraint |
|:--- |:--- |:--- |:---:|
| id | @id | Provides a unique identifier for an instance of the entity either in the form of a URI (i.e. either a publicly accessible URL or a URN). | Mandatory |
| type | @type | Defines the type of the entity. | Mandatory |
| createdAt | TemporalProperty | Indicates the date/ time that the instance of the entity was created in ISO 8601 format. The value of this will be set by the server when the entity was created. | Mandatory |
| modifiedAt | TemporalProperty | Indicates the date/ time when the entity was last modified in ISO 8601 format. The value of this will be set by the server when the entity was modified, if the entity has not been modified it may have a null value. | Optional |
| source | Property | Specifies the URL to the source of this data (either organisation or where relevant more specific source) | Recommended |
| dataProvider | Property | Specifies the URL to information about the provider of this information | Recommended |
| entityVersion | Property | The entity specification version as a number. A version number of 2.0 or later denotes the entity is represented using NGSI-LD | Recommended |
| name | Property | The name of this product type. | Mandatory |
| description | Property | A description of this product type. | Mandatory |
| root | Property | A logical indicator that this product is the root of an AgriProductType hierarchy. Logical true indicates it is the root. | Mandatory |
| hasAgriProductTypeParent | Relationship | Reference to the parent product type i.e. immediately above the entity in the hierarchy. | Optional |
| hasAgriProductTypeChildren | Relationship | Reference to child product types i.e. immediately below this entity in the hierarchy. | Optional |

## NGSI-LD Context Definition
The following NGSI-LD context definition applies to the **Agri Product Type** entity

[Download context definition.](../examples/Agri-Product-Type-context.jsonld)

```JavaScript
{
    "@context": {
        "name": "https://schema.org/name",
        "description": "https://schema.org/description"
    }
}
```
## Example of Agri Product Type Entity
The following is an example instance of the **Agri Product Type** entity

[Download example entity definition.](../examples/Agri-Product-Type.jsonld)

```JavaScript
{
    "@context": [
        "https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.json",
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Agri-Product-Type-context.jsonld"
    ],
    "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",
    "type": "AgriProductType",
    "createdAt": "2017-01-01T01:20:00Z",
    "modifiedAt": "2017-05-04T12:30:00Z",
    "source": "https://source.example.com",
    "dataProvider": "https://provider.example.com",
    "entityVersion": 2.0,
    "name": {
        "type": "Property",
        "value": "Soft Fruits"
    },
    "description": {
        "type": "Property",
        "value": "Soft edible fruits"
    },
    "root": {
        "type": "Property",
        "value": true
    },
    "hasAgriProductTypeParent": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e"
    },
    "hasAgriProductTypeChildren": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",
            "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",
            "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"
        ]
    }
}
```
