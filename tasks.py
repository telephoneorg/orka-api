from invoke import task


@task
def test(ctx):
    ctx.run("poetry run python3 -m pytest tests", pty=True)


@task
def update_snapshots(ctx):
    ctx.run("poetry run python3 -m pytest --snapshot-update tests", pty=True)


@task
def export_requirements(ctx):
    ctx.run("poetry export -f requirements.txt")


@task
def build_graphene_tests(ctx, op, data):
    ctx.run(f"poetry run python3 scripts/gen_graphene_tests.py {op} {data}")


@task
def serve(ctx):
    ctx.run(
        "poetry run flask run",
        env={"FLASK_APP": "orka_api.app", "FLASK_DEBUG": "true"},
        pty=True,
    )


@task
def init_db(ctx):
    ctx.run("poetry run python3 manage.py init_db")


@task
def clear_db(ctx):
    ctx.run("poetry run python3 manage.py clear_db")


@task
def zappa_shell(ctx):
    ctx.run(
        "docker run -it --rm --name sts-builder -v $(pwd):/var/task -v $HOME/.aws:/root/.aws joeblackwaslike/zappa-builder bash -l",
        pty=True,
    )
