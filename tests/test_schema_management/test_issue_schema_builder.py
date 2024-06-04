def test_issue_schema_building(issue_schema_builder, example_custom_issue_schema_data) -> None:
    """Test project schema building."""
    issue_schema = issue_schema_builder(example_custom_issue_schema_data)
    assert issue_schema.id
    assert issue_schema.fields_order
    assert issue_schema.name
