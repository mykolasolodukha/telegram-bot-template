"""The models used in the application."""

from __future__ import annotations

from tortoise import fields

from utils.tortoise_orm import Model


class BaseModel(Model):
    """The base model for all models."""

    date_added = fields.DatetimeField(auto_now_add=True)
    date_updated = fields.DatetimeField(auto_now=True)

    class Meta:
        """The metaclass for the base model."""

        abstract = True
