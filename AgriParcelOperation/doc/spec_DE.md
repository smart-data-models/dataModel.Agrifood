<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: AgriParcelOperation  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Vorgangs, der auf einer Parzelle durchgeführt wird. Diese Entität wird in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen in Verbindung gebracht.**  
Version: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `endedAt[date-time]`: Zeitstempel, wann der Vorgang tatsächlich beendet wurde  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `hasAgriParcel[*]`: Hinweis auf das AgriParcel  - `hasAgriProductType[*]`: Verweis auf den verwendeten/angewendeten AgriProductType  - `hasOperator[*]`: Hinweis auf den Betreiber, der den Vorgang durchführt  - `id[*]`: Eindeutiger Bezeichner der Entität  - `irrigationRecord[uri]`: Beziehung zur Bewässerungsaufzeichnung der Ausführung  . Model: [http://schema.org/URL](http://schema.org/URL)- `name[string]`: Der Name dieses Artikels  - `operationType[string]`: Eine Auswahl aus einer Aufzählungsliste, die den mit der Parzelle durchgeführten Vorgang beschreibt. Enum:'Dünger, Kontrolle, Pestizid, Wasser, Sonstiges'  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `plannedEndAt[date-time]`: Das geplante Enddatum/der Zeitstempel für den Vorgang. <br/><br/>Bitte beachten Sie, dass es sich hierbei um einen Hinweis handelt und der tatsächliche Zeitpunkt der Beendigung des Vorgangs vor oder nach dem geplanten Ende liegen kann.  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `plannedStartAt[date-time]`: Der geplante Starttermin/Zeitstempel für den Vorgang. Beachten Sie, dass es sich hierbei um einen Hinweis handelt und der tatsächliche Zeitpunkt des Vorgangsbeginns vor oder nach dem geplanten Start liegen kann  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `quantity[number]`: Die Gesamtmenge des verwendeten/aufgetragenen Wassers oder Produkts. Es wird empfohlen, diese Menge bei Flüssigkeiten in Litern und bei Feststoffen in Kilogramm zu messen.  . Model: [http://schema.org/Number](http://schema.org/Number)- `relatedSource[array]`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `reportedAt[date-time]`: Zeitstempel, zu dem der Ereignisfehler gemeldet wurde  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `result[string]`: Eine Beschreibung der Ergebnisse des Vorgangs. Enum:'ok, aborted, failed'  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startedAt[date-time]`: Zeitstempel des tatsächlichen Beginns der Durchführung des Vorgangs  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `status[string]`: Eine Auswahl aus einer Aufzählungsliste zur Beschreibung des Status. Enum:'geplant, laufend, beendet, vorgesehen, abgebrochen'  - `type[string]`: NGSI-Entitätstyp. Es muss AgriParcelOperation sein.  - `waterSource[string]`: Art der Wasserquellen. Enum:'Bohrloch, Niederschlag, Fluss, Regenwasserauffang, Wasserdamm, kommerzielle Versorgung'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `workOrder[uri]`: Zusammenhang mit dem Arbeitsauftrag für die Ausführung  . Model: [http://schema.org/URL](http://schema.org/URL)- `workRecord[uri]`: Beziehung zum Arbeitsnachweis der Ausführung  . Model: [http://schema.org/URL](http://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `hasAgriParcel`  - `id`  - `plannedEndAt`  - `plannedStartAt`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Dieses Unternehmen ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriParcelOperation:    
  description: This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    endedAt:    
      description: Timestamp when the operation actually finished    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    hasAgriParcel:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Reference to the AgriParcel    
      x-ngsi:    
        type: Relationship    
    hasAgriProductType:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Reference to the AgriProductType used/applied    
      x-ngsi:    
        type: Relationship    
    hasOperator:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Reference to the operator conducting the operation    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    irrigationRecord:    
      description: Relationship with the irrigation record of the execution    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'A choice from an enumerated list describing the operation performed on the parcel. Enum:''fertiliser, inspection, pesticide, water, other'''    
      enum:    
        - fertiliser    
        - inspection    
        - pesticide    
        - water    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    plannedEndAt:    
      description: The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    plannedStartAt:    
      description: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    quantity:    
      description: The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    relatedSource:    
      description: List of IDs the current entity may have in external applications    
      items:    
        properties:    
          application:    
            anyOf:    
              - description: Identifier format of any NGSI entity    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Identifier format of any NGSI entity    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
            description: Unique identifier of the entity    
            x-ngsi:    
              type: Property    
          applicationEntityId:    
            description: Identifier in the external application    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    reportedAt:    
      description: Timestamp when the event fault was reported    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    result:    
      description: 'A description of the results of the operation. Enum:''ok, aborted, failed'''    
      enum:    
        - ok    
        - aborted    
        - failed    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    startedAt:    
      description: Timestamp when the operation actually started to be performed    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    status:    
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''    
      enum:    
        - planned    
        - ongoing    
        - finished    
        - scheduled    
        - cancelled    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be AgriParcelOperation    
      enum:    
        - AgriParcelOperation    
      type: string    
      x-ngsi:    
        type: Property    
    waterSource:    
      description: 'Type of water sources. Enum:''borehole, rainfall, river, rainwater capture, water dam, commercial supply'''    
      enum:    
        - borehole    
        - rainfall    
        - river    
        - rainwater capture    
        - water dam    
        - commercial supply    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    workOrder:    
      description: Relationship with the workorder for the execution    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    workRecord:    
      description: Relationship with the work record of the execution    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
  required:    
    - id    
    - type    
    - hasAgriParcel    
    - plannedStartAt    
    - plannedEndAt    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriParcelOperation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### AgriParcelOperation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### AgriParcelOperation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### AgriParcelOperation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
    "type": "AgriParcelOperation",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": "Monthly fertiliser application",  
    "endedAt": {  
        "@type": "DateTime",  
        "@value": "2016-08-22T10:18:16Z"  
    },  
    "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
    "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
    "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
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
    "waterSource": "rainwater capture",  
    "workOrder": "https://example.com/agriparcelrecords/workorder1",  
    "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AgriParcelOperation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine AgriParcelOperation im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
    "type": "AgriParcelOperation",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Monthly fertiliser application"  
    },  
    "endedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "hasAgriParcel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
    },  
    "hasAgriProductType": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
    },  
    "hasOperator": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
    },  
    "irrigationRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "operationType": {  
        "type": "Property",  
        "value": "fertiliser"  
    },  
    "plannedEndAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "plannedStartAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "quantity": {  
        "type": "Property",  
        "value": 40,  
        "unitCode": "KGM"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:parcelop1"  
            }  
        ]  
    },  
    "reportedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "result": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agriparcelop",  
            "https://datamodel.org/example/agriparcelop"  
        ]  
    },  
    "startedAt": {  
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
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
