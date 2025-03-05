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
from gramps.version import major_version

_ = glocale.translation.gettext


# ------------------------------------------------------------------------
#
# Default citation formatters for Gramps
#
# ------------------------------------------------------------------------

register(
    CITE,
    id="cite-ATPA-PDC",
    name=_('DES1: Author, "Title", Publisher [Abbreviation] | Page : Date [Confidence]'),
    description=_('User citation formatter: Author, "Title", Publisher [Abbreviation] | Page : Date [Confidence]'),
    version="1.0",
    gramps_target_version = major_version,
    status=STABLE,
    fname="Citation-ATPA-PDC.py",
    authors=["Dave Scheipers"],
)

register(
    CITE,
    id="cite-ATP-PDC",
    name=_('DES2: Author, "Title", Publisher | Page : Date [Confidence]'),
    description=_('User citation formatter: Author, "Title", Publisher | Page : Date [Confidence]'),
    version="1.0",
    gramps_target_version = major_version,
    status=STABLE,
    fname="Citation-ATP-PDC.py",
    authors=["Dave Scheipers"],
)

register(
    CITE,
    id="cite-ATP-DPC",
    name=_('DES3: Author, "Title", Publisher | Date : Page [Confidence]'),
    description=_('User citation formatter: Author, "Title", Publisher | Date : Page [Confidence]'),
    version="1.0",
    gramps_target_version = major_version,
    status=STABLE,
    fname="Citation-ATP-DPC.py",
    authors=["Dave Scheipers"],
)

register(
    CITE,
    id="cite-AATP-PDC",
    name=_('DES4: Abbreviation: Author, "Title", Publisher | Page : Date [Confidence]'),
    description=_('User citation formatter: Abbreviation: Author, "Title", Publisher | Page : Date [Confidence]'),
    version="1.0",
    gramps_target_version = major_version,
    status=STABLE,
    fname="Citation-AATP-PDC.py",
    authors=["Dave Scheipers"],
)

register(
    CITE,
    id="cite-TAPA-PDC",
    name=_("DES5: Title, Author, Publisher [Abbreviation] | Page : Date [Confidence]"),
    description=_("User citation formatter: Title, Author, Publisher [Abbreviation] | Page : Date [Confidence]"),
    version="1.0",
    gramps_target_version = major_version,
    status=STABLE,
    fname="Citation-TAPA-PDC.py",
    authors=["Dave Scheipers"],
)

