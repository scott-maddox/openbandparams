#
#   Copyright (c) 2013-2014, Scott J Maddox
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
    take two arguments, 'self' and 'cls'. 'self' will be None
    if the method was called as a static or class method.
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, objtype=None):
        return _methodwrapper(self.func, obj=obj, objtype=objtype)


class _methodwrapper(object):

    def __init__(self, func, obj, objtype):
        self.func = func
        self.obj = obj
        self.objtype = objtype

    def __call__(self, *args, **kw):
        assert 'self' not in kw and 'cls' not in kw, (
            "You cannot use 'self' or 'cls' arguments to a "
            "classinstancemethod")
        return self.func(*((self.obj, self.objtype) + args), **kw)

    def __repr__(self):
        if self.obj is None:
            return ('<bound class method %s.%s>'
                    % (self.objtype.__name__, self.func.func_name))
        else:
            return ('<bound method %s.%s of %r>'
                    % (self.objtype.__name__, self.func.func_name, self.obj))
