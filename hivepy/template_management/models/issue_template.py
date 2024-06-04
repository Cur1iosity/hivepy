from hivepy.template_management.models.base_template import BaseTemplate
from hivepy.schema_management.models.issue_schema import IssueSchema


class IssueTemplate(BaseTemplate):
    """Issue template model."""
    schema: IssueSchema
    ...
