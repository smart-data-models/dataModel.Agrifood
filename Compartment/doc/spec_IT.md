<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Compartimento  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Compartment/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Area artificiale in un edificio o in un reparto che viene misurata da determinati sensori. Un compartimento non è necessariamente un separatore fisico. Può essere un reparto o un raggruppamento di più penne all'interno di un reparto che vengono misurate dallo stesso sensore **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `additionalInfo[array]`: elenco di tutti i valori grezzi inviati dal sensore/piattaforma con tutte le possibili proprietà extra non incluse nella struttura principale. Si tratta di una struttura JSON simile a questa: {"temperatura": "32", "umidità": "42"}.  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[string]`: Data e ora in cui l'animale è stato inserito nel compartimento  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `avgGrowth[number]`: La crescita media di peso degli animali in questo compartimento  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `avgWeight[number]`: Il peso medio dei suini in questo compartimento  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: Identificatore univoco dell'edificio in cui si trova il comparto  - `co2[number]`: La concentrazione di CO2 nel compartimento  - `companyId[*]`: Identificatore univoco di un'azienda  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `empty[boolean]`: Valore vero/falso se lo scomparto è vuoto  - `farmId[*]`: Identificatore univoco di un'azienda agricola in cui si trova il compartimento  - `feedConsumption[number]`: La quantità totale di cibo consumato dalle stazioni di alimentazione nel compartimento.  - `humidity[number]`: Quantità che rappresenta la quantità di vapore acqueo presente nell'atmosfera del compartimento.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `lastUpdate[number]`: Data e ora in cui sono state effettuate le misurazioni nello scomparto. Timestamp Unix  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `luminosity[number]`: La luminosità di una sorgente luminosa di una certa lunghezza d'onda al comparto  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Il nome di questo elemento.  - `numAnimals[number]`: Numero di animali nel compartimento  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `parentCompartmentId[*]`: Identificatore univoco dello scomparto di cui fa parte questo scomparto. Viene utilizzato solo quando un compartimento contiene altri compartimenti.  - `relatedSource[array]`: Elenco di ID che l'entità corrente può avere in applicazioni esterne.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sex[string]`: Il sesso degli animali contenuti nello scomparto  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `temperature[number]`: Temperatura dello scomparto.  - `type[string]`: Tipo di entità NGSI. deve essere Compartimento.  - `waterConsumption[number]`: La quantità totale di acqua che è uscita dal rubinetto o dai rubinetti del compartimento  - `weightStDev[number]`: La deviazione standard associata al peso medio dei suini/suinetti contenuti nel compartimento  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `lastUpdate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Compartment:    
  description: 'Artificial area in a building or department that is measured by certain sensors. A compartment is not necessarily a physical separator. It can be a department or a grouping of several pens within a department that are being measured by the same sensor.'    
  properties:    
    additionalInfo:    
      description: 'list of all the raw values sent by the sensor/platform with all the possible extra properties that are not included in the main structure. It is a JSON structure similar to this: { ''temperature'': ''32'', ''humidity'':''42''}'    
      items:    
        properties:    
          parameter:    
            type: string    
          value:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arrivalTimestamp:    
      description: 'Date and Time at which the animal were inserted in the compartment'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    avgGrowth:    
      description: 'The average growth in weight of the animals in this compartment'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    avgWeight:    
      description: 'The average weight of the pigs in this compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    buildingId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of a building the compartment is located in'    
      x-ngsi:    
        type: Relationship    
    co2:    
      description: 'The CO2 concentration in the compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    companyId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of a company'    
      x-ngsi:    
        type: Relationship    
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
    empty:    
      description: 'True/False value if the compartment is empty'    
      type: boolean    
      x-ngsi:    
        type: Property    
    farmId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of a farm where the compartment is located in'    
      x-ngsi:    
        type: Relationship    
    feedConsumption:    
      description: 'The total amount of food that has been eaten from the feeding station(s) in the compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    humidity:    
      description: 'Quantity representing the amount of water vapour in the atmosphere in the compartment'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &compartment_-_properties_-_owner_-_items_-_anyof    
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
    lastUpdate:    
      description: 'Date and time at which the measurements in the compartment were taken. Unix timestamp'    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    luminosity:    
      description: 'The brightness of a light source of a certain wavelength at the compartment'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numAnimals:    
      description: 'Number of animals in the compartment'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *compartment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    parentCompartmentId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the  compartment where this compartment is a part of. It is used only when a compartment contains other compartments'    
      x-ngsi:    
        type: Relationship    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        properties:    
          application:    
            anyOf: *compartment_-_properties_-_owner_-_items_-_anyof    
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
    sex:    
      description: 'The sex of the animals contained in the compartment'    
      enum:    
        - M    
        - F    
        - unknown    
        - ""    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the compartment.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be Compartment'    
      enum:    
        - Compartment    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: 'The total amount of water that came out from the tap or taps in the compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    weightStDev:    
      description: 'The standard deviation associated to the average weight of the pigs/piglets contained in the compartment'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - lastUpdate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Compartment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/Compartment/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Compartimento NGSI-v2 valori-chiave Esempio  
Ecco un esempio di un Compartimento in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "a88c6069-86c4-4c09-8621-fc5c58f216e0",  
  "type": "Compartment",  
  "additionalInfo": [  
    {  
      "name": "Farm2FeedTray",  
      "value": "4"  
    },  
    {  
      "name": "Farm2ValveId",  
      "value": ""  
    },  
    {  
      "name": "Farm2DepartmentId",  
      "value": "11"  
    }  
  ],  
  "arrivalTimestamp": "2020-04-14T22:00:00.000Z",  
  "avgGrowth": 1.0,  
  "avgWeight": 45.5,  
  "buildingId": "f6ce5251-e959-4269-9040-8056c6a093d9",  
  "co2": 20,  
  "companyId": "1401c9e0-c441-4bd1-b8d3-fb1194479aa7",  
  "empty": false,  
  "farmId": "7438345c-fdff-45c9-a02f-1d764cbc03a7",  
  "feedConsumption": 8.3,  
  "humidity": 0.7,  
  "lastUpdate": 1589841011000,  
  "luminosity": 3,  
  "name": "",  
  "numAnimals": 22,  
  "outputFeed": 8.2,  
  "parentCompartmentId": "f0ddd929-5a18-479b-9ad6-5947cc2cd05b",  
  "sex": "",  
  "startWeight": 26,  
  "temperature": 25,  
  "waterConsumption": 23,  
  "weightStDev": 2.3  
}  
```  
</details>  
#### Compartimento NGSI-v2 normalizzato Esempio  
Ecco un esempio di un Compartimento in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "a88c6069-86c4-4c09-8621-fc5c58f216e0"  
  ,  
  "type": "Compartment",  
  "additionalInfo": {  
    "type": "array",  
    "value": [  
      {  
        "name": "Farm2FeedTray",  
        "value": "4"  
      },  
      {  
        "name": "Farm2ValveId",  
        "value": ""  
      },  
      {  
        "name": "Farm2DepartmentId",  
        "value": "11"  
      }  
    ]  
  },  
  "arrivalTimestamp": {  
    "type": "string",  
    "value": "2020-04-14T22:00:00.000Z"  
  },  
  "avgGrowth": {  
    "type": "number",  
    "value": 4  
  },  
  "avgWeight": {  
    "type": "number",  
    "value": 45.5  
  },  
  "buildingId": {  
    "type": "string",  
    "value": "f6ce5251-e959-4269-9040-8056c6a093d9"  
  },  
  "co2": {  
    "type": "number",  
    "value": 20  
  },  
  "companyId": {  
    "type": "string",  
    "value": "1401c9e0-c441-4bd1-b8d3-fb1194479aa7"  
  },  
  "empty": {  
    "type": "boolean",  
    "value": false  
  },  
  "farmId": {  
    "type": "string",  
    "value": "7438345c-fdff-45c9-a02f-1d764cbc03a7"  
  },  
  "feedConsumption": {  
    "type": "number",  
    "value": 8.3  
  },  
  "humidity": {  
    "type": "number",  
    "value": 0.7  
  },  
  "lastUpdate": {  
    "type": "number",  
    "value": 1589841011000  
  },  
  "luminosity": {  
    "type": "number",  
    "value": 3  
  },  
  "name": {  
    "type": "string",  
    "value": ""  
  },  
  "numAnimals": {  
    "type": "number",  
    "value": 22  
  },  
  "outputFeed": {  
    "type": "number",  
    "value": 8.2  
  },  
  "parentCompartmentId": {  
    "type": "string",  
    "value": "f0ddd929-5a18-479b-9ad6-5947cc2cd05b"  
  },  
  "sex": {  
    "type": "string",  
    "value": ""  
  },  
  "startWeight": {  
    "type": "number",  
    "value": 26  
  },  
  "temperature": {  
    "type": "number",  
    "value": 25  
  },  
  "waterConsumption": {  
    "type": "number",  
    "value": 23  
  },  
  "weightStDev": {  
    "type": "number",  
    "value": 2.3  
  }  
}  
```  
</details>  
#### Compartimento NGSI-LD valori-chiave Esempio  
Ecco un esempio di un Compartimento in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:a88c6069-86c4-4c09-8621-fc5c58f216e0:001",  
    "type": "Compartment",  
    "additionalInfo": [  
        {  
            "name": "Farm2FeedTray",  
            "value": "4"  
        },  
        {  
            "name": "Farm2ValveId",  
            "value": ""  
        },  
        {  
            "name": "Farm2DepartmentId",  
            "value": "11"  
        }  
    ],  
    "arrivalTimestamp": "2020-04-14T22:00:00.000Z",  
    "avgGrowth": 1.0,  
    "avgWeight": 45.5,  
    "buildingId": "urn:ngsi-ld:f6ce5251-e959-4269-9040-8056c6a093d9:001",  
    "co2": 20,  
    "companyId": "urn:ngsi-ld:1401c9e0-c441-4bd1-b8d3-fb1194479aa7:002",  
    "empty": false,  
    "farmId": "urn:ngsi-ld:7438345c-fdff-45c9-a02f-1d764cbc03a7:005",  
    "feedConsumption": 8.3,  
    "humidity": 0.7,  
    "lastUpdate": 1589841011000,  
    "luminosity": 3,  
    "name": "",  
    "numAnimals": 22,  
    "outputFeed": 8.2,  
    "parentCompartmentId": "urn:ngsi-ld:f0ddd929-5a18-479b-9ad6-5947cc2cd05b:001",  
    "sex": "",  
    "startWeight": 26,  
    "temperature": 25,  
    "waterConsumption": 23,  
    "weightStDev": 2.3,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Compartimento NGSI-LD normalizzato Esempio  
Ecco un esempio di un Compartimento in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:a88c6069-86c4-4c09-8621-fc5c58f216e0:001",  
    "type": "Compartment",  
    "additionalInfo": {  
        "type": "array",  
        "value": [  
            {  
                "name": "Farm2FeedTray",  
                "value": "4"  
            },  
            {  
                "name": "Farm2ValveId",  
                "value": ""  
            },  
            {  
                "name": "Farm2DepartmentId",  
                "value": "11"  
            }  
        ]  
    },  
    "arrivalTimestamp": {  
        "type": "string",  
        "value": "2020-04-14T22:00:00.000Z"  
    },  
    "avgGrowth": {  
        "type": "boolean",  
        "value": true  
    },  
    "avgWeight": {  
        "type": "number",  
        "value": 45.5  
    },  
    "buildingId": {  
        "type": "string",  
        "value": "f6ce5251-e959-4269-9040-8056c6a093d9"  
    },  
    "co2": {  
        "type": "number",  
        "value": 20  
    },  
    "companyId": {  
        "type": "string",  
        "value": "urn:ngsi-ld:1401c9e0-c441-4bd1-b8d3-fb1194479aa7:007"  
    },  
    "empty": {  
        "type": "boolean",  
        "value": false  
    },  
    "farmId": {  
        "type": "string",  
        "value": "urn:ngsi-ld:7438345c-fdff-45c9-a02f-1d764cbc03a7:001"  
    },  
    "feedConsumption": {  
        "type": "number",  
        "value": 8.3  
    },  
    "humidity": {  
        "type": "number",  
        "value": 0.7  
    },  
    "lastUpdate": {  
        "type": "number",  
        "value": 1589841011000  
    },  
    "luminosity": {  
        "type": "number",  
        "value": 3  
    },  
    "name": {  
        "type": "string",  
        "value": ""  
    },  
    "numAnimals": {  
        "type": "number",  
        "value": 22  
    },  
    "outputFeed": {  
        "type": "number",  
        "value": 8.2  
    },  
    "parentCompartmentId": {  
        "type": "string",  
        "value": "urn:ngsi-ld:f0ddd929-5a18-479b-9ad6-5947cc2cd05b:001"  
    },  
    "sex": {  
        "type": "string",  
        "value": ""  
    },  
    "startWeight": {  
        "type": "number",  
        "value": 26  
    },  
    "temperature": {  
        "type": "number",  
        "value": 25  
    },  
    "waterConsumption": {  
        "type": "number",  
        "value": 23  
    },  
    "weightStDev": {  
        "type": "number",  
        "value": 2.3  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
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
