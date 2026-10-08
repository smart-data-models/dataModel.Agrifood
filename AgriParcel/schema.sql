/* (Beta) Export of data model AgriParcel of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriParcel_cropStatus_type AS ENUM ('seeded', 'justBorn', 'growing', 'maturing', 'readyForHarvesting');
CREATE TYPE AgriParcel_irrigationSystemType_type AS ENUM ('Surface irrigation', 'Localized irrigation', 'Drip irrigation', 'Sprinkler irrigation', 'Center pivot irrigation', 'Lateral move irrigation', 'Sub-irrigation', 'Manual irrigation');
CREATE TYPE AgriParcel_soilTextureType_type AS ENUM ('Sands', 'Loamy sands', 'Sandy loams', 'Loam', 'Silt loam', 'Silt', 'Sandy clay loam', 'Clay loam', 'Silty clay loam', 'Sandy clay', 'Silty clay', 'Clay');
CREATE TYPE AgriParcel_type AS ENUM ('AgriParcel');
CREATE TABLE AgriParcel (
  "address" JSON,
  "alternateName" TEXT,
  "area" NUMERIC,
  "areaServed" TEXT,
  "belongsTo" JSON,
  "category" TEXT,
  "cropStatus" AgriParcel_cropStatus_type,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "hasAgriCrop" JSON,
  "hasAgriParcelChildren" JSON,
  "hasAgriParcelParent" JSON,
  "hasAgriSoil" JSON,
  "hasAirQualityObserved" JSON,
  "hasDevice" JSON,
  "id" TEXT PRIMARY KEY,
  "irrigationSystemType" AgriParcel_irrigationSystemType_type,
  "lastPlantedAt" TIMESTAMP,
  "location" JSON,
  "name" TEXT,
  "ownedBy" JSON,
  "owner" JSON,
  "relatedSource" JSON,
  "seeAlso" JSON,
  "soilTextureType" AgriParcel_soilTextureType_type,
  "source" TEXT,
  "type" AgriParcel_type
);