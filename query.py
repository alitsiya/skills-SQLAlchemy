"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.brand_name == 'Chevrolet', Model.name == 'Corvette').all()


# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    cars = Model.query.filter(Model.year == year).all()
    for car in cars:
        print "Model: %s, brand name: %s , headquarters: % s" % (car.name, car.brand_name, car.brand[0].headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()
    for brand in brands:
        for model in brand.model:
            print brand.name, model.year, model.name

    # Fill in get_brands_summary so that it takes nothing as input and prints each brand name, 
    # and all of that brand's models. (Feel free to format with newlines 
    #     (\n) and/or tabs (\t) to create helpful and readable output.)

# -------------------------------------------------------------------

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    
    list_of_brands = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    return list_of_brands

# Design a function in python that takes in any string as parameter, and returns
#  a list of objects that are brands whose name contains or is equal to the input string.

def get_models_between(start_year, end_year):
    """Function takes in a start year and end year (two integers), and returns 
    a list of objects that are models with years that fall between the start year and end year."""
    
    list_of_models = Models.query.filter(Model.year >= start_year, Model.year <= end_year).all()
    return list_of_models

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# It's a query, datatype is an object of class flask_sqlalchemy


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# Assosiation table is a virtual table created by inner join using foreign key
# It can have one-to-many relationship.
