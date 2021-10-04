Entität: AgriParcelOperation  
============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Vorgangs, der auf einer Parzelle durchgeführt wird. Diese Entität ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endedAt`: Zeitstempel, wann der Vorgang tatsächlich beendet wurde.  - `hasAgriParcel`: Verweis auf das AgriParcel  - `hasAgriProductType`: Verweis auf den verwendeten/angewendeten AgriProductType.  - `hasOperator`: Hinweis auf den Bediener, der den Vorgang durchführt  - `id`: Eindeutiger Bezeichner der Entität  - `irrigationRecord`: Zusammenhang mit dem Bewässerungsprotokoll der Ausführung  - `name`: Der Name dieses Elements.  - `operationType`: Eine Auswahl aus einer Aufzählungsliste, die den an der Parzelle durchgeführten Vorgang beschreibt. Enum:'Dünger, Inspektion, Pestizid, Wasser, Sonstiges'  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `plannedEndAt`: Das geplante Enddatum/der Zeitstempel für den Vorgang. <br/><br/>Beachten Sie, dass es sich hierbei um einen Hinweis handelt und der tatsächliche Zeitpunkt der Beendigung des Vorgangs vor oder nach dem geplanten Ende liegen kann.  - `plannedStartAt`: Das geplante Startdatum/der Zeitstempel für den Vorgang. Beachten Sie, dass es sich hierbei um einen Hinweis handelt und der tatsächliche Startzeitpunkt des Vorgangs vor oder nach dem geplanten Start liegen kann  - `quantity`: Die Gesamtmenge des verwendeten/aufgetragenen Wassers oder Produkts. Es wird empfohlen, diese in Litern für Flüssigkeiten oder Kilogramm für Feststoffe zu messen.  - `relatedSource`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `reportedAt`: Zeitstempel, wann der Ereignisfehler gemeldet wurde.  - `result`: Eine Beschreibung der Ergebnisse des Vorgangs. Enum:'ok, aborted, failed'  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `startedAt`: Zeitstempel, wann die Ausführung des Vorgangs tatsächlich begann.  - `status`: Eine Auswahl aus einer Aufzählungsliste, die den Status beschreibt. Enum:'geplant, laufend, beendet, geplant, abgebrochen'  - `type`: NGSI-Entitätstyp. Es muss AgriParcelOperation sein  - `waterSource`: Enum:'Bohrloch, Regenfall, Fluss, Regenwasserauffang, Wasserdamm, kommerzielle Versorgung'.  - `workOrder`: Beziehung mit dem Arbeitsauftrag für die Ausführung  - `workRecord`: Zusammenhang mit dem Arbeitsprotokoll der Ausführung    
Erforderliche Eigenschaften  
- `hasAgriParcel`  - `id`  - `plannedEndAt`  - `plannedStartAt`  - `type`    
Dieses Unternehmen ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### AgriParcelOperation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriParcelOperation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriParcelOperation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
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
#### AgriParcelOperation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Monthly fertiliser application",  
  "endedAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "operationType": "fertiliser",  
  "plannedEndAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "plannedStartAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "quantity": 40,  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "reportedAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "result": "ok",  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "startedAt": {  
    "@type": "DateTime",  
    "@value": "2016-08-22T10:18:16Z"  
  },  
  "status": "finished",  
  "type": "AgriParcelOperation",  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1"  
}  
```  
