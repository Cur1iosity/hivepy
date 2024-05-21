def test_text_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Text initialization."""
    field_data = json_field_normalizer(example_field_data['text'])
    field = field_type_map[field_type.TEXT](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.type == field_type.TEXT
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_text_markdown_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Text Markdown initialization."""
    field_data = json_field_normalizer(example_field_data['text_markdown'])
    field = field_type_map[field_type.TEXT_MARKDOWN](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.type == field_type.TEXT_MARKDOWN
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_integer_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Integer initialization."""
    field_data = json_field_normalizer(example_field_data['integer'])
    field = field_type_map[field_type.INTEGER](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.type == field_type.INTEGER
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_float_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Float initialization."""
    field_data = json_field_normalizer(example_field_data['float'])
    field = field_type_map[field_type.FLOAT](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_single_text_suggested_initialization(example_field_data,
                                              field_type_map,
                                              field_type,
                                              json_field_normalizer) -> None:
    """Test Single Text Suggested initialization."""
    field_data = json_field_normalizer(example_field_data['single_text_suggested'])
    field = field_type_map[field_type.SINGLE_TEXT_SUGGESTED](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_multi_text_suggested_initialization(example_field_data,
                                             field_type_map,
                                             field_type,
                                             json_field_normalizer) -> None:
    """Test Multi Text Suggested initialization."""
    field_data = json_field_normalizer(example_field_data['multi_text_suggested'])
    field = field_type_map[field_type.MULTI_TEXT_SUGGESTED](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_checkbox_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Checkbox initialization."""
    field_data = json_field_normalizer(example_field_data['checkbox'])
    field = field_type_map[field_type.CHECKBOX](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_checkboxes_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Checkboxes initialization."""
    field_data = json_field_normalizer(example_field_data['checkboxes'])
    field = field_type_map[field_type.CHECKBOXES](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_radiobutton_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Radiobutton initialization."""
    field_data = json_field_normalizer(example_field_data['radiobutton'])
    field = field_type_map[field_type.RADIOBUTTON](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_select_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Select initialization."""
    field_data = json_field_normalizer(example_field_data['select'])
    field = field_type_map[field_type.SELECT](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_multiselect_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Multiselect initialization."""
    field_data = json_field_normalizer(example_field_data['multiselect'])
    field = field_type_map[field_type.MULTISELECT](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_date_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Date initialization."""
    field_data = json_field_normalizer(example_field_data['date'])
    field = field_type_map[field_type.DATE](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_datetime_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Datetime initialization."""
    field_data = json_field_normalizer(example_field_data['datetime'])
    field = field_type_map[field_type.DATETIME](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_link_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Link initialization."""
    field_data = json_field_normalizer(example_field_data['link'])
    field = field_type_map[field_type.LINK](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_image_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test Image initialization."""
    field_data = json_field_normalizer(example_field_data['image'])
    field = field_type_map[field_type.IMAGE](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']


def test_file_initialization(example_field_data, field_type_map, field_type, json_field_normalizer) -> None:
    """Test File initialization."""
    field_data = json_field_normalizer(example_field_data['file'])
    field = field_type_map[field_type.FILE](**field_data)

    assert field.display_name == field_data['display_name']
    assert field.name == field_data['name']
    assert field.allowed_values == field_data['allowed_values']
    assert field.is_list == field_data['is_list']
    assert field.required == field_data['required']
    assert field.hidden == field_data['hidden']
    assert field.initially_collapsed == field_data['initially_collapsed']
    assert field.placeholder == field_data['placeholder']
    assert field.hint == field_data['hint']
