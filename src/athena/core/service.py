from __future__ import annotations

from abc import ABC, abstractmethod


class BaseService(ABC):
    """Base class for all Athena services."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the service name."""

    @abstractmethod
    def start(self) -> None:
        """Start the service."""

    @abstractmethod
    def stop(self) -> None:
        """Stop the service."""

    def health_check(self) -> bool:
        """Return True if the service is healthy."""
        return True
