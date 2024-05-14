import random

from faker import Faker

from app.db import get_db

# Initialize Faker
fake = Faker()


# Function to generate a random price
def __generate_price():
    return round(random.uniform(10.0, 500.0), 2)


# Function to generate a random rating
def __generate_rating():
    return random.randint(1, 5)


# Function to generate a random collection
def __generate_collection():
    collections = ["T-Shirts", "Jackets", "Shorts"]
    return random.choice(collections)


# Function to generate a random category
def __generate_category():
    categories = ["Male", "Female" "Kids"]
    return random.choice(categories)


# Function to generate a random size
def __generate_size():
    sizes = ["S", "M", "L", "XL", "XXL"]
    return random.choice(sizes)


def seed_products(count=5):
    """
    Seed the products table with random data.

    Default count is 5 products.

    :param count:
    :return:
    """
    db = get_db()

    for _ in range(count):
        product = {
            "image_url": fake.image_url(),
            "name": fake.name(),
            "description": fake.text(),
            "collection": __generate_collection(),
            "category": __generate_category(),
            "size": __generate_size(),
            "price": __generate_price(),
            "ratings": __generate_rating(),
        }

        db.execute(
            "INSERT INTO rt_products (image_url, name, description, collection, category, size, price, ratings) "
            "VALUES (:image_url, :name, :description, :collection, :category, :size, :price, :ratings)",
            product,
        )
    db.commit()
    print("Products seeded successfully!")
