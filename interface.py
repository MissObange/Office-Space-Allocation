#!venv/bin/python
"""
Usage:
	Dojo create_room <room_type> <room_name> ...
	Dojo add_person <person_name> <FELLOW/STAFF> <wants_accommodation>
	Dojo print_room <room_name>
	Dojo print_allocations
	Dojo print_unallocated
	Dojo relocate_person <person_identifier> <new_room_name>
	Dojo load_people
	my_app (-i | --interactive)
    my_app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
#from ticket_booking_functions import New_events, New_tickets




def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class Allocations(cmd.Cmd):
	intro = "Welcome to the Andela Dojo Office and Space Allocation System"
	prompt = "Action: >>"
	file = None


	@docopt_cmd
	def do_create_room(self, arg):
		"""
		Usage: 
			create_room <room_type> <room_name> ...
		"""
