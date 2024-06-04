from typing import Union, ForwardRef

from hivepy.schema_management.factories.schema_factory import SchemaFactory
from hivepy.template_management.builders.project_template_builder import ProjectTemplateBuilder
from hivepy.template_management.builders.issue_template_builder import IssueTemplateBuilder


ProjectTemplate = ForwardRef('ProjectTemplate')
IssueTemplate = ForwardRef('IssueTemplate')


class TemplateBuilder:
    """Template builder class."""
    def __init__(self) -> None:
        """Initialize the template builder with schema and template builders."""
        self.schema_factory: SchemaFactory = SchemaFactory()
        self.project_template_builder: ProjectTemplateBuilder = ProjectTemplateBuilder(self.schema_factory)
        self.issue_template_builder: IssueTemplateBuilder = IssueTemplateBuilder(self.schema_factory)

    def build(self, template_type: str, template_data) -> Union[ProjectTemplate, IssueTemplate]:
        """Build a template object from a template data dictionary"""
        if template_type == 'project':
            return self.project_template_builder.build(template_data)
        elif template_type == 'issue':
            return self.issue_template_builder.build(template_data)
        else:
            raise ValueError(f'Unknown template type: {template_type}')

    def build_project_template(self, template_data) -> ProjectTemplate:
        """Build a project template object from a template data dictionary"""
        return self.project_template_builder.build(template_data)

    def build_issue_template(self, template_data) -> IssueTemplate:
        """Build an issue template object from a template data dictionary"""
        return self.issue_template_builder.build(template_data)
