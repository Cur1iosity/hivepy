import pydantic


class BaseSchema(pydantic.BaseModel):
    ...

    model_config = pydantic.ConfigDict(
        populate_by_name=True
    )

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__qualname__}({", ".join(f"{key}={value}" for key, value in self.dict().items())})'
