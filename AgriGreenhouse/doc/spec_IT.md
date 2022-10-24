<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AgriGreenhouse  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriGreenhouse/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata delle condizioni registrate all'interno di una serra generica, un tipo di AgriParcel.**  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `alternateName[string]`: Un nome alternativo per questa voce  - `belongsTo[*]`: Entità a cui appartiene la serra  - `co2[integer]`: La concentrazione interna di C02 misurata nominalmente in mg/L  . Model: [http://schema.org/Number](http://schema.org/Number)- `dailyLight[integer]`: Luce giornaliera accumulata misurata in kW per metro quadro  . Model: [http://schema.org/Number](http://schema.org/Number)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `drainFlow[object]`: La portata di scarico osservata in litri al secondo  . Model: [http://schema.org/Number](http://schema.org/Number)- `hasAgriParcelChildren[array]`: Registri sub AgriParcel correlati a cui questa entità si riferisce  - `hasAgriParcelParent[*]`: Riferimento all'entità AgriParcel a cui si riferisce questa entità.  - `hasDevice[array]`: Riferimento ai dispositivi IoT associati a questa serra, ad esempio sensori e controlli.  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasWaterQualityObserved[array]`: Riferimento a uno o più registri di osservazione della qualità dell'acqua aggiornati per questa entità.  - `hasWeatherObserved[*]`: Riferimento al record di osservazione meteorologica corrente per questa entità.  - `id[*]`: Identificatore univoco dell'entità  - `leafTemperature[integer]`: L'umidità relativa interna espressa come numero compreso tra 0 e 1 che rappresenta un intervallo da 0% a 100 (%).<br/><br/>0 <= relativeHumidity <= 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `name[string]`: Il nome di questo elemento.  - `ownedBy[*]`: Proprietario (persona o organizzazione) della serra agricola  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `relatedSource[array]`: Elenco di ID che l'entità corrente può avere in applicazioni esterne.  - `relativeHumidity[number]`: La temperatura media dell'aria della serra, nominalmente espressa in gradi centigradi.  . Model: [http://schema.org/Number](http://schema.org/Number)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NGSI. Deve essere AgriGreenhouse  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `hasAgriParcelParent`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questa entità è principalmente associata al settore agricolo verticale e alle relative applicazioni IoT.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriGreenhouse:    
  description: 'This entity contains a harmonised description of the conditions recorded within a generic greenhouse, a type of AgriParcel.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    belongsTo:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Entity the Greenhouse belongs to'    
      x-ngsi:    
        type: Relationship    
    co2:    
      description: 'The measured interior C02 concentration nominally in mg/L'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: mg/L    
    dailyLight:    
      description: 'Daily Accumulated light measured in kW per square metre'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kw/m2    
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
    drainFlow:    
      description: 'The observed drain flow rate in litres per second'    
      properties:    
        maxValue:    
          minimum: 0    
          type: number    
        minValue:    
          minimum: 0    
          type: number    
        unitText:    
          type: string    
        value:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: L/s    
    hasAgriParcelChildren:    
      description: 'Related sub AgriParcel records to which this entity relates'    
      items:    
        anyOf: &agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
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
    hasAgriParcelParent:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the AgriParcel entity to which this entity relates'    
      x-ngsi:    
        type: Relationship    
    hasDevice:    
      description: 'Reference to the IoT devices associated with this greenhouse i.e. sensors, controls.'    
      items:    
        anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasWaterQualityObserved:    
      description: 'Reference to one or more water quality observation records current for this entity'    
      items:    
        anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Relationship    
    hasWeatherObserved:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the weather observation record current for this entity'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    leafTemperature:    
      description: 'The inside relative humidity expressed as a number between 0 and 1 representing the range 0% to 100 (%).<br/><br/>0 <= relativeHumidity <= 1'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    ownedBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Owner (Person or Organization) of the AgriGreenhouse'    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        properties:    
          application:    
            anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          applicationEntityId:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    relativeHumidity:    
      description: 'The average greenhouse air temperature nominally in degrees centigrade.'    
      maximum: 1.0    
      minimum: 0.0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Degrees centigrade'    
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
      description: 'NGSI Entity Type. It has to be AgriGreenhouse'    
      enum:    
        - AgriGreenhouse    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasAgriParcelParent    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriGreenhouse/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriGreenhouse/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### AgriGreenhouse NGSI-v2 valori-chiave Esempio  
Ecco un esempio di una serra in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriGreenhouse",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:greenhouse1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agrigreenhouse",  
    "https://datamodel.org/example/agrigreenhouse"  
  ],  
  "belongsTo": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765",  
  "hasAgriParcelParent": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b",  
  "hasAgriParcelChildren": [  
    "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
    "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
  ],  
  "hasWeatherObserved": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d",  
  "hasWaterQualityObserved": [  
    "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
    "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
  ],  
  "relativeHumidity": 0.4,  
  "leafTemperature": 22,  
  "co2": 28,  
  "dailyLight": 24,  
  "drainFlow": {  
    "value": 33,  
    "maxValue": 50,  
    "minValue": 25,  
    "unitText": "Litre per second"  
  },  
  "hasDevice": [  
    "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
    "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
    "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
    "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
  ]  
}  
```  
</details>  
#### AgriGreenhouse NGSI-v2 normalizzato Esempio  
Ecco un esempio di AgriGreenhouse in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriGreenhouse",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:greenhouse1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/agrigreenhouse",  
      "https://datamodel.org/example/agrigreenhouse"  
    ]  
  },  
  "belongsTo": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
  },  
  "hasAgriParcelParent": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b"  
  },  
  "hasAgriParcelChildren": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
      "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
    ]  
  },  
  "hasWeatherObserved": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d"  
  },  
  "hasWaterQualityObserved": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
      "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
    ]  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "leafTemperature": {  
    "type": "Property",  
    "value": 22  
  },  
  "co2": {  
    "type": "Property",  
    "value": 28  
  },  
  "dailyLight": {  
    "type": "Property",  
    "value": 24  
  },  
  "drainFlow": {  
    "type": "Property",  
    "value": {  
      "value": 33,  
      "maxValue": 50,  
      "minValue": 25,  
      "unitText": "Litre per second"  
    }  
  },  
  "hasDevice": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
      "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
      "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
      "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
    ]  
  }  
}  
```  
</details>  
#### AgriGreenhouse NGSI-LD valori-chiave Esempio  
Ecco un esempio di una serra in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriGreenhouse",  
    "belongsTo": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765",  
    "co2": 28,  
    "createdAt": "2017-01-01T01:20:00Z",  
    "dailyLight": 24,  
    "drainFlow": {  
        "maxValue": 50,  
        "minValue": 25,  
        "unitText": "Litre per second",  
        "value": 33  
    },  
    "hasAgriParcelChildren": [  
        "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
        "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
    ],  
    "hasAgriParcelParent": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b",  
    "hasDevice": [  
        "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
        "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
        "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
        "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
    ],  
    "hasWaterQualityObserved": [  
        "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
        "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
    ],  
    "hasWeatherObserved": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d",  
    "leafTemperature": 22,  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
    "relatedSource": [  
        {  
            "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
            "applicationEntityId": "app:greenhouse1"  
        }  
    ],  
    "relativeHumidity": 0.4,  
    "seeAlso": [  
        "https://example.org/concept/agrigreenhouse",  
        "https://datamodel.org/example/agrigreenhouse"  
    ],  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AgriGreenhouse NGSI-LD normalizzato Esempio  
Ecco un esempio di AgriGreenhouse in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriGreenhouse",  
    "belongsTo": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
    },  
    "co2": {  
        "type": "Property",  
        "value": 28,  
        "unitCode": "M1",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "createdAt": "2017-01-01T01:20:00Z",  
    "dailyLight": {  
        "type": "Property",  
        "value": 24,  
        "unitCode": "N78",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "drainFlow": {  
        "type": "Property",  
        "value": {  
            "value": 33,  
            "maxValue": 50,  
            "minValue": 25,  
            "unitText": "Litre per second"  
        },  
        "unitCode": "G51",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "hasAgriParcelChildren": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
            "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
        ]  
    },  
    "hasAgriParcelParent": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b"  
    },  
    "hasDevice": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
            "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
            "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
            "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
        ]  
    },  
    "hasWaterQualityObserved": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
            "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
        ]  
    },  
    "hasWeatherObserved": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d"  
    },  
    "leafTemperature": {  
        "type": "Property",  
        "value": 22,  
        "unitCode": "CEL",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "ownedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:greenhouse1"  
            }  
        ]  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.4,  
        "unitCode": "C62",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agrigreenhouse",  
            "https://datamodel.org/example/agrigreenhouse"  
        ]  
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
