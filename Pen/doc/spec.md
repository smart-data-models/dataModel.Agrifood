<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: Pen    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Pen/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Fenced area in a building or department or outside housing a group of animals. Animals in a pen can move and interact freely. Pens are often not completely separated from each other (half walls, iron bars, fences,…), making it possible that animals from neighbouring pens can see/touch**    
version: 0.2.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `additionalInfo[array]`: list of all the raw values sent by the sensor/platform with all the possible extra properties that are not included in the main structure. It is a JSON structure similar to this: {'name': 'temperature', 'value' : 32}  - `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[date-time]`: Date and Time for the arrival of animals to the Pen  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `avgGrowth[number]`: The average growth in weight of the animal in this pen  . Model: [https://schema.org/Number](https://schema.org/Number)- `avgWeight[number]`: The average weight of the animal in this Pen.   . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: Unique identifier of the Building the item is located in  . Model: [https://schema.org/URL](https://schema.org/URL)- `co2[number]`: The CO2 concentration in the item  . Model: [https://schema.org/Number](https://schema.org/Number)- `companyId[*]`: Unique identifier of a company  . Model: [https://schema.org/URL](https://schema.org/URL)- `compartmentId[*]`: Unique identifier of the Compartment the Pen is located in  . Model: [https://schema.org/URL](https://schema.org/URL)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `deadAnimalsSinceDateOfArrival[number]`: Number of dead animals since the date of arrival  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: A description of this item  - `farmId[*]`: Unique identifier of the Farm the Pen is located in  . Model: [https://schema.org/URL](https://schema.org/URL)- `feedConsumption[number]`: The total amount of food that has been eaten from the feeding station(s) in the pen.It is measured through feed intakes and specific structure to let only one animal at a time to eat  . Model: [https://schema.org/Number](https://schema.org/Number)- `humidity[number]`: Quantity representing the amount of water vapour in the atmosphere in the pen.   . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Unique identifier of the entity  - `lastUpdate[date-time]`: Date and time at which the measurements in the item were taken  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `luminosity[number]`: The brightness of a light source of a certain wavelength at the item  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: The name of this item  - `numAnimals[number]`: Number of animals contained in the Pen  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `relatedSource[array]`: List of IDs the current entity may have in external applications  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `sex[string]`: The sex of the animals contained in the pen  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `temperature[number]`: Temperature of the Pen.  Unirs:' Celsius degree'  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI Entity type. it has to be Pen  - `waterConsumption[number]`: The total amount of water that came out from the tap or taps in the pen. It is measured through flowmeters and specific structure to let only one animal at a time drink  . Model: [https://schema.org/Number](https://schema.org/Number)- `weightStDev[number]`: The standard deviation associated to the average weight of the animals contained in the Pen  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `lastUpdate`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
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
## Example payloads      
#### Pen NGSI-v2 key-values Example      
Here is an example of a Pen in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
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
#### Pen NGSI-v2 normalized Example      
Here is an example of a Pen in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": "Pen",  
  "additionalInfo": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "5ee3dbc8-343b-40a7-ac04-dec67215ff98"  
  },  
  "companyId": {  
    "type": "Text",  
    "value": "4579b77f-31c1-44ef-b200-9a2407cc82e9"  
  },  
  "compartmentId": {  
    "type": "Text",  
    "value": "ab8680c6-3e82-40fb-8577-f6a0ab717586"  
  },  
  "empty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "farmId": {  
    "type": "Text",  
    "value": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff"  
  },  
  "lastUpdate": {  
    "type": "DateTime",  
    "value": "2020-04-12T20:44:55"  
  },  
  "sex": {  
    "type": "Text",  
    "value": ""  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 25  
  }  
}  
```  
</details>    
#### Pen NGSI-LD key-values Example      
Here is an example of a Pen in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
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
#### Pen NGSI-LD normalized Example      
Here is an example of a Pen in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
