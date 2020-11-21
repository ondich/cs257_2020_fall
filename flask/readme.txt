Flask samples for CS257
Jeff Ondich
Updated 6 November 2020

1. flask_sample.py
- This one illustrates a simple API that returns JSON results.
- The /actor/<last_name> route illustrates routes with variable URL components (<last_name> in this case)
- The /movies route illustrates the use of GET parameters (i.e. the name=value pairs that comes after a ? in a URL)

2. template_sample.py
This illustrates a couple ways Flask's templating features can be used
- [index.html, hello.html, shared-header/*.html] using url_for to generate links to files stored in the static folder
- [hello.html] incorporating user input into a template, with automatic protection against injection attacks
- [shared-header/*.html] using {% include ... %} to share common HTML code across multiple templates
- 
