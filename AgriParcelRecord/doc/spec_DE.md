Entität: AgriParcelRecord  
=========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelRecord/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung der auf einer Parzelle erfassten Bedingungen. Diese Entität ist in erster Linie mit der vertikalen Landwirtschaft und den damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `atmosphericPressure`: Atmosphärischer Druck, nominell in Einheiten von Hektopascal  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `depth`: Metadaten zur Angabe der zugehörigen Tiefe, in der die Bodenmessungen vorgenommen werden  - `description`: Eine Beschreibung dieses Artikels  - `hasAgriParcel`: Hinweis auf das AgriParcel  - `hasDevice`: Verweis auf die IoT-Geräte, die mit diesem Element verbunden sind, z. B. Sensoren, Steuerungen.  - `id`: Eindeutiger Bezeichner der Entität  - `leafRelativeHumidity`: Relative Feuchtigkeit auf der Oberfläche der Blätter  - `leafTemperature`: Die beobachtete Blatttemperatur wird in Grad Celsius angegeben.  - `leafWetness`: Es ist ein meteorologischer Parameter, der die Menge an Tau und Niederschlag beschreibt, die auf Oberflächen zurückbleibt.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `relatedSource`: Liste der IDs, die die aktuelle Entität in externen Anwendungen haben kann  - `relativeHumidity`: Relative Luftfeuchtigkeit eine Zahl zwischen 0 und 1, die den Bereich von 0% bis 100% repräsentiert.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `soilMoistureEC`: Gemessen als elektrische Leitfähigkeit, EC, nominell in Einheiten von Siemens pro Meter  - `soilMoistureVwc`: Gemessen als volumetrischer Wassergehalt, VWC in Prozent. 0 <= soilMoistureVwc <= 1  - `soilSalinity`: Es ist der Salzgehalt im Boden  - `soilTemperature`: Die beobachtete Bodentemperatur, angegeben in Grad Celsius  - `solarRadiaton`: Momentane Sonneneinstrahlung gemessen in kW/m2  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI-Entitätstyp. Es muss AgriParcelRecord sein.    
Erforderliche Eigenschaften  
- `hasAgriParcel`  - `id`  - `location`  - `type`    
Dieses Unternehmen ist in erster Linie mit der vertikalen Landwirtschaft und damit verbundenen IoT-Anwendungen verbunden.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
    atmosphericPressure:    
      description: 'Atmospheric Pressure nominally in units of hecto Pascals'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'hecto Pascals'    
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
    depth:    
      description: 'Metadata to indicate the associated depth where soil measurements are taken'    
      minimum: 0.0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
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
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    id:    
      anyOf: *agriparcelrecord_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    leafRelativeHumidity:    
      description: 'Relative humidity on the surface of the leaves'    
      maximum: 1.0    
      minimum: 0.0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    leafTemperature:    
      description: 'The observed leaf temperature nominally in degrees centigrade'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'degrees centigrade'    
    leafWetness:    
      description: 'It is a meteorological parameter that describes the amount of dew and precipitation left on surfaces.'    
      maximum: 1.0    
      minimum: 0.0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
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
        anyOf: *agriparcelrecord_-_properties_-_id_-_anyof    
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
              anyOf: *agriparcelrecord_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
      type: array    
      x-ngsi:    
        type: Property    
    relativeHumidity:    
      description: 'Relative Humidity a number between 0 and 1 representing the range of 0% to 100%.'    
      maximum: 1.0    
      minimum: 0.0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
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
    soilMoistureEC:    
      description: 'Measured as Electrical Conductivity, EC nominally in units of Siemens per meter'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'siemens / m'    
    soilMoistureVwc:    
      description: 'Measured as Volumetric Water Content, VWC as a percentage. 0 <= soilMoistureVwc <= 1 '    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    soilSalinity:    
      description: 'It is the salt content in the soil'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    soilTemperature:    
      description: 'The observed soil temperature nominally in degrees centigrade'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'degrees centigrade'    
    solarRadiaton:    
      description: 'Instantaneous solar radiation measured in kW/m2'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kW/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be AgriParcelRecord'    
      enum:    
        - AgriParcelRecord    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasAgriParcel    
    - location    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### AgriParcelRecord NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen AgriParcelRecord im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriParcelRecord NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen AgriParcelRecord im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### AgriParcelRecord NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen AgriParcelRecord im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelRecord:8f5445e6-f49b-496e-833b-e65fc97fcab7",  
  "type": "AgriParcelRecord",  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### AgriParcelRecord NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen AgriParcelRecord im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
