from typing import Dict

from hivepy.schema_management.models.issue_schema import IssueSchema


class IssueSchemaBuilder:
    """Class that builds an IssueSchema object from a raw issue schema dictionary."""
    @classmethod
    def build(cls, issue_schema: Dict) -> IssueSchema:
        ...

    def __call__(self, issue_schema: Dict) -> IssueSchema:
        """Build IssueSchema object from raw data."""
        return self.build(issue_schema)
