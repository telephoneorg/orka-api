import re

from sqlalchemy import inspect

from .models import Base, SoftDeletable


SNAKE_TO_CAMEL_RE = re.compile(r"(?:^|_)([a-z])")


def snake2pascal(name):
    return SNAKE_TO_CAMEL_RE.sub(lambda x: x.group(1).upper(), name)


def get_model(model_name, default=None):
    return Base._decl_class_registry.get(model_name, default)


def is_model_instance(obj, *model_names):
    models = tuple((get_model(model_name) for model_name in model_names))
    return isinstance(obj, models)


def recursive_create(model_name, **model_params):
    for key, val in model_params.items():
        if isinstance(val, dict):
            model_params[key] = recursive_create(snake2pascal(key), **val)

    model = get_model(model_name)
    return model(**model_params)


def recursive_patch(obj, params):
    for key, val in params.items():
        if isinstance(val, dict):
            recursive_patch(getattr(obj, key), val)
        else:
            setattr(obj, key, val)

    return obj


def recursive_soft_delete(obj, seen=None):
    seen = seen or []

    if isinstance(obj, Base):

        if isinstance(obj, SoftDeletable):
            obj.deleted = True
        seen.append(type(obj))
        for name, rel in inspect(obj).mapper.relationships.items():
            if rel.direction.name == "MANYTOONE":
                continue

            remote_class = rel.mapper.class_
            if remote_class not in seen:
                remote_attr = getattr(obj, name)
                recursive_soft_delete(remote_attr, seen)
    elif isinstance(obj, list):
        for item in obj:
            recursive_soft_delete(item, seen)
