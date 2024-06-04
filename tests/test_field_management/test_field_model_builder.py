def test_text_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test text-field validator."""
    text_base_field = json_field_normalizer(example_field_data['text'])
    assert field_model_builder.is_text(text_base_field)
    assert not field_model_builder.is_markdown(text_base_field)
    assert not field_model_builder.is_single_suggested_text(text_base_field)
    assert not field_model_builder.is_multi_suggested_text(text_base_field)
    assert not field_model_builder.is_radiobutton(text_base_field)
    assert not field_model_builder.is_checkbox(text_base_field)
    assert not field_model_builder.is_checkboxes(text_base_field)
    assert not field_model_builder.is_select(text_base_field)
    assert not field_model_builder.is_multiselect(text_base_field)
    assert not field_model_builder.is_date(text_base_field)
    assert not field_model_builder.is_datetime(text_base_field)
    assert not field_model_builder.is_link(text_base_field)
    assert not field_model_builder.is_image(text_base_field)
    assert not field_model_builder.is_file(text_base_field)
    assert not field_model_builder.is_integer(text_base_field)
    assert not field_model_builder.is_float(text_base_field)


def test_text_markdown_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test text-markdown-field validator."""
    text_markdown_base_field = json_field_normalizer(example_field_data['text_markdown'])
    assert not field_model_builder.is_text(text_markdown_base_field)
    assert field_model_builder.is_markdown(text_markdown_base_field)
    assert not field_model_builder.is_single_suggested_text(text_markdown_base_field)
    assert not field_model_builder.is_multi_suggested_text(text_markdown_base_field)
    assert not field_model_builder.is_radiobutton(text_markdown_base_field)
    assert not field_model_builder.is_checkbox(text_markdown_base_field)
    assert not field_model_builder.is_checkboxes(text_markdown_base_field)
    assert not field_model_builder.is_select(text_markdown_base_field)
    assert not field_model_builder.is_multiselect(text_markdown_base_field)
    assert not field_model_builder.is_date(text_markdown_base_field)
    assert not field_model_builder.is_datetime(text_markdown_base_field)
    assert not field_model_builder.is_link(text_markdown_base_field)
    assert not field_model_builder.is_image(text_markdown_base_field)
    assert not field_model_builder.is_file(text_markdown_base_field)
    assert not field_model_builder.is_integer(text_markdown_base_field)
    assert not field_model_builder.is_float(text_markdown_base_field)


def test_single_suggested_text_validator(example_field_data,
                                         json_field_normalizer,
                                         field_model_builder,
                                         field_type) -> None:
    """Test single-suggested-text-field validator."""
    single_suggested_text_base_field = json_field_normalizer(example_field_data['single_text_suggested'])
    assert not field_model_builder.is_text(single_suggested_text_base_field)
    assert not field_model_builder.is_markdown(single_suggested_text_base_field)
    assert field_model_builder.is_single_suggested_text(single_suggested_text_base_field)
    assert not field_model_builder.is_multi_suggested_text(single_suggested_text_base_field)
    assert not field_model_builder.is_radiobutton(single_suggested_text_base_field)
    assert not field_model_builder.is_checkbox(single_suggested_text_base_field)
    assert not field_model_builder.is_checkboxes(single_suggested_text_base_field)
    assert not field_model_builder.is_select(single_suggested_text_base_field)
    assert not field_model_builder.is_multiselect(single_suggested_text_base_field)
    assert not field_model_builder.is_date(single_suggested_text_base_field)
    assert not field_model_builder.is_datetime(single_suggested_text_base_field)
    assert not field_model_builder.is_link(single_suggested_text_base_field)
    assert not field_model_builder.is_image(single_suggested_text_base_field)
    assert not field_model_builder.is_file(single_suggested_text_base_field)
    assert not field_model_builder.is_integer(single_suggested_text_base_field)
    assert not field_model_builder.is_float(single_suggested_text_base_field)


def test_multi_suggested_text_validator(example_field_data,
                                        json_field_normalizer,
                                        field_model_builder,
                                        field_type) -> None:
    """Test multi-suggested-text-field validator."""
    multi_suggested_text_base_field = json_field_normalizer(example_field_data['multi_text_suggested'])
    assert not field_model_builder.is_text(multi_suggested_text_base_field)
    assert not field_model_builder.is_markdown(multi_suggested_text_base_field)
    assert not field_model_builder.is_single_suggested_text(multi_suggested_text_base_field)
    assert field_model_builder.is_multi_suggested_text(multi_suggested_text_base_field)
    assert not field_model_builder.is_radiobutton(multi_suggested_text_base_field)
    assert not field_model_builder.is_checkbox(multi_suggested_text_base_field)
    assert not field_model_builder.is_checkboxes(multi_suggested_text_base_field)
    assert not field_model_builder.is_select(multi_suggested_text_base_field)
    assert not field_model_builder.is_multiselect(multi_suggested_text_base_field)
    assert not field_model_builder.is_date(multi_suggested_text_base_field)
    assert not field_model_builder.is_datetime(multi_suggested_text_base_field)
    assert not field_model_builder.is_link(multi_suggested_text_base_field)
    assert not field_model_builder.is_image(multi_suggested_text_base_field)
    assert not field_model_builder.is_file(multi_suggested_text_base_field)
    assert not field_model_builder.is_integer(multi_suggested_text_base_field)
    assert not field_model_builder.is_float(multi_suggested_text_base_field)


def test_integer_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test integer-field validator."""
    integer_base_field = json_field_normalizer(example_field_data['integer'])
    assert not field_model_builder.is_text(integer_base_field)
    assert not field_model_builder.is_markdown(integer_base_field)
    assert not field_model_builder.is_single_suggested_text(integer_base_field)
    assert not field_model_builder.is_multi_suggested_text(integer_base_field)
    assert not field_model_builder.is_radiobutton(integer_base_field)
    assert not field_model_builder.is_checkbox(integer_base_field)
    assert not field_model_builder.is_checkboxes(integer_base_field)
    assert not field_model_builder.is_select(integer_base_field)
    assert not field_model_builder.is_multiselect(integer_base_field)
    assert not field_model_builder.is_date(integer_base_field)
    assert not field_model_builder.is_datetime(integer_base_field)
    assert not field_model_builder.is_link(integer_base_field)
    assert not field_model_builder.is_image(integer_base_field)
    assert not field_model_builder.is_file(integer_base_field)
    assert field_model_builder.is_integer(integer_base_field)
    assert not field_model_builder.is_float(integer_base_field)


def test_float_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test float-field validator."""
    float_base_field = json_field_normalizer(example_field_data['float'])
    assert not field_model_builder.is_text(float_base_field)
    assert not field_model_builder.is_markdown(float_base_field)
    assert not field_model_builder.is_single_suggested_text(float_base_field)
    assert not field_model_builder.is_multi_suggested_text(float_base_field)
    assert not field_model_builder.is_radiobutton(float_base_field)
    assert not field_model_builder.is_checkbox(float_base_field)
    assert not field_model_builder.is_checkboxes(float_base_field)
    assert not field_model_builder.is_select(float_base_field)
    assert not field_model_builder.is_multiselect(float_base_field)
    assert not field_model_builder.is_date(float_base_field)
    assert not field_model_builder.is_datetime(float_base_field)
    assert not field_model_builder.is_link(float_base_field)
    assert not field_model_builder.is_image(float_base_field)
    assert not field_model_builder.is_file(float_base_field)
    assert not field_model_builder.is_integer(float_base_field)
    assert field_model_builder.is_float(float_base_field)


def test_checkbox_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test checkbox-field validator."""
    checkbox_base_field = json_field_normalizer(example_field_data['checkbox'])
    assert not field_model_builder.is_text(checkbox_base_field)
    assert not field_model_builder.is_markdown(checkbox_base_field)
    assert not field_model_builder.is_single_suggested_text(checkbox_base_field)
    assert not field_model_builder.is_multi_suggested_text(checkbox_base_field)
    assert not field_model_builder.is_radiobutton(checkbox_base_field)
    assert field_model_builder.is_checkbox(checkbox_base_field)
    assert not field_model_builder.is_checkboxes(checkbox_base_field)
    assert not field_model_builder.is_select(checkbox_base_field)
    assert not field_model_builder.is_multiselect(checkbox_base_field)
    assert not field_model_builder.is_date(checkbox_base_field)
    assert not field_model_builder.is_datetime(checkbox_base_field)
    assert not field_model_builder.is_link(checkbox_base_field)
    assert not field_model_builder.is_image(checkbox_base_field)
    assert not field_model_builder.is_file(checkbox_base_field)
    assert not field_model_builder.is_integer(checkbox_base_field)
    assert not field_model_builder.is_float(checkbox_base_field)


def test_checkboxes_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test checkboxes-field validator."""
    checkboxes_base_field = json_field_normalizer(example_field_data['checkboxes'])
    assert not field_model_builder.is_text(checkboxes_base_field)
    assert not field_model_builder.is_markdown(checkboxes_base_field)
    assert not field_model_builder.is_single_suggested_text(checkboxes_base_field)
    assert not field_model_builder.is_multi_suggested_text(checkboxes_base_field)
    assert not field_model_builder.is_radiobutton(checkboxes_base_field)
    assert not field_model_builder.is_checkbox(checkboxes_base_field)
    assert field_model_builder.is_checkboxes(checkboxes_base_field)
    assert not field_model_builder.is_select(checkboxes_base_field)
    assert not field_model_builder.is_multiselect(checkboxes_base_field)
    assert not field_model_builder.is_date(checkboxes_base_field)
    assert not field_model_builder.is_datetime(checkboxes_base_field)
    assert not field_model_builder.is_link(checkboxes_base_field)
    assert not field_model_builder.is_image(checkboxes_base_field)
    assert not field_model_builder.is_file(checkboxes_base_field)
    assert not field_model_builder.is_integer(checkboxes_base_field)
    assert not field_model_builder.is_float(checkboxes_base_field)


def test_radiobutton_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test radiobutton-field validator."""
    radiobutton_base_field = json_field_normalizer(example_field_data['radiobutton'])
    assert not field_model_builder.is_text(radiobutton_base_field)
    assert not field_model_builder.is_markdown(radiobutton_base_field)
    assert not field_model_builder.is_single_suggested_text(radiobutton_base_field)
    assert not field_model_builder.is_multi_suggested_text(radiobutton_base_field)
    assert field_model_builder.is_radiobutton(radiobutton_base_field)
    assert not field_model_builder.is_checkbox(radiobutton_base_field)
    assert not field_model_builder.is_checkboxes(radiobutton_base_field)
    assert not field_model_builder.is_select(radiobutton_base_field)
    assert not field_model_builder.is_multiselect(radiobutton_base_field)
    assert not field_model_builder.is_date(radiobutton_base_field)
    assert not field_model_builder.is_datetime(radiobutton_base_field)
    assert not field_model_builder.is_link(radiobutton_base_field)
    assert not field_model_builder.is_image(radiobutton_base_field)
    assert not field_model_builder.is_file(radiobutton_base_field)
    assert not field_model_builder.is_integer(radiobutton_base_field)
    assert not field_model_builder.is_float(radiobutton_base_field)


def test_select_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test select-field validator."""
    select_base_field = json_field_normalizer(example_field_data['select'])
    assert not field_model_builder.is_text(select_base_field)
    assert not field_model_builder.is_markdown(select_base_field)
    assert not field_model_builder.is_single_suggested_text(select_base_field)
    assert not field_model_builder.is_multi_suggested_text(select_base_field)
    assert not field_model_builder.is_radiobutton(select_base_field)
    assert not field_model_builder.is_checkbox(select_base_field)
    assert not field_model_builder.is_checkboxes(select_base_field)
    assert field_model_builder.is_select(select_base_field)
    assert not field_model_builder.is_multiselect(select_base_field)
    assert not field_model_builder.is_date(select_base_field)
    assert not field_model_builder.is_datetime(select_base_field)
    assert not field_model_builder.is_link(select_base_field)
    assert not field_model_builder.is_image(select_base_field)
    assert not field_model_builder.is_file(select_base_field)
    assert not field_model_builder.is_integer(select_base_field)
    assert not field_model_builder.is_float(select_base_field)


def test_multiselect_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test multiselect-field validator."""
    multiselect_base_field = json_field_normalizer(example_field_data['multiselect'])
    assert not field_model_builder.is_text(multiselect_base_field)
    assert not field_model_builder.is_markdown(multiselect_base_field)
    assert not field_model_builder.is_single_suggested_text(multiselect_base_field)
    assert not field_model_builder.is_multi_suggested_text(multiselect_base_field)
    assert not field_model_builder.is_radiobutton(multiselect_base_field)
    assert not field_model_builder.is_checkbox(multiselect_base_field)
    assert not field_model_builder.is_checkboxes(multiselect_base_field)
    assert not field_model_builder.is_select(multiselect_base_field)
    assert field_model_builder.is_multiselect(multiselect_base_field)
    assert not field_model_builder.is_date(multiselect_base_field)
    assert not field_model_builder.is_datetime(multiselect_base_field)
    assert not field_model_builder.is_link(multiselect_base_field)
    assert not field_model_builder.is_image(multiselect_base_field)
    assert not field_model_builder.is_file(multiselect_base_field)
    assert not field_model_builder.is_integer(multiselect_base_field)
    assert not field_model_builder.is_float(multiselect_base_field)


def test_date_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test date-field validator."""
    date_base_field = json_field_normalizer(example_field_data['date'])
    assert not field_model_builder.is_text(date_base_field)
    assert not field_model_builder.is_markdown(date_base_field)
    assert not field_model_builder.is_single_suggested_text(date_base_field)
    assert not field_model_builder.is_multi_suggested_text(date_base_field)
    assert not field_model_builder.is_radiobutton(date_base_field)
    assert not field_model_builder.is_checkbox(date_base_field)
    assert not field_model_builder.is_checkboxes(date_base_field)
    assert not field_model_builder.is_select(date_base_field)
    assert not field_model_builder.is_multiselect(date_base_field)
    assert field_model_builder.is_date(date_base_field)
    assert not field_model_builder.is_datetime(date_base_field)
    assert not field_model_builder.is_link(date_base_field)
    assert not field_model_builder.is_image(date_base_field)
    assert not field_model_builder.is_file(date_base_field)
    assert not field_model_builder.is_integer(date_base_field)
    assert not field_model_builder.is_float(date_base_field)


def test_datetime_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test datetime-field validator."""
    datetime_base_field = json_field_normalizer(example_field_data['datetime'])
    assert not field_model_builder.is_text(datetime_base_field)
    assert not field_model_builder.is_markdown(datetime_base_field)
    assert not field_model_builder.is_single_suggested_text(datetime_base_field)
    assert not field_model_builder.is_multi_suggested_text(datetime_base_field)
    assert not field_model_builder.is_radiobutton(datetime_base_field)
    assert not field_model_builder.is_checkbox(datetime_base_field)
    assert not field_model_builder.is_checkboxes(datetime_base_field)
    assert not field_model_builder.is_select(datetime_base_field)
    assert not field_model_builder.is_multiselect(datetime_base_field)
    assert not field_model_builder.is_date(datetime_base_field)
    assert field_model_builder.is_datetime(datetime_base_field)
    assert not field_model_builder.is_link(datetime_base_field)
    assert not field_model_builder.is_image(datetime_base_field)
    assert not field_model_builder.is_file(datetime_base_field)
    assert not field_model_builder.is_integer(datetime_base_field)
    assert not field_model_builder.is_float(datetime_base_field)


def test_link_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test link-field validator."""
    link_base_field = json_field_normalizer(example_field_data['link'])
    assert not field_model_builder.is_text(link_base_field)
    assert not field_model_builder.is_markdown(link_base_field)
    assert not field_model_builder.is_single_suggested_text(link_base_field)
    assert not field_model_builder.is_multi_suggested_text(link_base_field)
    assert not field_model_builder.is_radiobutton(link_base_field)
    assert not field_model_builder.is_checkbox(link_base_field)
    assert not field_model_builder.is_checkboxes(link_base_field)
    assert not field_model_builder.is_select(link_base_field)
    assert not field_model_builder.is_multiselect(link_base_field)
    assert not field_model_builder.is_date(link_base_field)
    assert not field_model_builder.is_datetime(link_base_field)
    assert field_model_builder.is_link(link_base_field)
    assert not field_model_builder.is_image(link_base_field)
    assert not field_model_builder.is_file(link_base_field)
    assert not field_model_builder.is_integer(link_base_field)
    assert not field_model_builder.is_float(link_base_field)


def test_image_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test image-field validator."""
    image_base_field = json_field_normalizer(example_field_data['image'])
    assert not field_model_builder.is_text(image_base_field)
    assert not field_model_builder.is_markdown(image_base_field)
    assert not field_model_builder.is_single_suggested_text(image_base_field)
    assert not field_model_builder.is_multi_suggested_text(image_base_field)
    assert not field_model_builder.is_radiobutton(image_base_field)
    assert not field_model_builder.is_checkbox(image_base_field)
    assert not field_model_builder.is_checkboxes(image_base_field)
    assert not field_model_builder.is_select(image_base_field)
    assert not field_model_builder.is_multiselect(image_base_field)
    assert not field_model_builder.is_date(image_base_field)
    assert not field_model_builder.is_datetime(image_base_field)
    assert not field_model_builder.is_link(image_base_field)
    assert field_model_builder.is_image(image_base_field)
    assert not field_model_builder.is_file(image_base_field)
    assert not field_model_builder.is_integer(image_base_field)
    assert not field_model_builder.is_float(image_base_field)


def test_file_validator(example_field_data, json_field_normalizer, field_model_builder, field_type) -> None:
    """Test file-field validator."""
    file_base_field = json_field_normalizer(example_field_data['file'])
    assert not field_model_builder.is_text(file_base_field)
    assert not field_model_builder.is_markdown(file_base_field)
    assert not field_model_builder.is_single_suggested_text(file_base_field)
    assert not field_model_builder.is_multi_suggested_text(file_base_field)
    assert not field_model_builder.is_radiobutton(file_base_field)
    assert not field_model_builder.is_checkbox(file_base_field)
    assert not field_model_builder.is_checkboxes(file_base_field)
    assert not field_model_builder.is_select(file_base_field)
    assert not field_model_builder.is_multiselect(file_base_field)
    assert not field_model_builder.is_date(file_base_field)
    assert not field_model_builder.is_datetime(file_base_field)
    assert not field_model_builder.is_link(file_base_field)
    assert not field_model_builder.is_image(file_base_field)
    assert field_model_builder.is_file(file_base_field)
    assert not field_model_builder.is_integer(file_base_field)
    assert not field_model_builder.is_float(file_base_field)


def test_text_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test text-field model building."""
    field = json_field_normalizer(example_field_data['text'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.TEXT


def test_text_markdown_model_building(example_field_data,
                                      field_model_builder,
                                      field_type,
                                      json_field_normalizer) -> None:
    """Test text-markdown-field model building."""
    field = json_field_normalizer(example_field_data['text_markdown'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.TEXT_MARKDOWN


def test_single_suggested_text_model_building(example_field_data,
                                              field_model_builder,
                                              field_type,
                                              json_field_normalizer) -> None:
    """Test single-suggested-text-field model building."""
    field = json_field_normalizer(example_field_data['single_text_suggested'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.SINGLE_TEXT_SUGGESTED


def test_multi_suggested_text_model_building(example_field_data,
                                             field_model_builder,
                                             field_type,
                                             json_field_normalizer) -> None:
    """Test multi-suggested-text-field model building."""
    field = json_field_normalizer(example_field_data['multi_text_suggested'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.MULTI_TEXT_SUGGESTED


def test_integer_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test integer-field model building."""
    field = json_field_normalizer(example_field_data['integer'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.INTEGER


def test_float_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test float-field model building."""
    field = json_field_normalizer(example_field_data['float'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.FLOAT


def test_checkbox_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test checkbox-field model building."""
    field = json_field_normalizer(example_field_data['checkbox'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.CHECKBOX


def test_checkboxes_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test checkboxes-field model building."""
    field = json_field_normalizer(example_field_data['checkboxes'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.CHECKBOXES


def test_radiobutton_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test radiobutton-field model building."""
    field = json_field_normalizer(example_field_data['radiobutton'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.RADIOBUTTON


def test_select_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test select-field model building."""
    field = json_field_normalizer(example_field_data['select'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.SELECT


def test_multiselect_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test multiselect-field model building."""
    field = json_field_normalizer(example_field_data['multiselect'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.MULTISELECT


def test_date_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test date-field model building."""
    field = json_field_normalizer(example_field_data['date'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.DATE


def test_datetime_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test datetime-field model building."""
    field = json_field_normalizer(example_field_data['datetime'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.DATETIME


def test_link_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test link-field model building."""
    field = json_field_normalizer(example_field_data['link'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.LINK


def test_image_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test image-field model building."""
    field = json_field_normalizer(example_field_data['image'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.IMAGE


def test_file_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test file-field model building."""
    field = json_field_normalizer(example_field_data['file'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.FILE


def test_hostname_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test hostname-field model building."""
    field = json_field_normalizer(example_field_data['hostname'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.HOSTNAME


def test_ip_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test ip-field model building."""
    field = json_field_normalizer(example_field_data['ip'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.IP


def test_asset_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test asset-field model building."""
    field = json_field_normalizer(example_field_data['asset'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.ASSET


def test_request_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test request-field model building."""
    field = json_field_normalizer(example_field_data['request'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.REQUEST


def test_datasource_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test datasource-field model building."""
    field = json_field_normalizer(example_field_data['datasource'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.DATASOURCE


def test_status_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test status-field model building."""
    field = json_field_normalizer(example_field_data['status'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.STATUS


def test_cvss_score_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test cvss-base-score-field model building."""
    field = json_field_normalizer(example_field_data['cvss_score'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.CVSS_SCORE


def test_cvss_vector_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test cvss-base-vector-field model building."""
    field = json_field_normalizer(example_field_data['cvss_vector'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.CVSS_VECTOR


def test_uuid_field_model_building(example_field_data, field_model_builder, field_type, json_field_normalizer) -> None:
    """Test uuid-field model building."""
    field = json_field_normalizer(example_field_data['uuid'])
    model = field_model_builder(field)
    assert model.model_fields['type'].default == field_type.UUID
