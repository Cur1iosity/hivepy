def test_making_project_schema(schema_factory):
    """Test making schema."""
    example_schema_data = {
        'id': 'f6d4a506-0aa5-4b93-b5f7-44f8b4b7a449',
        'version': 1,
        'fieldsOrder': ['test', 'test2'],
        'created': '2021-09-29T14:00:00Z',
        'updated': None,
        'additionalFieldsSettings': [{
            "name": "test",
            "displayName": "Test",
            "type": "TEXT_SUGGESTED",
            "allowedValues": [],
            "hidden": False,
            "isList": True,
            "metadata": {
              "hint": "Test hint for text",
              "initiallyCollapsed": True,
              "placeholder": "Test Multiple Suggester"
            },
        },],}
    schema = schema_factory('project', example_schema_data)
    assert str(schema.id) == 'f6d4a506-0aa5-4b93-b5f7-44f8b4b7a449'
    assert schema.version == 1


def check_update_cache(schema_factory):
    """Check update cache."""
    example_schema_data = {
        'id': 'f6d4a506-0aa5-4b93-b5f7-44f8b4b7a449',
        'version': 1,
        'fieldsOrder': ['test', 'test2'],
        'created': '2021-09-29T14:00:00Z',
        'updated': None,
        'additionalFieldsSettings': [{
            "name": "test",
            "displayName": "Test",
            "type": "TEXT_SUGGESTED",
            "allowedValues": [],
            "hidden": False,
            "isList": True,
            "metadata": {
              "hint": "Test hint for text",
              "initiallyCollapsed": True,
              "placeholder": "Test Multiple Suggester"
            },
        },],}
    schema = schema_factory('project', example_schema_data)
    assert str(schema.id) == 'f6d4a506-0aa5-4b93-b5f7-44f8b4b7a449'
    assert schema.version == 1
    assert schema_factory.cache.get('f6d4a506-0aa5-4b93-b5f7-44f8b4b7a449_1') == f"{schema.id}_{schema.version}"
