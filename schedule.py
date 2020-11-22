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
from __future__ import print_function
from ortools.sat.python import cp_model
from wcontraint import all_week, num_week, WeekPublicHoliday
from pcontraints import people, people_constraints, people_constraints_
import argparse

class PeoplePartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, shifts, people, num_week, sols):
        cp_model.CpSolverSolutionCallback.__init__(self)

        self._shifts = shifts
        self._people = people
        self._num_people = len(people)
        self._num_week = num_week
        self.wph = WeekPublicHoliday(self._num_people)
        self._solutions = set(sols)
        self._solution_count = 0

    def display_solution(self, solution):
        for w in range(self._num_week):
            for p in range(self._num_people):
                if solution.Value(self._shifts[(p, w)]):
                    print('Week %i: %s' % (w, self._people[p]))
        print()
        print("Statistics special week:")
        people_stat = {}
        for p in range(self._num_people):
            nb_special_week = 0
            for w in range(self._num_week):
                if self.wph[w] == 1 and solution.Value(self._shifts[(p, w)]):
                    nb_special_week += 1
            people_stat[self._people[p]] = nb_special_week
        people_stat_sorted = {k: v for k, v in sorted(people_stat.items(),
                                                      key=lambda item: item[1],
                                                      reverse=True)}
        for p, v in people_stat_sorted.items():
            print("%s: %s" % (p, v))

    def on_solution_callback(self):
        if self._solution_count in self._solutions:
            print('Solution %i' % self._solution_count)
            self.display_solution(self)
        self._solution_count += 1

    def solution_count(self):
        return self._solution_count


def main():
    parser = argparse.ArgumentParser(prog='schedule')
    parser.add_argument('-p', '--with_preference', action='store_true',
                        help='Adding people preference, maximize solution')
    args = parser.parse_args()

    model = cp_model.CpModel()
    all_people = people_constraints.all_people
    num_people = people_constraints.num_people
    wph = WeekPublicHoliday(num_people)



    # variable for the system
    shifts = {}
    for p in all_people:
        for w in all_week:
            shifts[(p, w)] = model.NewBoolVar('shift_%s_%s' % (p, w))

    min_shifts_per_people = num_week // num_people
    max_shifts_per_people = min_shifts_per_people + (num_people - (num_week % num_people))

    # Each people works at most one shift per year.
    for p in all_people:
        model.Add(sum(shifts[(p, w)] for w in all_week) <= max_shifts_per_people)

    # one person per astreinte (work fine)
    for w in all_week:
        model.Add(sum(shifts[(p, w)] for p in all_people) == 1)

    # try to distribute evenly
    for p in all_people:
        num_shifts_worked = 0
        for w in all_week:
            num_shifts_worked += shifts[(p, w)]
        model.Add(min_shifts_per_people <= num_shifts_worked)
        model.Add(num_shifts_worked <= max_shifts_per_people)

    # never 2 astreinte in continious
    for w in range(1, num_week):
        for p in all_people:
            model.Add(shifts[(p, w-1)] + shifts[(p, w)] <= 1)

    # on 8 weeks, at least 1 no more 2
    for p in all_people:
        for b in range(6):
            model.Add(sum(shifts[(p, 8*b+qw)] for qw in range(8)) >= 1)
            model.Add(sum(shifts[(p, 8*b+qw)] for qw in range(8)) <= 2)

    # equity public holiday
    for p in all_people:
        constraint_eq = 0
        for w in range(num_week):
            if wph.is_public_holiday(w):
                constraint_eq += shifts[(p, w)]

        model.Add(constraint_eq >= wph.min_day_per_people())
        model.Add(constraint_eq <= wph.max_day_per_people())

    solver = cp_model.CpSolver()
    if args.with_preference:
        # try to satisfy preference
        model.Maximize(
            sum(people_constraints_[p][w] * shifts[(p, w)] for p in all_people
                for w in all_week))

        solver.Solve(model)
        ppsp = PeoplePartialSolutionPrinter(shifts, people, num_week, [])
        ppsp.display_solution(solver)
    else:
        # try to find the best
        # 0=the best only
        # 1=permit more flexibility on solutions
        solver.parameters.linearization_level = 0
        # solver.parameters.num_search_workers = 8
        # Sets a time limit of 10 seconds.
        solver.parameters.max_time_in_seconds = 10.0
        # Display the first five solutions.
        a_few_solutions = range(3)
        solution_printer = PeoplePartialSolutionPrinter(shifts, people,
                                                        num_week, a_few_solutions)
        status = solver.SearchForAllSolutions(model, solution_printer)
        print("Solution %s" % solver.StatusName(status))
        print('Statistics')
        print('  - conflicts       : %i' % solver.NumConflicts())
        print('  - branches        : %i' % solver.NumBranches())
        print('  - wall time       : %f s' % solver.WallTime())
        print('  - solutions found : %i' % solution_printer.solution_count())


if __name__ == '__main__':
    main()
