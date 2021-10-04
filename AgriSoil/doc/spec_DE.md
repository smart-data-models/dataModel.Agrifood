Entität: AgriSoil  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriSoil/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Bodens. Diese Entität ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `agroVocConcept`: Verweis auf den mit diesem Artikel verbundenen agrovoc-Begriff  - `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `hasAgriProductType`: Hinweis auf die empfohlenen Produkttypen (z. B. Düngemittel), die für die Aufbereitung dieses Bodentyps verwendet werden können.  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `relatedSource`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI-Entitätstyp: Es muss AgriSoil sein    
Erforderliche Eigenschaften  
- `id`  - `name`  - `type`    
Dieses Unternehmen ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriSoil:    
  description: 'This entity contains a harmonised description of a generic soil. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
    agroVocConcept:    
      description: 'Reference to the agrovoc term associated with this item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
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
    hasAgriProductType:    
      description: 'Reference to the recommended types of product (such as fertiliser) that can be used to condition this soil type.'    
      items:    
        - anyOf: &agrisoil_-_properties_-_id_-_anyof    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
          description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: *agrisoil_-_properties_-_id_-_anyof    
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
        anyOf: *agrisoil_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agrisoil_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
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
      description: 'NGSI Entity Type: It has to be AgriSoil'    
      enum:    
        - AgriSoil    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### AgriSoil NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen AgriSoil im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
  "type": "AgriSoil",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Clay",  
  "alternateName": "Heavy soil",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "seeAlso": [  
    "https://example.org/concept/clay",  
    "https://datamodel.org/example/clay"  
  ],  
  "description": "Fine grained, poor draining soil. Particle size less than 0.002mm",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:clay"  
    }  
  ],  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:ea54eedf-d5a7-4e44-bddd-50e9935237c0",  
    "urn:ngsi-ld:AgriProductType:275b4c08-5e52-4bb7-8523-74ce5d0007de"  
  ]  
}  
```  
#### AgriSoil NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein AgriSoil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
  "type": "AgriSoil",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Clay"  
  },  
  "alternateName": {  
    "value": "Heavy soil"  
  },  
  "description": {  
    "value": "Fine grained, poor draining soil. Particle size less than 0.002mm"  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/clay",  
      "https://datamodel.org/example/clay"  
    ]  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:clay"  
      }  
    ]  
  },  
  "hasAgriProductType": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriProductType:ea54eedf-d5a7-4e44-bddd-50e9935237c0",  
      "urn:ngsi-ld:AgriProductType:275b4c08-5e52-4bb7-8523-74ce5d0007de"  
    ]  
  }  
}  
```  
#### AgriSoil NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen AgriSoil im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
  "type": "AgriSoil",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "alternateName": "Heavy soil",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Fine grained, poor draining soil. Particle size less than 0.002mm",  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:ea54eedf-d5a7-4e44-bddd-50e9935237c0",  
    "urn:ngsi-ld:AgriProductType:275b4c08-5e52-4bb7-8523-74ce5d0007de"  
  ],  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Clay",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:clay"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/clay",  
    "https://datamodel.org/example/clay"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### AgriSoil NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein AgriSoil im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
  "type": "AgriSoil",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": {  
    "type": "Property",  
    "value": "Clay"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Heavy soil"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Fine grained, poor draining soil. Particle size less than 0.002mm"  
  },  
  "agroVocConcept": {  
    "type": "Property",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "https://example.org/concept/clay",  
      "https://datamodel.org/example/clay"  
    ]  
  },  
  "relatedSource": {  
    "type": "Property",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:clay"  
      }  
    ]  
  },  
  "hasAgriProductType": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriProductType:ea54eedf-d5a7-4e44-bddd-50e9935237c0",  
      "urn:ngsi-ld:AgriProductType:275b4c08-5e52-4bb7-8523-74ce5d0007de"  
    ]  
  },  
    "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
