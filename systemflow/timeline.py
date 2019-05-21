
import datetime
from dateutil.relativedelta import relativedelta

class Timeline:

    def __init__(self, start=None, stop=None, step=None):
        self.start = datetime.datetime.now() if isinstance(start, datetime.datetime) else start
        self.stop = stop
        self.step = relativedelta(**step) if isinstance(step, dict) else step

        self._cur_state = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_state >= self.stop:
            self._cur_state = self.start
            raise StopIteration
        self._cur_state += step

    @property
    def state(self):
        return self._cur_state


timeline = TimeLine()