import sys

from vyl.routing import route
from vyl.utils.process import joined_argv


def main() -> None:
    route(prompt=joined_argv())


if __name__ == '__main__':
    main()
