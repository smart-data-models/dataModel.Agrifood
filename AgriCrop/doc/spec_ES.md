<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: AgriCrop    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriCrop/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Esta entidad contiene una descripción armonizada de un cultivo genérico. Esta entidad se asocia principalmente con la vertical agrícola y las aplicaciones IoT relacionadas.**.    
versión: 0.0.4    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `agroVocConcept[uri]`: El enlace con el concepto definido en el vocabulario AgroVoc  . Model: [http://schema.org/URL](http://schema.org/URL)- `alternateName[string]`: Un nombre alternativo para este artículo  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `harvestingInterval[array]`: Lista de la(s) fecha(s) de intervalo de cosecha recomendada(s) para este cultivo. Se especifica utilizando intervalos de fechas de repetición ISO8601: <br/><br/>**intervalo, descripción**<br/><br/>Donde **intervalo** tiene la forma de **fecha de inicio/fecha de finalización**<br/><br/>--MM-DD/--MM-DD<br/><br/>Significa que se repite cada año desde esta fecha de inicio hasta esta fecha de finalización.  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasAgriFertiliser[array]`: Referencia a los tipos de abono recomendados para este cultivo  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasAgriPest[array]`: Referencia a las plagas que se sabe que atacan a este cultivo  . Model: [https://schema.org/URL](https://schema.org/URL)- `hasAgriSoil[array]`: Referencia a los tipos de suelo recomendados para este cultivo  . Model: [http://schema.org/URL](http://schema.org/URL)- `id[*]`: Identificador único de la entidad  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `plantingFrom[array]`: Lista de las fechas de intervalo de plantación recomendadas para este cultivo. Se especifica utilizando intervalos de fechas de repetición ISO8601: <br/><br/>**intervalo, descripción**<br/><br/>Donde **intervalo** tiene la forma de **fecha de inicio/fecha de finalización**<br/><br/>--MM-DD/--MM-DD<br/><br/>Significa que se repite cada año desde esta fecha de inicio hasta esta fecha de finalización.  . Model: [http://schema.org/URL](http://schema.org/URL)- `relatedSource[array]`: Lista de identificadores que la entidad actual puede tener en aplicaciones externas  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. tiene que ser AgriCrop  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Esta entidad está asociada principalmente con el vertical agrícola y las aplicaciones IoT relacionadas.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AgriCrop:      
  description: This entity contains a harmonised description of a generic crop. This entity is primarily associated with the agricultural vertical and related IoT applications.      
  properties:      
    agroVocConcept:      
      description: The link with the defined concept into the AgroVoc vocabulary      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Property      
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
    harvestingInterval:      
      description: 'A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date'      
      items:      
        properties:      
          dateRange:      
            pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$      
            type: string      
          description:      
            type: string      
        type: object      
      maxItems: 2      
      minItems: 2      
      type: array      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Property      
    hasAgriFertiliser:      
      description: Reference to the recommended types of fertiliser suitable for growing this crop      
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
      type: array      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    hasAgriPest:      
      description: Reference to the pests known to attack this crop      
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
      type: array      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    hasAgriSoil:      
      description: Reference to the recommended types of soil suitable for growing this crop      
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
      type: array      
      x-ngsi:      
        model: http://schema.org/URL      
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
    name:      
      description: The name of this item      
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
    plantingFrom:      
      description: 'A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date'      
      items:      
        properties:      
          dateRange:      
            pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$      
            type: string      
          description:      
            type: string      
        type: object      
      maxItems: 2      
      minItems: 2      
      type: array      
      x-ngsi:      
        model: http://schema.org/URL      
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
    type:      
      description: NGSI Entity Type. it has to be AgriCrop      
      enum:      
        - AgriCrop      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - name      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriCrop/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriCrop/schema.json      
  x-model-tags: ""      
  x-version: 0.0.4      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### AgriCrop NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un AgriCrop en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Wheat",  
  "alternateName": "Triticum aestivum",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "seeAlso": [  
    "https://example.org/concept/wheat",  
    "https://datamodel.org/example/wheat"  
  ],  
  "description": "Spring wheat",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:weat"  
    }  
  ],  
  "hasAgriSoil": [  
    "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
    "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
  ],  
  "hasAgriFertiliser": [  
    "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriPest": [  
    "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "plantingFrom": [  
    {  
      "dateRange": "-09-28/-10-12",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-10-11/-10-18",  
      "description": "Season OK"  
    }  
  ],  
  "harvestingInterval": [  
    {  
      "dateRange": "-03-21/-04-01",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-04-02/-04-15",  
      "description": "Season OK"  
    }  
  ],  
  "wateringFrequency": "daily"  
}  
```  
</details>    
#### AgriCrop NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un AgriCrop en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Wheat"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Triticum aestivum"  
  },  
  "agroVocConcept": {  
    "type": "Text",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "https://example.org/concept/wheat",  
      "https://datamodel.org/example/wheat"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "Spring wheat"  
  },  
  "relatedSource": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:weat"  
      }  
    ]  
  },  
  "hasAgriSoil": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ]  
  },  
  "hasAgriFertiliser": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "hasAgriPest": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "plantingFrom": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "daily"  
  }  
}  
```  
</details>    
#### AgriCrop NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un AgriCrop en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "alternateName": "Triticum aestivum",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Spring wheat",  
  "harvestingInterval": [  
    {  
      "dateRange": "-03-21/-04-01",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-04-02/-04-15",  
      "description": "Season OK"  
    }  
  ],  
  "hasAgriFertiliser": [  
    "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriPest": [  
    "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriSoil": [  
    "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
    "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
  ],  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Wheat",  
  "plantingFrom": [  
    {  
      "dateRange": "-09-28/-10-12",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-10-11/-10-18",  
      "description": "Season OK"  
    }  
  ],  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:weat"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/wheat",  
    "https://datamodel.org/example/wheat"  
  ],  
  "wateringFrequency": "daily",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AgriCrop NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un AgriCrop en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "agroVocConcept": {  
    "type": "Property",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Triticum aestivum"  
  },  
  "createdAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-01-01T01:20:00Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Spring wheat"  
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
  "hasAgriSoil": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ]  
  },  
  "modifiedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-05-04T12:30:00Z"  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Wheat"  
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
  "relatedSource": {  
    "type": "Property",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:weat"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "https://example.org/concept/wheat",  
      "https://datamodel.org/example/wheat"  
    ]  
  },  
  "wateringFrequency": {  
    "type": "Property",  
    "value": "daily"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
