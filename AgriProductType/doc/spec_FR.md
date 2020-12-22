Entité : AgriProductType  
========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriProductType/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un type de produit agricole générique. Cette entité est principalement associée aux applications verticales agricoles et aux applications IdO connexes. L'AgriProductType comprend une structure hiérarchique qui permet de regrouper les types de produits de manière flexible.**  

## Liste des biens  

- `agroVocConcept`: Référence au terme agrovoc associé à ce point  - `alternateName`: Un autre nom pour cet article  - `category`: Catégorie du produit. Enum : "engrais, cultureNutrition, cultureProtection, cultureVariété, récolteProduit".  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `hasAgriProductTypeChildren`: Référence aux types de produits enfants, c'est-à-dire immédiatement en dessous de cette entité dans la hiérarchie  - `hasAgriProductTypeParent`: Référence au type de produit parent, c'est-à-dire immédiatement au-dessus de l'entité dans la hiérarchie.  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans les applications externes  - `root`: Un indicateur logique que ce produit est la racine d'une hiérarchie AgriProductType. Un vrai logique indique qu'il est la racine.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI : Il doit s'agir de l'AgriProductType    
Propriétés requises  
- `id`  - `name`  - `root`  - `type`    
Cette entité est principalement associée aux applications verticales agricoles et aux applications IdO connexes. L'AgriProductType comprend une structure hiérarchique qui permet de regrouper les types de produits de manière flexible.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriProductType:    
  description: 'This entity contains a harmonised description of a generic agricultural product type. This entity is primarily associated with the agricultural vertical and related IoT applications. The AgriProductType includes a hierarchical structure that allows product types to be grouped in a flexible way.'    
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
    category:    
      description: 'Category of the product. Enum:''fertiliser, cropNutrition, cropProtection, cropVariety, harvestCommodity''.'    
      items:    
        enum:    
          - fertiliser    
          - cropNutrition    
          - cropProtection    
          - cropVariety    
          - harvestCommodity    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
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
    hasAgriProductTypeChildren:    
      description: 'Reference to child product types i.e. immediately below this entity in the hierarchy'    
      items:    
        - anyOf: &agriproducttype_-_properties_-_id_-_anyof    
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
    hasAgriProductTypeParent:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the parent product type i.e. immediately above the entity in the hierarchy.'    
      type: Relationship    
    id:    
      anyOf: *agriproducttype_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agriproducttype_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agriproducttype_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: Property    
    root:    
      description: 'A logical indicator that this product is the root of an AgriProductType hierarchy. Logical true indicates it is the root.'    
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
      description: 'NGSI Entity Type: It has to be AgriProductType'    
      enum:    
        - AgriProductType    
      type: Property    
  required:    
    - id    
    - type    
    - name    
    - root    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### AgriProductType NGSI V2 valeurs clés Exemple  
Voici un exemple d'un AgriProductType au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
  "type": "AgriProductType",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Soft Fruits",  
  "description": "Soft edible fruits",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:product1"  
    }  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_3128",  
  "category": ["cropVariety"],  
  "root": true,  
  "hasAgriProductTypeParent": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e",  
  "hasAgriProductTypeChildren": [  
    "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
    "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
    "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"  
  ]  
}  
```  
#### AgriProductType NGSI V2 normalisé Exemple  
Voici un exemple d'un AgriProductType au format JSON tel que normalisé. Ce format est compatible avec la version 2 de l'INSG lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
  "type": "AgriProductType",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Soft Fruits"  
  },  
  "description": {  
    "value": "Soft edible fruits"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:product1"  
      }  
    ]  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_3128"  
  },  
  "category": {  
    "value": ["cropVariety"]  
  },  
  "root": {  
    "value": true  
  },  
  "hasAgriProductTypeParent": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e"  
  },  
  "hasAgriProductTypeChildren": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
      "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
      "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"  
    ]  
  }  
}  
```  
#### AgriProductType NGSI-LD valeurs clés Exemple  
Voici un exemple d'un AgriProductType au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_3128",  
 "category": ["cropVariety"],  
 "createdAt": "2017-01-01T01:20:00Z",  
 "description": "Soft edible fruits",  
 "hasAgriProductTypeChildren": ["urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
                                "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
                                "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"],  
 "hasAgriProductTypeParent": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e",  
 "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
 "modifiedAt": "2017-05-04T12:30:00Z",  
 "name": "Soft Fruits",  
 "relatedSource": [{"application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                    "applicationEntityId": "app:product1"}],  
 "root": True,  
 "type": "AgriProductType"}  
```  
#### AgriProductType NGSI-LD normalisé Exemple  
Voici un exemple d'un AgriProductType au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
    "type": "AgriProductType",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "name": {  
        "type": "Property",  
        "value": "Soft Fruits"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Soft edible fruits"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:product1"  
            }  
        ]  
    },  
    "agroVocConcept": {  
        "type": "Property",  
        "value": "http://aims.fao.org/aos/agrovoc/c_3128"  
    },  
    "category": {  
        "type": "Property",  
        "value": ["cropVariety"]  
    },  
    "root": {  
        "type": "Property",  
        "value": true  
    },  
    "hasAgriProductTypeParent": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e"  
    },  
    "hasAgriProductTypeChildren": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
            "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
            "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"  
        ]  
    }  
}  
```  
