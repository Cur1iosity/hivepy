import uuid
from typing import Optional, List

import pydantic

from hivepy.template_management.models.base_template import BaseTemplate
from hivepy.schema_management.models.project_schema import ProjectSchema


class ProjectTemplate(BaseTemplate):
    """Project template model."""
    id: uuid.UUID
    name: str
    description: Optional[str] = pydantic.Field(default=None)
    is_default: Optional[bool] = pydantic.Field(default=None, alias='isDefault')
    default_issue_schema_id: Optional[uuid.UUID] = pydantic.Field(default=None, alias='defaultIssueSchemaID')
    default_report_template_name: Optional[str] = pydantic.Field(default=None, alias='defaultReportTemplateName')
    schema: Optional[ProjectSchema] = pydantic.Field(default=None, alias='projectSchema')
    checklists: Optional[List] = pydantic.Field(default=None)
    wiki_pages: Optional[List] = pydantic.Field(default=None, alias='wikiPages')
