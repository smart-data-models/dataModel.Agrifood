Entidad: AgriParcelOperation  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad contiene una descripción armonizada de una operación genérica realizada en una parcela. Esta entidad está asociada principalmente a las aplicaciones verticales agrícolas y a las aplicaciones IoT relacionadas.**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `endedAt`: Marca de tiempo cuando la operación realmente terminó.  - `hasAgriParcel`: Referencia a la parcela agrícola  - `hasAgriProductType`: Referencia al AgriProductType utilizado/aplicado.  - `hasOperator`: Referencia al operador que realiza la operación  - `id`: Identificador único de la entidad  - `irrigationRecord`: Relación con el registro de riego de la ejecución  - `name`: El nombre de este artículo.  - `operationType`: Una elección de una lista enumerada que describe la operación realizada en la parcela. Enum:'abono, inspección, plaguicida, agua, otros'  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `plannedEndAt`: La fecha/hora de finalización prevista para la operación. <br/><br/>Tenga en cuenta que esto es consultivo y que la hora real de finalización de la operación puede ser anterior o posterior a la fecha de finalización prevista.  - `plannedStartAt`: La fecha/hora de inicio prevista para la operación. Tenga en cuenta que se trata de un aviso y que la hora real de inicio de la operación puede ser anterior o posterior al inicio previsto  - `quantity`: La cantidad total de agua o producto utilizado/ aplicado. Se recomienda medirla en litros para los líquidos o en kilogramos para los sólidos.  - `relatedSource`: Lista de identificadores que la entidad actual puede tener en aplicaciones externas  - `reportedAt`: Marca de tiempo cuando se reportó la falla del evento.  - `result`: Una descripción de los resultados de la operación. Enum:'ok, aborted, failed'  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startedAt`: Marca de tiempo cuando la operación comenzó a realizarse.  - `status`: Una elección de una lista enumerada que describe el estado. Enum:'planeado, en curso, terminado, programado, cancelado'  - `type`: Tipo de entidad NGSI. Debe ser AgriParcelOperation  - `waterSource`: Enum:'pozo, precipitación, río, captación de agua de lluvia, presa de agua, suministro comercial'.  - `workOrder`: Relación con la orden de trabajo para la ejecución  - `workRecord`: Relación con el expediente de trabajo de la ejecución    
Propiedades requeridas  
- `hasAgriParcel`  - `id`  - `plannedEndAt`  - `plannedStartAt`  - `type`    
Esta entidad está asociada principalmente con el vertical agrícola y las aplicaciones de IoT relacionadas.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriParcelOperation:    
  description: 'This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    endedAt:    
      description: 'Timestamp when the operation actually finished.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    hasAgriParcel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the AgriParcel'    
      x-ngsi:    
        type: Relationship    
    hasAgriProductType:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the AgriProductType used/ applied.'    
      x-ngsi:    
        type: Relationship    
    hasOperator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the operator conducting the operation'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &agriparceloperation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    irrigationRecord:    
      description: 'Relationship with the irrigation record of the execution'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    name:    
      description: 'The name of this item.'    
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
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agriparceloperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plannedEndAt:    
      description: 'The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    plannedStartAt:    
      description: 'The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    quantity:    
      description: 'The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agriparceloperation_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: array    
      x-ngsi:    
        type: Property    
    reportedAt:    
      description: 'Timestamp when the event fault was reported.'    
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
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startedAt:    
      description: 'Timestamp when the operation actually started to be performed.'    
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
      description: 'NGSI Entity Type. It has to be AgriParcelOperation'    
      enum:    
        - AgriParcelOperation    
      type: string    
      x-ngsi:    
        type: Property    
    waterSource:    
      description: 'Enum:''borehole, rainfall, river, rainwater capture, water dam, commercial supply''.'    
      enum:    
        - borehole    
        - rainfall    
        - river    
        - 'rainwater capture'    
        - 'water dam'    
        - 'commercial supply'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    workOrder:    
      description: 'Relationship with the workorder for the execution'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    workRecord:    
      description: 'Relationship with the work record of the execution'    
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
```  
</details>    
## Ejemplo de carga útil  
#### AgriParcelOperation NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una AgriParcelOperation en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### AgriParcelOperation NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una AgriParcelOperation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelop1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/agriparcelop",  
      "https://datamodel.org/example/agriparcelop"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
  },  
  "operationType": {  
    "value": "fertiliser"  
  },  
  "description": {  
    "value": "Monthly fertiliser application"  
  },  
  "result": {  
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
    "value": "finished"  
  },  
  "hasOperator": {  
    "type": "Relationship",  
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
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
  },  
  "quantity": {  
    "value": 40  
  },  
  "waterSource": {  
    "value": "rainwater capture"  
  },  
  "workOrder": {  
    "type": "URL",  
    "value": "https://example.com/agriparcelrecords/workorder1"  
  },  
  "workRecord": {  
    "type": "URL",  
    "value": "https://example.com/agriparcelrecords/workrecord1"  
  },  
  "irrigationRecord": {  
    "type": "URL",  
    "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
  }  
}  
```  
#### AgriParcelOperation NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una AgriParcelOperation en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Monthly fertiliser application",  
  "endedAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "operationType": "fertiliser",  
  "plannedEndAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "plannedStartAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "quantity": 40,  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "reportedAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "result": "ok",  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "startedAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "status": "finished",  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### AgriParcelOperation NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una AgriParcelOperation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "relatedSource": {  
    "type": "Property",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelop1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "https://example.org/concept/agriparcelop",  
      "https://datamodel.org/example/agriparcelop"  
    ]  
  },  
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
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "plannedEndAt": {  
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
  "hasOperator": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "reportedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
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
  },  
  "workOrder": {  
    "type": "Property",  
    "value": "https://example.com/agriparcelrecords/workorder1"  
  },  
  "workRecord": {  
    "type": "Property",  
    "value": "https://example.com/agriparcelrecords/workrecord1"  
  },  
  "irrigationRecord": {  
    "type": "Property",  
    "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
  },  
    "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
