#!/usr/bin/env python
# Author: https://github.com/deunz
# From nurse example
# https://developers.google.com/optimization/scheduling/employee_scheduling
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
num_week = 52
all_week = range(num_week)


class WeekConstraint(list):
    def __init__(self, init=None):
        if init is None:
            init = [0] * num_week

        if len(init) != num_week:
            raise ValueError("week constraint must have 52 weeks")

        super(WeekConstraint, self).__init__(init)

        self.initialize()

    def initialize(self):
        pass


class WeekPublicHoliday(WeekConstraint):
    def __init__(self, num_people):
        self._num_people = num_people
        super(WeekPublicHoliday, self).__init__()

    def initialize(self):
        # nouvelle an
        self[0] = 1

        # paques
        self[13] = 1

        # fete du travail
        self[16] = 1

        # 8 mai
        self[17] = 1

        # ascension
        self[18] = 1

        # pentecote
        self[20] = 1

        # 14 juillet
        self[27] = 1

        # 15 aout
        self[32] = 1

        # toussaint
        self[43] = 1

        # armistice
        self[44] = 1

        # noel
        self[50] = 1

    def is_public_holiday(self, i):
        return self[i] == 1

    def num_weeks(self):
        return len(self)

    def num_of_off_days(self):
        return len(list(filter(lambda x: x == 1, self)))

    def min_day_per_people(self):
        return self.num_of_off_days() // self._num_people

    def max_day_per_people(self):
        return self.min_day_per_people() + 1


class WeekConstraintPeople(WeekConstraint):
    def is_want_not_working(self, i):
        return self[i] == -1

    def is_want_working(self, i):
        return self[i] == 1
