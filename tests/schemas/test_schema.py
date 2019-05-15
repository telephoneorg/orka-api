from orka_api.schemas import schema


def test_str_schema(snapshot):
    snapshot.assert_match(str(schema))
