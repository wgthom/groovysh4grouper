
# Enable tab-complete and readline support.
import rlcompleter
import readline
readline.parse_and_bind('tab: complete')

# Put some common names in scope.
import edu.internet2.middleware.grouper as grouper
import edu.internet2.middleware.grouper.filter as grouper_filter

def getRootSession():
    """
    Return a reference to the root session.
    Start a session if one does not exist.
    """
    session = grouper.GrouperSession.startRootSession()
    return session

def findSubject(subjectId, exceptionIfNotFound=True):
    """
    Get a subject by ID.
    """
    return grouper.SubjectFinder.findById(subjectId, exceptionIfNotFound)

def getGroup(session, name, exceptionIfNotFound=True):
    """
    Get a group.
    """
    return grouper.GroupFinder.findByName(session, name, exceptionIfNotFound)

def addGroup(session, stemName, extension, displayExtension, *args, **kwds):
    """
    Add a new group.
    """
    return getStem(session, stemName, *args, **kwds).addChildGroup(extension, displayExtension)

def getStem(session, name, exceptionIfNotFound=True):
    """
    Get a stem (folder).
    """
    return grouper.StemFinder.findByName(session, name, exceptionIfNotFound)

def delGroup(session, name, *args, **kwds):
    """
    Delete a group.
    """
    getGroup(session, name, *args, **kwds).delete()

def delStem(session, name, *args, **kwds):
    """
    Delete a stem.
    """
    getStem(session, name, *args, **kwds).delete()

def addStem(session, extension, displayExtension, parentStem=None):
    """
    Add a stem (folder).
    """
    if parentStem is None:
        parentStem = grouper.StemFinder.findRootStem(session)
    return parentStem.addChildStem(extension, displayExtension)

def getGroups(session, name):
    """
    Iterate over all groups that match `name`.
    """
    root = grouper.StemFinder.findRootStem(session)
    fltr = grouper_filter.GroupNameFilter(name, root)
    query = grouper_filter.GrouperQuery.createQuery(session, fltr)
    for item in query.getGroups():
        yield item

def getMembers(session, groupName, *args, **kwds):
    """
    Iterate over all members in the named group.
    """
    for member in getGroup(session, groupName, *args, **kwds).getMembers():
        yield member

def getStems(session, name):
    """
    Iterate over all stems that match `name`.
    """
    root = grouper.StemFinder.findRootStem(session)
    fltr = grouper_filter.StemNameAnyFilter(name, root)
    query = grouper_filter.GrouperQuery.createQuery(session, fltr)
    for item in query.getStems():
        yield item






















