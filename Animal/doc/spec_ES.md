Entidad: Animal  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Animal/LICENSE.md)  
Descripción global: **Una observación de las condiciones de los animales en un determinado lugar y momento. Este modelo de datos ha sido desarrollado para el IoF2020 UC ShareBeef por UCO y SensoWave.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `birthdate`: Fecha de nacimiento del animal  - `breed`: La raza del animal  - `calvedBy`: Madre del animal  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `fedWith`: El alimento utilizado para el animal  - `healthCondition`: Condición fenológica del animal. Enum:' sano, enfermo, enTratamiento'  - `id`: Identificador único de la entidad  - `legalId`: Identificación legal del animal  - `locatedAt`: Id de la relación de AgriParcel  - `location`:   - `name`: El nombre de este artículo.  - `ownedBy`: El dueño del animal  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `phenologicalCondition`: Condición fenológica del animal. Enum:'lactanteBebé, pastoreoBebé, machoAdulto, hembraAdulto, machoJoven, hembraJoven'.  - `relatedSource`: Lista de identificaciones que la entidad actual puede tener en aplicaciones externas  - `reproductiveCondition`: Condición reproductiva del animal. Enum:'noStatus, inactivo, inCalf, inHeat, activo'.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `sex`: Sexo del animal. Enum:'macho, hembra'.  - `siredBy`: Padre del animal  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `species`: Especie a la que pertenece el animal. Esta lista puede ser aumentada  - `type`: Tipo de entidad NGSI: Tiene que ser un animal  - `weight`: El peso del animal como un número  - `welfareCondition`: Indicador del bienestar de los animales. Enum:'asunto, adecuado'.    
Propiedades requeridas  
- `id`  - `legalId`  - `sex`  - `species`  - `type`    
El modelo de datos animales propuesto se ha hecho desde un punto de vista más general, tratando de ajustarlo a la información procedente de los dispositivos y sensores utilizados en la UC. El siguiente diagrama describe la cadena de la carne de vacuno. En este diagrama se describen los diferentes actores de la cadena cárnica, así como algunas de sus interacciones. ![ ](../recursos/diagrama1.jpg). Durante el uso de este modelo de datos será necesario definir varias entidades para manejar la información generada en la solución propuesta. Dentro de todas estas entidades, la entidad animal que es el centro de la solución se destaca en primer lugar  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Animal:    
  description: 'An observation of animal conditions at a certain place and time. This data model has been developed for the IoF2020 UC ShareBeef by UCO and SensoWave.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    birthdate:    
      description: 'Animal''s birthdate'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    breed:    
      description: 'Breed of the animal'    
      type: Property    
    calvedBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Mother of the animal'    
      type: Relationship    
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
    fedWith:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Food used for the animal'    
      type: Relationship    
    healthCondition:    
      description: 'Phenological condition of the animal. Enum:'' healthy, sick, inTreatment'''    
      enum:    
        - healthy    
        - sick    
        - inTreatment    
      type: Property    
    id:    
      anyOf: &animal_-_properties_-_owner_-_items_-_anyof    
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
    legalId:    
      description: 'Legal ID of the animal'    
      type: Property    
    locatedAt:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Id of the AgriParcel relationship'    
      type: Relationship    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    ownedBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The owner of the animal'    
      type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *animal_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    phenologicalCondition:    
      description: 'Phenological condition of the animal. Enum:''lactatingBaby, grazingBaby, maleAdult, femaleAdult, maleYoung, femaleYoung''.'    
      enum:    
        - lactatingBaby    
        - grazingBaby    
        - maleAdult    
        - femaleAdult    
        - maleYoung    
        - femaleYoung    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *animal_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: Property    
    reproductiveCondition:    
      description: 'Reproductive condition of the animal. Enum:''noStatus, inactive, inCalf, inHeat, active'''    
      enum:    
        - noStatus    
        - inactive    
        - inCalf    
        - inHeat    
        - active    
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
    sex:    
      description: 'Sex of the animal. Enum:''male, female'''    
      enum:    
        - male    
        - female    
      type: Property    
    siredBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Father of the animal'    
      type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    species:    
      description: 'Species to which the animal belongs. This enum can be increased'    
      enum:    
        - cow    
        - goat    
        - horse    
        - pig    
        - sheep    
        - 'dairy cattle'    
        - 'beef cattle'    
      type: Property    
      x-ngsi:    
        model: 'Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text'    
    type:    
      description: 'NGSI Entity Type: It has to be Animal'    
      enum:    
        - Animal    
      type: Property    
    weight:    
      description: 'The weight of the animal as a number'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/Number    
        units: kg    
    welfareCondition:    
      description: 'Indicator of the animal welfare. Enum:''issue, adequate'''    
      enum:    
        - issue    
        - adequate    
      type: Property    
  required:    
    - id    
    - type    
    - species    
    - legalId    
    - sex    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de NGSI V2 de los animales  
Aquí hay un ejemplo de un animal en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "species": "sheep",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:sheep1"  
    }  
  ],  
  "legalId": "ES142589652140",  
  "birthdate": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "sex": "female",  
  "breed": "Merina",  
  "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "location": {  
    "type": "Point",  
    "coordinates": [-4.754444444, 41.640833333]  
  },  
  "weight": 65.3,  
  "ownedBy": "http://person.org/leon",  
  "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "phenologicalCondition": "maleAdult",  
  "reproductiveCondition": "inCalf",  
  "healthCondition": "healthy",  
  "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
  "welfareCondition": "adequate"  
}  
```  
#### Ejemplo normalizado de NGSI V2 de animales  
Aquí hay un ejemplo de un animal en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "species": {  
    "value": "sheep"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:sheep1"  
      }  
    ]  
  },  
  "legalId": {  
    "value": "ES142589652140"  
  },  
  "birthdate": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "sex": {  
    "value": "female"  
  },  
  "breed": {  
    "value": "Merina"  
  },  
  "calvedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "siredBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.754444444, 41.640833333]  
    }  
  },  
  "weight": {  
    "value": 65.3  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "value": "http://person.org/leon"  
  },  
  "locatedAt": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
  },  
  "phenologicalCondition": {  
    "value": "adult"  
  },  
  "reproductiveCondition": {  
    "value": "inCalf"  
  },  
  "healthCondition": {  
    "value": "healthy"  
  },  
  "fedWith": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081"  
  },  
  "welfareCondition": {  
    "value": "adequate"  
  }  
}  
```  
#### Ejemplo de valores clave NGSI-LD de animales  
Aquí hay un ejemplo de un animal en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "birthdate": {"@type": "DateTime", "@value": "2017-01-01T01:20:00Z"},  
 "breed": "Merina",  
 "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
 "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
 "healthCondition": "healthy",  
 "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
 "legalId": "ES142589652140",  
 "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
 "location": {"coordinates": [-4.754444444, 41.640833333], "type": "Point"},  
 "modifiedAt": "2017-05-04T12:30:00Z",  
 "ownedBy": "http://person.org/leon",  
 "phenologicalCondition": "adult",  
 "relatedSource": [{"application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                    "applicationEntityId": "app:sheep1"}],  
 "reproductiveCondition": "inCalf",  
 "sex": "female",  
 "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
 "species": "sheep",  
 "type": "Animal",  
 "weight": 65.3,  
 "welfareCondition": "adequate"}  
```  
#### Ejemplo normalizado de NGSI-LD de animales  
Aquí hay un ejemplo de un animal en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "type": "Animal",  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "species": {  
        "type": "Property",  
        "value": "sheep"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:sheep1"  
            }  
        ]  
    },  
    "legalId": {  
        "type": "Property",  
        "value": "ES142589652140"  
    },  
    "birthdate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-01-01T01:20:00Z"  
        }  
    },  
    "sex": {  
        "type": "Property",  
        "value": "female"  
    },  
    "breed": {  
        "type": "Property",  
        "value": "Merina"  
    },  
    "calvedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
    },  
    "siredBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.754444444,  
                41.640833333  
            ]  
        }  
    },  
    "weight": {  
        "type": "Property",  
        "value": 65.3  
    },  
    "ownedBy": {  
        "type": "Relationship",  
        "object": "http://person.org/leon"  
    },  
    "locatedAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
    },  
    "phenologicalCondition": {  
        "type": "Property",  
        "value": "adult"  
    },  
    "reproductiveCondition": {  
        "type": "Property",  
        "value": "inCalf"  
    },  
    "healthCondition": {  
        "type": "Property",  
        "value": "healthy"  
    },  
    "fedWith": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081"  
    },  
    "welfareCondition": {  
        "type": "Property",  
        "value": "adequate"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
