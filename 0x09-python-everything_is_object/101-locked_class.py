#!/usr/bin/python3
"""LockedClasse."""


class LockedClass:
    """Slot prevents the creation of new attributes except for first_name."""

    __slots__ = ['first_name']
