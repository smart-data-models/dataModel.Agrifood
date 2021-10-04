Entité : Animal  
===============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Animal/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Observation des conditions d'un animal à un endroit et à un moment donnés. Ce modèle de données a été développé pour le projet IoF2020 UC ShareBeef par UCO et SensoWave.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `birthdate`: Date de naissance de l'animal  - `breed`: Race de l'animal  - `calvedBy`: Mère de l'animal  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `fedWith`: Nourriture utilisée pour l'animal  - `healthCondition`: État phénologique de l'animal. Enum:' healthy, sick, inTreatment' (sain, malade, en traitement)  - `id`: Identifiant unique de l'entité  - `legalId`: Identification légale de l'animal  - `locatedAt`: Id de la relation AgriParcel  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `ownedBy`: Le propriétaire de l'animal  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `phenologicalCondition`: Condition phénologique de l'animal. Enum : 'lactatingBaby, grazingBaby, maleAdult, femaleAdult, maleYoung, femaleYoung'.  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans des applications externes  - `reproductiveCondition`: État reproductif de l'animal. Enum : 'noStatus, inactive, inCalf, inHeat, active'.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `sex`: Sexe de l'animal. Enum : "mâle, femelle  - `siredBy`: Père de l'animal  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `species`: Espèce à laquelle appartient l'animal. Cet enum peut être augmenté  - `type`: Type d'entité NGSI : Il doit s'agir d'un animal  - `weight`: Le poids de l'animal en chiffre  - `welfareCondition`: Indicateur du bien-être animal. Enum : "problème, adéquat    
Propriétés requises  
- `id`  - `legalId`  - `sex`  - `species`  - `type`    
Le modèle de données animales proposé a été élaboré d'un point de vue plus général, en essayant de l'adapter aux informations provenant des dispositifs et des capteurs utilisés dans l'UC. Le diagramme suivant décrit la chaîne de la viande bovine. Dans ce diagramme, les différents acteurs de la chaîne de la viande sont décrits ainsi que certaines de leurs interactions. ![ ](../resources/diagram1.jpg). Lors de l'utilisation de ce modèle de données, il sera nécessaire de définir plusieurs entités pour traiter les informations générées par la solution proposée. Parmi toutes ces entités, l'entité animal qui est le centre de la solution se distingue en premier lieu  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Animal:    
  description: 'An observation of animal conditions at a certain place and time. This data model has been developed for the IoF2020 UC ShareBeef by UCO and SensoWave.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      type: Geoproperty    
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
            format: uri    
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
## Exemples de charges utiles  
#### Valeurs-clés NGSI-v2 pour animaux Exemple  
Voici un exemple d'animal au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Animal NGSI-v2 normalisé Exemple  
Voici un exemple d'un animal au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Valeurs-clés NGSI-LD pour animaux Exemple  
Voici un exemple d'animal au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Animal NGSI-LD normalisé Exemple  
Voici un exemple d'un animal au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "birthdate": {  
    "@type": "DateTime",  
    "@value": "2017-01-01T01:20:00Z"  
  },  
  "breed": "Merina",  
  "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
  "healthCondition": "healthy",  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "legalId": "ES142589652140",  
  "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "location": {  
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ],  
    "type": "Point"  
  },  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "ownedBy": "http://person.org/leon",  
  "phenologicalCondition": "adult",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:sheep1"  
    }  
  ],  
  "reproductiveCondition": "inCalf",  
  "sex": "female",  
  "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "species": "sheep",  
  "type": "Animal",  
  "weight": 65.3,  
  "welfareCondition": "adequate"  
}  
```  
