--
Add flight table
-- create flights_metadata table
CREATE TABLE flights_metadata (
    blank varchar(6) PRIMARY KEY,
    flight_date date,
    flight_year year,
    carrier varchar(5),
    carrier_name varchar(45),
    airport varchar(5),
    airport_name varchar(60),
    arr_flights int,
    arr_del15 int,
    carrier_ct int,
    weather_ct int,
    nas_ct int,
    security_ct int,
    late_aircraft_ct int,
    arr_cancelled int,
    arr_diverted int
    arr_delay int,
    carrier_delay int,
    weather_delay int,
    nas_delay int,
    security_delay int,
    late_aircraft_delay int
);

  
-- create topairports table
CREATE TABLE topairports_metadata (
    blank varchar(6) PRIMARY KEY,
    flight_date date,
    flight_year year,
    carrier varchar(5),
    carrier_name varchar(45),
    airport varchar(5),
    airport_name varchar(60),
    arr_flights int,
    arr_del15 int,
    carrier_ct int,
    weather_ct int,
    nas_ct int,
    security_ct int,
    late_aircraft_ct int,
    arr_cancelled int,
    arr_diverted int
    arr_delay int,
    carrier_delay int,
    weather_delay int,
    nas_delay int,
    security_delay int,
    late_aircraft_delay int
);

-- create airport_codes table
CREATE TABLE airport_codes (
    locationID varchar(5) references topairports_metadata(airport),
    Latitude float(7,4),
    Longitude float(6,4)
);


-- create airport_codes table
CREATE TABLE airport_codes (
    locationID varchar(5) references flights_metadata(airport),
    Latitude float(7,4),
    Longitude float(6,4)
);
