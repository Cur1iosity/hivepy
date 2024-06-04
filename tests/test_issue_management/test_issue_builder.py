def test_default_issue_building(issue_schema_builder, issue_builder,
                                example_default_project_data,
                                example_default_issue_data) -> None:
    """Test building a default project."""

    issue_schema_raw = example_default_project_data.get('issueSettings')
    issue_schema = issue_schema_builder.build(issue_schema_raw)
    issue = issue_builder.build(issue_schema, example_default_issue_data)
    assert issue.id
    assert issue.name
    assert issue.status


def test_custom_issue_building(issue_builder, example_custom_issue_data) -> None:
    """Test building a custom project."""
    # issue = issue_builder.build(example_custom_issue_data)
    # assert issue.id
    # assert issue.name
    # assert issue.status
    ...
