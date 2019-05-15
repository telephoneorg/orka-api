def test_get_me_query(snapshot, graphene_client, graphene_context):
    query = """
        query GetMe {
          me {
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
            contexts {
              count
              pageInfo {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
              }
              edges {
                cursor
                node {
                  __typename
                  id
                  status
                  profile {
                    id
                    displayName
                    avatar
                    bio
                  }
                  ... facilitatorFields
                }
              }
            }
          }
        }

        fragment facilitatorFields on FacilitatorContext {
          npi
          availability
          licenses {
            pageInfo {
              startCursor
              endCursor
              hasNextPage
              hasPreviousPage
            }
            edges {
              cursor
              node {
                id
                type
                number
                expiry
                usState
              }
            }
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


def test_get_profile_query(snapshot, graphene_client, graphene_context):
    query = """
        query GetProfile($id: ID!) {
          profile(id: $id) {
            id
            displayName
            avatar
            bio
          }
        }
    """
    snapshot.assert_match(
        graphene_client.execute(
            query,
            context=graphene_context(user=None, jwt=None),
            variables={"id": "UHJvZmlsZTox"},
        )
    )
