Entité : AgriFarm  
=================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriFarm/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une ferme générique composée de bâtiments et de parcelles. Cette entité est principalement associée à la verticale agricole et aux applications IoT connexes.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `contactPoint`: Les coordonnées à contacter avec l'article.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `hasAgriParcel`: Liste des parcelles agricoles appartenant à l'exploitation  - `hasBuilding`: Liste des bâtiments appartenant à la ferme  - `id`: Identifiant unique de l'entité  - `landLocation`:   - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `ownedBy`: Propriétaire (personne ou organisation) de l'exploitation agricole  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans des applications externes  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir de AgriFarm    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriFarm:    
  description: 'This entity contains a harmonised description of a generic farm made up of buildings and parcels. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
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
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        contactType:    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        name:    
          type: string    
        telephone:    
          type: string    
        url:    
          format: uri    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
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
    hasAgriParcel:    
      description: 'List of agri parcels belonging to the farm'    
      items:    
        - anyOf: &anyof    
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
    hasBuilding:    
      description: 'List of buildings belonging to the farm'    
      items:    
        - anyOf: *anyof    
          description: 'Property. Unique identifier of the entity'    
      type: Relationship    
    id:    
      anyOf: *anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    landLocation:    
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
      description: 'Owner (Person or Organization) of the farm'    
      type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *anyof    
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
      description: 'NGSI Entity Type. It has to be AgriFarm'    
      enum:    
        - AgriFarm    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### AgriFarm NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'une AgriFarm au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "type": "AgriFarm",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Wheat farm",  
  "description": "A farm producing wheat",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:farm1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/farm",  
    "https://datamodel.org/example/farm"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [100, 0]  
  },  
  "landLocation": {  
    "type": "Polygon",  
    "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
  },  
  "address": {  
    "addressLocality": "Valdepeñas",  
    "addressCountry": "ES",  
    "streetAddress": "Camino de Membrilla 17"  
  },  
  "contactPoint": {  
    "email": "wheatfarm@email.com",  
    "telephone": "00349674532"  
  },  
  "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "hasBuilding": [  
    "urn:ngsi-ld:Building:a6ba44e0-4474-11e8-8ed1-ab9e0ea93827",  
    "urn:ngsi-ld:Building:d95b8874-4474-11e8-8d6b-dbe144258354"  
  ],  
  "hasAgriParcel": [  
    "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
    "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
  ]  
}  
```  
#### AgriFarm NGSI-v2 normalisé Exemple  
Voici un exemple d'une AgriFarm au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "type": "AgriFarm",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Wheat farm"  
  },  
  "description": {  
    "value": "A farm producing wheat"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:farm1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/farm",  
      "https://datamodel.org/example/farm"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [101, 0]  
    }  
  },  
  "landLocation": {  
    "value": {  
      "type": "Polygon",  
      "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valdepeñas",  
      "addressCountry": "ES",  
      "streetAddress": "Camino de Membrilla 17"  
    }  
  },  
  "contactPoint": {  
    "type": "ContactPoint",  
    "value": {  
      "email": "wheatfarm@email.com",  
      "telephone": "00349674532"  
    }  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "hasBuilding": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Building:a6ba44e0-4474-11e8-8ed1-ab9e0ea93827",  
      "urn:ngsi-ld:Building:d95b8874-4474-11e8-8d6b-dbe144258354"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
      "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
    ]  
  }  
}  
```  
#### AgriFarm NGSI-LD key-values Exemple  
Voici un exemple d'une AgriFarm au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "type": "AgriFarm",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": {  
    "type": "Property",  
    "value": "Wheat farm"  
  },  
  "description": {  
    "type": "Property",  
    "value": "A farm producing wheat"  
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
      "https://example.org/concept/farm",  
      "https://datamodel.org/example/farm"  
    ]  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        100,  
        0  
      ]  
    }  
  },  
  "landLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            100,  
            0  
          ],  
          [  
            101,  
            0  
          ],  
          [  
            101,  
            1  
          ],  
          [  
            100,  
            1  
          ],  
          [  
            100,  
            0  
          ]  
        ]  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "type": "PostalAddress",  
      "addressLocality": "Valdepe\u00f1as",  
      "addressCountry": "ES",  
      "streetAddress": "Camino de Membrilla 17"  
    }  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "type": "ContactPoint",  
      "email": "wheatfarm@email.com",  
      "telephone": "00349674532"  
    }  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "hasBuilding": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Building:a6ba44e0-4474-11e8-8ed1-ab9e0ea93827",  
      "urn:ngsi-ld:Building:d95b8874-4474-11e8-8d6b-dbe144258354"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
      "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
    ]  
  }  
}  
```  
#### AgriFarm NGSI-LD normalisé Exemple  
Voici un exemple d'une AgriFarm au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Valdepe\u00f1as",  
    "streetAddress": "Camino de Membrilla 17",  
    "type": "PostalAddress"  
  },  
  "contactPoint": {  
    "email": "wheatfarm@email.com",  
    "telephone": "00349674532",  
    "type": "ContactPoint"  
  },  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "A farm producing wheat",  
  "hasAgriParcel": [  
    "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
    "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
  ],  
  "hasBuilding": [  
    "urn:ngsi-ld:Building:a6ba44e0-4474-11e8-8ed1-ab9e0ea93827",  
    "urn:ngsi-ld:Building:d95b8874-4474-11e8-8d6b-dbe144258354"  
  ],  
  "id": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "landLocation": {  
    "coordinates": [  
      [  
        [  
          100,  
          0  
        ],  
        [  
          101,  
          0  
        ],  
        [  
          101,  
          1  
        ],  
        [  
          100,  
          1  
        ],  
        [  
          100,  
          0  
        ]  
      ]  
    ],  
    "type": "Polygon"  
  },  
  "location": {  
    "coordinates": [  
      100,  
      0  
    ],  
    "type": "Point"  
  },  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Wheat farm",  
  "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:farm1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/farm",  
    "https://datamodel.org/example/farm"  
  ],  
  "type": "AgriFarm"  
}  
```  
