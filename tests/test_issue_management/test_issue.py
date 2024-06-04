def test_default_issue_initialization(default_issue_class, example_default_issue_data) -> None:
    """Test building a default issue."""
    issue = default_issue_class(**example_default_issue_data)
    assert issue.id
    assert issue.status
    assert issue.post_time
    assert issue.edit_time
