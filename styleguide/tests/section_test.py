# coding: spec

import sure
from mock import Mock
from styleguide.models import Section, Partial
import glob

describe "Section":
    before_each:
        self.path = "/magnetic/Sputum"

    describe "#title":
        def title(self):
            return Section(self.path).title()

        context "with a single word":
            it "returns a capitalized string":
                (self.title()).should.equal("Sputum")

        context "with two words joined by an underscore":
            before_each:
                self.path = "/tasty/bicycle_tires"

            it "returns two capitalized words":
                (self.title()).should.equal("Bicycle Tires")

        context "with a crazy mixed-up string":
            before_each:
                self.path = "/help/kocher%has-m1y=keyb^oaard"

            it "returns the right thing":
                (self.title()).should.equal("Kocher%Has M1y=Keyb^Oaard")

    describe "#id":
        def id(self):
            return Section(self.path).id()

        context "with a single word":
            it "returns a lowercase string":
                (self.id()).should.equal("sputum")

        context "with spaces in the path":
            before_each:
                self.path = "/magical/ dis appointment"

            it "returns a stripped word":
                (self.id()).should.equal("dis_appointment")

        context "with a crazy mixed-up string":
            before_each:
                self.path = "/help/jr%has-m1y=keyb^oaard"

            it "returns the right thing":
                (self.id()).should.equal("jr_has_m1y_keyb_oaard")

    describe "#partials":
        before_each:
            self.partial_paths = ["/corrosive/chapstick", "/rusty/derringer"]
            glob.glob = Mock(return_value=self.partial_paths)

        def partials(self):
            return Section(self.path).partials()

        it "globs for partials in its path":
            self.partials()
            glob.glob.assert_called_once_with("/magnetic/Sputum/_*.html")

        it "has two partials":
            (self.partials()).should.have.length_of(2)
