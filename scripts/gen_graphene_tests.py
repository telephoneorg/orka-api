import sys

from jinja2 import Environment, FileSystemLoader
import oyaml as yaml


yaml.add_representer(
    str,
    lambda dumper, data: dumper.represent_scalar(
        u"tag:yaml.org,2002:str", data, style="|" if "\n" in data else None
    ),
)

env = Environment(loader=FileSystemLoader("tests/schemas/"))
test_template = env.get_template("test_template.py.j2")


def main(operation, path):
    with open(path) as fd:
        tests = yaml.load(fd)
    for test in tests:
        print(test_template.render(operation=operation, test=test))
        print()


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*args)
