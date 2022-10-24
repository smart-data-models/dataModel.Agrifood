<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: AgriCrop  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriCrop/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung einer generischen Kulturpflanze. Diese Entität ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  
Version: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `agroVocConcept[string]`: Die Verknüpfung mit dem definierten Konzept in das AgroVoc-Vokabular  . Model: [http://schema.org/URL](http://schema.org/URL)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `harvestingInterval[array]`: Eine Liste der empfohlenen Erntedaten für diese Kultur. Angegeben unter Verwendung von sich wiederholenden ISO8601-Datumsintervallen: <br/><br/>**Intervall, Beschreibung**<br/><br/>wobei **Intervall** in der Form **Startdatum/Enddatum**<br/><br/>--MM-TT/--MM-TT<br/><br/>bedeutet, dass jedes Jahr von diesem Startdatum bis zu diesem Enddatum wiederholt wird.  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasAgriFertiliser[array]`: Hinweis auf die empfohlenen Düngemitteltypen, die für den Anbau dieser Kultur geeignet sind.  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasAgriPest[array]`: Hinweis auf die bekannten Schädlinge, die diese Pflanze befallen  . Model: [https://schema.org/URL](https://schema.org/URL)- `hasAgriSoil[array]`: Hinweis auf die empfohlenen Bodentypen, die für den Anbau dieser Pflanze geeignet sind.  . Model: [http://schema.org/URL](http://schema.org/URL)- `id[*]`: Eindeutiger Bezeichner der Entität  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `plantingFrom[array]`: Eine Liste der empfohlenen Pflanzintervalldaten für diese Kultur. Angegeben unter Verwendung von sich wiederholenden ISO8601-Datumsintervallen: <br/><br/>**Intervall, Beschreibung**<br/><br/>wobei **Intervall** in der Form **Startdatum/Enddatum**<br/><br/>--MM-TT/--MM-TT<br/><br/>bedeutet, dass jedes Jahr von diesem Startdatum bis zu diesem Enddatum wiederholt wird.  . Model: [http://schema.org/URL](http://schema.org/URL)- `relatedSource[array]`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type[string]`: NGSI Entity Type. es muss AgriCrop sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
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
AgriCrop:    
  description: 'This entity contains a harmonised description of a generic crop. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
    agroVocConcept:    
      description: 'The link with the defined concept into the AgroVoc vocabulary'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    harvestingInterval:    
      description: 'A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date.'    
      items:    
        properties:    
          dateRange:    
            pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$    
            type: string    
          description:    
            type: string    
        type: object    
      maxItems: 2    
      minItems: 2    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    hasAgriFertiliser:    
      description: 'Reference to the recommended types of fertiliser suitable for growing this crop.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasAgriPest:    
      description: 'Reference to the pests known to attack this crop'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    hasAgriSoil:    
      description: 'Reference to the recommended types of soil suitable for growing this crop.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    id:    
      anyOf: &agricrop_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agricrop_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plantingFrom:    
      description: 'A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date.'    
      items:    
        properties:    
          dateRange:    
            pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$    
            type: string    
          description:    
            type: string    
        type: object    
      maxItems: 2    
      minItems: 2    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        properties:    
          application:    
            anyOf: *agricrop_-_properties_-_owner_-_items_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          applicationEntityId:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity Type. it has to be AgriCrop'    
      enum:    
        - AgriCrop    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriCrop/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriCrop/schema.json    
  x-model-tags: ""    
  x-version: 0.0.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### AgriCrop NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine AgriCrop im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Wheat",  
  "alternateName": "Triticum aestivum",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "seeAlso": [  
    "https://example.org/concept/wheat",  
    "https://datamodel.org/example/wheat"  
  ],  
  "description": "Spring wheat",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:weat"  
    }  
  ],  
  "hasAgriSoil": [  
    "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
    "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
  ],  
  "hasAgriFertiliser": [  
    "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriPest": [  
    "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "plantingFrom": [  
    {  
      "dateRange": "-09-28/-10-12",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-10-11/-10-18",  
      "description": "Season OK"  
    }  
  ],  
  "harvestingInterval": [  
    {  
      "dateRange": "-03-21/-04-01",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-04-02/-04-15",  
      "description": "Season OK"  
    }  
  ],  
  "wateringFrequency": "daily"  
}  
```  
</details>  
#### AgriCrop NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine AgriCrop im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Wheat"  
  },  
  "alternateName": {  
    "value": "Triticum aestivum"  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/wheat",  
      "https://datamodel.org/example/wheat"  
    ]  
  },  
  "description": {  
    "value": "Spring wheat"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:weat"  
      }  
    ]  
  },  
  "hasAgriSoil": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ]  
  },  
  "hasAgriFertiliser": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "hasAgriPest": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "plantingFrom": {  
    "value": [  
      {  
        "dateRange": "-09-28/-10-12",  
        "description": "Best Season"  
      },  
      {  
        "dateRange": "-10-11/-10-18",  
        "description": "Season OK"  
      }  
    ]  
  },  
  "harvestingInterval": {  
    "value": [  
      {  
        "dateRange": "-03-21/-04-01",  
        "description": "Best Season"  
      },  
      {  
        "dateRange": "-04-02/-04-15",  
        "description": "Season OK"  
      }  
    ]  
  },  
  "wateringFrequency": {  
    "value": "daily"  
  }  
}  
```  
</details>  
#### AgriCrop NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine AgriCrop im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriCrop",  
    "agroVocConcept": {  
        "type": "Property",  
        "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Triticum aestivum"  
    },  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Spring wheat"  
    },  
    "harvestingInterval": {  
        "type": "Property",  
        "value": [  
            {  
                "dateRange": "-03-21/-04-01",  
                "description": "Best Season"  
            },  
            {  
                "dateRange": "-04-02/-04-15",  
                "description": "Season OK"  
            }  
        ]  
    },  
    "hasAgriFertiliser": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
            "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
        ]  
    },  
    "hasAgriPest": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
            "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
        ]  
    },  
    "hasAgriSoil": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
            "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
        ]  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "name": {  
        "type": "Property",  
        "value": "Wheat"  
    },  
    "plantingFrom": {  
        "type": "Property",  
        "value": [  
            {  
                "dateRange": "-09-28/-10-12",  
                "description": "Best Season"  
            },  
            {  
                "dateRange": "-10-11/-10-18",  
                "description": "Season OK"  
            }  
        ]  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:weat"  
            }  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/wheat",  
            "https://datamodel.org/example/wheat"  
        ]  
    },  
    "wateringFrequency": {  
        "type": "Property",  
        "value": "daily"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AgriCrop NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine AgriCrop im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriCrop",  
    "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
    "alternateName": "Triticum aestivum",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": "Spring wheat",  
    "harvestingInterval": [  
        {  
            "dateRange": "-03-21/-04-01",  
            "description": "Best Season"  
        },  
        {  
            "dateRange": "-04-02/-04-15",  
            "description": "Season OK"  
        }  
    ],  
    "hasAgriFertiliser": [  
        "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
        "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ],  
    "hasAgriPest": [  
        "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
        "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ],  
    "hasAgriSoil": [  
        "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
        "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ],  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "name": "Wheat",  
    "plantingFrom": [  
        {  
            "dateRange": "-09-28/-10-12",  
            "description": "Best Season"  
        },  
        {  
            "dateRange": "-10-11/-10-18",  
            "description": "Season OK"  
        }  
    ],  
    "relatedSource": [  
        {  
            "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
            "applicationEntityId": "app:weat"  
        }  
    ],  
    "seeAlso": [  
        "https://example.org/concept/wheat",  
        "https://datamodel.org/example/wheat"  
    ],  
    "wateringFrequency": "daily",  
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
