def test_project_schema_building(project_schema_builder, example_project_schema_data) -> None:
    """Test project schema building."""
    project_schema = project_schema_builder(example_project_schema_data)
    assert project_schema.id
    assert project_schema.fields_order
