def test_create_me_mutation(snapshot, graphene_client, graphene_context):
    query = """
        mutation CreateMe($input: CreateMeInput!) {
          createMe(input: $input) {
            ok
            user {
              id
              firstName
              lastName
              email
              dob
              cellPhone
              notificationPolicy {
                id
                allowEmail
                allowSms
                allowMarketing
              }
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(
                user=False,
                jwt={
                    "email": "jackmasters@gmail.com",
                    "sub": "c6e73532-83fa-4723-962b-7c7b3d1993aa",
                },
            ),
            variables={
                "input": {
                    "firstName": "Jack",
                    "lastName": "Masters",
                    "cellPhone": "+16465552671",
                    "dob": "1983-04-20",
                    "notificationPolicy": {
                        "allowEmail": True,
                        "allowSms": False,
                        "allowMarketing": True,
                    },
                }
            },
        )
    )


def test_update_me_mutation(snapshot, graphene_client, graphene_context):
    query = """
        mutation UpdateMe($input: UpdateMeInput!) {
          updateMe(input: $input) {
            ok
            user {
              id
              firstName
              lastName
              email
              cellPhone
              dob
              notificationPolicy {
                id
                allowEmail
                allowSms
                allowMarketing
              }
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "lastName": "Black",
                    "notificationPolicy": {"allowMarketing": True},
                }
            },
        )
    )


def test_delete_me_mutation(snapshot, graphene_client, graphene_context):
    query = """
        mutation DeleteMe {
          deleteMe(input: {}) {
            ok
            userId
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables=None,
        )
    )


def test_add_participant_context_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation AddParticipantContext($input: AddParticipantContextInput!) {
          addParticipantContext(input: $input) {
            ok
            participantContext {
              id
              type
              status
              profile {
                displayName
                avatar
                bio
              }
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "profile": {
                        "displayName": "Big J",
                        "avatar": "https://example.com/img/photo.jpg",
                        "bio": "Hello\n\nHow are you?",
                    }
                }
            },
        )
    )


def test_update_participant_context_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation UpdateParticipantContext($input: UpdateParticipantContextInput!) {
          updateParticipantContext(input: $input) {
            ok
            participantContext {
              id
              type
              status
              profile {
                displayName
                avatar
                bio
              }
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "id": "UGFydGljaXBhbnRDb250ZXh0OjE=",
                    "participantContext": {
                        "profile": {
                            "avatar": "https://example.com/img/new-photo.jpg"
                        }
                    },
                }
            },
        )
    )


def test_remove_participant_context_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation RemoveParticipantContext($input: RemoveParticipantContextInput!) {
          removeParticipantContext(input: $input) {
            ok
            participantContextId
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={"input": {"id": "UGFydGljaXBhbnRDb250ZXh0OjE="}},
        )
    )


def test_add_facilitator_context_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation AddFacilitatorContext($input: AddFacilitatorContextInput!) {
          addFacilitatorContext(input: $input) {
            ok
            facilitatorContext {
              id
              type
              status
              npi
              availability
              profile {
                displayName
                avatar
                bio
              }
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "npi": "335978n3905n903459",
                    "availability": "<json payload>",
                    "profile": {
                        "displayName": "Big J",
                        "avatar": "https://example.com/img/photo.jpg",
                        "bio": "Hello\n\nHow are you?",
                    },
                }
            },
        )
    )


def test_update_facilitator_context_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation UpdateFacilitatorContext($input: UpdateFacilitatorContextInput!) {
          updateFacilitatorContext(input: $input) {
            ok
            facilitatorContext {
              id
              type
              status
              npi
              availability
              profile {
                displayName
                avatar
                bio
              }
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "id": "RmFjaWxpdGF0b3JDb250ZXh0OjI=",
                    "facilitatorContext": {
                        "npi": "xxxxUPDATEDxxxx",
                        "availability": "<json payload>",
                        "profile": {"displayName": "New Big J"},
                    },
                }
            },
        )
    )


def test_remove_facilitator_context_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation RemoveFacilitatorContext($input: RemoveFacilitatorContextInput!) {
          removeFacilitatorContext(input: $input) {
            ok
            facilitatorContextId
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={"input": {"id": "RmFjaWxpdGF0b3JDb250ZXh0OjI="}},
        )
    )


def test_add_facilitator_license_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation AddFacilitatorLicense($input: AddFacilitatorLicenseInput!) {
          addFacilitatorLicense(input: $input) {
            ok
            facilitatorLicense {
              id
              type
              number
              expiry
              usState
            }
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "facilitatorContextId": "RmFjaWxpdGF0b3JDb250ZXh0OjI=",
                    "facilitatorLicense": {
                        "type": "TBD",
                        "number": "xxx",
                        "expiry": "2020-01-01",
                        "usState": "NY",
                    },
                }
            },
        )
    )


def test_remove_facilitator_license_mutation(
    snapshot, graphene_client, graphene_context
):
    query = """
        mutation RemoveFacilitatorLicense($input: RemoveFacilitatorLicenseInput!) {
          removeFacilitatorLicense(input: $input) {
            ok
            facilitatorLicenseId
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={
                "input": {
                    "facilitatorContextId": "RmFjaWxpdGF0b3JDb250ZXh0OjI=",
                    "facilitatorLicenseId": "RmFjaWxpdGF0b3JMaWNlbnNlOjE=",
                }
            },
        )
    )
