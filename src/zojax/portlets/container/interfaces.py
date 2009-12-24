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
from zope import interface, schema
from zope.i18n import MessageFactory

from zojax.portlet.interfaces import IPortletManagerConfiguration
from zojax.portlet.browser.interfaces import IPortletConfigMarker

_ = MessageFactory('zojax.portlets')


class IContainerPortlet(IPortletManagerConfiguration, IPortletConfigMarker):
    """Container Portlet for other portlets to contain """

    portlettype = interface.Attribute('portlettype')
    view = interface.Attribute('view')
    portlets = interface.Attribute('portlets')
    __schema__ = interface.Attribute('__schema__')

    propagate = schema.Bool(title = _(u'Propagate portlet to contained objects'),
                            default=True)


class IContainerPortletConfigMarker(interface.Interface):
    """config marker"""
