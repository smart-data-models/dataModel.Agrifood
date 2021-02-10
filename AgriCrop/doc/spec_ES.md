Entidad: AgriCrop  
=================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriCrop/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un cultivo genérico. Esta entidad se asocia principalmente con las aplicaciones agrícolas verticales y las aplicaciones conexas de IO**.  

## Lista de propiedades  

- `agroVocConcept`: El vínculo con el concepto definido en el vocabulario del AgroVoc  - `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `harvestingInterval`: Una lista de las fechas de intervalo de cosecha recomendadas para este cultivo. Se especifica utilizando los intervalos de fechas repetidas de la norma ISO8601: <br/><br/>**intervalo, descripción**<br/><br/> Donde **intervalo** es en forma de **fecha de inicio/final**<br/><br/>--MMM-DD/--MMM-DD<br/><br/> Significa repetir cada año desde esta fecha de inicio hasta esta fecha final.  - `hasAgriFertiliser`: Referencia a los tipos de fertilizantes recomendados y adecuados para el cultivo de este cultivo.  - `hasAgriPest`: La referencia a las plagas que se sabe que atacan este cultivo  - `hasAgriSoil`: Referencia a los tipos de suelo recomendados y adecuados para el cultivo de este cultivo.  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `plantingFrom`: Una lista de la(s) fecha(s) de intervalo de plantación recomendada(s) para este cultivo. Se especifica utilizando los intervalos de fechas repetidas de la norma ISO8601: <br/><br/>**intervalo, descripción**<br/><br/> Donde **intervalo** es en forma de **fecha de inicio/final**<br/><br/>--MMM-DD/--MMM-DD<br/><br/> Significa repetir cada año desde esta fecha de inicio hasta esta fecha final.  - `relatedSource`: Lista de identificaciones que la entidad actual puede tener en aplicaciones externas  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser AgriCrop  - `wateringFrequency`: Una descripción del programa de riego recomendado. Una elección de una lista enumerada. Una de: **diario, semanal, quincenal, mensual, a pedido, otro**. Enum:'diario, semanal, quincenal, mensual, a demanda, otros'.    
Propiedades requeridas  
- `id`  - `name`  - `type`    
Esta entidad se asocia principalmente con las aplicaciones verticales agrícolas y las aplicaciones conexas de IO.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriCrop:    
  description: 'This entity contains a harmonised description of a generic crop. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
    agroVocConcept:    
      description: 'The link with the defined concept into the AgroVoc vocabulary'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
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
    harvestingInterval:    
      description: 'A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date.'    
      items:    
        - type: object    
          values:    
            dateRange:    
              pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$    
              type: string    
            description:    
              type: string    
      maxItems: 2    
      minItems: 2    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
    hasAgriFertiliser:    
      description: 'Reference to the recommended types of fertiliser suitable for growing this crop.'    
      items:    
        - anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasAgriPest:    
      description: 'Reference to the pests known to attack this crop'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    hasAgriSoil:    
      description: 'Reference to the recommended types of soil suitable for growing this crop.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    id:    
      anyOf: &agricrop_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agricrop_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    plantingFrom:    
      description: 'A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date.'    
      items:    
        - type: object    
          values:    
            dateRange:    
              pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$    
              type: string    
            description:    
              type: string    
      maxItems: 2    
      minItems: 2    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agricrop_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type. it has to be AgriCrop'    
      enum:    
        - AgriCrop    
      type: Property    
    wateringFrequency:    
      description: 'A description of the recommended watering schedule. A choice from an enumerated list. One of: **daily, weekly, biweekly, monthly, onDemand, other**. Enum:''daily, weekly, biweekly, monthly, onDemand,    other'''    
      enum:    
        - daily    
        - weekly    
        - biweekly    
        - monthly    
        - onDemand    
        - other    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
        units: ""    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de AgriCrop NGSI V2  
Aquí hay un ejemplo de un AgriCrop en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### AgriCrop NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un AgriCrop en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "value": "Wheat"  
  },  
  "alternateName": {  
    "value": "Triticum aestivum"  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/wheat",  
      "https://datamodel.org/example/wheat"  
    ]  
  },  
  "description": {  
    "value": "Spring wheat"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:weat"  
      }  
    ]  
  },  
  "hasAgriSoil": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ]  
  },  
  "hasAgriFertiliser": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "hasAgriPest": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "plantingFrom": {  
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
    "value": "daily"  
  }  
}  
```  
#### Ejemplo de valores clave de AgriCrop NGSI-LD  
Aquí hay un ejemplo de un AgriCrop en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
 "alternateName": "Triticum aestivum",  
 "createdAt": "2017-01-01T01:20:00Z",  
 "description": "Spring wheat",  
 "harvestingInterval": [{"dateRange": "-03-21/-04-01",  
                         "description": "Best Season"},  
                        {"dateRange": "-04-02/-04-15",  
                         "description": "Season OK"}],  
 "hasAgriFertiliser": ["urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
                       "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"],  
 "hasAgriPest": ["urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
                 "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"],  
 "hasAgriSoil": ["urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
                 "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"],  
 "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
 "modifiedAt": "2017-05-04T12:30:00Z",  
 "name": "Wheat",  
 "plantingFrom": [{"dateRange": "-09-28/-10-12", "description": "Best Season"},  
                  {"dateRange": "-10-11/-10-18", "description": "Season OK"}],  
 "relatedSource": [{"application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                    "applicationEntityId": "app:weat"}],  
 "seeAlso": ["https://example.org/concept/wheat",  
             "https://datamodel.org/example/wheat"],  
 "type": "AgriCrop",  
 "wateringFrequency": "daily"}  
```  
#### AgriCrop NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un AgriCrop en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriCrop",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "name": {  
        "type": "Property",  
        "value": "Wheat"  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Triticum aestivum"  
    },  
    "agroVocConcept": {  
        "type": "Property",  
        "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/wheat",  
            "https://datamodel.org/example/wheat"  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Spring wheat"  
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
