#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 26 September 2020

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2020.

    An instance of the BooksDataSource class described below is intended
    to provide access to data about books and authors. The particular form
    in which the books and authors are stored may depend on the context,
    but the method interfaces will remain unchanged from context to context.

    This is intended in part as a reminder, post-CS201, that any given
    class or function interface might have many different implementations.
    (Think about Java, where both ArrayList and LinkedList provide
    implementations of the List interface, but with different time complexity
    for various operations.)

    This class's two methods (not including __init__) return lists of
    dictionaries, each dictionary representing either a book or an author.

    Each author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    An author's ID is an arbitrary integer, whose only constraint is that
    different authors must have different IDs. For example, Jane Austen
    would be represented like this (assuming her ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 134, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'title',
    'publication_year', and 'author_id'. For example, "A Wild Sheep Chase"
    would look like this:

        {'title': 'A Wild Sheep Chase', 'publication_year': 1982, 'author_id': 134}

    Note that unlike in your first books-related assignment, books accessible
    through a BooksDataSource object may only have one author. (So sad, no
    "Good Omens" for us.) We'll take a closer look at this issue in a later
    assignment.
'''

class BooksDataSource:
    def __init__(self, books_csv_file_name, authors_csv_file_name):
        ''' Initializes whatever instance variables are required to implement the
            other methods in this class.
            
            The books CSV file format:

                author_id,title,publication_year
                4,Jane Eyre,1847
                22,Bleak House,1852

            The authors CSV file format:
                id,last_name,first_name,birth_year,death_year
                23,Carré,John Le,1931,NULL
                18,DuMaurier,Daphne,1907,1989

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.
        '''
        pass

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return a list of
            dictionaries representing all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
                
            See the BooksDataSource comment for a description of how a book is represented.

            This method raises a ValueError if author_id is non-None but is not a valid author ID.
        '''
        return []

    def authors(self, search_text=None):
        ''' Returns a list of all the authors in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then authors
            returns all of the authors, sorted by birth year.

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        return []


'''
    Some things to think about.

    1. Here are some examples :

        data_source = BooksDataSource()
        books = data_source.books(search_text='the')

    The books variable should now refer to a list like this:
    
        [{'title':'The Fire Next Time',...}, {'title':'There, There',...},...]

    with one dictionary per book.

    Similarly:

        data_source = BooksDataSource()
        authors = data_source.authors(search_text='ill')

    should give us a list something like this:

        [{'id':27, 'last_name':'Melville',...}, {'id':142, 'last_name':'Willis',...},...]

    One way to get comfortable with an interface is to generate examples like this to
    see if they make sense to you.

    2. Do you know what it means to "raise an exception" in Python? If not, ask me or do some research.
       (By the way, it is common to use the verb "throw" instead of "raise" when talking about
       exceptions in general, but Python's exception syntax uses "raise".)

    3. QUESTION: Should the books() and authors() interfaces raise TypeError, and if so, when?
       For example, books() could raise a TypeError if author_id, start_year, or end_year are
       not None but not of type int, or if search_text is not None but not of type str.
       That is, we could raise TypeError any time a parameter has an unexpected type.
       ANSWER, FOR NOW: We won't do this for this assignment, but it deserves discussion.

    4. QUESTION: How about ValueError? And if so, for which parameters?
       ANSWER: note that we've specified a ValueError in books() if author_id is non-None.
       For now, we won't try to raise ValueError in any other context.
'''

