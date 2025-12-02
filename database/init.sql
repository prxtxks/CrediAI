-- init.sql
-- Initialize the PostgreSQL database for CrediAI

-- Replace 'credi_ai_db' with your desired database name
CREATE DATABASE credi_ai_db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;

\connect credi_ai_db;

-- You can also create the schema if needed
CREATE SCHEMA IF NOT EXISTS public;