CREATE TABLE `Movies` (
  `movid` VARCHAR(10) NOT NULL,
  `movname` VARCHAR(100) NOT NULL ,
  `movyear` INT NOT NULL,
  `genre` VARCHAR(100) NOT NULL ,
  `director` VARCHAR(100) NOT NULL ,
  `actor` VARCHAR(10000) NOT NULL ,
  `description` VARCHAR(10000) NOT NULL ,
  `movTrailerUrl` VARCHAR(10000) NOT NULL ,
  `movScreenshotUrl` VARCHAR(10000) NOT NULL ,
  `CreatedAt` timestamp NOT NULL DEFAULT current_timestamp,
  `UpdatedAt`timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (`movid`));


LOAD DATA LOCAL INFILE '/Users/Chris/GoogleDrive/Cloud_Computing/Project/fetchIMDB/movie_str.csv' INTO TABLE Movies
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@imdb,@name,@movyear,@genre,@director,@actor,@image,@trailer,@description) set movid=@imdb, movname=@name, movyear=@movyear, genre=@genre,director=@director,actor=@actor,description=@description, movScreenshotUrl=@image, movTrailerUrl=@trailer;
#\r is very important
