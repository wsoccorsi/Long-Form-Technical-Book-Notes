# Understanding Normalization

Based on https://www.youtube.com/watch?v=GFQaEYEc8_8

## Why do we normalize data?
* To make data agree with itself, ex: a customer id with two birthdays
* To make a database not express redudant information so it can only represent one version of the truth
* Easier to understand
* Easier to enhance and extend
* Protected from
	- Insertin Anamolies
	- Update Anamolies
	- Delete Anamolies
* Normal forms represent levels of database safety

## First Normal Form
* Violates 1nF
 - Cannot use row order to convey information, i/e the beetles inserted into a table by height
 - Cannot mix data types i/e height column in centimers which says "somewhere between 5'7 and 5'9"
 - Designing a column without a primary key
 - Repeating groups, a csv column

## Second Normal Form
* Violates 2nF
 - Attributes that don't belong to the primary key

2nF: Each non-key attribute must depend on the entire primary key. EX a players
inventory (primary key) does not depend on their player rating.

## Third Normal Form
* Violates 3nF
 - A non key attribute is dependant on another non key attribute

3nf: Every non-key attribute in a table should depend on the key, the whole key, and nothing but 
the key. (Boyce-Codd normal form wipes out the non-key word)

1, 2, 3 normal form is usually a fully normalized table and thats all you really need.

## Fourth Normal Form
* The only kinds of multivalued dependy allowed in a table are multivalued dependenices on the key

## Fifth Normal Form
* It must not be possible to describe the table as being the logical result of joining some other tables together.
