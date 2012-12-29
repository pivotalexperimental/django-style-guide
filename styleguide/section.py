import os.path
import inflection
import re
import glob

from styleguide.models import Partial


class Section:
    def __init__(self,  path):
        self.path = path

    def title(self):
        return inflection.titleize(self.__section_directory())

    def id(self):
        mangled_id = self.__section_directory().lower()
        mangled_id = re.sub(r'[^a-zA-Z0-9]', " ", mangled_id)
        return mangled_id.strip().replace(" ", "_")

    def partials(self):
        return [Partial(path) for path in self.__partial_paths()]

    def __section_directory(self):
        return os.path.basename(self.path)

    def __partial_paths(self):
        return glob.glob(os.path.join(self.path, "_*.html"))
