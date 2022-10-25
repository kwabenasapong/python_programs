#!/usr/bin/python3
'''for studying object serialisation and deserialisation'''
import json
from datetime import datetime
from pprint import pprint


simple = dict(int_list=[1, 2, 3],
            text='string',
            number=3.44,
            boolean=True,
            none=None)

print(json.dumps(simple, indent=4))


class A(object):

    def __init__(self, simple):
        self.simple = simple

    def __eq__(self, other):
        if not hasattr(other, 'simple'):
            return False
        return self.simple == other.simple

    def __ne__(self, other):
        if not hasattr(other, 'simple'):
            return True
        return self.simple != other.simple

complex = dict(a=A(simple), when=datetime(2016, 3, 7))

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__': o.replace(microsecond=0).isoformat()}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}

serialized = json.dumps(complex, indent=4, cls=CustomEncoder)
print(serialized)

def decode_object(o):
    if '__A__' in o:
        a = A(o)
        a.__dict__.update(o['__A__'])
        return a
    elif '__datetime__' in o:
        return datetime.strptime(o['__datetime__'], '%Y-%m-%dT%H:%M:%S')
    return o

deserialized = json.loads(serialized, object_hook=decode_object)

print(deserialized)



