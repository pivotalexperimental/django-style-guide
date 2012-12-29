import os.path
import inflection
import re


class Partial:
    def __init__(self, path):
        self.path = path

    def title(self):
        return inflection.titleize(self.__partial_name()).strip()

    def id(self):
        mangled_id = self.title().lower()
        mangled_id = re.sub(r'[^a-zA-Z0-9]+', "_", mangled_id)
        return mangled_id

    def content(self):
        with open(self.path) as file:
            return file.read()

    def __partial_name(self):
        return os.path.splitext(os.path.basename(self.path))[0]
