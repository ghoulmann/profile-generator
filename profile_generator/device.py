from profile_generator.profile import Profile
from random import choice

class Device:
    def __init__(self, *owner):
        Profile.__init__(self)
        if owner:
            self.owner = owner
        self.hostname = self.fake.hostname()
        self.ipv4 = self.fake.ipv4_public()
        self.password = self.fake.password()
        self.user_name = self.fake.user_name()
        self.wireless_device = choice([True, False])
        if self.wireless_device:
            self.ssid = self.fake.mac_address()
        del(self.fake)