# Objective
* Find all week that impact each people with according to following constraint
    
    
# Constraints
* same number of on call per people (+ or - one)
* no on-call 2 week right now
* right division on year (at least on on-call each 8 weeks), because 6 people at on-call
* right division of public holiday (+ or - one)
* (maximized solution with people preference)


# How to create a people preference
In the file `pcontraints.py`, complete your array (constrainte_ _votreprenom_):
* 0 = no preference
* 1 = request on-call

# How to use it
* Execute the file `schedule.py` with or without the -p flags

Pass the -p flags for maximize solution with preference, otherwise don't use it


**Very important**

Keep and respect all systems constraint, otherwise the solver can't find any suitable solution
