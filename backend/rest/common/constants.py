from enum import Enum


class Method(Enum):
    GET = 'get'
    OPTIONS = 'options'
    HEAD = 'head'
    PUT = 'put'
    POST = 'post'
    PATCH = 'patch'
    DELETE = 'delete'
