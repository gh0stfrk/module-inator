"""
Tesla api controller.
"""

import time
from modules.models import BaseModule


class Tesla(BaseModule):
    """
    Fordcraft ships api mapped to base module
    """

    def __init__(self, name, space_type, size, code) -> None:
        super().__init__(name, space_type, size, code)
        self.auth_status = False
        self.target_coords = {}

    def authenticate(self):
        """
        Log into the sssytem
        """
        print("Logging in...")
        time.sleep(3.1)
        print("Logged in Tesla69.")
        if self.name:
            self.auth_status = True
        return True

    def focus_on_targets(self):
        """
        Lock the targets.
        """
        self.target_coords["alpha"] = 82.33
        self.target_coords["beta"] = 33.23
        print("Targets recorded.")
        return True

    def reboot_system(self, admin_id):
        """
        Reboots entire spacecraft.
        """
