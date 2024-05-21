import json
import os
from typing import Dict, Type, List

import pytest

from hivepy.builders import FieldModelBuilder
from hivepy.field_management import JsonFieldNormalizer, FIELD_TYPE_MAP
from hivepy.field_management.enums import BaseFieldType, FieldType
from hivepy.field_management.models import BaseField

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
            }


@pytest.fixture
def json_field_normalizer() -> JsonFieldNormalizer:
    """Returns BaseFieldFactory class."""
    return JsonFieldNormalizer()


@pytest.fixture
def field_model_builder() -> FieldModelBuilder:
    """Returns FieldModelBuilder class."""
    return FieldModelBuilder()


@pytest.fixture
def field_builder() -> FieldModelBuilder:
    """Returns FieldModelBuilder class."""
    return FieldModelBuilder()


@pytest.fixture
def base_field_class() -> Type[BaseField]:
    """Returns BaseField class."""
    return BaseField


@pytest.fixture
def field_type_map():
    """Returns FIELD_TYPE_MAP."""
    return FIELD_TYPE_MAP


@pytest.fixture
def base_field_type() -> Type[BaseFieldType]:
    """Returns BaseFieldType Enum."""
    return BaseFieldType


@pytest.fixture
def field_type() -> Type[FieldType]:
    """Returns FieldType Enum."""
    return FieldType
