from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaTomcat.Definition import *

class TomcatGlobalRequestProcessorMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(TomcatGlobalRequestProcessorDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'Catalina:type=GlobalRequestProcessor,name=*'

