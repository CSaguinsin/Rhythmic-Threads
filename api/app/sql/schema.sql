DROP TABLE IF EXISTS rt_users;
DROP TABLE IF EXISTS rt_products;
DROP TABLE IF EXISTS rt_carts;
DROP TABLE IF EXISTS rt_cart_items;

CREATE TABLE rt_users
(
    id       INT PRIMARY KEY UNIQUE,
    name     TEXT      NOT NULL,
    email    TEXT      NOT NULL,
    password TEXT      NOT NULL,
    created  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated  TIMESTAMP          DEFAULT NULL
);

CREATE TABLE rt_products
(
    id          INT PRIMARY KEY UNIQUE,
    name        TEXT           NOT NULL,
    description TEXT           NOT NULL,
    collection  TEXT           NOT NULL,
    category    TEXT           NOT NULL,
    sx          TEXT           NOT NULL,
    size        TEXT           NOT NULL,
    price       DECIMAL(10, 2) NOT NULL,
    ratings     INT,
    created     TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated     TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rt_carts
(
    id         INT PRIMARY KEY UNIQUE,
    user_id    INT       NOT NULL,
    cart_items INT       NOT NULL,
    created    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES rt_users (uid),
    FOREIGN KEY (cart_items) REFERENCES rt_cart_item (id)
);

CREATE TABLE rt_cart_items
(
    id         INT PRIMARY KEY UNIQUE,
    cart_id    INT       NOT NULL,
    product_id INT       NOT NULL,
    qty        INT       NOT NULL,
    date_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cart_id) REFERENCES rt_carts (id),
    FOREIGN KEY (product_id) REFERENCES rt_products (id)
);
