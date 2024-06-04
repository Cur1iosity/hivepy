from typing import Dict

from hivepy.schema_management.factories.schema_factory import SchemaFactory
from hivepy.template_management.models.issue_template import IssueTemplate


class IssueTemplateBuilder:
    """Issue template builder."""
    def __init__(self, schema_factory) -> None:
        self.schema_factory: SchemaFactory = SchemaFactory()

    def build(self, issue: Dict) -> IssueTemplate:
        """Build issue template."""
        issue['schema'] = self.schema_factory.make_issue_schema(issue['schema'])
        return IssueTemplate(**issue)
