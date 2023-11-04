################################################################################
#     ____                          __     _                           ______
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____           / ____/
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         /___ \  
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ____/ /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_____/   
#                                                                            
#  Question 5
################################################################################
#
# Instructions:
# This questions continues to use the database we worked with in Question 4. In 
# this question, we will made some modifications ot the table.

# Part 5.A:
# Create a new table, 'favorite_foods.' It should have the columns:
# food_id integer
# name text
# vegetarian integer

sql_create_favorite_foods = """

CREATE TABLE FAVORITE_FOODS (
    food_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    vegetarian INTEGER NOT NULL CHECK (vegetarian IN (0, 1))
);


"""

# Part 5.B:
# Alter the animals and people tables by adding a new column to each called 'favorite_food_id'
# The test suite will verify the new changes by inserting some new rows. 


sql_alter_tables_with_favorite_food = """

ALTER TABLE ANIMALS
ADD COLUMN favorite_food_id INTEGER;

ALTER TABLE PEOPLE
ADD COLUMN favorite_food_id INTEGER;


/*
    The FK allows us to do faster queries (since they are usually a prime target for indexing)
    and to enforce the business model

    SADLY, sqlite does not allow to ADD CONSTRAINT while doing an ALTER TABLE operation.

    Constrains are only available during table creation (IN SQLITE, other engines allow it during ALTER TABLE Ops)
    
    For reference, here the instructions to do FK on ANIMALS and PEOPLE:

    -- Create a foreign key constraint on 'favorite_food_id' in the 'ANIMALS' table
    ALTER TABLE ANIMALS
    ADD CONSTRAINT fk_animals_favorite_food
    FOREIGN KEY (favorite_food_id)
    REFERENCES FAVORITE_FOODS(food_id);

    -- Create a foreign key constraint on 'favorite_food_id' in the 'PEOPLE' table
    ALTER TABLE PEOPLE
    ADD CONSTRAINT fk_people_favorite_food
    FOREIGN KEY (favorite_food_id)
    REFERENCES FAVORITE_FOODS(food_id);


*/



"""

# Part 5.C:
# Write a query to select all pets that are vegetarian.
# THe output should be a list of tuples in the format: (<pet name>, <food name>)

sql_select_all_vegetarian_pets = """

SELECT A.name AS pet_name, F.name AS food_name
FROM ANIMALS A
JOIN FAVORITE_FOODS F ON A.favorite_food_id = F.food_id
WHERE F.vegetarian = 1;

"""