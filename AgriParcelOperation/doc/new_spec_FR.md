Entité : AgriParcelOperation  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'une opération générique effectuée sur une parcelle de terrain. Cette entité est principalement associée aux applications verticales agricoles et aux applications IdO connexes.**  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `endedAt`: Horodatage de la fin effective de l'opération.  - `hasAgriParcel`: Référence à l'AgriParcel  - `hasAgriProductType`: Référence au type de produit agricole utilisé/appliqué.  - `hasOperator`: Référence à l'opérateur qui conduit l'opération  - `id`: Identifiant unique de l'entité  - `irrigationRecord`: Relation avec le dossier d'irrigation de l'exécution  - `name`: Le nom de cet article.  - `operationType`: Un choix dans une liste énumérée décrivant l'opération effectuée sur le colis. Enum : "engrais, inspection, pesticide, eau, autre".  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `plannedEndAt`: La date/heure de fin prévue pour l'opération. <br/><br/> Notez qu'il s'agit d'un avis et que l'heure réelle de fin de l'opération peut être antérieure ou postérieure à la fin prévue.  - `plannedStartAt`: La date/heure de début prévue pour l'opération. Notez qu'il s'agit d'un avis et que l'heure réelle de début de l'opération peut être antérieure ou postérieure à la date de début prévue  - `quantity`: La quantité totale d'eau ou de produit utilisée/appliquée. Il est recommandé de mesurer cette quantité en litres pour les liquides ou en kilogrammes pour les solides.  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans les applications externes  - `reportedAt`: Horodatage de l'événement de défaut.  - `result`: Une description des résultats de l'opération. Enum : "ok, avorté, échoué  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `startedAt`: Horodatage de la date à laquelle l'opération a effectivement commencé à être effectuée.  - `status`: Un choix dans une liste énumérée décrivant le statut. Enum : "planifié, en cours, terminé, programmé, annulé".  - `type`: Type d'entité NGSI. Il doit s'agir d'AgriParcelOperation  - `waterSource`: Enum : "forage, précipitations, rivière, captage d'eau de pluie, barrage, approvisionnement commercial".  - `workOrder`: Relation avec l'ordre de travail pour l'exécution  - `workRecord`: Relation avec le dossier de travail de l'exécution    
Propriétés requises  
- `hasAgriParcel`  - `id`  - `plannedEndAt`  - `plannedStartAt`  - `type`    
Cette entité est principalement associée aux applications verticales agricoles et aux applications IdO connexes.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriParcelOperation:    
  description: 'This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
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
    endedAt:    
      description: 'Timestamp when the operation actually finished.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    hasAgriParcel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the AgriParcel'    
      type: Relationship    
    hasAgriProductType:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the AgriProductType used/ applied.'    
      type: Relationship    
    hasOperator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the operator conducting the operation'    
      type: Relationship    
    id:    
      anyOf: &agriparceloperation_-_properties_-_owner_-_items_-_anyof    
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
    irrigationRecord:    
      description: 'Relationship with the irrigation record of the execution'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    name:    
      description: 'The name of this item.'    
      type: Property    
    operationType:    
      description: 'A choice from an enumerated list describing the operation performed on the parcel. Enum:''fertiliser, inspection, pesticide, water, other'''    
      enum:    
        - fertiliser    
        - inspection    
        - pesticide    
        - water    
        - other    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agriparceloperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    plannedEndAt:    
      description: 'The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    plannedStartAt:    
      description: 'The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    quantity:    
      description: 'The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agriparceloperation_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: Property    
    reportedAt:    
      description: 'Timestamp when the event fault was reported.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    result:    
      description: 'A description of the results of the operation. Enum:''ok, aborted, failed'''    
      enum:    
        - ok    
        - aborted    
        - failed    
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
    startedAt:    
      description: 'Timestamp when the operation actually started to be performed.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    status:    
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''    
      enum:    
        - planned    
        - ongoing    
        - finished    
        - scheduled    
        - cancelled    
      type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be AgriParcelOperation'    
      enum:    
        - AgriParcelOperation    
      type: Property    
    waterSource:    
      description: 'Enum:''borehole, rainfall, river, rainwater capture, water dam, commercial supply''.'    
      enum:    
        - borehole    
        - rainfall    
        - river    
        - 'rainwater capture'    
        - 'water dam'    
        - 'commercial supply'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    workOrder:    
      description: 'Relationship with the workorder for the execution'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    workRecord:    
      description: 'Relationship with the work record of the execution'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
  required:    
    - id    
    - type    
    - hasAgriParcel    
    - plannedStartAt    
    - plannedEndAt    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### AgriParcelOperation NGSI V2 - Exemple de valeurs clés  
Voici un exemple d'AgriParcelOperation en format JSON comme valeurs clés. Ce format est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "operationType": "fertiliser",  
  "description": "Monthly fertiliser application",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "finished",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "quantity": 40,  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1"  
}  
```  
#### AgriParcelOperation NGSI V2 normalisé Exemple  
Voici un exemple d'AgriParcelOpération au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelop1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/agriparcelop",  
      "https://datamodel.org/example/agriparcelop"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
  },  
  "operationType": {  
    "value": "fertiliser"  
  },  
  "description": {  
    "value": "Monthly fertiliser application"  
  },  
  "result": {  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "value": "finished"  
  },  
  "hasOperator": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "reportedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "hasAgriProductType": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
  },  
  "quantity": {  
    "value": 40  
  },  
  "waterSource": {  
    "value": "rainwater capture"  
  },  
  "workOrder": {  
    "type": "URL",  
    "value": "https://example.com/agriparcelrecords/workorder1"  
  },  
  "workRecord": {  
    "type": "URL",  
    "value": "https://example.com/agriparcelrecords/workrecord1"  
  },  
  "irrigationRecord": {  
    "type": "URL",  
    "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
  }  
}  
```  
#### AgriParcelOperation NGSI-LD valeurs clés Exemple  
Voici un exemple d'AgriParcelOperation en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "createdAt": "2017-01-01T01:20:00Z",  
 "description": "Monthly fertiliser application",  
 "endedAt": {"@type": "DateTime", "@value": "2016-08-22T10:18:16Z"},  
 "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
 "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
 "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
 "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
 "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1",  
 "modifiedAt": "2017-05-04T12:30:00Z",  
 "operationType": "fertiliser",  
 "plannedEndAt": {"@type": "DateTime", "@value": "2016-08-22T10:18:16Z"},  
 "plannedStartAt": {"@type": "DateTime", "@value": "2016-08-22T10:18:16Z"},  
 "quantity": 40,  
 "relatedSource": [{"application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                    "applicationEntityId": "app:parcelop1"}],  
 "reportedAt": {"@type": "DateTime", "@value": "2016-08-22T10:18:16Z"},  
 "result": "ok",  
 "seeAlso": ["https://example.org/concept/agriparcelop",  
             "https://datamodel.org/example/agriparcelop"],  
 "startedAt": {"@type": "DateTime", "@value": "2016-08-22T10:18:16Z"},  
 "status": "finished",  
 "type": "AgriParcelOperation",  
 "waterSource": "rainwater capture",  
 "workOrder": "https://example.com/agriparcelrecords/workorder1",  
 "workRecord": "https://example.com/agriparcelrecords/workrecord1"}  
```  
#### AgriParcelOperation NGSI-LD normalisé Exemple  
Voici un exemple d'AgriParcelOperation au format JSON-LD tel que normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
    "type": "AgriParcelOperation",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:parcelop1"  
            }  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agriparcelop",  
            "https://datamodel.org/example/agriparcelop"  
        ]  
    },  
    "hasAgriParcel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
    },  
    "operationType": {  
        "type": "Property",  
        "value": "fertiliser"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Monthly fertiliser application"  
    },  
    "result": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "plannedStartAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "plannedEndAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "status": {  
        "type": "Property",  
        "value": "finished"  
    },  
    "hasOperator": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
    },  
    "startedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "endedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "reportedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "hasAgriProductType": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
    },  
    "quantity": {  
        "type": "Property",  
        "value": 40,  
        "unitCode": "KGM"  
    },  
    "waterSource": {  
        "type": "Property",  
        "value": "rainwater capture"  
    },  
    "workOrder": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/workorder1"  
    },  
    "workRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/workrecord1"  
    },  
    "irrigationRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
    }  
}  
```  
