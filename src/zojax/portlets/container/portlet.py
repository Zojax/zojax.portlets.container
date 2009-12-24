##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from rwproperty import setproperty, getproperty

from zope.component import getMultiAdapter

from zojax.portlet.manager import PortletManagerBase
from zojax.portlet.portlet import PortletBase
from zojax.portlet.interfaces import IPortlet
from zojax.portlet.browser.portlet import PortletPublicAbsoluteURL
from zojax.layout.interfaces import ILayout

from interfaces import IContainerPortlet


class ContainerPortlet(PortletManagerBase, PortletBase):
    """ Container portlet """

    portlets = ()

    def __init__(self, context, request, manager=None, view=None):
        if view is None:
            view = manager
            PortletManagerBase.__init__(self, context, request, view)
        PortletBase.__init__(self, context, request, manager, view)

    @getproperty
    def view(self):
        if self.manager is None:
            return
        return self.manager.view

    @setproperty
    def view(self, value):
        pass

    def isAvailable(self):
        if not self.propagate:
            if ILayout.providedBy(self.view):
                self.context, self.view.maincontext
                return self.context == self.view.maincontext
            elif self.view is not None:
                return self.context == self.view.context
            return self.context == self.manager.context
        return super(ContainerPortlet, self).isAvailable()


class PortletContainerPublicAbsoluteURL(PortletPublicAbsoluteURL):

    def __str__(self):
        if IPortlet.providedBy(self.context.manager):
            return '%s/%s'%(
                getMultiAdapter((self.context.manager, self.request), name='public_absolute_url'),
                self.context.__name__)
        return super(PortletContainerPublicAbsoluteURL, self).__str__()

    __call__ = __str__
