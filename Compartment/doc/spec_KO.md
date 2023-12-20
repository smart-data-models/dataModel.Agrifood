<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

==========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->


- `additionalInfo[array]`: 기본 구조에 포함되지 않은 모든 가능한 추가 속성과 함께 센서/플랫폼에서 전송한 모든 원시 값의 목록입니다. 다음과 유사한 JSON 구조입니다: { '온도': '32', '습도':'42'}  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>      

Compartment:      
  description: Artificial area in a building or department that is measured by certain sensors. A compartment is not necessarily a physical separator. It can be a department or a grouping of several pens within a department that are being measured by the same sensor.      
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
      description: Date and Time at which the animal were inserted in the compartment      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Datetime      
        type: Property      
    avgGrowth:      
      description: The average growth in weight of the animals in this compartment      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    avgWeight:      
      description: The average weight of the pigs in this compartment      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    buildingId:      
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
      description: Unique identifier of a building the compartment is located in      
      x-ngsi:      
        type: Relationship      
    co2:      
      description: The CO2 concentration in the compartment      
      minimum: 0      
      type: number      
      x-ngsi:      
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
    empty:      
      description: True/False value if the compartment is empty      
      type: boolean      
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
      description: Unique identifier of a farm where the compartment is located in      
      x-ngsi:      
        type: Relationship      
    feedConsumption:      
      description: The total amount of food that has been eaten from the feeding station(s) in the compartment      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    humidity:      
      description: Quantity representing the amount of water vapour in the atmosphere in the compartment      
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
      description: Date and time at which the measurements in the compartment were taken. Unix timestamp      
      type: number      
      x-ngsi:      
        type: Property      
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
      description: The brightness of a light source of a certain wavelength at the compartment      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    numAnimals:      
      description: Number of animals in the compartment      
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
    parentCompartmentId:      
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
      description: Unique identifier of the  compartment where this compartment is a part of. It is used only when a compartment contains other compartments      
      x-ngsi:      
        type: Relationship      
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
      description: The sex of the animals contained in the compartment      
      enum:      
        - M      
        - F      
        - unknown      
        - ""      
      type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    temperature:      
      description: Temperature of the compartment      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. it has to be Compartment      
      enum:      
        - Compartment      
      type: string      
      x-ngsi:      
        type: Property      
    waterConsumption:      
      description: The total amount of water that came out from the tap or taps in the compartment      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    weightStDev:      
      description: The standard deviation associated to the average weight of the pigs/piglets contained in the compartment      
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



<details><summary><strong>show/hide example</strong></summary>      


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


<details><summary><strong>show/hide example</strong></summary>      


  "id": "a88c6069-86c4-4c09-8621-fc5c58f216e0",  
  "type": "Compartment",  
  "additionalInfo": {  
    "type": "StructuredValue",  
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
    "type": "DateTime",  
    "value": "2020-04-14T22:00:00.000Z"  
  },  
  "avgGrowth": {  
    "type": "Number",  
    "value": 4  
  },  
  "avgWeight": {  
    "type": "Number",  
    "value": 45.5  
  },  
  "buildingId": {  
    "type": "Text",  
    "value": "f6ce5251-e959-4269-9040-8056c6a093d9"  
  },  
  "co2": {  
    "type": "Number",  
    "value": 20  
  },  
  "companyId": {  
    "type": "Text",  
    "value": "1401c9e0-c441-4bd1-b8d3-fb1194479aa7"  
  },  
  "empty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "farmId": {  
    "type": "Text",  
    "value": "7438345c-fdff-45c9-a02f-1d764cbc03a7"  
  },  
  "feedConsumption": {  
    "type": "Number",  
    "value": 8.3  
  },  
  "humidity": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "lastUpdate": {  
    "type": "Number",  
    "value": 1589841011000  
  },  
  "luminosity": {  
    "type": "Number",  
    "value": 3  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "numAnimals": {  
    "type": "Number",  
    "value": 22  
  },  
  "outputFeed": {  
    "type": "Number",  
    "value": 8.2  
  },  
  "parentCompartmentId": {  
    "type": "Text",  
    "value": "f0ddd929-5a18-479b-9ad6-5947cc2cd05b"  
  },  
  "sex": {  
    "type": "Text",  
    "value": ""  
  },  
  "startWeight": {  
    "type": "Number",  
    "value": 26  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 25  
  },  
  "waterConsumption": {  
    "type": "Number",  
    "value": 23  
  },  
  "weightStDev": {  
    "type": "Number",  
    "value": 2.3  
  }  
}  
```  
</details>    


<details><summary><strong>show/hide example</strong></summary>      


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


<details><summary><strong>show/hide example</strong></summary>      


  "id": "urn:ngsi-ld:a88c6069-86c4-4c09-8621-fc5c58f216e0:001",  
  "type": "Compartment",  
  "additionalInfo": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": "2020-04-14T22:00:00.000Z"  
  },  
  "avgGrowth": {  
    "type": "Property",  
    "value": true  
  },  
  "avgWeight": {  
    "type": "Property",  
    "value": 45.5  
  },  
  "buildingId": {  
    "type": "Property",  
    "value": "f6ce5251-e959-4269-9040-8056c6a093d9"  
  },  
  "co2": {  
    "type": "Property",  
    "value": 20  
  },  
  "companyId": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:1401c9e0-c441-4bd1-b8d3-fb1194479aa7:007"  
  },  
  "empty": {  
    "type": "Property",  
    "value": false  
  },  
  "farmId": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:7438345c-fdff-45c9-a02f-1d764cbc03a7:001"  
  },  
  "feedConsumption": {  
    "type": "Property",  
    "value": 8.3  
  },  
  "humidity": {  
    "type": "Property",  
    "value": 0.7  
  },  
  "lastUpdate": {  
    "type": "Property",  
    "value": 1589841011000  
  },  
  "luminosity": {  
    "type": "Property",  
    "value": 3  
  },  
  "name": {  
    "type": "Property",  
    "value": ""  
  },  
  "numAnimals": {  
    "type": "Property",  
    "value": 22  
  },  
  "outputFeed": {  
    "type": "Property",  
    "value": 8.2  
  },  
  "parentCompartmentId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:f0ddd929-5a18-479b-9ad6-5947cc2cd05b:001"  
  },  
  "sex": {  
    "type": "Property",  
    "value": ""  
  },  
  "startWeight": {  
    "type": "Property",  
    "value": 26  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 25  
  },  
  "waterConsumption": {  
    "type": "Property",  
    "value": 23  
  },  
  "weightStDev": {  
    "type": "Property",  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---    
