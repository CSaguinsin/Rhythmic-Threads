DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS cart;

CREATE TABLE users
(
    uid      INTEGER PRIMARY KEY UNIQUE,
    name     VARCHAR(255) NOT NULL,
    email    VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated  TIMESTAMP             DEFAULT NULL
);

CREATE TABLE products
(
    id          INTEGER PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    collection  VARCHAR(255) NOT NULL,
    category    VARCHAR(255) NOT NULL,
    sx          VARCHAR(255) NOT NULL,
    size        VARCHAR(255) NOT NULL,
    price       DECIMAL(10, 2) NOT NULL,
    ratings     INTEGER,
    created     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE carts
(
    id         INTEGER PRIMARY KEY UNIQUE,
    user_id    INT NOT NULL,
    product_id INT NOT NULL,
    qty        INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (uid),
    FOREIGN KEY (product_id) REFERENCES product (id)
);
