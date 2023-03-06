# Learn PostgreSQL - by Luca Ferrari and Enrico Pirozzi

Build and manage high-performance database solutions using PostgreSQL 12 and 13 


## Chapter 4 - Basic Statements

* DDL (Data Definition Language) - To manage db and tabs 
* DML (Data Manipulation Language) - Used to insert, delete, update, and select

## Chapter 5 - Advanced Statements


Safe operator equivalent, if null you can sub in a value. Think in terms of columns

    select coalesce(NULL, 'test');
    
    coalesce
    --------
    test
    

##### Learning Joins

* We can think of a join as a combination of rows from two or more tables (115.)
* 