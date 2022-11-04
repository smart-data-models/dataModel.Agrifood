<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Pen  
============<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Pen/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Área cercada en un edificio o departamento o en el exterior que alberga un grupo de animales. Los animales de un corral pueden moverse e interactuar libremente. Los corrales a menudo no están completamente separados unos de otros (medias paredes, barras de hierro, vallas,...), lo que hace posible que los animales de los corrales vecinos puedan verse/tocarse**.  
versión: 0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `additionalInfo[array]`: lista de todos los valores crudos enviados por el sensor/plataforma con todas las posibles propiedades extra que no están incluidas en la estructura principal. Es una estructura JSON similar a esta: {'nombre': 'temperatura', 'valor' : 32}  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[string]`: Fecha y hora de llegada de los animales al corral  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `avgGrowth[number]`: El crecimiento medio del peso del animal en este corral  . Model: [https://schema.org/Number](https://schema.org/Number)- `avgWeight[number]`: El peso medio del animal en este corral.  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: Identificador único del edificio en el que se encuentra el artículo  . Model: [https://schema.org/URL.](https://schema.org/URL.)- `co2[number]`: La concentración de CO2 en el artículo  . Model: [https://schema.org/Number](https://schema.org/Number)- `companyId[*]`: Identificador único de una empresa  . Model: [https://schema.org/URL](https://schema.org/URL)- `compartmentId[*]`: Identificador único del compartimento en el que se encuentra la pluma.  . Model: [https://schema.org/URL](https://schema.org/URL)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `deadAnimalsSinceDateOfArrival[number]`: Número de animales muertos desde la fecha de llegada  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: Una descripción de este artículo  - `farmId[*]`: Identificador único de la granja en la que se encuentra el corral.  . Model: [https://schema.org/URL](https://schema.org/URL)- `feedConsumption[number]`: La cantidad total de alimento que se ha ingerido en los puestos de alimentación en el corral. Se mide a través de las ingestas de alimento y la estructura específica para dejar que sólo un animal a la vez coma  . Model: [https://schema.org/Number](https://schema.org/Number)- `humidity[number]`: Cantidad que representa la cantidad de vapor de agua en la atmósfera en la pluma.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `lastUpdate[string]`: Fecha y hora en que se tomaron las medidas en el artículo  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `luminosity[number]`: El brillo de una fuente de luz de una determinada longitud de onda en el elemento  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `numAnimals[number]`: Número de animales contenidos en el corral.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `relatedSource[array]`: Lista de identificadores que la entidad actual puede tener en aplicaciones externas  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `sex[string]`: El sexo de los animales contenidos en el corral  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `temperature[number]`: Temperatura de la pluma.  Unirs:' Grado Celsius'  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Tiene que ser Pen  - `waterConsumption[number]`: La cantidad total de agua que sale del grifo o los grifos del corral. Se mide a través de caudalímetros y de una estructura específica para que sólo pueda beber un animal a la vez.  . Model: [https://schema.org/Number](https://schema.org/Number)- `weightStDev[number]`: La desviación estándar asociada al peso medio de los animales contenidos en el corral.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `lastUpdate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
      description: 'Date and Time for the arrival of animals to the Pen'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    avgGrowth:    
      description: 'The average growth in weight of the animal in this pen'    
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
        - description: 'Property. Identifier with format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity.'    
          format: uri    
          type: string    
      description: 'Unique identifier of the Building the item is located in'    
      x-ngsi:    
        model: https://schema.org/URL.    
        type: Relationship    
    co2:    
      description: 'The CO2 concentration in the item'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        model: https://schema.org/URL    
        type: Relationship    
    compartmentId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the Compartment the Pen is located in.'    
      x-ngsi:    
        model: https://schema.org/URL    
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
    deadAnimalsSinceDateOfArrival:    
      description: 'Number of dead animals since the date of arrival'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
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
      description: 'Unique identifier of the Farm the Pen is located in.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    feedConsumption:    
      description: 'The total amount of food that has been eaten from the feeding station(s) in the pen.It is measured through feed intakes and specific structure to let only one animal at a time to eat'    
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
      anyOf: &pen_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Date and time at which the measurements in the item were taken'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Seconds    
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
      description: 'The brightness of a light source of a certain wavelength at the item'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: LUX    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numAnimals:    
      description: 'Number of animals contained in the Pen.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pen_-_properties_-_owner_-_items_-_anyof    
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
              anyOf: *pen_-_properties_-_owner_-_items_-_anyof    
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
    sex:    
      description: 'The sex of the animals contained in the pen'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'NGSI Entity type. it has to be Pen'    
      enum:    
        - Pen    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: 'The total amount of water that came out from the tap or taps in the pen. It is measured through flowmeters and specific structure to let only one animal at a time drink.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    weightStDev:    
      description: 'The standard deviation associated to the average weight of the animals contained in the Pen.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## Ejemplo de carga útil  
#### Pen NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un Pen en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Pen NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un Pen en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": "pen",  
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
    "value": "false"  
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
#### Pen NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un Pen en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Pluma NGSI-LD normalizada Ejemplo  
Este es un ejemplo de una Pluma en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
        "value": "false"  
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
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
