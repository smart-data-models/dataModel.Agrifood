Entité : Animal  
===============  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Une observation des conditions des animaux à un certain endroit et à un certain moment. Ce modèle de données a été développé pour l'IoF2020 UC ShareBeef par UCO et SensoWave.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `birthdate`: Date de naissance de l'animal  - `breed`: Race de l'animal  - `calvedBy`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `fedWith`:   - `healthCondition`: État phénologique de l'animal  - `id`:   - `legalId`: Identification légale de l'animal  - `locatedAt`:   - `location`:   - `name`: Le nom de cet article.  - `ownedBy`:   - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `phenologicalCondition`: État phénologique de l'animal  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans les applications externes  - `reproductiveCondition`: État reproducteur de l'animal  - `seeAlso`:   - `sex`: Sexe de l'animal  - `siredBy`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `species`: Espèce à laquelle l'animal appartient  - `type`: Type d'entité NGSI  - `weight`:   - `welfareCondition`: Indicateur du bien-être des animaux  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
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
</details>    
## Exemples de charges utiles  
#### Valeurs clés de l'INSG V2 pour les animaux Exemple  
Voici un exemple d'un animal au format JSON comme valeurs clés. Ce format est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### Exemple de normalisation du NGSI V2 pour les animaux  
Voici un exemple d'un animal au format JSON tel que normalisé. Il est compatible avec la version 2 du NGSI lorsque l'on utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### Valeurs clés de l'INSMT-LD pour les animaux Exemple  
Voici un exemple d'un animal au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Exemple de normalisation de l'INSG-LD pour les animaux  
Voici un exemple d'un animal au format JSON-LD tel que normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
