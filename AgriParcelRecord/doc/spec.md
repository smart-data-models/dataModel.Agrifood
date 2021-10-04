Entity: AgriParcelRecord  
========================  
[Open License](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelRecord/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of the conditions recorded on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `atmosphericPressure`: Atmospheric Pressure nominally in units of hecto Pascals  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `depth`: Metadata to indicate the associated depth where soil measurements are taken  - `description`: A description of this item  - `hasAgriParcel`: Reference to the AgriParcel  - `hasDevice`: Reference to the IoT devices associated with this item i.e. sensors, controls.  - `id`: Unique identifier of the entity  - `leafRelativeHumidity`: Relative humidity on the surface of the leaves  - `leafTemperature`: The observed leaf temperature nominally in degrees centigrade  - `leafWetness`: It is a meteorological parameter that describes the amount of dew and precipitation left on surfaces.  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `relatedSource`: List of IDs the current entity may have in external applications  - `relativeHumidity`: Relative Humidity a number between 0 and 1 representing the range of 0% to 100%.  - `seeAlso`: list of uri pointing to additional resources about the item  - `soilMoistureEC`: Measured as Electrical Conductivity, EC nominally in units of Siemens per meter  - `soilMoistureVwc`: Measured as Volumetric Water Content, VWC as a percentage. 0 <= soilMoistureVwc <= 1   - `soilSalinity`: It is the salt content in the soil  - `soilTemperature`: The observed soil temperature nominally in degrees centigrade  - `solarRadiaton`: Instantaneous solar radiation measured in kW/m2  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity Type. It has to be AgriParcelRecord    
Required properties  
- `hasAgriParcel`  - `id`  - `location`  - `type`    
This entity is primarily associated with the agricultural vertical and related IoT applications.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriParcelRecord:    
  description: 'This entity contains a harmonised description of the conditions recorded on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    atmosphericPressure:    
      description: 'Atmospheric Pressure nominally in units of hecto Pascals'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'hecto Pascals'    
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
    depth:    
      description: 'Metadata to indicate the associated depth where soil measurements are taken'    
      minimum: 0.0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    description:    
      description: 'A description of this item'    
      type: Property    
    hasAgriParcel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the AgriParcel'    
      type: Relationship    
    hasDevice:    
      description: 'Reference to the IoT devices associated with this item i.e. sensors, controls.'    
      items:    
        - anyOf: &agriparcelrecord_-_properties_-_id_-_anyof    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
          description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    id:    
      anyOf: *agriparcelrecord_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    leafRelativeHumidity:    
      description: 'Relative humidity on the surface of the leaves'    
      maximum: 1.0    
      minimum: 0.0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    leafTemperature:    
      description: 'The observed leaf temperature nominally in degrees centigrade'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'degrees centigrade'    
    leafWetness:    
      description: 'It is a meteorological parameter that describes the amount of dew and precipitation left on surfaces.'    
      maximum: 1.0    
      minimum: 0.0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agriparcelrecord_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agriparcelrecord_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: Property    
    relativeHumidity:    
      description: 'Relative Humidity a number between 0 and 1 representing the range of 0% to 100%.'    
      maximum: 1.0    
      minimum: 0.0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
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
      type: Property    
    soilMoistureEC:    
      description: 'Measured as Electrical Conductivity, EC nominally in units of Siemens per meter'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'siemens / m'    
    soilMoistureVwc:    
      description: 'Measured as Volumetric Water Content, VWC as a percentage. 0 <= soilMoistureVwc <= 1 '    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    soilSalinity:    
      description: 'It is the salt content in the soil'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    soilTemperature:    
      description: 'The observed soil temperature nominally in degrees centigrade'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'degrees centigrade'    
    solarRadiaton:    
      description: 'Instantaneous solar radiation measured in kW/m2'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: kW/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be AgriParcelRecord'    
      enum:    
        - AgriParcelRecord    
      type: Property    
  required:    
    - id    
    - type    
    - hasAgriParcel    
    - location    
  type: object    
```  
</details>    
## Example payloads    
#### AgriParcelRecord NGSI-v2 key-values Example    
Here is an example of a AgriParcelRecord in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelRecord:8f5445e6-f49b-496e-833b-e65fc97fcab7",  
  "type": "AgriParcelRecord",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelrec1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agriparcelrec",  
    "https://datamodel.org/example/agriparcelrec"  
  ],  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:d3676010-d815-468c-9e01-25739c5a25ed",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
  },  
  "soilTemperature": 27,  
  "soilMoistureVwc": 0.08,  
  "soilMoistureEc": 17,  
  "soilSalinity": 1198.11,  
  "leafWetness": 1.0,  
  "leafRelativeHumidity": 0.25,  
  "leafTemperature": 25.1,  
  "airTemperature": 20,  
  "solarRadiation": 15,  
  "relativeHumidity": 0.15,  
  "atmosphericPressure": 1013.25,  
  "description": "Monthly fertiliser application",  
  "hasDevice": [  
    "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
    "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
    "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
    "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
  ],  
  "observedAt": "2017-05-04T10:18:16Z"  
}  
```  
#### AgriParcelRecord NGSI-v2 normalized Example    
Here is an example of a AgriParcelRecord in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelRecord:8f5445e6-f49b-496e-833b-e65fc97fcab7",  
  "type": "AgriParcelRecord",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelrec1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/agriparcelrec",  
      "https://datamodel.org/example/agriparcelrec"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:d3676010-d815-468c-9e01-25739c5a25ed"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
    }  
  },  
  "soilTemperature": {  
    "value": 27,  
    "metadata": {  
      "unitCode": {  
        "value": "CEL"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      },  
      "depth": {  
        "value": {  
          "value": 20,  
          "unitCode": "CMT"  
        }  
      }  
    }  
  },  
  "soilMoistureVwc": {  
    "value": 0.08,  
    "metadata": {  
      "unitCode": {  
        "value": "C62"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "soilMoistureEc": {  
    "value": 17,  
    "metadata": {  
      "unitCode": {  
        "value": "D10"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "soilSalinity": {  
    "value": 1198.11,  
    "metadata": {  
      "unitCode": {  
        "value": "D10"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "leafWetness": {  
    "value": 1.0,  
    "metadata": {  
      "unitCode": {  
        "value": "P1"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "leafRelativeHumidity": {  
    "value": 0.25,  
    "metadata": {  
      "unitCode": {  
        "value": "P1"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "leafTemperature": {  
    "value": 25.1,  
    "metadata": {  
      "unitCode": {  
        "value": "CEL"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "airTemperature": {  
    "value": 20,  
    "metadata": {  
      "unitCode": {  
        "value": "CEL"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "solarRadiation": {  
    "value": 15,  
    "metadata": {  
      "unitCode": {  
        "value": "CEL"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "relativeHumidity": {  
    "value": 0.15,  
    "metadata": {  
      "unitCode": {  
        "value": "C62"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "atmosphericPressure": {  
    "value": 1013.25,  
    "metadata": {  
      "unitCode": {  
        "value": "A97"  
      },  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2017-05-04T12:30:00Z"  
      }  
    }  
  },  
  "description": {  
    "value": "Monthly fertiliser application"  
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
  "observedAt": {  
    "type": "DateTime",  
    "value": "2017-05-04T10:18:16Z"  
  }  
}  
```  
#### AgriParcelRecord NGSI-LD key-values Example    
Here is an example of a AgriParcelRecord in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:AgriParcelRecord:8f5445e6-f49b-496e-833b-e65fc97fcab7",  
  "type": "AgriParcelRecord",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "relatedSource": {  
    "type": "Property",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelrec1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "https://example.org/concept/agriparcelrec",  
      "https://datamodel.org/example/agriparcelrec"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:AgriParcel:d3676010-d815-468c-9e01-25739c5a25ed"  
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
  "soilTemperature": {  
    "type": "Property",  
    "value": 27,  
    "unitCode": "CEL",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "soilMoistureVwc": {  
    "type": "Property",  
    "value": 0.08,  
    "unitCode": "C62",  
    "observedAt": "2017-05-04T12:30:00Z",  
    "depth": {  
      "type": "Property",  
      "value": 20,  
      "unitCode": "CMT"  
    }  
  },  
  "soilMoistureEc": {  
    "type": "Property",  
    "value": 17,  
    "unitCode": "D10",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "airTemperature": {  
    "type": "Property",  
    "value": 20,  
    "unitCode": "CEL",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "solarRadiation": {  
    "type": "Property",  
    "value": 15,  
    "unitCode": "N78",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 0.15,  
    "unitCode": "C62",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "atmosphericPressure": {  
    "type": "Property",  
    "value": 1013.25,  
    "unitCode": "A97",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "soilSalinity": {  
    "type": "Property",  
    "value": 1198.11,  
    "unitCode": "D10",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "leafWetness": {  
    "type": "Property",  
    "value": 1.0,  
    "unitCode": "P1",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "leafRelativeHumidity": {  
    "type": "Property",  
    "value": 0.25,  
    "unitCode": "P1",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "leafTemperature": {  
    "type": "Property",  
    "value": 25.1,  
    "unitCode": "CEL",  
    "observedAt": "2017-05-04T12:30:00Z"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Monthly fertiliser application"  
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
  "observedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-05-04T12:30:00Z"  
    }  
  }  
}  
```  
#### AgriParcelRecord NGSI-LD normalized Example    
Here is an example of a AgriParcelRecord in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "airTemperature": 20,  
  "atmosphericPressure": 1013.25,  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Monthly fertiliser application",  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:d3676010-d815-468c-9e01-25739c5a25ed",  
  "hasDevice": [  
    "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
    "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
    "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
    "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
  ],  
  "id": "urn:ngsi-ld:AgriParcelRecord:8f5445e6-f49b-496e-833b-e65fc97fcab7",  
  "leafRelativeHumidity": 0.25,  
  "leafTemperature": 25.1,  
  "leafWetness": 1.0,  
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
  "observedAt": {  
    "@type": "DateTime",  
    "@value": "2017-05-04T12:30:00Z"  
  },  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelrec1"  
    }  
  ],  
  "relativeHumidity": 0.15,  
  "seeAlso": [  
    "https://example.org/concept/agriparcelrec",  
    "https://datamodel.org/example/agriparcelrec"  
  ],  
  "soilMoistureEc": 17,  
  "soilMoistureVwc": 0.08,  
  "soilSalinity": 1198.11,  
  "soilTemperature": 27,  
  "solarRadiation": 15,  
  "type": "AgriParcelRecord"  
}  
```  
