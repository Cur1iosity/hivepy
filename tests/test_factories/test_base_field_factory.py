# def test_base_field_factory(example_raw_fields_data, base_field_factory) -> None:
#     """Test BaseField initialization."""
#     for field_data in example_raw_fields_data:
#         field = base_field_factory(**field_data)
#
#         assert field.display_name == field_data['displayName']
#         assert field.name == field_data['name']
#         assert field.allowed_values == [val['value'] for val in field_data['allowedValues']]
#         assert field.is_list == field_data['isList']
#         assert field.required == field_data['required']
#         assert field.hidden == field_data['hidden']
#         assert field.initially_collapsed == field_data['metadata'].get('initiallyCollapsed', None)
#         assert field.native_type.value == field_data['type']
#         assert field.placeholder == field_data['metadata'].get('placeholder', None)
#         assert field.hint == field_data['metadata'].get('hint', None)
