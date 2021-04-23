#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys


def area_of_rectangle(height, width = None): #default of width=none. if width is none, assumed equal to height, or can specify with two numbers
    """
    Returns the area of a rectangle.

    Parameters
    ----------
    height : int or float 
        The height of the rectangle.
    width : int or float
        The width of the rectangle. If `None` width is assumed to be equal to 
        the height.

    Returns
    -------
    int or float
        The area of the rectangle

    Examples
    --------
    >>> area_of_rectangle(7)
    49
    >>> area_of_rectangle (7, 2)
    14
    """
    if width:
        width = height
    import pdb; pdb.set_trace()
    area = int(height) * int(width)
    return area

if __name__ == '__main__':
    if (len(sys.argv) < 2) or (len(sys.argv) > 3): #need more than one argument
        message = (
                "{script_name}: Expecting one or two command-line arguments:\n"
                "\tthe height of a square or the height and width of a "
                "rectangle".format(script_name = sys.argv[0])) #sys.argv[0] the name of the argument/script name is at 0
        sys.exit(message) #length of sys.argv . the list of arguments at command line when script is run. first argument is name of scrpt itself, then the arguments passed. here checking the length, if <2 or >3, will print this message using the new line, tab format. 
    height = float(sys.argv[1])
    width = height
    if len(sys.argv) > 3:
        width = float(sys.argv[1])

    area = area_of_rectangle(height, width) #use function to get area

    message = "The area of a {h} X {w} rectangle is {a}".format(  #compose string to replace wiwth height, width, area in a string using those vvariables
            h = height,
            w = width,
            a = area)
    print(message)
#print and then done
