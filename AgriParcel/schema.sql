/* (Beta) Export of data model AgriParcel of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE cropStatus_type AS ENUM ('seeded','justBorn','growing','maturing','readyForHarvesting');CREATE TYPE irrigationSystemType_type AS ENUM ('Surface irrigation','Localized irrigation','Drip irrigation','Sprinkler irrigation','Center pivot irrigation','Lateral move irrigation','Sub-irrigation','Manual irrigation');CREATE TYPE soilTextureType_type AS ENUM ('Sands','Loamy sands','Sandy loams','Loam','Silt loam','Silt','Sandy clay loam','Clay loam','Silty clay loam','Sandy clay','Silty clay','Clay');CREATE TYPE AgriParcel_type AS ENUM ('AgriParcel');
CREATE TABLE AgriParcel (address JSON, alternateName TEXT, area NUMERIC, areaServed TEXT, category TEXT, cropStatus cropStatus_type, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasAgriParcelChildren JSON, hasAirQualityObserved JSON, hasDevice JSON, id TEXT PRIMARY KEY, irrigationSystemType irrigationSystemType_type, lastPlantedAt TIMESTAMP, location JSON, name TEXT, owner JSON, relatedSource JSON, seeAlso JSON, soilTextureType soilTextureType_type, source TEXT, type AgriParcel_type);