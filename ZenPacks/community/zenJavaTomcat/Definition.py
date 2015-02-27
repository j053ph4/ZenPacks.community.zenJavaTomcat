from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *
from ZenPacks.community.zenJavaApp.Definition import getMBeanDef, addMBeanRelations


ROOT = "ZenPacks.community"
BASE = "zenJavaTomcat"
VERSION = Version(1, 0, 0)

###################### TomcatGlobalRequestProcessor
TomcatGlobalRequestProcessorDefinition = type('TomcatGlobalRequestProcessorDefinition', (BasicDefinition,), 
                                      getMBeanDef(VERSION, ROOT, BASE, 'TomcatGlobalRequestProcessor','Tomcat Global Request Processor', 'Tomcat Global Request Processors'))
addMBeanRelations(TomcatGlobalRequestProcessorDefinition)

###################### TomcatThreadPool


TomcatThreadPoolDefinition = type('TomcatThreadPoolDefinition', (BasicDefinition,), 
                                      getMBeanDef(VERSION, ROOT, BASE, 'TomcatThreadPool','Tomcat Thread Pool', 'Tomcat Thread Pools'))
addMBeanRelations(TomcatThreadPoolDefinition)

###################### TomcatCache

TomcatAppCacheDefinition = type('TomcatAppCacheDefinition', (BasicDefinition,), 
                                      getMBeanDef(VERSION, ROOT, BASE, 'TomcatAppCache','Tomcat App Cache', 'Tomcat App Caches'))
addMBeanRelations(TomcatAppCacheDefinition)

