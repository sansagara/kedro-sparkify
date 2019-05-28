from kedro.config import ConfigLoader


# CONFIG
conf_paths = ['conf/base']
conf_loader = ConfigLoader(conf_paths)
config = conf_loader.get('credentials*', 'credentials*/**')


# DROP TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create = ("""
CREATE TABLE staging_events 
(
  artist        VARCHAR(200),
  auth          VARCHAR(50),
  firstName     VARCHAR(200),
  gender        CHAR(1),
  itemInSession INTEGER,
  lastname      VARCHAR(50),
  length        NUMERIC(10,5),
  level         VARCHAR(10),
  location      VARCHAR(50),
  method        VARCHAR(10),
  page          VARCHAR(50),
  registration  VARCHAR(50),
  sessionId     INTEGER,
  song          VARCHAR(250),
  status        INTEGER,
  ts            BIGINT,
  userAgent     VARCHAR(200),
  userId        INTEGER
)
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs
(
  numSongs         INTEGER,
  artist_id         VARCHAR(20),
  artist_latitude   NUMERIC(8,5),
  artist_longitude  NUMERIC(8,5),
  artist_location   VARCHAR(100),
  artist_name       VARCHAR(200),
  song_id           VARCHAR(20),
  title            VARCHAR(200),
  duration         NUMERIC(10,5),
  year             INTEGER
)
""")

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id INTEGER IDENTITY(0,1) sortkey distkey, 
    start_time TIMESTAMP NOT NULL,
    user_id INTEGER NOT NULL, 
    level VARCHAR(10) NOT NULL, 
    song_id VARCHAR(20), 
    artist_id VARCHAR(20), 
    session_id INTEGER NOT NULL, 
    location VARCHAR(50) NOT NULL, 
    user_agent VARCHAR(150) NOT NULL
)
""")

user_table_create = ("""
CREATE TABLE users (
    user_id INTEGER sortkey, 
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    gender CHAR(1) NOT NULL, 
    level VARCHAR(10) NOT NULL
)
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id VARCHAR(20) sortkey, 
    title VARCHAR(100) NOT NULL, 
    artist_id VARCHAR(20) NOT NULL, 
    year INT NOT NULL, 
    duration NUMERIC(6,5) NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id VARCHAR(20) sortkey, 
    name VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    latitude NUMERIC(6,5), 
    longitude NUMERIC(6,5)
)
""")

time_table_create = ("""
CREATE TABLE time (
    start_time TIMESTAMP sortkey, 
    hour INTEGER NOT NULL, 
    day INTEGER NOT NULL, 
    week INTEGER NOT NULL, 
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    weekday INTEGER NOT NULL
)
""")

# STAGING TABLES

staging_events_copy = ("""
copy staging_events from {}
credentials 'aws_iam_role={}'
region 'us-west-2' FORMAT AS JSON {};
""").format(config['dev_s3']['log_data'], config['dev_iam_role']['arn'], config['dev_s3']['log_jsonpath'])

staging_songs_copy = ("""
copy staging_songs from {}
credentials 'aws_iam_role={}'
region 'us-west-2' FORMAT AS JSON 'auto';
""").format(config['dev_s3']['song_data'], config['dev_iam_role']['arn'])

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
