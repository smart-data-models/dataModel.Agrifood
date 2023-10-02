/* (Beta) Export of data model AgriFarm of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriFarm_type AS ENUM ('AgriFarm');
CREATE TABLE AgriFarm (address JSON, alternateName TEXT, areaServed TEXT, contactPoint JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasAgriParcel JSON, hasBuilding JSON, name TEXT, owner JSON, relatedSource JSON, source TEXT, type AgriFarm_type);