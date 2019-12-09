# aiohttpdemo_polls/db.py
from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

meta = MetaData()

question = Table(
    "question",
    meta,
    Column("id", Integer, primary_key=True),
    Column("question_text", String(200), nullable=False),
    Column("pub_date", Date, nullable=False),
)

choice = Table(
    "choice",
    meta,
    Column("id", Integer, primary_key=True),
    Column("choice_text", String(200), nullable=False),
    Column("votes", Integer, server_default="0", nullable=False),
    Column(
        "question_id", Integer, ForeignKey("question.id", ondelete="CASCADE")
    ),
)
