Entität: AgriPest  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriPest/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines landwirtschaftlichen Schädlings. **  

## Liste der Eigenschaften  

- `agroVocConcept`: Verweis auf den mit diesem Artikel verbundenen agrovoc-Begriff  - `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `hasAgriProductType`: Hinweis auf die empfohlenen Produkttypen, die zur Behandlung dieses Schädlings verwendet werden können.  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `relatedSource`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI-Entitätstyp: Es muss AgriPest sein    
Erforderliche Eigenschaften  
- `id`  - `name`  - `type`    
Dieses Unternehmen ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriPest:    
  description: 'This entity contains a harmonised description of an agricultural pest. '    
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
      description: 'Reference to the recommended types of product that can be used to treat this pest.'    
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
          description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    id:    
      anyOf: *agripest_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agripest_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agripest_-_properties_-_id_-_anyof    
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
      description: 'NGSI Entity Type: It has to be AgriPest'    
      enum:    
        - AgriPest    
      type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### AgriPest NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen AgriPest im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriPest NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen AgriPest im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriPest NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen AgriPest im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
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
#### AgriPest NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen AgriPest im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_31924",  
  "alternateName": "Chorthippus parallelus",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Common European grasshopper",  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
    "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
    "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
  ],  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Grasshopper",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:farm1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/pest",  
    "https://datamodel.org/example/pest"  
  ],  
  "type": "AgriPest"  
}  
```  
