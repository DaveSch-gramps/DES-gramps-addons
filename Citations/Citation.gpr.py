#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2022       Nick Hall
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
#
from gramps.gen.const import GRAMPS_LOCALE as glocale

_ = glocale.translation.gettext

MODULE_VERSION = "5.2"

# ------------------------------------------------------------------------
#
# Default citation formatters for Gramps
#
# ------------------------------------------------------------------------

register(
    CITE,
    id="cite-AATP",
    name=_('Abbreviation: Author, "Title", Publisher | Page - Date [Confidence]'),
    description=_("Default citation formatter"),
    version="1.0",
    gramps_target_version=MODULE_VERSION,
    status=STABLE,
    fname="Citation-AATP.py",
    authors=["Dave Scheipers"],
)

register(
    CITE,
    id="cite-ATPA",
    name=_('Author, "Title", Publisher; [Abbreviation] | Page - Date [Confidence]'),
    description=_("Default citation formatter"),
    version="1.0",
    gramps_target_version=MODULE_VERSION,
    status=STABLE,
    fname="Citation-ATPA.py",
    authors=["Dave Scheipers"],
)

register(
    CITE,
    id="cite-TAPA",
    name=_("Title, Author, Publisher; [Abbreviation] | Page - Date [Confidence]"),
    description=_("Default citation formatter"),
    version="1.0",
    gramps_target_version=MODULE_VERSION,
    status=STABLE,
    fname="Citation-TAPA.py",
    authors=["Dave Scheipers"],
)
