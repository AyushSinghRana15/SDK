"""Data models."""

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class Task:
    title: str
    completed: bool = False
