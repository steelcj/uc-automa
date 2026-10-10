"""The one exception uc-automa raises for anything it refuses to do."""


class AutomaError(Exception):
    """A configuration, layout or repository uc-automa will not act on.

    The command line turns it into a message and exit status 1.
    """
