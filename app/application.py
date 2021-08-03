import importlib
import inspect
import sys
import os

from typing import Union

from iris.logger import Logger
from iris.module import Module, ModuleWrapper
from iris.command import Shell
from iris.util import PathUtil, ConsoleUtil


class Application:

    class __ModuleManager:
        """ Used to manage IRIS modules """

        DISABLE_PREFIX = '-'
        """ The module manager will ignore (not register) any modules which file name is prefixed with this prefix """

        def __init__(self):
            self.__modules = []

        def register_module(self, path: str, mod: "Module"):
            """ Register module wrapper to module list """
            self.__modules.append(ModuleWrapper(path, mod))

        def get_module_by_name(self, mod_name: str) -> Union["ModuleWrapper", None]:
            """ Get module wrapper object by string name from module list """
            mod_name = mod_name.lower()
            for mod in self.get_registered_modules():
                if mod_name == mod.name.lower():
                    return mod
            return None

        def get_module(self, module: Union[str, int]) -> "ModuleWrapper":
            """ Get module by name or index. This method will raise an Exception if module is not found """
            if module.isdigit():
                mod_index = int(module) - 1

                if mod_index < 0:
                    raise Exception('Module not found')

                try:
                    mod = self.get_registered_modules()[mod_index]
                except IndexError:
                    raise Exception('Module not found')
            else:
                mod = self.get_module_by_name(module)

                if mod is None:
                    raise Exception('Module not found')
            return mod

        def get_registered_modules(self) -> list["ModuleWrapper"]:
            """ Get list of registered modules sorted in alphabetical order """
            return sorted(self.__modules.copy(), key=(lambda x : x.name))

        def clear(self):
            """ Clear module list """
            self.__modules.clear()

        def register_modules_from_path(self, path):
            """ Register modules from system path """
            for root, _, files in os.walk(path):
                for file_name in files:
                    if not file_name.endswith('.py') or file_name.startswith('__') or file_name.startswith(self.DISABLE_PREFIX):
                        continue

                    file_path = os.path.join(root, file_name)
                    mod_path = PathUtil.sys_to_module(file_path)

                    try:
                        if not importlib.import_module(mod_path):
                            continue
                    except Exception as e:
                        Logger.error(f'Failed to import module: {file_path}')
                        Logger.error(f'Exception: \x1b[91m{e}\x1b[0m')

                        if ConsoleUtil.yn_prompt('Continue? (Y/n): ') is True:
                            continue

                        sys.exit(-1)

                    for _, Class in inspect.getmembers(sys.modules[mod_path], inspect.isclass):
                        if issubclass(Class, Module) and Class != Module:
                            self.register_module(file_path, Class())

    def __init__(self):
        if os.name == 'nt':  
            import colorama
            colorama.init(convert=True)

        self.__shell = Shell('\x1b[94m➜\x1b[0m ')

        self.__module_manager = self.__ModuleManager()
        self.__module_manager.register_modules_from_path('modules')

        self.__shell.command_manager.register_commands_from_path(os.path.join('iris', 'command', 'impl'))

    @property
    def modules(self):
        """ Get module manager """
        return self.__module_manager

    def start(self):
        """ Start application """
        ConsoleUtil.clear_screen()
        ConsoleUtil.set_title('IRIS v%(version)s by %(author)s')
        ConsoleUtil.print_banner()

        self.__shell.start()
