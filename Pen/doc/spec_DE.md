<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Stift  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Pen/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eingezäunter Bereich in einem Gebäude oder einer Abteilung oder im Freien, in dem eine Gruppe von Tieren untergebracht ist. Die Tiere in einem Pferch können sich frei bewegen und interagieren. Die Ställe sind oft nicht vollständig voneinander getrennt (halbe Wände, Eisenstangen, Zäune,...), so dass Tiere aus benachbarten Ställen sich sehen/berühren können**  
Version: 0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `additionalInfo[array]`: Liste aller vom Sensor/Plattform gesendeten Rohwerte mit allen möglichen zusätzlichen Eigenschaften, die nicht in der Hauptstruktur enthalten sind. Es handelt sich um eine JSON-Struktur ähnlich der folgenden: {'Name': 'Temperatur', 'Wert' : 32}  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[date-time]`: Datum und Uhrzeit der Ankunft der Tiere im Stall  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `avgGrowth[number]`: Die durchschnittliche Gewichtszunahme des Tieres in dieser Bucht  . Model: [https://schema.org/Number](https://schema.org/Number)- `avgWeight[number]`: Das Durchschnittsgewicht des Tieres in diesem Pferch.  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: Eindeutige Kennung des Gebäudes, in dem sich der Artikel befindet  . Model: [https://schema.org/URL](https://schema.org/URL)- `co2[number]`: Die CO2-Konzentration im Artikel  . Model: [https://schema.org/Number](https://schema.org/Number)- `companyId[*]`: Eindeutige Kennung eines Unternehmens  . Model: [https://schema.org/URL](https://schema.org/URL)- `compartmentId[*]`: Eindeutige Kennung des Fachs, in dem sich der Stift befindet  . Model: [https://schema.org/URL](https://schema.org/URL)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `deadAnimalsSinceDateOfArrival[number]`: Anzahl der toten Tiere seit dem Tag der Ankunft  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Eine Beschreibung dieses Artikels  - `farmId[*]`: Eindeutige Kennung des Betriebs, in dem sich der Pferch befindet  . Model: [https://schema.org/URL](https://schema.org/URL)- `feedConsumption[number]`: Die Gesamtmenge an Futter, die von der/den Fütterungsstation(en) im Stall gefressen wurde; sie wird anhand der Futteraufnahme und der spezifischen Struktur gemessen, um jeweils nur ein Tier fressen zu lassen  . Model: [https://schema.org/Number](https://schema.org/Number)- `humidity[number]`: Menge, die die Menge an Wasserdampf in der Atmosphäre in dem Stift darstellt.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `lastUpdate[date-time]`: Datum und Uhrzeit, zu der die Messungen in der Position vorgenommen wurden  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `luminosity[number]`: Die Helligkeit einer Lichtquelle mit einer bestimmten Wellenlänge am Gegenstand  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `numAnimals[number]`: Anzahl der im Pferch enthaltenen Tiere  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `relatedSource[array]`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `sex[string]`: Das Geschlecht der Tiere in der Bucht  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `temperature[number]`: Temperatur des Stiftes.  Unirs:' Celsius Grad'  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI Entity type. es muss Pen sein  - `waterConsumption[number]`: Die gesamte Wassermenge, die aus dem Wasserhahn oder den Wasserhähnen im Stall austritt. Sie wird mit Hilfe von Durchflussmessern und einer speziellen Struktur gemessen, damit immer nur ein Tier gleichzeitig trinken kann.  . Model: [https://schema.org/Number](https://schema.org/Number)- `weightStDev[number]`: Die Standardabweichung in Bezug auf das Durchschnittsgewicht der in der Bucht enthaltenen Tiere  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `lastUpdate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pen:    
  description: 'Fenced area in a building or department or outside housing a group of animals. Animals in a pen can move and interact freely. Pens are often not completely separated from each other (half walls, iron bars, fences,…), making it possible that animals from neighbouring pens can see/touch'    
  properties:    
    additionalInfo:    
      description: 'list of all the raw values sent by the sensor/platform with all the possible extra properties that are not included in the main structure. It is a JSON structure similar to this: {''name'': ''temperature'', ''value'' : 32}'    
      items:    
        properties:    
          name:    
            type: string    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
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
    arrivalTimestamp:    
      description: Date and Time for the arrival of animals to the Pen    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    avgGrowth:    
      description: The average growth in weight of the animal in this pen    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    avgWeight:    
      description: 'The average weight of the animal in this Pen. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kg    
    buildingId:    
      anyOf:    
        - description: Identifier with format of any NGSI entity    
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
      description: Unique identifier of the Building the item is located in    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    co2:    
      description: The CO2 concentration in the item    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    companyId:    
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
      description: Unique identifier of a company    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    compartmentId:    
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
      description: Unique identifier of the Compartment the Pen is located in    
      x-ngsi:    
        model: https://schema.org/URL    
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
    deadAnimalsSinceDateOfArrival:    
      description: Number of dead animals since the date of arrival    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    farmId:    
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
      description: Unique identifier of the Farm the Pen is located in    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    feedConsumption:    
      description: The total amount of food that has been eaten from the feeding station(s) in the pen.It is measured through feed intakes and specific structure to let only one animal at a time to eat    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kg    
    humidity:    
      description: 'Quantity representing the amount of water vapour in the atmosphere in the pen. '    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    lastUpdate:    
      description: Date and time at which the measurements in the item were taken    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Seconds    
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
    luminosity:    
      description: The brightness of a light source of a certain wavelength at the item    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: LUX    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    numAnimals:    
      description: Number of animals contained in the Pen    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: The sex of the animals contained in the pen    
      enum:    
        - M    
        - F    
        - unknown    
        - ""    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the Pen.  Unirs:'' Celsius degree'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. it has to be Pen    
      enum:    
        - Pen    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: The total amount of water that came out from the tap or taps in the pen. It is measured through flowmeters and specific structure to let only one animal at a time drink    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    weightStDev:    
      description: The standard deviation associated to the average weight of the animals contained in the Pen    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - lastUpdate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Pen/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/Pen/schema.json    
  x-model-tags: ""    
  x-version: 0.2.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Stift NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Pen im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": "Pen",  
  "additionalInfo": [  
    {  
      "name": "Farm1FeedTray",  
      "value": 1  
    },  
    {  
      "name": "Farm1DepartmentId",  
      "value": "43"  
    },  
    {  
      "name": "Farm1ValveId",  
      "value": "69"  
    },  
    {  
      "name": "Farm1PenId",  
      "value": "1"  
    },  
    {  
      "name": "Farm1BuildingId",  
      "value": "2"  
    }  
  ],  
  "buildingId": "5ee3dbc8-343b-40a7-ac04-dec67215ff98",  
  "companyId": "4579b77f-31c1-44ef-b200-9a2407cc82e9",  
  "compartmentId": "ab8680c6-3e82-40fb-8577-f6a0ab717586",  
  "empty": false,  
  "farmId": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff",  
  "lastUpdate": "2020-04-12T20:44:55",  
  "sex": "",  
  "temperature": 25  
}  
```  
</details>  
#### Stift NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Pen im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": "Pen",  
  "additionalInfo": {  
    "type": "array",  
    "value": [  
      {  
        "name": "Farm1FeedTray",  
        "value": 1  
      },  
      {  
        "name": "Farm1DepartmentId",  
        "value": "43"  
      },  
      {  
        "name": "Farm1ValveId",  
        "value": "69"  
      },  
      {  
        "name": "Farm1PenId",  
        "value": "1"  
      },  
      {  
        "name": "Farm1BuildingId",  
        "value": "2"  
      }  
    ]  
  },  
  "buildingId": {  
    "type": "string",  
    "value": "5ee3dbc8-343b-40a7-ac04-dec67215ff98"  
  },  
  "companyId": {  
    "type": "string",  
    "value": "4579b77f-31c1-44ef-b200-9a2407cc82e9"  
  },  
  "compartmentId": {  
    "type": "string",  
    "value": "ab8680c6-3e82-40fb-8577-f6a0ab717586"  
  },  
  "empty": {  
    "type": "boolean",  
    "value": false  
  },  
  "farmId": {  
    "type": "string",  
    "value": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff"  
  },  
  "lastUpdate": {  
    "type": "string",  
    "value": "2020-04-12T20:44:55"  
  },  
  "sex": {  
    "type": "string",  
    "value": ""  
  },  
  "temperature": {  
    "type": "number",  
    "value": 25  
  }  
}  
```  
</details>  
#### Stift NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Pen im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
    "type": "Pen",  
    "additionalInfo": [  
        {  
            "name": "Farm1FeedTray",  
            "value": 1  
        },  
        {  
            "name": "Farm1DepartmentId",  
            "value": "43"  
        },  
        {  
            "name": "Farm1ValveId",  
            "value": "69"  
        },  
        {  
            "name": "Farm1PenId",  
            "value": "1"  
        },  
        {  
            "name": "Farm1BuildingId",  
            "value": "2"  
        }  
    ],  
    "buildingId": "5ee3dbc8-343b-40a7-ac04-dec67215ff98",  
    "companyId": "4579b77f-31c1-44ef-b200-9a2407cc82e9",  
    "compartmentId": "ab8680c6-3e82-40fb-8577-f6a0ab717586",  
    "empty": false,  
    "farmId": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff",  
    "lastUpdate": "2020-04-12T20:44:55",  
    "sex": "",  
    "temperature": 25,  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Stift NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Pen im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
    "type": "Pen",  
    "additionalInfo": {  
        "type": "Property",  
        "value": [  
            {  
                "name": "Farm1FeedTray",  
                "value": 1  
            },  
            {  
                "name": "Farm1DepartmentId",  
                "value": "43"  
            },  
            {  
                "name": "Farm1ValveId",  
                "value": "69"  
            },  
            {  
                "name": "Farm1PenId",  
                "value": "1"  
            },  
            {  
                "name": "Farm1BuildingId",  
                "value": "2"  
            }  
        ]  
    },  
    "buildingId": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:5ee3dbc8-343b-40a7-ac04-dec67215ff98"  
    },  
    "companyId": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:4579b77f-31c1-44ef-b200-9a2407cc82e9"  
    },  
    "compartmentId": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:ab8680c6-3e82-40fb-8577-f6a0ab717586"  
    },  
    "empty": {  
        "type": "Property",  
        "value": "false"  
    },  
    "farmId": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:3b6473e3-fdc9-4646-b1cf-d41e3af58eff"  
    },  
    "lastUpdate": {  
        "type": "Property",  
        "value": "2020-04-12T20:44:55"  
    },  
    "sex": {  
        "type": "Property",  
        "value": ""  
    },  
    "temperature": {  
        "type": "Property",  
        "value": 25  
    },  
    "@context": [  
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
