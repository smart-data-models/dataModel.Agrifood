<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Compartiment  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Compartment/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Zone artificielle dans un bâtiment ou un service qui est mesurée par certains capteurs. Un compartiment n'est pas nécessairement un séparateur physique. Il peut s'agir d'un département ou d'un regroupement de plusieurs enclos dans un département qui sont mesurés par le même capteur.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `additionalInfo[array]`: liste de toutes les valeurs brutes envoyées par le capteur/la plateforme avec toutes les propriétés supplémentaires éventuelles qui ne sont pas incluses dans la structure principale. Il s'agit d'une structure JSON similaire à celle-ci : {'température' : '32', 'humidité' : '42'}  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[string]`: Date et heure auxquelles l'animal a été inséré dans le compartiment  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `avgGrowth[number]`: La croissance moyenne du poids des animaux de ce compartiment  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `avgWeight[number]`: Le poids moyen des porcs dans ce compartiment  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: Identifiant unique d'un bâtiment dans lequel le compartiment est situé  - `co2[number]`: La concentration de CO2 dans le compartiment  - `companyId[*]`: Identifiant unique d'une entreprise  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `empty[boolean]`: Valeur True/False si le compartiment est vide  - `farmId[*]`: Identifiant unique d'une exploitation agricole où se trouve le compartiment dans  - `feedConsumption[number]`: La quantité totale de nourriture qui a été consommée à partir de la ou des stations d'alimentation du compartiment.  - `humidity[number]`: Quantité représentant la quantité de vapeur d'eau dans l'atmosphère du compartiment.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `lastUpdate[number]`: Date et heure auxquelles les mesures du compartiment ont été effectuées. Horodatage Unix  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `luminosity[number]`: La luminosité d'une source lumineuse d'une certaine longueur d'onde au compartiment  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément.  - `numAnimals[number]`: Nombre d'animaux dans le compartiment  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `parentCompartmentId[*]`: Identifiant unique du compartiment dont ce compartiment fait partie. Il n'est utilisé que lorsqu'un compartiment contient d'autres compartiments.  - `relatedSource[array]`: Liste des identifiants que l'entité actuelle peut avoir dans des applications externes  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `sex[string]`: Le sexe des animaux contenus dans le compartiment  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `temperature[number]`: Température du compartiment.  - `type[string]`: Type d'entité NGSI. Il doit s'agir d'un compartiment.  - `waterConsumption[number]`: La quantité totale d'eau qui est sortie du ou des robinets du compartiment.  - `weightStDev[number]`: L'écart-type associé au poids moyen des porcs/porcelets contenus dans le compartiment.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `lastUpdate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Compartiment Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de Compartiment au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Compartiment NGSI-v2 normalisé Exemple  
Voici un exemple de Compartiment au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Compartiment Valeurs-clés NGSI-LD Exemple  
Voici un exemple de compartiment au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Compartiment NGSI-LD normalisé Exemple  
Voici un exemple de Compartiment au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
