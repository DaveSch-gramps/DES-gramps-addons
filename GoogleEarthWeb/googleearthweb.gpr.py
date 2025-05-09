#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Benny Malengier
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

register(
    MAPSERVICE,
    id="GoogleEarthWeb",
    name=_("Google Earth Web"),
    description=_("Open on maps.earth.google.com"),
    version="1.0.1",
    gramps_target_version = major_version,
    status=STABLE,
    fname="googleearthweb.py",
    authors=["Dave Scheipers"],
    authors_email=["dave.scheipers@gmail.com"],
    mapservice="GoogleEarthWeb",
)
