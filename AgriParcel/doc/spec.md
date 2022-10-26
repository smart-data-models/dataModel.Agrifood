<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: AgriParcel  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains a harmonised description of a generic parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.**  
version: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `area[number]`: The area of the parcel nominally in square meters.  . Model: [http://schema.org/Number](http://schema.org/Number)- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `belongsTo[*]`: Entity the item belongs to  - `category[string]`: The category of the parcel of land e.g.: **arable, grassland, vineyard, orchard, mixed crop, lowland, upland, set-aside, forestry, wetland.**  . Model: [http://schema.org/Text](http://schema.org/Text)- `cropStatus[string]`: Enum:'seeded, justBorn, growing, maturing, readyForHarvesting'. A choice from an enumerated list describing the crop planting status  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `hasAgriCrop[*]`: Reference to the crop associated with this parcel  - `hasAgriParcelChildren[array]`: Related sub AgriParcel records to which this entity relates  - `hasAgriParcelParent[*]`: Reference to the parent AgriParcel  - `hasAgriSoil[*]`: Reference to the soil associated with this parcel of land  - `hasDevices[array]`: Reference to the IoT devices associated with this parcel i.e. sensors, controls.  - `id[*]`: Unique identifier of the entity  - `irrigationSystemType[string]`: Enum: 'Surface irrigation', 'Localized irrigation', 'Drip irrigation', 'Sprinkler irrigation', 'Center pivot irrigation', 'Lateral move irrigation', 'Sub-irrigation', 'Manual irrigation'. Based on common types of irrigation systems as defined by Centers for Disease Control and Prevention (CDC): https://www.cdc.gov/healthywater/other/agricultural/types.html  - `lastPlantedAt[string]`: Indicates the date when the crop was last planted  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `ownedBy[*]`: Owner (Person or Organization) of the item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `relatedSource[array]`: List of IDs the current entity may have in external applications  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `soilTextureType[string]`: Enum: 'Sands', 'Loamy sands', 'Sandy loams', 'Loam', 'Silt loam', 'Silt', 'Sandy clay loam', 'Clay loam', 'Silty clay loam', 'Sandy clay', 'Silty clay', 'Clay'. Based on the soil texture classification of the United States Department of Agriculture (USDA): https://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/soils/ref/?cid=nrcs142p2_054262  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type[string]`: NGSI Entity Type. It has to be AgriParcel  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `area`  - `hasAgriCrop`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
This entity is primarily associated with the agricultural vertical and related IoT applications.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriParcel:    
  description: 'This entity contains a harmonised description of a generic parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
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
    area:    
      description: 'The area of the parcel nominally in square meters.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: m2    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Entity the item belongs to'    
      x-ngsi:    
        type: Relationship    
    category:    
      description: 'The category of the parcel of land e.g.: **arable, grassland, vineyard, orchard, mixed crop, lowland, upland, set-aside, forestry, wetland.**'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    cropStatus:    
      description: 'Enum:''seeded, justBorn, growing, maturing, readyForHarvesting''. A choice from an enumerated list describing the crop planting status'    
      enum:    
        - seeded    
        - justBorn    
        - growing    
        - maturing    
        - readyForHarvesting    
      type: string    
      x-ngsi:    
        type: Property    
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
    hasAgriCrop:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the crop associated with this parcel'    
      x-ngsi:    
        type: Relationship    
    hasAgriParcelChildren:    
      description: 'Related sub AgriParcel records to which this entity relates'    
      items:    
        anyOf: &agriparcel_-_properties_-_hasdevices_-_items_-_anyof    
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
      description: 'Reference to the parent AgriParcel'    
      x-ngsi:    
        type: Relationship    
    hasAgriSoil:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the soil associated with this parcel of land'    
      x-ngsi:    
        type: Relationship    
    hasDevices:    
      description: 'Reference to the IoT devices associated with this parcel i.e. sensors, controls.'    
      items:    
        anyOf: *agriparcel_-_properties_-_hasdevices_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: *agriparcel_-_properties_-_hasdevices_-_items_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    irrigationSystemType:    
      description: 'Enum: ''Surface irrigation'', ''Localized irrigation'', ''Drip irrigation'', ''Sprinkler irrigation'', ''Center pivot irrigation'', ''Lateral move irrigation'', ''Sub-irrigation'', ''Manual irrigation''. Based on common types of irrigation systems as defined by Centers for Disease Control and Prevention (CDC): https://www.cdc.gov/healthywater/other/agricultural/types.html'    
      enum:    
        - 'Surface irrigation'    
        - 'Localized irrigation'    
        - 'Drip irrigation'    
        - 'Sprinkler irrigation'    
        - 'Center pivot irrigation'    
        - 'Lateral move irrigation'    
        - Sub-irrigation    
        - 'Manual irrigation'    
      type: string    
      x-ngsi:    
        type: Property    
    lastPlantedAt:    
      description: 'Indicates the date when the crop was last planted'    
      format: date-time    
      type: string    
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
      description: 'Owner (Person or Organization) of the item'    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agriparcel_-_properties_-_hasdevices_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        properties:    
          application:    
            anyOf: *agriparcel_-_properties_-_hasdevices_-_items_-_anyof    
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
    soilTextureType:    
      description: 'Enum: ''Sands'', ''Loamy sands'', ''Sandy loams'', ''Loam'', ''Silt loam'', ''Silt'', ''Sandy clay loam'', ''Clay loam'', ''Silty clay loam'', ''Sandy clay'', ''Silty clay'', ''Clay''. Based on the soil texture classification of the United States Department of Agriculture (USDA): https://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/soils/ref/?cid=nrcs142p2_054262'    
      enum:    
        - Sands    
        - 'Loamy sands'    
        - 'Sandy loams'    
        - Loam    
        - 'Silt loam'    
        - Silt    
        - 'Sandy clay loam'    
        - 'Clay loam'    
        - 'Silty clay loam'    
        - 'Sandy clay'    
        - 'Silty clay'    
        - Clay    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be AgriParcel'    
      enum:    
        - AgriParcel    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - area    
    - hasAgriCrop    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriParcel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriParcel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### AgriParcel NGSI-v2 key-values Example    
Here is an example of a AgriParcel in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriParcel:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "type": "AgriParcel",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
  },  
  "area": 200,  
  "description": "Spring wheat",  
  "category": "arable",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcel1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agriparcel",  
    "https://datamodel.org/example/agriparcel"  
  ],  
  "belongsTo": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765",  
  "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "hasAgriParcelParent": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "hasAgriParcelChildren": [  
    "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
    "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
  ],  
  "hasAgriCrop": "urn:ngsi-ld:AgriCrop:36021150-4474-11e8-a721-af07c5fae7c8",  
  "cropStatus": "seeded",  
  "lastPlantedAt": "2016-08-23T10:18:16Z",  
  "hasAgriSoil": "urn:ngsi-ld:AgriSoil:429d1338-4474-11e8-b90a-d3e34ceb73df",  
  "hasDevice": [  
    "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
    "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
    "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
    "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
  ],  
  "soilTextureType": "Clay",  
  "irrigationSystemType": "Drip irrigation"  
}  
```  
</details>  
#### AgriParcel NGSI-v2 normalized Example    
Here is an example of a AgriParcel in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriParcel:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "type": "AgriParcel",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
    }  
  },  
  "area": {  
    "value": 200  
  },  
  "description": {  
    "value": "Spring wheat"  
  },  
  "category": {  
    "value": "arable"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcel1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/agriparcel",  
      "https://datamodel.org/example/agriparcel"  
    ]  
  },  
  "belongsTo": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "hasAgriParcelParent": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
  },  
  "hasAgriParcelChildren": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
      "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
    ]  
  },  
  "hasAgriCrop": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriCrop:36021150-4474-11e8-a721-af07c5fae7c8"  
  },  
  "cropStatus": {  
    "value": "seeded"  
  },  
  "lastPlantedAt": {  
    "type": "DateTime",  
    "value": "2016-08-23T10:18:16Z"  
  },  
  "hasAgriSoil": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriSoil:429d1338-4474-11e8-b90a-d3e34ceb73df"  
  },  
  "hasDevice": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
      "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
      "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
      "urn:ngsi-ld:Device:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
    ]  
  },  
  "soilTextureType": {  
      "type": "string",  
      "value": "Clay"  
  },  
  "irrigationSystemType": {  
      "type": "string",  
      "value": "Drip irrigation"  
  }  
}  
```  
</details>  
#### AgriParcel NGSI-LD key-values Example    
Here is an example of a AgriParcel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriParcel:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
    "type": "AgriParcel",  
    "area": 200,  
    "belongsTo": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765",  
    "category": "arable",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "cropStatus": "seeded",  
    "description": "Spring wheat",  
    "hasAgriCrop": "urn:ngsi-ld:AgriCrop:36021150-4474-11e8-a721-af07c5fae7c8",  
    "hasAgriParcelChildren": [  
        "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
        "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
    ],  
    "hasAgriParcelParent": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
    "hasAgriSoil": "urn:ngsi-ld:AgriSoil:429d1338-4474-11e8-b90a-d3e34ceb73df",  
    "hasDevice": [  
        "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
        "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
        "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
        "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
    ],  
    "lastPlantedAt": {  
        "@type": "DateTime",  
        "@value": "2016-08-22T10:18:16Z"  
    },  
    "location": {  
        "coordinates": [  
            [  
                100,  
                0  
            ],  
            [  
                101,  
                0  
            ],  
            [  
                101,  
                1  
            ],  
            [  
                100,  
                1  
            ],  
            [  
                100,  
                0  
            ]  
        ],  
        "type": "Polygon"  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
    "relatedSource": [  
        {  
            "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
            "applicationEntityId": "app:parcel1"  
        }  
    ],  
    "seeAlso": [  
        "https://example.org/concept/agriparcel",  
        "https://datamodel.org/example/agriparcel"  
    ],  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AgriParcel NGSI-LD normalized Example    
Here is an example of a AgriParcel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriParcel:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
    "type": "AgriParcel",  
    "area": {  
        "type": "Property",  
        "value": 200  
    },  
    "belongsTo": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
    },  
    "category": {  
        "type": "Property",  
        "value": "arable"  
    },  
    "createdAt": "2017-01-01T01:20:00Z",  
    "cropStatus": {  
        "type": "Property",  
        "value": "seeded"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Spring wheat"  
    },  
    "hasAgriCrop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriCrop:36021150-4474-11e8-a721-af07c5fae7c8"  
    },  
    "hasAgriParcelChildren": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriParcel:26ba4be0-4474-11e8-8ec1-ab9e0ea93835",  
            "urn:ngsi-ld:AgriParcel:2d5b8874-4474-11e8-8d6b-dbe14425b5e4"  
        ]  
    },  
    "hasAgriParcelParent": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
    },  
    "hasAgriSoil": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriSoil:429d1338-4474-11e8-b90a-d3e34ceb73df"  
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
    "lastPlantedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Polygon",  
            "coordinates": [  
                [  
                    100,  
                    0  
                ],  
                [  
                    101,  
                    0  
                ],  
                [  
                    101,  
                    1  
                ],  
                [  
                    100,  
                    1  
                ],  
                [  
                    100,  
                    0  
                ]  
            ]  
        }  
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
                "applicationEntityId": "app:parcel1"  
            }  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agriparcel",  
            "https://datamodel.org/example/agriparcel"  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
