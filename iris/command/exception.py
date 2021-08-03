class CommandException(Exception):
    """ Command base exception """
    pass


class UsageException(CommandException):
    """ Raised when usage message should be displayed """
    pass


class ArgumentValueError(CommandException):
    """ Raised when argument value doesn't match argument type """
    pass
