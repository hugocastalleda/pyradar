# -*- coding: utf-8 *-*
"""
Utils for calculating time periods for the runs of the algorithms.
"""
from datetime import datetime


class Timer(object):

    def __init__(self):
        self.start_instant = datetime.now()
        self.stop_instant = None

    def __unicode__(self):
        """
        Docs about timetuple:
        http://docs.python.org/library/datetime.html#datetime.datetime.strftime
        """
        tt = self.start_instant.timetuple()
        return 'Timer started at: hour: %s, min: %s, sec: %s' % \
                                        (tt.tm_hour, tt.tm_min, tt.tm_sec)

    def restart_timer(self):
        """
        Overwrite the start time of the timer.
        """
        self.start_instant = datetime.now()

    def stop_timer(self):
        self.stop_instant = datetime.now()

    def calculate_time_elapsed(self, print_value=False):

        start_time = self.start_instant
        time_now = datetime.now()

        diff = time_now - start_time

        mins = diff.min if diff.min.seconds else 0
        secs = diff.seconds if diff.seconds else 0
        microsecs = diff.microseconds if diff.microseconds else 0

        if secs > 60:
            mins = secs / 60
            secs = secs % 60

        if print_value:
            print "Run took: %s mins, %s secs, %s microsecs." \
                                                % (mins, secs, microsecs)

        time_diff = {'full_diff': diff,
                     'mins': mins,
                     'secs': secs,
                     'microsecs': microsecs,
                    }
        return time_diff
