# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_me_query 1'] = {
    'data': {
        'me': {
            'cellPhone': '+14153334444',
            'contexts': {
                'count': 2,
                'edges': [
                    {
                        'cursor': 'YXJyYXljb25uZWN0aW9uOjA=',
                        'node': {
                            '__typename': 'ParticipantContext',
                            'id': 'UGFydGljaXBhbnRDb250ZXh0OjE=',
                            'profile': {
                                'avatar': 'https://example.com/images/me.jpg',
                                'bio': '''Hey!

What are you looking at?''',
                                'displayName': 'Johnny',
                                'id': 'UHJvZmlsZTox'
                            },
                            'status': 'CREATED'
                        }
                    },
                    {
                        'cursor': 'YXJyYXljb25uZWN0aW9uOjE=',
                        'node': {
                            '__typename': 'FacilitatorContext',
                            'availability': '[{"isoWeekDay": 1, "start": "14:49:31.947740", "end": "22:49:31.947749"}, {"isoWeekDay": 2, "start": "14:49:31.947758", "end": "22:49:31.947760"}, {"isoWeekDay": 3, "start": "14:49:31.947765", "end": "22:49:31.947766"}, {"isoWeekDay": 4, "start": "14:49:31.947770", "end": "22:49:31.947772"}, {"isoWeekDay": 5, "start": "14:49:31.947776", "end": "22:49:31.947777"}, {"isoWeekDay": 6, "start": "14:49:31.947781", "end": "22:49:31.947782"}, {"isoWeekDay": 7, "start": "14:49:31.947786", "end": "22:49:31.947788"}]',
                            'id': 'RmFjaWxpdGF0b3JDb250ZXh0OjI=',
                            'licenses': {
                                'edges': [
                                    {
                                        'cursor': 'YXJyYXljb25uZWN0aW9uOjA=',
                                        'node': {
                                            'expiry': '2022-02-08',
                                            'id': 'RmFjaWxpdGF0b3JMaWNlbnNlOjE=',
                                            'number': 'xpii23420e90',
                                            'type': 'TBD',
                                            'usState': 'NY'
                                        }
                                    },
                                    {
                                        'cursor': 'YXJyYXljb25uZWN0aW9uOjE=',
                                        'node': {
                                            'expiry': None,
                                            'id': 'RmFjaWxpdGF0b3JMaWNlbnNlOjI=',
                                            'number': 'xpn342300309e8',
                                            'type': 'TBD',
                                            'usState': None
                                        }
                                    },
                                    {
                                        'cursor': 'YXJyYXljb25uZWN0aW9uOjI=',
                                        'node': {
                                            'expiry': '2016-02-08',
                                            'id': 'RmFjaWxpdGF0b3JMaWNlbnNlOjM=',
                                            'number': 'expired',
                                            'type': 'TBD',
                                            'usState': 'NY'
                                        }
                                    }
                                ],
                                'pageInfo': {
                                    'endCursor': 'YXJyYXljb25uZWN0aW9uOjI=',
                                    'hasNextPage': False,
                                    'hasPreviousPage': False,
                                    'startCursor': 'YXJyYXljb25uZWN0aW9uOjA='
                                }
                            },
                            'npi': 'nc2394jt98ddeesd',
                            'profile': {
                                'avatar': 'https://dr-smith.com/photos/dr-smith.jpg',
                                'bio': '''I don't know how to put this but I'm kind of a big deal.

 People know me. I'm very important. 

I have many leather-bound books and my apartment smells of rich mahogany.''',
                                'displayName': 'Dr. Smith',
                                'id': 'UHJvZmlsZToy'
                            },
                            'status': 'CREATED'
                        }
                    }
                ],
                'pageInfo': {
                    'endCursor': 'YXJyYXljb25uZWN0aW9uOjE=',
                    'hasNextPage': False,
                    'hasPreviousPage': False,
                    'startCursor': 'YXJyYXljb25uZWN0aW9uOjA='
                }
            },
            'dob': '1980-01-04',
            'email': 'johnsmith@gmail.com',
            'firstName': 'John',
            'id': 'VXNlcjox',
            'lastName': 'Smith',
            'notificationPolicy': {
                'allowEmail': True,
                'allowMarketing': False,
                'allowSms': True,
                'id': 'Tm90aWZpY2F0aW9uUG9saWN5OjE='
            }
        }
    }
}

snapshots['test_get_profile_query 1'] = {
    'data': {
        'profile': {
            'avatar': 'https://example.com/images/me.jpg',
            'bio': '''Hey!

What are you looking at?''',
            'displayName': 'Johnny',
            'id': 'UHJvZmlsZTox'
        }
    }
}
