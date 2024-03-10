"""create a model BaseModel that other classes inherit from."""
import uuid
import datetime


class BaseModel:
    """This is a model called BaseModel, other classes will inherit from"""
    def __init__(self):
        """
        This method initialises the public instance attributes
        Attributes:
            id (string) - a uniques id
            created_at (datetime) - the time an instance was created
            updated_at (datetime) - the updated time
        """
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """This method returns a string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at attribute """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """This method returns a dictionary
        representation of an object."""
        dict_rep = self.__dict__
        dict_rep['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        return dict_rep
