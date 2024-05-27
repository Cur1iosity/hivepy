def test_default_project_building(project_builder, example_default_project_data) -> None:
    """Test building a default project."""
    project = project_builder.build(example_default_project_data)
    assert project.id
    assert project.name


def test_custom_project_building(project_builder, example_custom_project_data) -> None:
    """Test building a custom project."""
    project = project_builder.build(example_custom_project_data)
    print(project)
    assert project.id
    assert project.name

# TODO Добавить десереализацию проектов в методы REST API
# TODO Разработать issue_management и issue_template в template_management
