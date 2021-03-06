###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('UrbanDictionary')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('UrbanDictionary', True)


UrbanDictionary = conf.registerPlugin('UrbanDictionary')
conf.registerGlobalValue(UrbanDictionary, 'maxNumberOfDefinitions', registry.Integer(10, """Number of definition and examples in output. Max 10."""))
conf.registerGlobalValue(UrbanDictionary, 'disableANSI', registry.Boolean(False, """Do not display any ANSI (color/bold) in output."""))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=250:
