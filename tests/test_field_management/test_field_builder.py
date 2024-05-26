def test_text_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test TextField building."""
    field_data = example_field_data['text']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Text'


def test_text_markdown_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test TextMarkdownField building."""
    field_data = example_field_data['text_markdown']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'TextMarkdown'


def test_integer_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test IntegerField building."""
    field_data = example_field_data['integer']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Integer'


def test_float_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test FloatField building."""
    field_data = example_field_data['float']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Float'


def test_single_text_suggested_building(example_field_data,
                                        json_field_normalizer,
                                        field_model_builder,
                                        field_builder) -> None:
    """Test SingleTextSuggestedField building."""
    field_data = example_field_data['single_text_suggested']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'SingleTextSuggested'


def test_multi_text_suggested_building(example_field_data,
                                       json_field_normalizer,
                                       field_model_builder,
                                       field_builder) -> None:
    """Test MultiTextSuggestedField building."""
    field_data = example_field_data['multi_text_suggested']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'MultiTextSuggested'


def test_checkbox_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test CheckboxField building."""
    field_data = example_field_data['checkbox']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Checkbox'


def test_checkboxes_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test CheckboxesField building."""
    field_data = example_field_data['checkboxes']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Checkboxes'


def test_radiobutton_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test RadiobuttonField building."""
    field_data = example_field_data['radiobutton']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'RadioButton'


def test_select_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test SelectField building."""
    field_data = example_field_data['select']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Select'


def test_multiselect_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test MultiselectField building."""
    field_data = example_field_data['multiselect']
    normal_data = json_field_normalizer(field_data)
    defined_type = field_model_builder.define_field_type(normal_data)
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'MultiSelect'


def test_date_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test DateField building."""
    field_data = example_field_data['date']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Date'


def test_datetime_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test DatetimeField building."""
    field_data = example_field_data['datetime']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'DateTime'


def test_link_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test LinkField building."""
    field_data = example_field_data['link']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Link'


def test_image_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test ImageField building."""
    field_data = example_field_data['image']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'Image'


def test_file_building(example_field_data, json_field_normalizer, field_model_builder, field_builder) -> None:
    """Test FileField building."""
    field_data = example_field_data['file']
    field = field_builder(field_data)

    assert field.__class__.__name__ == 'File'
