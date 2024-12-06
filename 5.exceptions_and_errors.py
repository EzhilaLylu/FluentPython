try:
    message = describe_favorite("dessert")
    print(message)
except KeyError:
    print("I have no favorite dessert. I love them all!")


# With exception object
nobles = {'He': 2, 'Ne': 10,
  'Ar': 18, 'Kr': 36, 'Xe': 54}
def show_element_info(elements):
   for element in elements:
       print('Atomic number of {} is {}'.format(
             element, nobles[element]))
try:
    show_element_info(['Ne', 'Ar', 'Br'])
except KeyError as err: # Notice how err created and being used in the except block
    missing_element = err.args[0]
    print(f"Missing data for element: {missing_element}")


# Raising Exceptions
def positive_int(value):
    number = int(value)
    if number <= 0:
        raise ValueError(f"Bad value: {value}") #raise
    return number


#check re
import re
def money_from_string(amount):
    match = re.search(
        r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
    # Adding the next two lines here
    if match is None:
        raise ValueError(f"Invalid amount: {amount}")
    dollars = int(match.group('dollars'))
    cents = int(match.group('cents'))
    return Money(dollars, cents)


# catching and re-raising
import os
import logging
from errno import EEXIST
UPLOAD_ROOT = "/var/www/uploads/"
def create_upload_dir(username):
    userdir = os.path.join(UPLOAD_ROOT, username)
    try:
        os.makedirs(userdir)
    except OSError as err:
        if err.errno != EEXIST:
            raise # re-raise in order to pass it to higher-level code
        logging.error("Upload dir already exists: %s",
            err.filename)
        

# error trace from logging module
import logging

def get_number():
    return int('foo')
try:
    x = get_number()
except:
    logging.exception('Caught an error')