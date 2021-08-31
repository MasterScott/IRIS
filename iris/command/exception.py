class IRISCommandException(Exception):
    """ Command base exception """
    pass


class UsageException(IRISCommandException):
    """ Raised when usage message should be displayed """
    pass


class ArgumentValueError(IRISCommandException):
    """ Raised when argument value doesn't match argument type """
    pass
