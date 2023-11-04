import pets_db
import sqlite3
################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)


sql_pets_owned_by_nobody = """

SELECT ANIMALS.name, ANIMALS.species, ANIMALS.age
FROM ANIMALS
LEFT JOIN PEOPLE_ANIMALS ON ANIMALS.animal_id = PEOPLE_ANIMALS.pet_id
WHERE PEOPLE_ANIMALS.owner_id IS NULL;

"""
                        

# Part 4.B:
# Write SQL to select  the number of pets that are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT SUM(CASE WHEN ANIMALS.age > PEOPLE.age THEN 1 ELSE 0 END) AS count
FROM ANIMALS
INNER JOIN PEOPLE_ANIMALS ON ANIMALS.animal_id = PEOPLE_ANIMALS.pet_id
INNER JOIN PEOPLE ON PEOPLE_ANIMALS.owner_id = PEOPLE.person_id;

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)


# This query aims to be as efficient as possible by limiting subqueries usage 
# We used an existential subquery to facilitate the conditional filtering
sql_only_owned_by_bessie = """ 

SELECT P.name AS person_name, A.name AS pet_name, A.species
FROM ANIMALS A
JOIN PEOPLE_ANIMALS PA ON A.animal_id = PA.pet_id
JOIN PEOPLE P ON PA.owner_id = P.person_id
WHERE LOWER(P.name) = 'bessie'
AND NOT EXISTS (
    SELECT 1
    FROM PEOPLE_ANIMALS PA2
    WHERE PA2.pet_id = PA.pet_id
    AND PA2.owner_id <> P.person_id
);

"""