# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_update_me_mutation 1'] = {
    'data': {
        'updateMe': {
            'ok': True,
            'user': {
                'cellPhone': '+14153334444',
                'dob': '1980-01-04',
                'email': 'johnsmith@gmail.com',
                'firstName': 'John',
                'id': 'VXNlcjox',
                'lastName': 'Black',
                'notificationPolicy': {
                    'allowEmail': True,
                    'allowMarketing': True,
                    'allowSms': True,
                    'id': 'Tm90aWZpY2F0aW9uUG9saWN5OjE='
                }
            }
        }
    }
}

snapshots['test_delete_me_mutation 1'] = {
    'data': {
        'deleteMe': {
            'ok': True,
            'userId': 'VXNlcjox'
        }
    }
}

snapshots['test_create_me_mutation 1'] = {
    'data': {
        'createMe': {
            'ok': True,
            'user': {
                'cellPhone': '+16465552671',
                'dob': '1983-04-20',
                'email': 'jackmasters@gmail.com',
                'firstName': 'Jack',
                'id': 'VXNlcjox',
                'lastName': 'Masters',
                'notificationPolicy': {
                    'allowEmail': True,
                    'allowMarketing': True,
                    'allowSms': False,
                    'id': 'Tm90aWZpY2F0aW9uUG9saWN5OjE='
                }
            }
        }
    }
}

snapshots['test_add_participant_context_mutation 1'] = {
    'data': {
        'addParticipantContext': {
            'ok': True,
            'participantContext': {
                'id': 'UGFydGljaXBhbnRDb250ZXh0OjM=',
                'profile': {
                    'avatar': 'https://example.com/img/photo.jpg',
                    'bio': '''Hello

How are you?''',
                    'displayName': 'Big J'
                },
                'status': 'CREATED',
                'type': 'PARTICIPANT'
            }
        }
    }
}

snapshots['test_update_participant_context_mutation 1'] = {
    'data': {
        'updateParticipantContext': {
            'ok': True,
            'participantContext': {
                'id': 'UGFydGljaXBhbnRDb250ZXh0OjE=',
                'profile': {
                    'avatar': 'https://example.com/img/new-photo.jpg',
                    'bio': '''Hey!

What are you looking at?''',
                    'displayName': 'Johnny'
                },
                'status': 'CREATED',
                'type': 'PARTICIPANT'
            }
        }
    }
}

snapshots['test_remove_participant_context_mutation 1'] = {
    'data': {
        'removeParticipantContext': {
            'ok': True,
            'participantContextId': 'UGFydGljaXBhbnRDb250ZXh0OjE='
        }
    }
}

snapshots['test_add_facilitator_context_mutation 1'] = {
    'data': {
        'addFacilitatorContext': {
            'facilitatorContext': {
                'availability': '<json payload>',
                'id': 'RmFjaWxpdGF0b3JDb250ZXh0OjM=',
                'npi': '335978n3905n903459',
                'profile': {
                    'avatar': 'https://example.com/img/photo.jpg',
                    'bio': '''Hello

How are you?''',
                    'displayName': 'Big J'
                },
                'status': 'CREATED',
                'type': 'FACILITATOR'
            },
            'ok': True
        }
    }
}

snapshots['test_update_facilitator_context_mutation 1'] = {
    'data': {
        'updateFacilitatorContext': {
            'facilitatorContext': {
                'availability': '<json payload>',
                'id': 'RmFjaWxpdGF0b3JDb250ZXh0OjI=',
                'npi': 'xxxxUPDATEDxxxx',
                'profile': {
                    'avatar': 'https://dr-smith.com/photos/dr-smith.jpg',
                    'bio': '''I don't know how to put this but I'm kind of a big deal.

 People know me. I'm very important. 

I have many leather-bound books and my apartment smells of rich mahogany.''',
                    'displayName': 'New Big J'
                },
                'status': 'CREATED',
                'type': 'FACILITATOR'
            },
            'ok': True
        }
    }
}

snapshots['test_remove_facilitator_context_mutation 1'] = {
    'data': {
        'removeFacilitatorContext': {
            'facilitatorContextId': 'RmFjaWxpdGF0b3JDb250ZXh0OjI=',
            'ok': True
        }
    }
}

snapshots['test_add_facilitator_license_mutation 1'] = {
    'data': {
        'addFacilitatorLicense': {
            'facilitatorLicense': {
                'expiry': '2020-01-01',
                'id': 'RmFjaWxpdGF0b3JMaWNlbnNlOjQ=',
                'number': 'xxx',
                'type': 'TBD',
                'usState': 'NY'
            },
            'ok': True
        }
    }
}

snapshots['test_remove_facilitator_license_mutation 1'] = {
    'data': {
        'removeFacilitatorLicense': {
            'facilitatorLicenseId': 'RmFjaWxpdGF0b3JMaWNlbnNlOjE=',
            'ok': True
        }
    }
}
