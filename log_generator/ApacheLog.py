from faker import Faker
from faker_web import WebProvider
from datetime import timedelta, datetime
from log_generator import Log
from random import choice, randint
class ApacheLog(Log):
    def __init__(self, timestamp):
        Log.__init__(self)
        self._fake = Faker('en_US')
        self._fake.add_provider(WebProvider)
        self._ipv4 = self._fake.ipv4_public()
    #_faketime = _fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
    #logdate = LogLine.faketime + timedelta(seconds=randint(0, 50000))
    #LogLine.faketime = logdate
    #tz
        self._timestamp = timestamp
        self._useragent = self._fake.user_agent()
        self._uri_path = self._fake.uri_path(deep=2)
        self._uri_page = self._fake.uri_page()
        self._uri_extension = self._fake.uri_extension()
        self._endpoint = choice(["/uploads/" + self._fake.file_name(), "/"\
         + self._uri_path + "/" + self._uri_page + self._uri_extension])


        self._user = self._makeUser(self._fake.user_name())
        if not timestamp:
            self._faketime = self._fake.date_time_between_dates(datetime_start=datetime.now() - timedelta(days=15), datetime_end=datetime.now(), tzinfo=None)
        
        else:
            print("This is the timestamp:", self._timestamp)
            try:
                self._faketime = self._fake.date_time_between_dates(datetime_start=self._timestamp, datetime_end=datetime.now(), tzinfo=None)
            except ValueError:
                pass
        self._logtime = self._faketime + timedelta(seconds=randint(0, 360))
    def _makeUser(self, uname):
        return choice(["-", uname])
#self.fake.date_time_between_dates
