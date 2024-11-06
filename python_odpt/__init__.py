"""
.. include:: ../README.md

A client library for accessing ODPT API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
