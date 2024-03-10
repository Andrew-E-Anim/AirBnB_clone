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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """This method returns a string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at attribute """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """This method returns a dictionary
        representation of an object.
        Returns:
            dictionary of instance key-value pairs
        """
        dict_rep = dict(self.__dict__)
        dict_rep['__class__'] = type(self).__name__
        dict_rep['created_at'] = dict_rep['created_at'].isoformat()
        dict_rep['updated_at'] = dict_rep['updated_at'].isoformat()
        return dict_rep
