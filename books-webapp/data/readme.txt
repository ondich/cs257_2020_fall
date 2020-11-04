Setting up the books/authors database
CS257 Software Design
Fall 2020
Jeff Ondich

How to set up my books/authors data so you can run my sample web application.

1. Creating the database and using psql

- If you're on your own computer, you know how to set up a database and use psql to populate it and access it. You know your username, you know which database you're using (e.g. "books" or "postgres" or whatever you've been doing your work on), and you know whether you require a password to launch psql.

- If you're logged in to perlman.mathcs.carleton.edu using your Carleton user name (see books-webapp/readme.txt, item 2), then:

  * your database name is your Carleton user name, and you are barred
    from creating new databases (you can try, but it won't work).
    So your books/authors tables will be in the YOURUSERNAME database,
    not in a database named "books" or something like that.
        
  * your user name is your Carleton user name, too

  * you don't need to enter a password

So to connect to your database with psql while logged in to perlman? Just do this:

    psql


2. Create the tables in your PostgreSQL database

    CREATE TABLE authors (
        id integer NOT NULL,
        last_name text,
        first_name text,
        birth_year integer,
        death_year integer
    );

    CREATE TABLE books (
        id integer NOT NULL,
        title text,
        publication_year integer
    );

    CREATE TABLE books_authors (
        book_id integer,
        author_id integer
    );

3. Load the data. In psql:

    \copy authors from 'authors.csv' DELIMITER ',' CSV NULL AS 'NULL'
    \copy books from 'books.csv' DELIMITER ',' CSV NULL AS 'NULL'
    \copy books_authors from 'books_authors.csv' DELIMITER ',' CSV NULL AS 'NULL'

