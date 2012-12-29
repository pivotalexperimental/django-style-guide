# coding: spec

import sure
from mock import Mock
from styleguide.models import Partial
import glob
import tempfile

describe "Partial":
    before_each:
        self.path = "/magnetic/_Sputum.html"

    describe "#title":
        def title(self):
            return Partial(self.path).title()

        context "with a single word":
            it "returns a capitalized string":
                (self.title()).should.equal("Sputum")

        context "with two words joined by an underscore":
            before_each:
                self.path = "/tasty/_tree-leather.html"

            it "returns two capitalized words":
                (self.title()).should.equal("Tree Leather")

        context "with a crazy mixed-up string":
            before_each:
                self.path = "/help/_a_dog%has-m1y=keyb^oaard.html"

            it "returns the right thing":
                (self.title()).should.equal("A Dog%Has M1y=Keyb^Oaard")

    describe "#id":
        def id(self):
            return Partial(self.path).id()

        context "with a single word":
            it "returns a capitalized string":
                (self.id()).should.equal("sputum")

        context "with two words joined by a hyphen":
            before_each:
                self.path = "/tasty/_tree-leather.html"

            it "returns two capitalized words":
                (self.id()).should.equal("tree_leather")

        context "with two words joined by an underscore":
            before_each:
                self.path = "/tasty/_duck_teats.html"

            it "returns two capitalized words":
                (self.id()).should.equal("duck_teats")

        context "with a crazy mixed-up string":
            before_each:
                self.path = "/help/_Mugabe%has-m1y=keyb^oaard.html"

            it "returns the right thing":
                (self.id()).should.equal("mugabe_has_m1y_keyb_oaard")

    describe "#content":
        it "reads from the file system":
            with tempfile.NamedTemporaryFile() as partial_path:
                partial_path.write("<h1>i love my drugboat</h1>")
                partial_path.flush()

                partial = Partial(partial_path.name)
                (partial.content()).should.equal("<h1>i love my drugboat</h1>")
