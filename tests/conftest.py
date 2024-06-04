import json
import os
from typing import Dict, Type, List

import pytest

from hivepy.field_management import JsonFieldNormalizer, FIELD_TYPE_MAP
from hivepy.field_management.builder import FieldModelBuilder, FieldBuilder
from hivepy.field_management.enums import BaseFieldType, FieldType
from hivepy.field_management.models import BaseField
from hivepy.issue_management.issue import Issue
from hivepy.issue_management.issue_builder import IssueBuilder
from hivepy.project_management.project_builder import ProjectBuilder
from hivepy.schema_management.builders import ProjectSchemaBuilder
from hivepy.schema_management.builders.issue_schema_builder import IssueSchemaBuilder
from hivepy.schema_management.factories import SchemaFactory
from hivepy.template_management.builders import TemplateBuilder

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'test_data')


def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as file:
        return json.load(file)


@pytest.fixture
def example_raw_fields_data() -> List:
    """Returns example raw fields data."""
    return load_json('example_fields.json')


@pytest.fixture
def example_field_data(example_raw_fields_data) -> Dict:
    """Returns example fields data."""
    field_list = example_raw_fields_data
    return {
        'text': next(field for field in field_list if field['name'] == 'text_field'),
        'text_markdown': next(field for field in field_list if field['type'] == 'TEXT_MD'),
        'integer': next(field for field in field_list if field['type'] == 'INTEGER'),
        'float': next(field for field in field_list if field['type'] == 'FLOAT'),
        'single_text_suggested': next(field for field in field_list if field['name'] == 'single_suggest_text'),
        'multi_text_suggested': next(field for field in field_list if field['name'] == 'multi_suggest_text'),
        'checkbox': next(field for field in field_list if field['name'] == 'checkbox'),
        'checkboxes': next(field for field in field_list if field['name'] == 'checkboxes'),
        'radiobutton': next(field for field in field_list if field['name'] == 'radiobutton'),
        'select': next(field for field in field_list if field['name'] == 'select'),
        'multiselect': next(field for field in field_list if field['name'] == 'multiselect'),
        'date': next(field for field in field_list if field['type'] == 'DATE'),
        'datetime': next(field for field in field_list if field['type'] == 'DATETIME'),
        'link': next(field for field in field_list if field['type'] == 'LINK'),
        'image': next(field for field in field_list if field['type'] == 'IMAGE'),
        'file': next(field for field in field_list if field['type'] == 'FILE'),
        'uuid': next(field for field in field_list if field['type'] == 'UUID'),
        'ip': next(field for field in field_list if field['type'] == 'IP'),
        'hostname': next(field for field in field_list if field['type'] == 'HOSTNAME'),
        'asset': next(field for field in field_list if field['type'] == 'ASSET'),
        'request': next(field for field in field_list if field['type'] == 'REQUEST'),
        'datasource': next(field for field in field_list if field['type'] == 'DATASOURCE'),
        'status': next(field for field in field_list if field['type'] == 'STATUS'),
        'cvss_score': next(field for field in field_list if field['type'] == 'CVSS_BASE_SCORE'),
        'cvss_vector': next(field for field in field_list if field['type'] == 'CVSS_BASE_VECTOR'),
            }


@pytest.fixture
def example_project_schema_data() -> Dict:
    """Returns example project schema data."""
    return load_json('example_project_schema.json')


@pytest.fixture
def example_default_project_template_data() -> Dict:
    """Returns example default project data."""
    return load_json('example_default_project_template.json')


@pytest.fixture
def example_custom_issue_schema_data() -> Dict:
    """Returns example issue schema data."""
    return load_json('example_custom_issue_schema.json')


@pytest.fixture
def example_default_issue_schema_data() -> Dict:
    """Returns example issue schema data."""
    return load_json('example_default_issue_schema.json')


@pytest.fixture
def example_project_template_data() -> Dict:
    """Returns example project data."""
    return load_json('example_project_template.json')


@pytest.fixture
def example_custom_project_data() -> Dict:
    """Returns example project data."""
    return load_json('example_custom_project.json')


@pytest.fixture
def example_custom_issue_data() -> Dict:
    """Returns example issue data."""
    return load_json('example_custom_issue.json')


@pytest.fixture
def example_default_project_data() -> Dict:
    """Returns example project data."""
    return load_json('example_default_project.json')


@pytest.fixture
def example_default_issue_data() -> Dict:
    """Returns example issue data."""
    return load_json('example_default_issue.json')


@pytest.fixture
def json_field_normalizer() -> JsonFieldNormalizer:
    """Returns BaseFieldFactory class."""
    return JsonFieldNormalizer()


@pytest.fixture
def field_model_builder() -> FieldModelBuilder:
    """Returns FieldModelBuilder class."""
    return FieldModelBuilder()


@pytest.fixture
def field_builder() -> FieldBuilder:
    """Returns FieldModelBuilder class."""
    return FieldBuilder()


@pytest.fixture
def project_schema_builder(field_builder) -> ProjectSchemaBuilder:
    """Returns ProjectSchemaBuilder class."""
    return ProjectSchemaBuilder(field_builder)


@pytest.fixture
def issue_schema_builder(field_builder) -> IssueSchemaBuilder:
    """Returns ProjectSchemaBuilder class."""
    return IssueSchemaBuilder(field_builder)


@pytest.fixture
def schema_factory():
    """Returns SchemaFactory class."""
    return SchemaFactory()


@pytest.fixture
def template_builder() -> TemplateBuilder:
    """Returns TemplateBuilder class."""
    return TemplateBuilder()


@pytest.fixture
def project_builder() -> ProjectBuilder:
    """Returns ProjectBuilder class."""
    return ProjectBuilder()


@pytest.fixture
def issue_builder() -> IssueBuilder:
    """Returns ProjectBuilder class."""
    return IssueBuilder()


@pytest.fixture
def base_field_class() -> Type[BaseField]:
    """Returns BaseField class."""
    return BaseField


@pytest.fixture
def base_field_type() -> Type[BaseFieldType]:
    """Returns BaseFieldType Enum."""
    return BaseFieldType


@pytest.fixture
def field_type_map() -> Dict[str, Type[FieldType]]:
    """Returns FIELD_TYPE_MAP."""
    return FIELD_TYPE_MAP


@pytest.fixture
def field_type() -> Type[FieldType]:
    """Returns FieldType Enum."""
    return FieldType


@pytest.fixture
def default_issue_class() -> Type[Issue]:
    """Returns Issue class."""
    return Issue
