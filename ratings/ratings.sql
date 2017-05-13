CREATE TABLE `Ratings` (
  `movid` VARCHAR(10) NOT NULL ,
  `cusid` INT NOT NULL ,
  `rating` INT NOT NULL ,
  `CreatedAt` timestamp NOT NULL DEFAULT current_timestamp,
  `UpdatedAt`timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (`movid`,`cusid`));

LOAD DATA LOCAL INFILE '/Users/Chris/GoogleDrive/Cloud_Computing/Project/ratings.csv' INTO TABLE Ratings
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@cusid,@imdbid,@rating) set movid=@imdbid, cusid=@cusid, rating=@rating;
#\r is very important!
