from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaTomcat.Definition import *


__doc__ = """TomcatAppCacheMap

TomcatAppCacheMap detects Tomcat App Caches on a per-JVM basis.

This version adds a relation to associated ipservice and javaapp components.

"""


class TomcatAppCacheMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(TomcatAppCacheDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'Catalina:type=Cache,host=*,path=*'
    
    def postprocess(self, result, om, log):
        '''optional method before appending to relmap'''
        delattr(om,'path')
        return om

