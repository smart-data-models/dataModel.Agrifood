<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: AgriParcelOperation    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.**    
version: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `alternateName[string]`: An alternative name for this item  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `endedAt[date-time]`: Timestamp when the operation actually finished  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `hasAgriParcel[*]`: Reference to the AgriParcel  - `hasAgriProductType[*]`: Reference to the AgriProductType used/applied  - `hasOperator[*]`: Reference to the operator conducting the operation  - `id[*]`: Unique identifier of the entity  - `irrigationRecord[uri]`: Relationship with the irrigation record of the execution  . Model: [http://schema.org/URL](http://schema.org/URL)- `name[string]`: The name of this item  - `operationType[string]`: A choice from an enumerated list describing the operation performed on the parcel. Enum:'fertiliser, inspection, pesticide, water, other'  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `plannedEndAt[date-time]`: The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `plannedStartAt[date-time]`: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `quantity[number]`: The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids  . Model: [http://schema.org/Number](http://schema.org/Number)- `relatedSource[array]`: List of IDs the current entity may have in external applications  - `reportedAt[date-time]`: Timestamp when the event fault was reported  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `result[string]`: A description of the results of the operation. Enum:'ok, aborted, failed'  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `startedAt[date-time]`: Timestamp when the operation actually started to be performed  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `status[string]`: A choice from an enumerated list describing the status. Enum:'planned, ongoing, finished, scheduled, cancelled'  - `type[string]`: NGSI Entity Type. It has to be AgriParcelOperation  - `waterSource[string]`: Type of water sources. Enum:'borehole, rainfall, river, rainwater capture, water dam, commercial supply'  . Model: [http://schema.org/Text](http://schema.org/Text)- `workOrder[uri]`: Relationship with the workorder for the execution  . Model: [http://schema.org/URL](http://schema.org/URL)- `workRecord[uri]`: Relationship with the work record of the execution  . Model: [http://schema.org/URL](http://schema.org/URL)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `hasAgriParcel`  - `id`  - `plannedEndAt`  - `plannedStartAt`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
This entity is primarily associated with the agricultural vertical and related IoT applications.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AgriParcelOperation:      
  description: This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    endedAt:      
      description: Timestamp when the operation actually finished      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    hasAgriParcel:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Reference to the AgriParcel      
      x-ngsi:      
        type: Relationship      
    hasAgriProductType:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Reference to the AgriProductType used/applied      
      x-ngsi:      
        type: Relationship      
    hasOperator:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Reference to the operator conducting the operation      
      x-ngsi:      
        type: Relationship      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    irrigationRecord:      
      description: Relationship with the irrigation record of the execution      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationType:      
      description: 'A choice from an enumerated list describing the operation performed on the parcel. Enum:''fertiliser, inspection, pesticide, water, other'''      
      enum:      
        - fertiliser      
        - inspection      
        - pesticide      
        - water      
        - other      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    plannedEndAt:      
      description: The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    plannedStartAt:      
      description: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    quantity:      
      description: The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    relatedSource:      
      description: List of IDs the current entity may have in external applications      
      items:      
        properties:      
          application:      
            anyOf:      
              - description: Identifier format of any NGSI entity      
                maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
                x-ngsi:      
                  type: Property      
              - description: Identifier format of any NGSI entity      
                format: uri      
                type: string      
                x-ngsi:      
                  type: Property      
            description: Unique identifier of the entity      
            x-ngsi:      
              type: Property      
          applicationEntityId:      
            description: Identifier in the external application      
            type: string      
            x-ngsi:      
              type: Property      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    reportedAt:      
      description: Timestamp when the event fault was reported      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    result:      
      description: 'A description of the results of the operation. Enum:''ok, aborted, failed'''      
      enum:      
        - ok      
        - aborted      
        - failed      
      type: string      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startedAt:      
      description: Timestamp when the operation actually started to be performed      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    status:      
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''      
      enum:      
        - planned      
        - ongoing      
        - finished      
        - scheduled      
        - cancelled      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity Type. It has to be AgriParcelOperation      
      enum:      
        - AgriParcelOperation      
      type: string      
      x-ngsi:      
        type: Property      
    waterSource:      
      description: 'Type of water sources. Enum:''borehole, rainfall, river, rainwater capture, water dam, commercial supply'''      
      enum:      
        - borehole      
        - rainfall      
        - river      
        - rainwater capture      
        - water dam      
        - commercial supply      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    workOrder:      
      description: Relationship with the workorder for the execution      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    workRecord:      
      description: Relationship with the work record of the execution      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
  required:      
    - id      
    - type      
    - hasAgriParcel      
    - plannedStartAt      
    - plannedEndAt      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriParcelOperation/schema.json      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### AgriParcelOperation NGSI-v2 key-values Example      
Here is an example of a AgriParcelOperation in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "operationType": "fertiliser",  
  "description": "Monthly fertiliser application",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "finished",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "quantity": 40,  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1"  
}  
```  
</details>    
#### AgriParcelOperation NGSI-v2 normalized Example      
Here is an example of a AgriParcelOperation in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "relatedSource": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelop1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "https://example.org/concept/agriparcelop",  
      "https://datamodel.org/example/agriparcelop"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "fertiliser"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Monthly fertiliser application"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "type": "Text",  
    "value": "finished"  
  },  
  "hasOperator": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "reportedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "hasAgriProductType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
  },  
  "quantity": {  
    "type": "Number",  
    "value": 40  
  },  
  "waterSource": {  
    "type": "Text",  
    "value": "rainwater capture"  
  },  
  "workOrder": {  
    "type": "Text",  
    "value": "https://example.com/agriparcelrecords/workorder1"  
  },  
  "workRecord": {  
    "type": "Text",  
    "value": "https://example.com/agriparcelrecords/workrecord1"  
  },  
  "irrigationRecord": {  
    "type": "Text",  
    "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
  }  
}  
```  
</details>    
#### AgriParcelOperation NGSI-LD key-values Example      
Here is an example of a AgriParcelOperation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Monthly fertiliser application",  
  "endedAt": "2016-08-22T10:18:16Z",  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "operationType": "fertiliser",  
  "plannedEndAt": "2016-08-22T10:18:16Z",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "quantity": 40,  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "reportedAt": "2016-08-22T10:18:16Z",  
  "result": "ok",  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "startedAt": "2016-08-22T10:18:16Z",  
  "status": "finished",  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AgriParcelOperation NGSI-LD normalized Example      
Here is an example of a AgriParcelOperation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
    "type": "AgriParcelOperation",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Monthly fertiliser application"  
    },  
    "endedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "hasAgriParcel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
    },  
    "hasAgriProductType": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
    },  
    "hasOperator": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
    },  
    "irrigationRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "operationType": {  
        "type": "Property",  
        "value": "fertiliser"  
    },  
    "plannedEndAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "plannedStartAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "quantity": {  
        "type": "Property",  
        "value": 40,  
        "unitCode": "KGM"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:parcelop1"  
            }  
        ]  
    },  
    "reportedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "result": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agriparcelop",  
            "https://datamodel.org/example/agriparcelop"  
        ]  
    },  
    "startedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "status": {  
        "type": "Property",  
        "value": "finished"  
    },  
    "waterSource": {  
        "type": "Property",  
        "value": "rainwater capture"  
    },  
    "workOrder": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/workorder1"  
    },  
    "workRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/workrecord1"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
