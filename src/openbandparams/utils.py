#
#   Copyright (c) 2013, Scott J Maddox
#
#   This file is part of OpenBandParams.
#
#   OpenBandParams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   PhotonAcq is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with PhotonAcq.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
#
#   This file contains code from formencode.
#
#   formencode is licenced under Python Software Foundation (PSF) license,
#   which is compatable with the GNU Affero General Public License.
#
#   You should have received a copy of the PSF license along with this
#   package. If not, see <http://opensource.org/licenses/Python-2.0>.
#
###############################################################################

class classinstancemethod(object):
    """
    Acts like a class method when called from a class, like an
    instance method when called by an instance.  The method should
    take two arguments, 'self' and 'cls'; one of these will be None
    depending on how the method was called.
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, type=None):
        return _methodwrapper(self.func, obj=obj, type=type)

class _methodwrapper(object):

    def __init__(self, func, obj, type):
        self.func = func
        self.obj = obj
        self.type = type

    def __call__(self, *args, **kw):
        assert 'self' not in kw and 'cls' not in kw, (
            "You cannot use 'self' or 'cls' arguments to a "
            "classinstancemethod")
        return self.func(*((self.obj, self.type) + args), **kw)

    def __repr__(self):
        if self.obj is None:
            return ('<bound class method %s.%s>'
                    % (self.type.__name__, self.func.func_name))
        else:
            return ('<bound method %s.%s of %r>'
                    % (self.type.__name__, self.func.func_name, self.obj))
