Entity: AgriProductType  
=======================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **This entity contains a harmonised description of a generic agricultural product type. This entity is primarily associated with the agricultural vertical and related IoT applications. The AgriProductType includes a hierarchical structure that allows product types to be grouped in a flexible way.**  

## List of properties  

- `agroVocConcept`:   - `alternateName`: An alternative name for this item  - `category`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `hasAgriProductTypeChildren`:   - `hasAgriProductTypeParent`:   - `id`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `relatedSource`: List of IDs the current entity may have in external applications  - `root`:   - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity Type  ## Data Model description of properties  
Sorted alphabetically  
```yaml  
AgriProductType:    
  description: 'This entity contains a harmonised description of a generic agricultural product type. This entity is primarily associated with the agricultural vertical and related IoT applications. The AgriProductType includes a hierarchical structure that allows product types to be grouped in a flexible way.'    
  properties:    
    agroVocConcept:    
      format: uri    
      type: string    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    category:    
      items:    
        enum:    
          - fertiliser    
          - cropNutrition    
          - cropProtection    
          - cropVariety    
          - harvestCommodity    
        type: string    
      type: array    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    hasAgriProductTypeChildren:    
      items:    
        - anyOf: &agriproducttype_-_properties_-_hasagriproducttypeparent_-_anyof    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
      type: array    
    hasAgriProductTypeParent:    
      anyOf: *agriproducttype_-_properties_-_hasagriproducttypeparent_-_anyof    
    id:    
      anyOf: *agriproducttype_-_properties_-_hasagriproducttypeparent_-_anyof    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agriproducttype_-_properties_-_hasagriproducttypeparent_-_anyof    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agriproducttype_-_properties_-_hasagriproducttypeparent_-_anyof    
            applicationEntityId:    
              type: string    
      type: Property    
    root:    
      type: boolean    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type'    
      enum:    
        - AgriProductType    
      type: string    
  required:    
    - id    
    - type    
    - name    
    - root    
  type: object    
```  
#### AgriProductType NGSI V2 key-values Example    
Here is an example of a AgriProductType in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
  "type": "AgriProductType",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Soft Fruits",  
  "description": "Soft edible fruits",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:product1"  
    }  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_3128",  
  "category": ["cropVariety"],  
  "root": true,  
  "hasAgriProductTypeParent": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e",  
  "hasAgriProductTypeChildren": [  
    "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
    "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
    "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"  
  ]  
}  
```  
#### AgriProductType NGSI V2 normalized Example    
Here is an example of a AgriProductType in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
  "type": "AgriProductType",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Soft Fruits"  
  },  
  "description": {  
    "value": "Soft edible fruits"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:product1"  
      }  
    ]  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_3128"  
  },  
  "category": {  
    "value": ["cropVariety"]  
  },  
  "root": {  
    "value": true  
  },  
  "hasAgriProductTypeParent": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e"  
  },  
  "hasAgriProductTypeChildren": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
      "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
      "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"  
    ]  
  }  
}  
```  
#### AgriProductType NGSI-LD key-values Example    
Here is an example of a AgriProductType in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_3128",  
 "category": ["cropVariety"],  
 "createdAt": "2017-01-01T01:20:00Z",  
 "description": "Soft edible fruits",  
 "hasAgriProductTypeChildren": ["urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
                                "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
                                "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"],  
 "hasAgriProductTypeParent": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e",  
 "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
 "modifiedAt": "2017-05-04T12:30:00Z",  
 "name": "Soft Fruits",  
 "relatedSource": [{"application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                    "applicationEntityId": "app:product1"}],  
 "root": True,  
 "type": "AgriProductType"}  
```  
#### AgriProductType NGSI-LD normalized Example    
Here is an example of a AgriProductType in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
    "type": "AgriProductType",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "name": {  
        "type": "Property",  
        "value": "Soft Fruits"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Soft edible fruits"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:product1"  
            }  
        ]  
    },  
    "agroVocConcept": {  
        "type": "Property",  
        "value": "http://aims.fao.org/aos/agrovoc/c_3128"  
    },  
    "category": {  
        "type": "Property",  
        "value": ["cropVariety"]  
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
