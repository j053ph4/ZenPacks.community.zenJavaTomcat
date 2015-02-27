
from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaTomcat.Definition import *

class TomcatAppCacheMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(TomcatAppCacheDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'Catalina:type=Cache,host=*,path=*'
    
    def process(self, device, results, log):
        log.info("The plugin %s returned %s results." % (self.name(), len(results)))
        self.scan =  None
        rm = self.relMap()
        for result in results:
            result.pop('path')
            enabled = result['enabled']
            result.pop('enabled')
            om = self.objectMap(result)
            om.setJavaapp = ''
            om.setIpservice = ''
            om.monitor = enabled 
            rm.append(om)
            log.debug(om)
        return rm

