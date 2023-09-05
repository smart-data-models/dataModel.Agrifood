<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Animale  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Animal/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Un'osservazione delle condizioni degli animali in un determinato luogo e momento. Questo modello di dati è stato sviluppato per l'IoF2020 UC ShareBeef da UCO e SensoWave.  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `birthdate[date-time]`: Data di nascita dell'animale  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `breed[string]`: Razza dell'animale  - `calvedBy[*]`: Madre dell'animale  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `fedWith[*]`: Cibo utilizzato per l'animale  - `healthCondition[string]`: Condizione fenologica dell'animale. Enum:" sano, malato, inTrattamento".  - `id[*]`: Identificatore univoco dell'entità  - `legalId[string]`: Documento d'identità legale dell'animale  - `locatedAt[*]`: Id del rapporto AgriParcel  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `ownedBy[*]`: Il proprietario dell'animale  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `phenologicalCondition[string]`: Condizione fenologica dell'animale. Enum:'bambino in lattazione, bambino al pascolo, maschio adulto, femmina adulta, maschio giovane, femmina giovane'.  - `relatedSource[array]`: Elenco di ID che l'entità corrente può avere in applicazioni esterne.  - `reproductiveCondition[string]`: Stato riproduttivo dell'animale. Enum:'noStatus, inactive, inCalf, inHeat, active'.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sex[string]`: Sesso dell'animale. Enum:'maschio, femmina'  - `siredBy[*]`: Padre dell'animale  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `species[string]`: Specie a cui appartiene l'animale. Questo enum può essere aumentato  . Model: [Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text](Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text)- `type[string]`: Tipo di entità NGSI: Deve essere Animale  - `weight[number]`: Il peso dell'animale come numero  . Model: [http://schema.org/Number](http://schema.org/Number)- `welfareCondition[string]`: Indicatore del benessere animale. Enum:'problema, adeguato'  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `legalId`  - `sex`  - `species`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Il modello di dati animali proposto è stato realizzato da un punto di vista più generale, cercando di adattarlo alle informazioni provenienti dai dispositivi e dai sensori utilizzati nell'UC. Il diagramma successivo descrive la filiera della carne. In questo diagramma sono descritti i diversi attori della filiera della carne e alcune delle loro interazioni. ![ ](../resources/diagram1.jpg). Durante l'utilizzo di questo modello di dati sarà necessario definire diverse entità per gestire le informazioni generate nella soluzione proposta. All'interno di tutte queste entità, spicca in primo luogo l'entità animale che è al centro della soluzione  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Animal:    
  description: An observation of animal conditions at a certain place and time. This data model has been developed for the IoF2020 UC ShareBeef by UCO and SensoWave.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    birthdate:    
      description: Animal's birthdate    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    breed:    
      description: Breed of the animal    
      type: string    
      x-ngsi:    
        type: Property    
    calvedBy:    
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
      description: Mother of the animal    
      x-ngsi:    
        type: Relationship    
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
    fedWith:    
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
      description: Food used for the animal    
      x-ngsi:    
        type: Relationship    
    healthCondition:    
      description: 'Phenological condition of the animal. Enum:'' healthy, sick, inTreatment'''    
      enum:    
        - healthy    
        - inTreatment    
        - sick    
      type: string    
      x-ngsi:    
        type: Property    
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
    legalId:    
      description: Legal ID of the animal    
      type: string    
      x-ngsi:    
        type: Property    
    locatedAt:    
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
      description: Id of the AgriParcel relationship    
      x-ngsi:    
        type: Relationship    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    ownedBy:    
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
      description: The owner of the animal    
      x-ngsi:    
        type: Relationship    
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
    phenologicalCondition:    
      description: 'Phenological condition of the animal. Enum:''lactatingBaby, grazingBaby, maleAdult, femaleAdult, maleYoung, femaleYoung'''    
      enum:    
        - femaleAdult    
        - femaleYoung    
        - grazingBaby    
        - lactatingBaby    
        - maleAdult    
        - maleYoung    
      type: string    
      x-ngsi:    
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
    reproductiveCondition:    
      description: 'Reproductive condition of the animal. Enum:''noStatus, inactive, inCalf, inHeat, active'''    
      enum:    
        - active    
        - inactive    
        - inCalf    
        - inHeat    
        - noStatus    
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
    sex:    
      description: 'Sex of the animal. Enum:''male, female'''    
      enum:    
        - female    
        - male    
      type: string    
      x-ngsi:    
        type: Property    
    siredBy:    
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
      description: Father of the animal    
      x-ngsi:    
        type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    species:    
      description: Species to which the animal belongs. This enum can be increased    
      enum:    
        - beef cattle    
        - cow    
        - dairy cattle    
        - goat    
        - horse    
        - pig    
        - sheep    
      type: string    
      x-ngsi:    
        model: 'Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text'    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be Animal'    
      enum:    
        - Animal    
      type: string    
      x-ngsi:    
        type: Property    
    weight:    
      description: The weight of the animal as a number    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Relationship    
        units: kg    
    welfareCondition:    
      description: 'Indicator of the animal welfare. Enum:''issue, adequate'''    
      enum:    
        - issue    
        - adequate    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - species    
    - legalId    
    - sex    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Animal/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori chiave animali NGSI-v2 Esempio  
Ecco un esempio di Animale in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "species": "sheep",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:sheep1"  
    }  
  ],  
  "legalId": "ES142589652140",  
  "birthdate": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "sex": "female",  
  "breed": "Merina",  
  "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "location": {  
    "type": "Point",  
    "coordinates": [-4.754444444, 41.640833333]  
  },  
  "weight": 65.3,  
  "ownedBy": "http://person.org/leon",  
  "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "phenologicalCondition": "maleAdult",  
  "reproductiveCondition": "inCalf",  
  "healthCondition": "healthy",  
  "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
  "welfareCondition": "adequate"  
}  
```  
</details>  
#### Animale NGSI-v2 normalizzato Esempio  
Ecco un esempio di Animale in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "species": {  
    "value": "sheep"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:sheep1"  
      }  
    ]  
  },  
  "legalId": {  
    "value": "ES142589652140"  
  },  
  "birthdate": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "sex": {  
    "value": "female"  
  },  
  "breed": {  
    "value": "Merina"  
  },  
  "calvedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "siredBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.754444444, 41.640833333]  
    }  
  },  
  "weight": {  
    "value": 65.3  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "value": "http://person.org/leon"  
  },  
  "locatedAt": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
  },  
  "phenologicalCondition": {  
    "value": "maleAdult"  
  },  
  "reproductiveCondition": {  
    "value": "inCalf"  
  },  
  "healthCondition": {  
    "value": "healthy"  
  },  
  "fedWith": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081"  
  },  
  "welfareCondition": {  
    "value": "adequate"  
  }  
}  
```  
</details>  
#### Valori chiave NGSI-LD animali Esempio  
Ecco un esempio di Animale in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "birthdate": {  
      "@type": "DateTime",  
      "@value": "2017-01-01T01:20:00Z"  
  },  
  "breed": "Merina",  
  "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
  "healthCondition": "healthy",  
  "legalId": "ES142589652140",  
  "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "location": {  
      "coordinates": [  
          -4.754444444,  
          41.640833333  
      ],  
      "type": "Point"  
  },  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "ownedBy": "http://person.org/leon",  
  "phenologicalCondition": "maleAdult",  
  "relatedSource": [  
      {  
          "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
          "applicationEntityId": "app:sheep1"  
      }  
  ],  
  "reproductiveCondition": "inCalf",  
  "sex": "female",  
  "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "species": "sheep",  
  "weight": 65.3,  
  "welfareCondition": "adequate",  
  "@context": [  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Animale NGSI-LD normalizzato Esempio  
Ecco un esempio di Animale in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "birthdate": {  
      "type": "Property",  
      "value": {  
          "@type": "DateTime",  
          "@value": "2017-01-01T01:20:00Z"  
      }  
  },  
  "breed": {  
      "type": "Property",  
      "value": "Merina"  
  },  
  "calvedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "fedWith": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081"  
  },  
  "healthCondition": {  
      "type": "Property",  
      "value": "healthy"  
  },  
  "legalId": {  
      "type": "Property",  
      "value": "ES142589652140"  
  },  
  "locatedAt": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
  },  
  "location": {  
      "type": "GeoProperty",  
      "value": {  
          "type": "Point",  
          "coordinates": [  
              -4.754444444,  
              41.640833333  
          ]  
      }  
  },  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "ownedBy": {  
      "type": "Relationship",  
      "object": "http://person.org/leon"  
  },  
  "phenologicalCondition": {  
      "type": "Property",  
      "value": "maleAdult"  
  },  
  "relatedSource": {  
      "type": "Property",  
      "value": [  
          {  
              "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
              "applicationEntityId": "app:sheep1"  
          }  
      ]  
  },  
  "reproductiveCondition": {  
      "type": "Property",  
      "value": "inCalf"  
  },  
  "sex": {  
      "type": "Property",  
      "value": "female"  
  },  
  "siredBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "species": {  
      "type": "Property",  
      "value": "sheep"  
  },  
  "weight": {  
      "type": "Property",  
      "value": 65.3  
  },  
  "welfareCondition": {  
      "type": "Property",  
      "value": "adequate"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
