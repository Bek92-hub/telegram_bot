-- Categories
INSERT INTO categories (name) 
VALUES ("Lavash"), ("Ichimliklar");

-- Products
INSERT INTO products (category_id, name, photo, price)
VALUES (1, "Mini lavash", "https://shorturl.at/6dos0", 22000.00),
       (1, "Standart lavash", "https://shorturl.at/6dos0", 30000.00),
       (1, "Extra lavash", "https://shorturl.at/6dos0", 35000.00),
       (2, "Coca-Cola 0.5", "https://shorturl.at/TEDvq", 9000.00),
       (2, "Coca-Cola 1.0", "https://shorturl.at/TEDvq", 12000.00),
       (2, "Coca-Cola 1.5", "https://shorturl.at/TEDvq", 15000.00);