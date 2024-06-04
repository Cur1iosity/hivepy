def test_text_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test TEXT field normalization."""
    field = json_field_normalizer(example_field_data['text'])
    assert field['display_name'] == example_field_data['text']['displayName']
    assert field['name'] == example_field_data['text']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_text_markdown_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test TEXT_MD field normalization."""
    field = json_field_normalizer(example_field_data['text_markdown'])
    assert field['display_name'] == example_field_data['text_markdown']['displayName']
    assert field['name'] == example_field_data['text_markdown']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_integer_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test INTEGER field normalization."""
    field = json_field_normalizer(example_field_data['integer'])
    assert field['display_name'] == example_field_data['integer']['displayName']
    assert field['name'] == example_field_data['integer']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_float_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test FLOAT field normalization."""
    field = json_field_normalizer(example_field_data['float'])
    assert field['display_name'] == example_field_data['float']['displayName']
    assert field['name'] == example_field_data['float']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_single_text_suggested_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test TEXT_SUGGESTED field normalization."""
    field = json_field_normalizer(example_field_data['single_text_suggested'])
    assert field['display_name'] == example_field_data['single_text_suggested']['displayName']
    assert field['name'] == example_field_data['single_text_suggested']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_multi_text_suggested_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test TEXT_SUGGESTED field normalization."""
    field = json_field_normalizer(example_field_data['multi_text_suggested'])
    assert field['display_name'] == example_field_data['multi_text_suggested']['displayName']
    assert field['name'] == example_field_data['multi_text_suggested']['name']
    assert not field['allowed_values']
    assert field['is_list']


def test_checkbox_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test CHECKBOX field normalization."""
    field = json_field_normalizer(example_field_data['checkbox'])
    assert field['display_name'] == example_field_data['checkbox']['displayName']
    assert field['name'] == example_field_data['checkbox']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_checkboxes_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test CHECKBOXES field normalization."""
    field = json_field_normalizer(example_field_data['checkboxes'])
    assert field['display_name'] == example_field_data['checkboxes']['displayName']
    assert field['name'] == example_field_data['checkboxes']['name']
    assert field['allowed_values']
    assert field['is_list']


def test_radiobutton_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test RADIOBUTTON field normalization."""
    field = json_field_normalizer(example_field_data['radiobutton'])
    assert field['display_name'] == example_field_data['radiobutton']['displayName']
    assert field['name'] == example_field_data['radiobutton']['name']
    assert field['allowed_values']
    assert not field['is_list']


def test_select_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test SELECT field normalization."""
    field = json_field_normalizer(example_field_data['select'])
    assert field['display_name'] == example_field_data['select']['displayName']
    assert field['name'] == example_field_data['select']['name']
    assert field['allowed_values']
    assert not field['is_list']


def test_multiselect_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test MULTISELECT field normalization."""
    field = json_field_normalizer(example_field_data['multiselect'])
    assert field['display_name'] == example_field_data['multiselect']['displayName']
    assert field['name'] == example_field_data['multiselect']['name']
    assert field['allowed_values']
    assert field['is_list']


def test_date_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test DATE field normalization."""
    field = json_field_normalizer(example_field_data['date'])
    assert field['display_name'] == example_field_data['date']['displayName']
    assert field['name'] == example_field_data['date']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_datetime_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test DATETIME field normalization."""
    field = json_field_normalizer(example_field_data['datetime'])
    assert field['display_name'] == example_field_data['datetime']['displayName']
    assert field['name'] == example_field_data['datetime']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_link_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test LINK field normalization."""
    field = json_field_normalizer(example_field_data['link'])
    assert field['display_name'] == example_field_data['link']['displayName']
    assert field['name'] == example_field_data['link']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_image_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test IMAGE field normalization."""
    field = json_field_normalizer(example_field_data['image'])
    assert field['display_name'] == example_field_data['image']['displayName']
    assert field['name'] == example_field_data['image']['name']
    assert not field['allowed_values']
    assert not field['is_list']


def test_file_field_normalization(example_field_data, json_field_normalizer) -> None:
    """Test FILE field normalization."""
    field = json_field_normalizer(example_field_data['file'])
    assert field['display_name'] == example_field_data['file']['displayName']
    assert field['name'] == example_field_data['file']['name']
    assert not field['allowed_values']
    assert field['is_list']
