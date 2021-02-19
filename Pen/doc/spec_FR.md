Entité : Plume :  
================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Pen/LICENSE.md)  
Description globale : **Aire clôturée dans un bâtiment ou un département ou à l'extérieur abritant un groupe d'animaux. Les animaux dans un enclos peuvent se déplacer et interagir librement. Les enclos ne sont souvent pas complètement séparés les uns des autres (demi-murs, barres de fer, clôtures,...), ce qui permet aux animaux des enclos voisins de voir/toucher**  

## Liste des biens  

- `additionalInfo`: liste de toutes les valeurs brutes envoyées par le capteur/plate-forme avec toutes les propriétés supplémentaires possibles qui ne sont pas incluses dans la structure principale. Il s'agit d'une structure JSON similaire à celle-ci : {'nom' : 'température', 'valeur' : 32}  - `address`: L'adresse postale  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `arrivalTimestamp`: Date et heure d'arrivée des animaux dans l'enclos  - `avgGrowth`: La croissance moyenne du poids de l'animal dans cet enclos  - `avgWeight`: Le poids moyen de l'animal dans cet enclos.  - `buildingId`: Identifiant unique du bâtiment dans lequel se trouve l'objet  - `co2`: La concentration de CO2 dans l'article  - `companyId`: Identifiant unique d'une entreprise  - `compartmentId`: Identifiant unique du compartiment dans lequel se trouve le stylo.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `deadAnimalsSinceDateOfArrival`: Nombre d'animaux morts depuis la date d'arrivée  - `description`: Une description de cet article  - `farmId`: Identifiant unique de la ferme dans laquelle se trouve le stylo.  - `feedConsumption`: La quantité totale de nourriture qui a été consommée à partir de la ou des stations d'alimentation dans l'enclos. Elle est mesurée par les apports alimentaires et la structure spécifique permettant de ne laisser manger qu'un seul animal à la fois  - `humidity`: Quantité représentant la quantité de vapeur d'eau dans l'atmosphère de l'enclos.  - `id`:   - `lastUpdate`: Date et heure auxquelles les mesures de l'article ont été prises  - `location`:   - `luminosity`: La luminosité d'une source de lumière d'une certaine longueur d'onde au niveau de l'objet  - `name`: Le nom de cet article.  - `numAnimals`: Nombre d'animaux contenus dans l'enclos.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `relatedSource`: Liste des identifiants que l'entité actuelle peut avoir dans les applications externes  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `sex`: Le sexe des animaux contenus dans l'enclos  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `temperature`: Température du stylo.  Unirs : "degré Celsius".  - `type`: Type d'entité NGSI. Il doit s'agir de Pen  - `waterConsumption`: La quantité totale d'eau qui est sortie du robinet ou des robinets de l'enclos. Elle est mesurée à l'aide de débitmètres et d'une structure spécifique pour ne laisser boire qu'un seul animal à la fois.  - `weightStDev`: L'écart-type associé au poids moyen des animaux contenus dans l'enclos.    
Propriétés requises  
- `id`  - `lastUpdate`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/adddress    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    arrivalTimestamp:    
      description: 'Date and Time for the arrival of animals to the Pen'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    avgGrowth:    
      description: 'The average growth in weight of the animal in this pen'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    avgWeight:    
      description: 'The average weight of the animal in this Pen. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Kg    
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
      description: 'Unique identifier of the Building the item is located in'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    co2:    
      description: 'The CO2 concentration in the item'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
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
    deadAnimalsSinceDateOfArrival:    
      description: 'Number of dead animals since the date of arrival'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    description:    
      description: 'A description of this item'    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    feedConsumption:    
      description: 'The total amount of food that has been eaten from the feeding station(s) in the pen.It is measured through feed intakes and specific structure to let only one animal at a time to eat'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Kg    
    humidity:    
      description: 'Quantity representing the amount of water vapour in the atmosphere in the pen. '    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      type: string    
    lastUpdate:    
      description: 'Date and time at which the measurements in the item were taken'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
        units: Seconds    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    luminosity:    
      description: 'The brightness of a light source of a certain wavelength at the item'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: LUX    
    name:    
      description: 'The name of this item.'    
      type: Property    
    numAnimals:    
      description: 'Number of animals contained in the Pen.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: &values_-_application_-_anyof    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *values_-_application_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    sex:    
      description: 'The sex of the animals contained in the pen'    
      enum:    
        - M    
        - F    
        - unknown    
        - ""    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    temperature:    
      description: 'Temperature of the Pen.  Unirs:'' Celsius degree'''    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI Entity type. it has to be Pen'    
      enum:    
        - Pen    
      type: Property    
    waterConsumption:    
      description: 'The total amount of water that came out from the tap or taps in the pen. It is measured through flowmeters and specific structure to let only one animal at a time drink.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    weightStDev:    
      description: 'The standard deviation associated to the average weight of the animals contained in the Pen.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
    - lastUpdate    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Exemple de valeurs clés de l'INSG V2  
Voici un exemple de stylo au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
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
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "lastUpdate": "2020-04-12T20:44:55",  
  "sex": "",  
  "temperature": 25  
}  
```  
#### Stylo NGSI V2 normalisé Exemple  
Voici un exemple de stylo au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": {  
    "type": "string",  
    "value": "pen"  
  },  
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
#### Exemple de valeurs clés de l'INSMT-LD  
Voici un exemple de stylo au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
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
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "lastUpdate": "2020-04-12T20:44:55",  
  "sex": "",  
  "temperature": 25,  
  "@context": ["https://smart-data-models.github.io/data-models/context.jsonld"]  
}  
```  
#### Stylo NGSI-LD normalisé Exemple  
Voici un exemple de stylo au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": {  
    "type": "string",  
    "value": "pen"  
  },  
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
  "@context": ["https://smart-data-models.github.io/data-models/context.jsonld"]  
}  
```  
