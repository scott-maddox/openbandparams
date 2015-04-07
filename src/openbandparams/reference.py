#
#   Copyright (c) 2013-2015, Scott J Maddox
#
#   This file is part of openbandparams.
#
#   openbandparams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   openbandparams is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with openbandparams.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

class Reference(object):
    def __init__(self, author, journal, volume, pages, year,
                 title=None, number=None):
        self.author = author
        self.journal = journal
        self.volume = volume
        self.pages = pages
        self.year = year
        self.title = title
        self.number = number
        self.bibtex = None
    
    @classmethod
    def from_bibtex(cls, bibtex):
        #TODO: parse this into the various fields
        result = cls(None, None, None, None, None, None)
        result.bibtex = bibtex
        return result