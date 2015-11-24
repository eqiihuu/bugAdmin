from django.test import TestCase
from bugs.models import Stage, Bug
import time
# Create your tests here.

problem = 'Connection failed'
create_person = 'Diana'
create_time = time.strftime('%Y-%m-%d %H:%M:%S')
note = 'For test of stage time'
new_bug = Bug(id=1, problem=problem, create_person=create_person, create_time=create_time, note=note)

update_person = 'Charles'
update_time = time.strftime('%Y-%m-%d %H:%M:%S')
status = 'Ongoing'
note = 'For test'
new_stage = Stage(bug=new_bug, status=status, update_person=update_person, update_time=update_time, note=note)

print new_stage
