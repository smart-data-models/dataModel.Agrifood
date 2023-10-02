/* (Beta) Export of data model AgriApp of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriApp_type AS ENUM ('AgriApp');
CREATE TABLE AgriApp (address JSON, alternateName TEXT, areaServed TEXT, category JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, endpoint TEXT, name TEXT, owner JSON, relatedSource JSON, source TEXT, type AgriApp_type, version TEXT);