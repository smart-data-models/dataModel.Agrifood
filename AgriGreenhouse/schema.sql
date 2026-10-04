/* (Beta) Export of data model AgriGreenhouse of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriGreenhouse_type AS ENUM ('AgriGreenhouse');
CREATE TABLE AgriGreenhouse (
  "alternateName" TEXT,
  "belongsTo" JSON,
  "co2" NUMERIC,
  "dailyLight" NUMERIC,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "drainFlow" JSON,
  "hasAgriParcelChildren" JSON,
  "hasAgriParcelParent" JSON,
  "hasDevice" JSON,
  "hasWaterQualityObserved" JSON,
  "hasWeatherObserved" JSON,
  "id" TEXT PRIMARY KEY,
  "leafTemperature" NUMERIC,
  "name" TEXT,
  "ownedBy" JSON,
  "owner" JSON,
  "relatedSource" JSON,
  "relativeHumidity" NUMERIC,
  "seeAlso" JSON,
  "source" TEXT,
  "type" AgriGreenhouse_type
);