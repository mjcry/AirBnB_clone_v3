#!/usr/bin/python3
# DBStorage

class DBStorage:
    # other methods...

    def get(self, cls, id):
        """Retrieve an object by ID."""
        if cls and id:
            return self.__session.query(cls).get(id)
        return None

    def count(self, cls=None):
        """Count the number of objects in storage."""
        if cls:
            return self.__session.query(cls).count()
        return sum(len(objects) for objects in self.__session.all_objects().values())


# FileStorage

class FileStorage:
    # other methods...

    def get(self, cls, id):
        """Retrieve an object by ID."""
        if cls and id:
            key = "{}.{}".format(cls.__name__, id)
            return self.__objects.get(key)
        return None

    def count(self, cls=None):
        """Count the number of objects in storage."""
        if cls:
            return sum(1 for obj in self.__objects.values() if isinstance(obj, cls))
        return len(self.__objects)

