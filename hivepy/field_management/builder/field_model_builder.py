from typing import Any, Optional, Dict, ForwardRef

import pydantic

from hivepy.field_management.enums import BaseFieldType, FieldType, ValueType
from hivepy.field_management import FIELD_TYPE_MAP


class FieldModelBuilder:
    @classmethod
    def define_field_type(cls, base_field: Dict) -> FieldType:
        if cls.is_single_suggested_text(base_field):
            return FieldType.SINGLE_TEXT_SUGGESTED
        if cls.is_multi_suggested_text(base_field):
            return FieldType.MULTI_TEXT_SUGGESTED
        if cls.is_text(base_field):
            return FieldType.TEXT
        if cls.is_markdown(base_field):
            return FieldType.TEXT_MARKDOWN
        if cls.is_radiobutton(base_field):
            return FieldType.RADIOBUTTON
        if cls.is_checkbox(base_field):
            return FieldType.CHECKBOX
        if cls.is_checkboxes(base_field):
            return FieldType.CHECKBOXES
        if cls.is_select(base_field):
            return FieldType.SELECT
        if cls.is_multiselect(base_field):
            return FieldType.MULTISELECT
        if cls.is_date(base_field):
            return FieldType.DATE
        if cls.is_datetime(base_field):
            return FieldType.DATETIME
        if cls.is_link(base_field):
            return FieldType.LINK
        if cls.is_image(base_field):
            return FieldType.IMAGE
        if cls.is_file(base_field):
            return FieldType.FILE
        if cls.is_integer(base_field):
            return FieldType.INTEGER
        if cls.is_float(base_field):
            return FieldType.FLOAT
        if cls.is_cvss_base_score(base_field):
            return FieldType.CVSS_SCORE
        if cls.is_cvss_base_vector(base_field):
            return FieldType.CVSS_VECTOR
        if cls.is_asset(base_field):
            return FieldType.ASSET
        if cls.is_request(base_field):
            return FieldType.REQUEST
        if cls.is_datasource(base_field):
            return FieldType.DATASOURCE
        if cls.is_status(base_field):
            return FieldType.STATUS
        if cls.is_hostname(base_field):
            return FieldType.HOSTNAME
        if cls.is_uuid(base_field):
            return FieldType.UUID
        if cls.is_ip(base_field):
            return FieldType.IP
        raise ValueError(f"Unknown field type: {base_field['type']}\n{base_field}")

    @classmethod
    def is_text(cls, base_field: Dict) -> bool:
        """Check if field is text field."""
        return base_field['type'] == BaseFieldType.TEXT and not base_field.get('allowed_values')

    @classmethod
    def is_single_suggested_text(cls, base_field: Dict) -> bool:
        """Check if field is single suggested text field."""
        return base_field['type'] == BaseFieldType.TEXT_SUGGESTED and base_field.get('is_list') is False

    @classmethod
    def is_multi_suggested_text(cls, base_field: Dict) -> bool:
        """Check if field is multi suggested text field."""
        return base_field['type'] == BaseFieldType.TEXT_SUGGESTED and base_field.get('is_list') is True

    @classmethod
    def is_radiobutton(cls, base_field: Dict) -> bool:
        """Check if field is radiobutton field."""
        return base_field['type'] == BaseFieldType.TEXT \
            and base_field.get('allowed_values') \
            and base_field.get('is_list') is False \
            and base_field.get('select') is False

    @classmethod
    def is_checkbox(cls, base_field: Dict) -> bool:
        """Check if field is single checkbox field."""
        return base_field['type'] == BaseFieldType.BOOLEAN \
            and not base_field.get('allowed_values') \
            and not base_field.get('is_list', False) \
            and not base_field.get('select', False)

    @classmethod
    def is_checkboxes(cls, base_field: Dict) -> bool:
        """Check if field is checkboxes field."""
        return base_field['type'] == BaseFieldType.TEXT \
            and base_field.get('allowed_values') \
            and base_field.get('is_list', False) \
            and not base_field.get('select', False)

    @classmethod
    def is_select(cls, base_field: Dict) -> bool:
        """Check if field is select field."""
        return (base_field['type'] == BaseFieldType.TEXT
                and base_field.get('allowed_values')
                and not base_field.get('is_list')
                and base_field.get('select'))

    @classmethod
    def is_multiselect(cls, base_field: Dict) -> bool:
        """Check if field is multi select field."""
        return base_field['type'] == BaseFieldType.TEXT \
            and base_field.get('allowed_values') \
            and base_field.get('is_list') \
            and base_field.get('select')

    @classmethod
    def is_date(cls, base_field: Dict) -> bool:
        """Check if field is date field."""
        return base_field['type'] == BaseFieldType.DATE

    @classmethod
    def is_datetime(cls, base_field: Dict) -> bool:
        """Check if field is datetime field."""
        return base_field['type'] == BaseFieldType.DATETIME

    @classmethod
    def is_link(cls, base_field: Dict) -> bool:
        """Check if field is link field."""
        return base_field['type'] == BaseFieldType.LINK

    @classmethod
    def is_image(cls, base_field: Dict) -> bool:
        """Check if field is image field."""
        return base_field['type'] == BaseFieldType.IMAGE

    @classmethod
    def is_file(cls, base_field: Dict) -> bool:
        """Check if field is file field."""
        return base_field['type'] == BaseFieldType.FILE

    @classmethod
    def is_integer(cls, base_field: Dict) -> bool:
        """Check if field is integer field."""
        return base_field['type'] == BaseFieldType.INTEGER

    @classmethod
    def is_markdown(cls, base_field: Dict) -> bool:
        """Check if field is markdown field."""
        return base_field['type'] == BaseFieldType.TEXT_MARKDOWN

    @classmethod
    def is_float(cls, base_field: Dict) -> bool:
        """Check if field is float field."""
        return base_field['type'] == BaseFieldType.FLOAT

    @classmethod
    def is_cvss_base_score(cls, base_field: Dict) -> bool:
        """Check if field is CVSS Base Score field."""
        return base_field['type'] == BaseFieldType.CVSS_SCORE

    @classmethod
    def is_cvss_base_vector(cls, base_field: Dict) -> bool:
        """Check if field is CVSS Base Vector field."""
        return base_field['type'] == BaseFieldType.CVSS_VECTOR

    @classmethod
    def is_asset(cls, base_field: Dict) -> bool:
        """Check if field is Asset field."""
        return base_field['type'] == BaseFieldType.ASSET

    @classmethod
    def is_request(cls, base_field: Dict) -> bool:
        """Check if field is Request field."""
        return base_field['type'] == BaseFieldType.REQUEST

    @classmethod
    def is_datasource(cls, base_field: Dict) -> bool:
        """Check if field is Datasource field."""
        return base_field['type'] == BaseFieldType.DATASOURCE

    @classmethod
    def is_status(cls, base_field: Dict) -> bool:
        """Check if field is Status field."""
        return base_field['type'] == BaseFieldType.STATUS

    @classmethod
    def is_hostname(cls, base_field: Dict) -> bool:
        """Check if field is Hostname field."""
        return base_field['type'] == BaseFieldType.HOSTNAME

    @classmethod
    def is_uuid(cls, base_field: Dict) -> bool:
        """Check if field is UUID field."""
        return base_field['type'] == BaseFieldType.UUID

    @classmethod
    def is_ip(cls, base_field: Dict) -> bool:
        """Check if field is IP field."""
        return base_field['type'] == BaseFieldType.IP

    def build(self, field: Dict) -> ForwardRef('Field'):
        """Make from BaseField object advanced Field model."""
        final_type: FieldType = self.define_field_type(field)
        extra_fields = {
            'type': (Optional[FieldType], final_type),
            'value': (Optional[ValueType[final_type.name].value], None)
        }

        model = pydantic.create_model(
            FIELD_TYPE_MAP[final_type].__name__,
            **extra_fields,
            __base__=FIELD_TYPE_MAP[final_type]
        )
        return model

    def __call__(self, field: Dict) -> Any:
        """Make from BaseField object advanced Field model."""
        return self.build(field)
