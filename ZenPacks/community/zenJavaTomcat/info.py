from ZenPacks.community.ConstructionKit.ClassHelper import *

def TomcatGlobalRequestProcessorgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class TomcatGlobalRequestProcessorInfo(ClassHelper.TomcatGlobalRequestProcessorInfo):
    ''''''

def TomcatThreadPoolgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class TomcatThreadPoolInfo(ClassHelper.TomcatThreadPoolInfo):
    ''''''

def TomcatAppCachegetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class TomcatAppCacheInfo(ClassHelper.TomcatAppCacheInfo):
    ''''''


