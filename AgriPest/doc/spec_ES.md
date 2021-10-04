Entidad: AgriPest  
=================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriPest/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad contiene una descripción armonizada de una plaga agrícola. **  

## Lista de propiedades  

- `agroVocConcept`: Referencia al término agrovoc asociado a este artículo  - `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `hasAgriProductType`: Referencia a los tipos de productos recomendados que pueden utilizarse para tratar esta plaga.  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `relatedSource`: Lista de identificadores que la entidad actual puede tener en aplicaciones externas  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI: Tiene que ser AgriPest    
Propiedades requeridas  
- `id`  - `name`  - `type`    
Esta entidad está asociada principalmente con el vertical agrícola y las aplicaciones de IoT relacionadas.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriPest:    
  description: 'This entity contains a harmonised description of an agricultural pest. '    
  properties:    
    agroVocConcept:    
      description: 'Reference to the agrovoc term associated with this item'    
      format: uri    
      type: Relationship    
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
    hasAgriProductType:    
      description: 'Reference to the recommended types of product that can be used to treat this pest.'    
      items:    
        - anyOf: &agripest_-_properties_-_id_-_anyof    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
          description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    id:    
      anyOf: *agripest_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agripest_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agripest_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be AgriPest'    
      enum:    
        - AgriPest    
      type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### Ejemplo de valores clave de AgriPest NGSI-v2  
Aquí hay un ejemplo de un AgriPest en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "type": "AgriPest",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Grasshopper",  
  "alternateName": "Chorthippus parallelus",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:pest1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/pest",  
    "https://datamodel.org/example/pest"  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_31924",  
  "description": "Common European grasshopper",  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
    "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
    "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
  ]  
}  
```  
#### AgriPest NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un AgriPest en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "type": "AgriPest",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Grasshopper"  
  },  
  "alternateName": {  
    "value": "Chorthippus parallelus"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:pest1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/pest",  
      "https://datamodel.org/example/pest"  
    ]  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_31924"  
  },  
  "description": {  
    "value": "Common European grasshopper"  
  },  
  "hasAgriProductType": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
      "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
      "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
    ]  
  }  
}  
```  
#### AgriPest NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un AgriPest en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "type": "AgriPest",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": {  
    "type": "Property",  
    "value": "Grasshopper"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Chorthippus parallelus"  
  },  
  "relatedSource": {  
    "type": "Property",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:farm1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "https://example.org/concept/pest",  
      "https://datamodel.org/example/pest"  
    ]  
  },  
  "agroVocConcept": {  
    "type": "Property",  
    "value": "http://aims.fao.org/aos/agrovoc/c_31924"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Common European grasshopper"  
  },  
  "hasAgriProductType": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
      "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
      "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
    ]  
  }  
}  
```  
#### AgriPest NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una AgriPest en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_31924",  
  "alternateName": "Chorthippus parallelus",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Common European grasshopper",  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
    "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
    "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
  ],  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Grasshopper",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:farm1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/pest",  
    "https://datamodel.org/example/pest"  
  ],  
  "type": "AgriPest"  
}  
```  
