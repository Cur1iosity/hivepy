from datetime import datetime

import pydantic


class Issue(pydantic.BaseModel):
    ...

    class Config:
        populate_by_name = True

    # @pydantic.field_validator('create_date', 'update_date', 'start_date', 'end_date', mode='before')
    # def validate_datetime(cls, value: str) -> str:
    #     """Validate datetime field."""
    #     try:
    #         dt: datetime = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    #     except ValueError:
    #         raise ValueError('Invalid datetime.')
    #     return datetime.strftime(dt, '%d-%m-%Y %H:%M:%S')

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'
