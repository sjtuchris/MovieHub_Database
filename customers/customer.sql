CREATE VIEW Rating_cusid AS
  SELECT cusid
  FROM Ratings
  GROUP BY cusid;

CREATE TABLE `Customers` (
  `cusid` INT NOT NULL AUTO_INCREMENT,
  `cusname` VARCHAR(45) NOT NULL UNIQUE ,
  `cusemail` VARCHAR(45) NOT NULL UNIQUE ,
  `cuspassword` VARCHAR(45) NOT NULL,
  `cusPortraitUrl` VARCHAR(10000) NOT NULL ,
  `CreatedAt` timestamp NOT NULL DEFAULT current_timestamp,
  `UpdatedAt`timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (`cusid`));

LOAD DATA LOCAL INFILE '/Users/Chris/GoogleDrive/Cloud_Computing/Project/customers/customers_dummy.csv' INTO TABLE Customers
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES
(@cusid,@cusname,@cusemail,@cuspassword,@cusPortraitUrl) set cusid=@cusid, cusname=@cusname,cusemail=@cusemail,cuspassword=@cuspassword,cusPortraitUrl=@cusPortraitUrl;

#INSERT INTO Customers (`cusid`, `cusname`, `cusemail`, `cuspassword`,`cusPortraitUrl`)
#  SELECT cusid,'default', 'default@default.com','default','https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwjN0tSugP3SAhWs5oMKHevTB5YQjRwIBw&url=http%3A%2F%2Fsx.xinhuanet.com%2Fsjyw%2F20160506%2F3112655_c.html&bvm=bv.151325232,d.amc&psig=AFQjCNE72cHUoor6RVt549fDHdRlIU42QQ&ust=1490921181771462'
# FROM Rating_cusid