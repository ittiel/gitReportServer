from sqlalchemy import Column, String, Integer
from database import Base
from datetime import datetime


class GitMsg(Base):
    __tablename__ = 'gitMsg'
    id = Column(Integer, primary_key=True)
    user = Column(String(50))
    branch = Column(String(50))
    repository = Column(String(120))
    files = Column(String(500))
    diff = Column(String(500))
    commitMsg = Column(String(120))

    def __init__(self, user=None, branch=None, repository=None, files=None, diff=None, commitMsg=None):
        self.user = user
        self.branch = branch
        self.repository = repository
        self.files = files
        self.diff = diff
        self.commitMsg = commitMsg

    def __repr__(self):
        return '<gitMsg %r>' % (self.gitMsg)