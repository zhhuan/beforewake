-- create database weather_alarm;
-- create user johan identified by 'AlarmJohan';
-- grant all on weather_alarm.* to johan;
-- set password for 'johan'@'localhost' = Password('AlarmJohan')

-- create table weather (
-- stat_id  int      not null auto_increment,
-- climate  char(20) null,
-- tep_cur  int      null,
-- tep_low  int      null,
-- tep_high int      null,
-- wind_dir char(10) null,
-- wind_scl int      null,
-- air_aqi  int      null,
-- air_sta  char(10) null,
-- primary key(stat_id)
-- )engine=InnoDB default charset=utf8;
-- 
-- create table suggestion (
-- sugg_id     int      not null auto_increment,
-- sugg_UV     tinytext null,
-- sugg_cold   tinytext null,
-- sugg_cloth  tinytext null,
-- sugg_car    tinytext null,
-- sugg_sport  tinytext null,
-- sugg_air    tinytext null,
-- primary key(sugg_id)
-- )engine=InnoDB default charset=utf8;
