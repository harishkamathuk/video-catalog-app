"""Seed media types

Revision ID: 6a77b0fb8d0a
Revises: 9ce52d784685
Create Date: 2024-12-17 20:49:12.216495

"""
from typing import Sequence, Union

from alembic import op

import sqlalchemy as sa

from sqlalchemy import String
from sqlalchemy.orm import Session

from app.models.media_type import MediaType  # Import the MediaType model


# revision identifiers, used by Alembic.
revision: str = '6a77b0fb8d0a'
down_revision: Union[str, None] = '9ce52d784685'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a session to interact with the database
    session = Session(bind=op.get_bind())

    # List of media types to seed
    media_types = ["video", "audio", "image"]

    for media_type_name in media_types:
        if not session.query(MediaType).filter_by(name=media_type_name).first():
            new_media_type = MediaType(name=media_type_name)
            session.add(new_media_type)

    session.commit()


def downgrade() -> None:
    # Logic to remove seeded data if you need to roll back
    session = Session(bind=op.get_bind())

    media_types = ["video", "audio", "image"]
    for media_type_name in media_types:
        session.query(MediaType).filter_by(name=media_type_name).delete()

    session.commit()
