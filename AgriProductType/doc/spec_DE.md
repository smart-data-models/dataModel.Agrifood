Entität: AgriProductType  
========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriProductType/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen landwirtschaftlichen Produkttyps. Diese Entität ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden. Der AgriProductType enthält eine hierarchische Struktur, die eine flexible Gruppierung von Produkttypen ermöglicht.**  

## Liste der Eigenschaften  

- `agroVocConcept`: Verweis auf den mit diesem Artikel verbundenen agrovoc-Begriff  - `alternateName`: Ein alternativer Name für diesen Artikel  - `category`: Kategorie des Produkts. Enum:'fertiliser, cropNutrition, cropProtection, cropVariety, harvestCommodity'.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `hasAgriProductTypeChildren`: Verweis auf untergeordnete Produkttypen, d. h. direkt unterhalb dieser Entität in der Hierarchie  - `hasAgriProductTypeParent`: Verweis auf den übergeordneten Produkttyp, d. h. unmittelbar über der Entität in der Hierarchie.  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `relatedSource`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `root`: Ein logischer Indikator, dass dieses Produkt die Wurzel einer AgriProductType-Hierarchie ist. Das logische true zeigt an, dass es die Wurzel ist.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI Entity Type: Es muss AgriProductType sein    
Erforderliche Eigenschaften  
- `id`  - `name`  - `root`  - `type`    
Diese Entität ist in erster Linie mit der vertikalen Landwirtschaft und den damit verbundenen IoT-Anwendungen verbunden. Der AgriProductType enthält eine hierarchische Struktur, die eine flexible Gruppierung von Produkttypen ermöglicht.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### AgriProductType NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen AgriProductType im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriProductType NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen AgriProductType im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriProductType NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen AgriProductType im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
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
    "value": [  
      "cropVariety"  
    ]  
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
#### AgriProductType NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen AgriProductType im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_3128",  
  "category": [  
    "cropVariety"  
  ],  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Soft edible fruits",  
  "hasAgriProductTypeChildren": [  
    "urn:ngsi-ld:AgriProductType:836258d0-448b-11e8-84ec-ef61d9425fe8",  
    "urn:ngsi-ld:AgriProductType:83d607f8-448b-11e8-9fe3-0fd5140ae8db",  
    "urn:ngsi-ld:AgriProductType:90cbac88-448b-11e8-acb0-a78dab9d0555"  
  ],  
  "hasAgriProductTypeParent": "urn:ngsi-ld:AgriProductType:b99c940d-7156-4280-9a2b-4a9e533cd20e",  
  "id": "urn:ngsi-ld:AgriProductType:398aa5f4-6a81-4dea-9f85-e9869441a257",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Soft Fruits",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:product1"  
    }  
  ],  
  "root": true,  
  "type": "AgriProductType"  
}  
```  
