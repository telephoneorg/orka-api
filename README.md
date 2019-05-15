# STS GraphQL Server
https://897qfp0jei.execute-api.us-east-1.amazonaws.com/dev/graphql

## Servers
### Locally
* `FLASK_APP=orka_api.app poetry run flask run`
* goto http://127.0.0.1:5000/graphql

### Dev
* goto https://897qfp0jei.execute-api.us-east-1.amazonaws.com/dev/graphql

## Schema
* You can view the graphql schema [here](schema.graphql)
* You can view the query data used to generate tests [here](tests/schemas/users/test_data)
* You can view the api documentation [here](docs/schema)

## Insomnia
I recommend the Insomnia App for GraphQL: https://insomnia.rest/, you can import the api requests using the [Orka API Context for Insomnia](Orka-API-Context-for-Insomnia.yaml).  The only thing lacking is schema documentation, for that I recommend using the graphqli interface @ https://897qfp0jei.execute-api.us-east-1.amazonaws.com/dev/graphql

## Special Dependencies
This package depends on specific bugfixes I've applied to the graphene and graphql-core packages, I've bumped the versions of these packages to prioritize their installation when the dependency graph is generated.


## Management
These commands also work on aws lambda if you invoke them as `manage.<command>`

## Deployment
This API is deployed to AWS using zappa

### To deploy
```bash
zappa deploy dev
```

### To update
```bash
zappa update dev
```

### To invoke a management command
```bash
zappa invoke dev manage.<command>
```

### To tail logs
```bash
zappa tail dev
```

### To initialize database:
```bash
poetry run python3 manage.py init_db
```
### To reset:
```bash
poetry run python3 manage.py clear_db
```

## Tests
To run tests:
```bash
poetry run python3 -m pytest tests
```

## Scripts

### Test generation
To generate graphql tests configured using yaml, run:
```bash
poetry run python3 scripts/gen_graphene_tests.py <operation> <path-to-data.yaml>
```
Operation can be: query, mutation, etc

