# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2007-2009  Douglas S. Blank <doug.blank@gmail.com>
# Copyright (C) 2020       Dave Scheipers
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#------------------------------------------------------------------------
#
# Gtk modules
#
#------------------------------------------------------------------------
from gi.repository import Gtk

#------------------------------------------------------------------------
#
# Gramps modules
#
#------------------------------------------------------------------------
from gramps.gen.const import (URL_WIKISTRING, URL_MANUAL_PAGE,
                              URL_HOMEPAGE, WIKI_EXTRAPLUGINS)
from gramps.gen.plug import Gramplet
from gramps.gui.widgets.styledtexteditor import StyledTextEditor
from gramps.gen.lib import StyledText, StyledTextTag, StyledTextTagType
from gramps.gen.const import GRAMPS_LOCALE as glocale
_ = glocale.translation.sgettext

#------------------------------------------------------------------------
#
# Functions
#
#------------------------------------------------------------------------
def st(text):
    """ Return text as styled text
    """
    return StyledText(text)

def boldst(text):
    """ Return text as bold styled text
    """
    tags = [StyledTextTag(StyledTextTagType.BOLD, True, [(0, len(text))])]
    return StyledText(text, tags)

def linkst(text, url):
    """ Return text as link styled text
    """
    tags = [StyledTextTag(StyledTextTagType.LINK, url, [(0, len(text))])]
    return StyledText(text, tags)

#------------------------------------------------------------------------
#
# Gramplet class
#
#------------------------------------------------------------------------

class GlossaryGramplet(Gramplet):
    """
    Displays a Glossary list to the user.
    """
    def init(self):
        self.gui.WIDGET = self.build_gui()
        self.gui.get_container_widget().remove(self.gui.textview)
        self.gui.get_container_widget().add(self.gui.WIDGET)
        self.gui.WIDGET.show()

    def build_gui(self):
        """
        Build the GUI interface.
        """
        top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_policy(Gtk.PolicyType.AUTOMATIC,
                                  Gtk.PolicyType.AUTOMATIC)
        self.texteditor = StyledTextEditor()
        self.texteditor.set_editable(False)
        self.texteditor.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolledwindow.add(self.texteditor)

        self.display_text()

        top.pack_start(scrolledwindow, True, True, 0)
        top.show_all()
        return top

    def display_text(self):
        """
        Display the Glossary text.
        """
        glossary = boldst(_('Intro')) + '\n\n'
        glossary += _(
            '   1. ')
        glossary += linkst(_('Term 1'), URL_HOMEPAGE) + '\n'
        glossary += _(
            'Description.\n\n   2. ')
        glossary += linkst(_('Term 2'),
                          URL_WIKISTRING + URL_MANUAL_PAGE +
                          _('locale_suffix|')) + '\n'
        glossary += _(
            'Description.\n\n   3. ')
        glossary += linkst(_('Term 3'),
                          '%(gramps_home_url)scontact/' %
                          {'gramps_home_url': URL_HOMEPAGE}) + '\n'
        glossary += _(
            'Description.\n\n   4. ')
        glossary += linkst(_('Term 4'),
		                  'https://gramps.discourse.group/t/welcome-to-discourse/') + '\n'
        glossary += _(
            'Description.\n\n   5. ')
        glossary += linkst(_('Term 5'),
                          '%(gramps_wiki_url)sStart_with_Genealogy' %
                          {'gramps_wiki_url': URL_WIKISTRING}) + '\n'
        glossary += _(
            'Description.\n\n   6. ')
        glossary += boldst(_('Term 6')) + '\n' + _(
            'Description.\n\n   7. ')

        self.texteditor.set_text(glossary)

    def get_has_data(self, obj):
        """
        Return True if the gramplet has data, else return False.
        """
        return True
