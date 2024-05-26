def test_project_default_project_building(project_builder, example_default_project_data) -> None:
    """Test building a default project."""
    project = project_builder.build(example_default_project_data)
