<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AnimaleMalattia  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AnimalDisease/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Oggetto che modella una malattia animale per un'azienda zootecnica.**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `animals[array]`: Animali o elenco di animali a cui è stata diagnosticata la malattia. Modello https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Animal/schema.json  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `date[string]`: Data di diagnosi della malattia da parte di un veterinario.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `diagnosticTest[string]`: Test diagnostico eseguito sugli animali per la determinazione della malattia da parte di un veterinario.  - `disease[string]`: Malattia dell'animale. Indica la malattia dell'animale diagnosticata da un veterinario. Fonte spagnola di malattie https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/sanidad-animal/enfermedades/  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NGSI. Deve essere AnimalDisease  - `veterinarian[string]`: Veterinario diagnostico. Rapporto con il veterinario prescrittore  - `veterinarianTreatment[string]`: Trattamento medico diagnosticato dal veterinario per curare la malattia. https://github.com/smart-data-models/dataModel.Agrifood/blob/master/VeterinarianTreatment/schema.json  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `disease`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnimalDisease:    
  description: 'Object modelling an animal disease for a livestock farm.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    animals:    
      description: 'Animals or list of animals diagnosed with the disease. Model https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Animal/schema.json'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    date:    
      description: 'Date of diagnosis of the disease by a veterinarian.'    
      format: date-time    
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
    diagnosticTest:    
      description: 'Diagnostic test performed in the animals for the determination of the disease by a veterinarian.'    
      type: string    
      x-ngsi:    
        type: Property    
    disease:    
      description: 'Animal disease. Indicates the disease the animal has as diagnosed by a veterinarian. Spanish source of diseases https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/sanidad-animal/enfermedades/'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &animaldisease_-_properties_-_owner_-_items_-_anyof    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *animaldisease_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'NGSI entity type. It has to be AnimalDisease'    
      enum:    
        - AnimalDisease    
      type: string    
      x-ngsi:    
        type: Property    
    veterinarian:    
      description: 'Diagnostic veterinarian. Relationship to the prescribing veterinarian'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    veterinarianTreatment:    
      description: 'Medical treatment diagnosed by the veterinarian to treat the disease. https://github.com/smart-data-models/dataModel.Agrifood/blob/master/VeterinarianTreatment/schema.json'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
    - disease    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AnimalDisease/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AnimalDisease/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### AnimalDisease Valori-chiave NGSI-v2 Esempio  
Ecco un esempio di AnimalDisease in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "AnimalDisease",  
  "disease": "Lameness",  
  "diagnosticTest": "Visual inspection",  
  "date": "2022-01-01T01:20:00Z",  
  "animals": [  
    "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
  ],  
  "veterinarianTreatment": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65",  
  "veterinarian": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11"  
}  
```  
</details>  
#### AnimalDisease NGSI-v2 normalizzato Esempio  
Ecco un esempio di AnimalDisease in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "AnimalDisease",  
  "disease": {  
    "type": "Text",  
    "value": "Lameness"  
  },  
  "diagnosticTest": {  
    "type": "Text",  
    "value": "Visual inspection"  
  },  
  "date": {  
    "type": "Date-Time",  
    "value": "2022-01-01T01:20:00Z"  
  },  
  "animals": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
      "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
    ]  
  },  
  "veterinarianTreatment": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65"  
  },  
  "veterinarian": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11"  
  }  
}  
```  
</details>  
#### AnimalDisease Valori chiave NGSI-LD Esempio  
Ecco un esempio di AnimalDisease in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "type": "AnimalDisease",  
    "disease": "Lameness",  
    "diagnosticTest": "Visual inspection",  
    "date": "2022-01-01T01:20:00Z",  
    "animals": [  
        "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
        "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
    ],  
    "veterinarianTreatment": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65",  
    "veterinarian": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Agrifood/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AnimalDisease NGSI-LD normalizzato Esempio  
Ecco un esempio di AnimalDisease in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "type": "AnimalDisease",  
    "disease": {  
        "type": "Property",  
        "value": "Lameness"  
    },  
    "diagnosticTest": {  
        "type": "Property",  
        "value": "Visual inspection"  
    },  
    "date": {  
        "type": "Property",  
        "value": {  
            "@type": "Date-Time",  
            "@value": "2022-01-01T01:20:00Z"  
        }  
    },  
    "animals": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
            "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
        ]  
    },  
    "veterinarianTreatment": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65"  
    },  
    "veterinarian": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Agrifood/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
