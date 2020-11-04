Running the books/authors web application
CS257 Software Design
Fall 2020
Jeff Ondich

0. Read all the code!

This sample contains simple examples of all or nearly all of the techniques you will need to complete your web application. Read the code, collect questions, and ask them.


1. Running this example on your own machine

(a) Set up the database of books and authors. See books-webapp/data/readme.txt for instructions.

(b) Pick your port. I'll use 5000 in my examples

(c) Change config.py to use whatever database, user, and password works on your machine.

(d) Launch the web application & API

    python3 books_webapp.py localhost 5000

(e) Try it out. Direct your browser to:

    http://localhost:5000/

Assuming all goes well, you'll be able to click on the "Get Authors" button and get the list of authors.


2. Running this example on perlman.mathcs.carleton.edu

(a) Connect to the Carleton network. Either do your work from on campus, or use Carleton's VPN to connect to the campus network. VPN instructions are here: https://apps.carleton.edu/campus/its/services/accounts/offcampus/

(b) Login to perlman.mathcs.carleton.edu

    ssh YOURUSERNAME@perlman.mathcs.carleton.edu

The first time, it will bug you like so:

    The authenticity of host 'perlman.mathcs.carleton.edu (137.22.4.17)' can't be established.
    ECDSA key fingerprint is SHA256:SNNPkZGLd/E9fOOeYOVsq6zkaQ26aCRv128fXSrK/B0.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?

If the fingerprint listed is exactly as shown here, then type yes and hit Enter. Otherwise, type no and then let Mike Tie (mtie) and me know immediately, preferably with a screenshot.

(c) Go to your perlman web directory

    cd /Accounts/courses/cs257/jondich/web-f2020/YOURUSERNAME

(d) Grab a clone of this repository and go to the books-webapp directory

    git clone https://github.com/ondich/cs257_2020_fall
    cd cs257_2020_fall/books-webapp

(e) Obtain the port numbers that are available for your use. Jeff will email them to you. I'll call your port number YOURPORT below.

(f) Set up the database of books and authors. See books-webapp/data/readme.txt for instructions.

(g) Change config.py to use your perlman user name (i.e. your Carleton user name) for both user and database, and the empty string for password.

    user='YOURUSERNAME'
    database='YOURUSERNAME'
    password=''

(h) Launch the web application & API

    python3 books_webapp.py perlman.mathcs.carleton.edu YOURPORT

(i) Try it out. Direct your browser to:

    http://perlman.mathcs.carleton.edu:YOURPORT/

Assuming all goes well, you'll be able to click on the "Get Authors" button and get the list of authors.

(j) When you're done, Ctrl-C in the terminal to terminate the web application.

(k) [Instructions for running your page even when you're logged off of perlman will be forthcoming.]
