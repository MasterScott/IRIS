import inspect

from abc import ABC, abstractmethod

from .exception import UsageException, ArgumentValueError


class Command(ABC):

    def __init__(self, shell):
        if not issubclass(self.__class__, Command):
            raise NotImplementedError('you cannot instantiate this class')

        self.shell = shell
        self.exit = False

    @property
    @abstractmethod
    def name(self) -> str:
        """ Command instance name """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """ Command instance description """
        pass

    @abstractmethod
    def run(self, *args):
        """ Abstract run method """
        pass

    @property
    def aliases(self) -> list[str]:
        """ Command instance name aliases """
        pass

    @property
    def has_aliases(self) -> bool:
        """ Check if Command instance has aliases """
        return self.__has_attrb('aliases')

    def __has_attrb(self, attrb: str) -> bool:
        """ Check if Command instance has specific attribute """
        try:
            return getattr(self, attrb) is not None
        except:
            return False

    @staticmethod
    def execute(fn):
        def _wrapper(*fn_args):
            args = inspect.getfullargspec(fn).annotations

            if len(fn_args) - 1 < len(args):
                raise UsageException(' '.join(f'<{arg_name.replace("__", "/").replace("_", " ")}>' for arg_name in args.keys()))

            self = fn_args[0]

            kwargs = {'self': self}

            for i, (param_name, param_type) in enumerate(args.items()):
                if param_type == tuple or param_type == list:  # used for starred expression 
                    kwargs[param_name] = param_type(fn_args[1 + i:])
                    break

                param_value = ' '.join(list(map(str, fn_args[1 + i:]))) if i == len(args.items()) - 1 else fn_args[1 + i]

                try:
                    kwargs[param_name] = param_type(param_value)
                except ValueError:
                    raise ArgumentValueError('Invalid value for argument \'%s\'. Was expecting type \'%s\'' % (param_name, param_type.__name__))

            return fn(**kwargs)
        return _wrapper
