from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaTomcat.Definition import *

class TomcatThreadPoolMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(TomcatThreadPoolDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'Catalina:type=ThreadPool,name=*'

