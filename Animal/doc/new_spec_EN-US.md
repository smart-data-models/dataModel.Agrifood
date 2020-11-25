Entity: Animal  
==============  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **An observation of animal conditions at a certain place and time. This data model has been developed for the IoF2020 UC ShareBeef by UCO and SensoWave.**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided.  - `birthdate`: Animal’s birthdate  - `breed`: Breed of the animal  - `calvedBy`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `fedWith`:   - `healthCondition`: Phenological condition of the animal  - `id`:   - `legalId`: Legal ID of the animal  - `locatedAt`:   - `location`:   - `name`: The name of this item.  - `ownedBy`:   - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `phenologicalCondition`: Phenological condition of the animal  - `relatedSource`: List of IDs the current entity may have in external applications  - `reproductiveCondition`: Reproductive condition of the animal  - `seeAlso`:   - `sex`: Sex of the animal  - `siredBy`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `species`: Species to which the animal belongs  - `type`: NGSI Entity Type  - `weight`:   - `welfareCondition`: Indicator of the animal welfare  ## Data Model description of properties  
Sorted alphabetically  
```yaml  
Animal:    
  description: 'An observation of animal conditions at a certain place and time. This data model has been developed for the IoF2020 UC ShareBeef by UCO and SensoWave.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    birthdate:    
      description: 'Animal’s birthdate'    
      format: date-time    
      type: string    
    breed:    
      description: 'Breed of the animal'    
      type: string    
    calvedBy:    
      anyOf: &animal_-_properties_-_fedwith_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
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
      anyOf: *animal_-_properties_-_fedwith_-_anyof    
    healthCondition:    
      description: 'Phenological condition of the animal'    
      enum:    
        - healthy    
        - sick    
        - inTreatment    
      type: string    
    id:    
      anyOf: *animal_-_properties_-_fedwith_-_anyof    
    legalId:    
      description: 'Legal ID of the animal'    
      type: string    
    locatedAt:    
      anyOf: *animal_-_properties_-_fedwith_-_anyof    
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
      anyOf: *animal_-_properties_-_fedwith_-_anyof    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *animal_-_properties_-_fedwith_-_anyof    
      type: Property    
    phenologicalCondition:    
      description: 'Phenological condition of the animal'    
      enum:    
        - lactatingBaby    
        - grazingBaby    
        - maleAdult    
        - femaleAdult    
        - maleYoung    
        - femaleYoung    
      type: string    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *animal_-_properties_-_fedwith_-_anyof    
            applicationEntityId:    
              type: string    
      type: Property    
    reproductiveCondition:    
      description: 'Reproductive condition of the animal'    
      enum:    
        - noStatus    
        - inactive    
        - inCalf    
        - inHeat    
        - active    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    sex:    
      description: 'Sex of the animal'    
      enum:    
        - male    
        - female    
      type: string    
    siredBy:    
      anyOf: *animal_-_properties_-_fedwith_-_anyof    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    species:    
      description: 'Species to which the animal belongs'    
      enum:    
        - cow    
        - goat    
        - horse    
        - pig    
        - sheep    
      type: string    
    type:    
      description: 'NGSI Entity Type'    
      enum:    
        - Animal    
      type: string    
    weight:    
      type: number    
    welfareCondition:    
      description: 'Indicator of the animal welfare'    
      enum:    
        - issue    
        - adequate    
      type: string    
  required:    
    - id    
    - type    
    - species    
    - legalId    
    - sex    
  type: object    
```  
#### Animal NGSI V2 key-values Example    
Here is an example of a Animal in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Animal NGSI V2 normalized Example    
Here is an example of a Animal in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Animal NGSI-LD key-values Example    
Here is an example of a Animal in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
#### Animal NGSI-LD normalized Example    
Here is an example of a Animal in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
