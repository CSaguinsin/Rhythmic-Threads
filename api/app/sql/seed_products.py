import random

from faker import Faker

from app.db import get_db

# Initialize Faker
fake = Faker()


# Function to generate a random price
def generate_price():
    return round(random.uniform(10.0, 500.0), 2)


# Function to generate a random rating
def generate_rating():
    return random.randint(1, 5)


# Function to generate a random collection
def generate_collection():
    collections = ['Summer 2023', 'Winter 2023', 'Fall 2023', 'Spring 2023']
    return random.choice(collections)


# Function to generate a random category
def generate_category():
    categories = ['Clothing', 'Accessories', 'Shoes', 'Bags']
    return random.choice(categories)


# Function to generate a random gender
def generate_sx():
    genders = ['Men', 'Women', 'Unisex']
    return random.choice(genders)


# Function to generate a random size
def generate_size():
    sizes = ['S', 'M', 'L', 'XL', 'One Size']
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
            "name": fake.name(),
            "description": fake.text(),
            "collection": generate_collection(),
            "category": generate_category(),
            "sx": generate_sx(),
            "size": generate_size(),
            "price": generate_price(),
            "ratings": generate_rating()
        }

        db.execute("INSERT INTO rt_products (name, description, collection, category, sx, size, price, ratings) "
                   "VALUES (:name, :description, :collection, :category, :sx, :size, :price, "
                   ":ratings)", product)
    db.commit()
    print("Products seeded successfully!")
