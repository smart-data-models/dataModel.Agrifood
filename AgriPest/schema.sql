/* (Beta) Export of data model AgriPest of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriPest_type AS ENUM ('AgriPest');
CREATE TABLE AgriPest (agroVocConcept TEXT, alternateName TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasAgriProductType JSON, id TEXT PRIMARY KEY, name TEXT, owner JSON, relatedSource JSON, seeAlso JSON, source TEXT, type AgriPest_type);