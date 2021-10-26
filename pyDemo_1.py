import collections
from pprint import pprint

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

# all courses
poop = course(name='poop', field="python", attendee=10, remote=False)
bdpy = course(name='bdpy', field="python", attendee=15, remote=True)
andbiz3 = course(name='andbiz', field='android', attendee=18, remote=True)
pykt = course(name='pykt', field="python", attendee=9, remote=True)
aiocv = course(name='aiocv', field="python", attendee=20, remote=False)
courses = (poop, bdpy, andbiz3, pykt, aiocv)
print("COURSE DATA >>", ''.join([str(value) for value in courses]))

# filter
# filter(lambda x: x.remote is True, courses) => filter object
# tuple(filter object) => tuple list
remoteCourses = tuple(filter(lambda x: x.remote is True, courses))
print("REMOTE COURSE DATA >>")
pprint(remoteCourses)

# pickup attendee >15
print("REMOTE COURSE DATA THAT　attendee>15 >>")
pprint(tuple(c for c in remoteCourses if c.attendee > 15))

name_and_field = map(lambda x: {'name': x.name, 'field': x.field}, courses)
pprint(name_and_field)
pprint([c for c in name_and_field])
pprint(tuple([c for c in name_and_field]))
pprint(tuple(name_and_field))

