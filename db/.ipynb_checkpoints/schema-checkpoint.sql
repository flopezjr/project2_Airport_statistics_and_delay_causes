--
Add flight table
-- create flights_metadata table

CREATE TABLE airport_delays (
    uid varchar(6) PRIMARY KEY,
    flight_date date,
    flight_year int,
    flight_month int,
    carrier varchar(5),
    carrier_name varchar(60),
    airport varchar(5),
    airport_name varchar(155),
    Latitude float8,
    Longitude float8,
    arr_flights int,
    arr_del15 int,
    carrier_ct int,
    weather_ct int,
    nas_ct int,
    security_ct int,
    late_aircraft_ct int,
    arr_cancelled int,
    arr_diverted int,
    arr_delay int,
    carrier_delay int,
    weather_delay int,
    nas_delay int,
    security_delay int,
    late_aircraft_delay int
);
