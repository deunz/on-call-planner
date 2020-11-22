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
from wcontraint import WeekConstraintPeople
constraint_base = [
    # January (Start at 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    0, 0, 0, 0,

    # August
    0, 0, 0, 0, 0,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]

constraint_denis = [
    # January (Commence le 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    1, 1, 0, 0,

    # August
    0, 0, 0, 0, 1,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]

constraint_gilles = [
    # January (Commence le 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    0, 0, 0, 0,

    # August
    0, 0, 0, 0, 0,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]

constraint_phiphi = [
    # January (Commence le 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    0, 0, 0, 0,

    # August
    0, 0, 0, 0, 0,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]

constraint_azzedine = [
    # January (Commence le 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    0, 0, 0, 0,

    # August
    0, 0, 0, 0, 0,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]

constraint_shenly = [
    # January (Commence le 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    0, 0, 0, 0,

    # August
    0, 0, 0, 0, 0,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]

constraint_kevin = [
    # January (Commence le 4 January)
    0, 0, 0, 0,

    # February
    0, 0, 0, 0,

    # March
    0, 0, 0, 0, 0,

    # April
    0, 0, 0, 0,

    # May
    0, 0, 0, 0, 0,

    # June
    0, 0, 0, 0,

    # July
    0, 0, 0, 0,

    # August
    0, 0, 0, 0, 0,

    # September
    0, 0, 0, 0,

    # October
    0, 0, 0, 0,

    # November
    0, 0, 0, 0, 0,

    # December
    0, 0, 0, 0,
]


people = ['Denis', 'Gilles', 'Phiphi', 'Shenly', 'Kevin', 'Azzedine']
# num_people = len(people)
# all_people = range(num_people)

# Keep same order dude!
people_constraints_ = [WeekConstraintPeople(constraint_denis),
                      WeekConstraintPeople(constraint_gilles),
                      WeekConstraintPeople(constraint_phiphi),
                      WeekConstraintPeople(constraint_shenly),
                      WeekConstraintPeople(constraint_kevin),
                      WeekConstraintPeople(constraint_azzedine)
                      ]


class PeopleConstraints(object):
    def __init__(self, people, people_constraints_: list):
        self.num_people = len(people)
        self.all_people = range(self.num_people)
        self.people_constraints = people_constraints_

    def is_want_not_working(self, p, w):
        return self.people_constraints[p].is_want_not_working(w)

    def is_want_work(self, p, w):
        return self.people_constraints[p].is_want_work(w)


people_constraints = PeopleConstraints(people, people_constraints_)