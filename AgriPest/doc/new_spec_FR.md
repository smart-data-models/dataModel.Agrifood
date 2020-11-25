Entité : AgriPest  
=================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Cette entité contient une description harmonisée d'un parasite agricole. Cette entité est principalement associée aux applications verticales agricoles et aux applications IdO connexes.**  

## Liste des biens  

- `agroVocConcept`:   - `alternateName`: Un autre nom pour cet article  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `hasAgriProductType`:   - `id`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans les applications externes  - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriPest:    
  description: 'This entity contains a harmonised description of an agricultural pest. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
    agroVocConcept:    
      format: uri    
      type: string    
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
      type: array    
    id:    
      anyOf: *agripest_-_properties_-_id_-_anyof    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agripest_-_properties_-_id_-_anyof    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agripest_-_properties_-_id_-_anyof    
            applicationEntityId:    
              type: string    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type'    
      enum:    
        - AgriPest    
      type: string    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Exemple de valeurs clés de l'INSG V2 d'AgriPest  
Voici un exemple d'AgriPest en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### AgriPest NGSI V2 normalisé Exemple  
Voici un exemple d'un AgriPest au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### Exemple de valeurs clés de l'INSG-LD AgriPest  
Voici un exemple d'AgriPest en format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_31924",  
 "alternateName": "Chorthippus parallelus",  
 "createdAt": "2017-01-01T01:20:00Z",  
 "description": "Common European grasshopper",  
 "hasAgriProductType": ["urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
                        "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
                        "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"],  
 "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
 "modifiedAt": "2017-05-04T12:30:00Z",  
 "name": "Grasshopper",  
 "relatedSource": [{"application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                    "applicationEntityId": "app:farm1"}],  
 "seeAlso": ["https://example.org/concept/pest",  
             "https://datamodel.org/example/pest"],  
 "type": "AgriPest"}  
```  
#### AgriPest NGSI-LD normalisé Exemple  
Voici un exemple d'un AgriPest au format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
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
