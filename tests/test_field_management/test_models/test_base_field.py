def test_text_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Text BaseField."""
    field = base_field_class(**example_field_data['text'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.TEXT
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'TEXT'


def test_text_markdown_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test TextMarkdown BaseField."""
    field = base_field_class(**example_field_data['text_markdown'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.TEXT_MARKDOWN
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'TEXT_MD'


def test_integer_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Integer BaseField."""
    field = base_field_class(**example_field_data['integer'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.INTEGER
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'INTEGER'


def test_float_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Float BaseField."""
    field = base_field_class(**example_field_data['float'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.FLOAT
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'FLOAT'


def test_single_text_suggested_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test SingleTextSuggested BaseField."""
    field = base_field_class(**example_field_data['single_text_suggested'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.TEXT_SUGGESTED
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'TEXT_SUGGESTED'


def test_multi_text_suggested_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test MultiTextSuggested BaseField."""
    field = base_field_class(**example_field_data['multi_text_suggested'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is True
    assert field.type == base_field_type.TEXT_SUGGESTED
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is True
    assert field_dict['type'] == 'TEXT_SUGGESTED'


def test_checkbox_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Checkbox BaseField."""
    field = base_field_class(**example_field_data['checkbox'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.BOOLEAN
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'BOOLEAN'


def test_checkboxes_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Checkboxes BaseField."""
    field = base_field_class(**example_field_data['checkboxes'])
    field_dict = field.model_dump()
    assert field.allowed_values
    assert field.is_list is True
    assert field.type == base_field_type.TEXT
    assert field_dict['allowed_values']
    assert field_dict['is_list'] is True
    assert field_dict['type'] == 'TEXT'


def test_radiobutton_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test RadioButton BaseField."""
    field = base_field_class(**example_field_data['radiobutton'])
    field_dict = field.model_dump()
    assert field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.TEXT
    assert field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'TEXT'


def test_select_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Select BaseField."""
    field = base_field_class(**example_field_data['select'])
    field_dict = field.model_dump()
    assert field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.TEXT
    assert field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'TEXT'


def test_multiselect_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test MultiSelect BaseField."""
    field = base_field_class(**example_field_data['multiselect'])
    field_dict = field.model_dump()
    assert field.allowed_values
    assert field.is_list is True
    assert field.type == base_field_type.TEXT
    assert field_dict['allowed_values']
    assert field_dict['is_list'] is True
    assert field_dict['type'] == 'TEXT'


def test_link_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Link BaseField."""
    field = base_field_class(**example_field_data['link'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.LINK
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'LINK'


def test_image_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test Image BaseField."""
    field = base_field_class(**example_field_data['image'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is False
    assert field.type == base_field_type.IMAGE
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is False
    assert field_dict['type'] == 'IMAGE'


def test_file_base_field(example_field_data, base_field_type, base_field_class) -> None:
    """Test File BaseField."""
    field = base_field_class(**example_field_data['file'])
    field_dict = field.model_dump()
    assert not field.allowed_values
    assert field.is_list is True
    assert field.type == base_field_type.FILE
    assert not field_dict['allowed_values']
    assert field_dict['is_list'] is True
    assert field_dict['type'] == 'FILE'
