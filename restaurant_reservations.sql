CREATE database restaurant_reservations;
USE restaurant_reservations;
CREATE TABLE Customers
(
CustomerId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
CustomerName VARCHAR(45) NOT NULL,
ContactInfo VARCHAR(200)
);
CREATE TABLE Reservations
(
ReservationId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
CustomerId INT NOT NULL,
ReservationTime DATETIME NOT NULL,
NumberOfGuests INT NOT NULL,
SpecialRequests VARCHAR(200),
FOREIGN KEY (CustomerId) REFERENCES Customers (CustomerId)
);
CREATE TABLE DiningPreferences
(
PreferenceId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
CustomerId INT NOT NULL,
FavoriteTable VARCHAR(45),
DietaryRestrictions VARCHAR(200),
FOREIGN KEY (CustomerId) REFERENCES Customers (CustomerId)
);
# STANDARD WAY
Delimiter //
CREATE PROCEDURE FindReservations (IN CustomerId INT)
BEGIN
	SELECT * FROM Reservations 
    WHERE CustomerId = CustomerId;
END//
Delimiter ;

# STANDARD WAY
Delimiter //
CREATE PROCEDURE addSpecialRequest (IN ReservationID INT, IN Requests VARCHAR(255))
BEGIN
	UPDATE RESERVATIONS
    SET SpecialRequest = Requests
    WHERE ReservationId = ReservationId;
END//
Delimiter ;

# STANDARD WAY
DELIMITER //

CREATE PROCEDURE addReservation(
    IN CustomerId INT, 
    IN CustomerName VARCHAR(45),
    IN ReservationTime DATETIME, 
    IN NumberOfGuests INT,
    IN ContactInfo VARCHAR(200),
    IN SpecialRequests VARCHAR(200),
    IN FavoriteTable VARCHAR(45),
    IN DietaryRestrictions VARCHAR(200)
)
BEGIN
    DECLARE custId INT;
    
    -- Check if customer already exists
    SELECT customerId INTO custId 
    FROM Customers 
    WHERE ContactInfo = Email 
    LIMIT 1;
    
    -- If customer does not exist, create a new customer
    IF custId IS NULL THEN
        INSERT INTO Customers (CustomerId, CustomerName, ContactInfo) 
        VALUES (12, "Kemar Kerr" , "kkerr23@yahoo.com");
        SET custId = LAST_INSERT_ID();
    END IF;
    
    -- Add the reservation
    INSERT INTO Reservations (customerId, reservationDate, specialRequests) 
    VALUES (12, '2024-05-13 17:00:00', 'No Special Request');
END //

DELIMITER ;

INSERT INTO Customers (CustomerId, CustomerName, ContactInfo) VALUES
	(1, "Andre William", "Andre21@yahoo.com"),
	(2, "Pamela Alston", "thatgirl21@gmail.com"),
	(3, "Karon Bowen" , "kb22@yahoo.com");

INSERT INTO Reservations (ReservationId, customerId, reservationTime, numberOfGuests, specialRequests) VALUES
(111, 1, '2024-05-12 18:00:00', 4, "No special requests"),
(763, 2, '2024-05-20 19:30:00', 5, "High chair needed"),
(345, 3, '2024-05-15 20:00:00', 2, "Vegetarian options required");

INSERT INTO DiningPreferences (PreferenceId, CustomerId, favoriteTable, dietaryRestrictions) VALUES
(23, 1, "Table by the window", "None"),
(25, 2,  "Outside Seating", "None"),
(33, 3, "Private dining room", "Vegetarian");