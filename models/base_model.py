#!/usr/bin/python3
"""create a model BaseModel that other classes inherit from."""
import uuid
import datetime
import models


class BaseModel:
    """This is a model called BaseModel, other classes will inherit from"""
    def __init__(self, *args, **kwargs):
        """
        This method initialises the public instance attributes
        Attributes:
            id (string) - a uniques id
            created_at (datetime) - the time an instance was created
            updated_at (datetime) - the updated time
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.strptime
                                (val, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method returns a string representation"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """ updates the updated_at attribute """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary
        representation of an object.
        Returns:
            dictionary of instance key-value pairs
        """
        dict_rep = dict(self.__dict__)
        dict_rep['__class__'] = type(self).__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
