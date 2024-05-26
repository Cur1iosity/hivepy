def test_default_project_template(template_builder, example_default_project_template_data) -> None:
    """Test building a default project template."""
    project_template = template_builder.build_project_template(example_default_project_template_data)
    assert project_template.is_default


def test_custom_project_template(template_builder, example_project_template_data) -> None:
    """Test building a custom project template."""
    project_template = template_builder.build_project_template(example_project_template_data)
    assert not project_template.is_default
