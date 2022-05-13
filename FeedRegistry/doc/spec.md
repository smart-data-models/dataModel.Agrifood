[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: FeedRegistry  
====================  
[Open License](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/FeedRegistry/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Object modelling a feed registry for a livestock farm.**  
version: 0.0.1  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `amount`: Amount of feed supplied to animals.  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `date`: Date of supply of food to animals  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `deliveryNote`: Description of the feed registry  - `description`: A description of this item  - `farm`: Farm where the operation is carried out. https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriFarm/schema.json  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `supplier`: Supplier of the feed  - `type`: NGSI entity type. It has to be FeedRegistry    
Required properties  
- `id`  - `name`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FeedRegistry:    
  description: 'Object modelling a feed registry for a livestock farm.'    
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
    amount:    
      description: 'Amount of feed supplied to animals.'    
      type: integer    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    date:    
      description: 'Date of supply of food to animals'    
      format: date-time    
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
    deliveryNote:    
      description: 'Description of the feed registry'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    farm:    
      description: 'Farm where the operation is carried out. https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriFarm/schema.json'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &feedregistry_-_properties_-_owner_-_items_-_anyof    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *feedregistry_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    supplier:    
      description: 'Supplier of the feed'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be FeedRegistry'    
      enum:    
        - FeedRegistry    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/FeedRegistry/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/FeedRegistry/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
```  
</details>    
## Example payloads    
#### FeedRegistry NGSI-v2 key-values Example    
Here is an example of a FeedRegistry in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:FeedRegistry:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "type": "FeedRegistry",  
    "name":"Biona tacos Campero Vacuno 40 kg",  
    "date":"2022-01-01T01:20:00Z",  
    "farm":"urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
    "amount":1230,  
    "supplier": "GEPISA",  
    "deliveryNote":"Primera entrega 2022"  
}  
```  
#### FeedRegistry NGSI-v2 normalized Example    
Here is an example of a FeedRegistry in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:FeedRegistry:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "FeedRegistry",  
  "name": {  
    "type": "Text",  
    "value": "Biona tacos Campero Vacuno 40 kg"  
  },  
  "date": {  
    "type": "Date-Time",  
    "value": "2022-01-01T01:20:00Z"  
  },  
  "farm": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a"  
  },  
  "amount": {  
    "type": "number",  
    "value": 1230  
  },  
  "supplier": {  
    "type": "Text",  
    "value": "GEPISA"  
  },  
  "deliveryNote": {  
    "type": "Text",  
    "value": "Primera entrega 2022"  
  }  
}  
```  
#### FeedRegistry NGSI-LD key-values Example    
Here is an example of a FeedRegistry in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:FeedRegistry:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "FeedRegistry",  
  "name": "Biona tacos Campero Vacuno 40 kg",  
  "date": "2022-01-01T01:20:00Z",  
  "farm": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
  "amount": 1230,  
  "supplier": "GEPISA",  
  "deliveryNote": "Primera entrega 2022",  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Agrifood/context.jsonld"  
  ]  
}  
```  
#### FeedRegistry NGSI-LD normalized Example    
Here is an example of a FeedRegistry in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:FeedRegistry:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "FeedRegistry",  
  "name": {  
    "type": "Property",  
    "value": "Biona tacos Campero Vacuno 40 kg"  
  },  
  "date": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2022-01-01T01:20:00Z"  
    }  
  },  
  "farm": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:AgriFarm:72d9fb43-53f8-4ec8-a33c-fa931360259a"  
  },  
  "amount": {  
    "type": "Property",  
    "value": 1230  
  },  
  "supplier": {  
    "type": "Property",  
    "value": "GEPISA"  
  },  
  "deliveryNote": {  
    "type": "Property",  
    "value": "Primera entrega 2022"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Agrifood/context.jsonld"  
  ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
