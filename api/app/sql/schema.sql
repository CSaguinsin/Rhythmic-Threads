DROP TABLE IF EXISTS rt_users;
DROP TABLE IF EXISTS rt_products;
DROP TABLE IF EXISTS rt_carts;

CREATE TABLE rt_users
(
    id       INTEGER PRIMARY KEY UNIQUE,
    name     VARCHAR(255) NOT NULL,
    email    VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated  TIMESTAMP             DEFAULT NULL
);

CREATE TABLE rt_products
(
    id          INTEGER PRIMARY KEY UNIQUE,
    name        VARCHAR(255)   NOT NULL,
    description TEXT           NOT NULL,
    collection  VARCHAR(255)   NOT NULL,
    category    VARCHAR(255)   NOT NULL,
    sx          VARCHAR(255)   NOT NULL,
    size        VARCHAR(255)   NOT NULL,
    price       DECIMAL(10, 2) NOT NULL,
    ratings     INTEGER,
    created     TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated     TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rt_carts
(
    id         INTEGER PRIMARY KEY UNIQUE,
    user_id    INT       NOT NULL,
    cart_items INT       NOT NULL,
    created    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES rt_users (uid),
    FOREIGN KEY (cart_items) REFERENCES rt_cart_item (id)
);

CREATE TABLE rt_cart_item
(
    id         INT PRIMARY KEY UNIQUE,
    cart_id    INT       NOT NULL,
    product_id INT       NOT NULL,
    qty        INT       NOT NULL,
    date_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cart_id) REFERENCES rt_carts (id),
    FOREIGN KEY (product_id) REFERENCES rt_products (id)
);
