
# Enable tab-complete and readline support.
import rlcompleter 
import readline 
readline.parse_and_bind('tab: complete') 

# Put some common names in scope.
import edu.internet2.middleware.grouper as grouper 

def getRootSession():
    """
    Return a reference to the root session.
    Start a session if one does not exist.
    """
    session = grouper.GrouperSession.startRootSession()
    return session

def getSubject(subjectId):
    """
    Get a subject by ID.
    """    
    subj_finder = grouper.SubjectFinder()
    return subj_finder.findById(subjectId)

