import pydantic


class UnknownHiveObject(pydantic.BaseModel):
    """Base model for all models."""
    pydantic.ConfigDict(
        populate_by_name=True,
    )

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'
