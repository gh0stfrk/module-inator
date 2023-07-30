from abc import ABC, abstractmethod

class BaseModule(ABC):
    """
    Base module for all sub-modules
    """

    def __init__(self, name, space_type, size, code) -> None:
        self.name = name
        self.space_type = space_type
        self.size = size
        self.code = code

    @abstractmethod
    def authenticate(self):
        """
        Autheticate into your spacecraft api system.
        """

    @abstractmethod
    def focus_on_targets(self):
        """
        Take aim on enemy space craft and lock sights on them.
        """
    
    @abstractmethod
    def reboot_system(self, admin_id):
        """
        Reebot spacecraft.
        """
