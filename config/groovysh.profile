// Grouper Shell Bootstrap
import edu.internet2.middleware.grouper.*
import edu.internet2.middleware.grouper.app.gsh.*
import edu.internet2.middleware.grouper.audit.*
import edu.internet2.middleware.grouper.filter.*
import edu.internet2.middleware.grouper.hibernate.*
import edu.internet2.middleware.grouper.misc.*

// creates threadlocal and stores information about the current context of the database transactions. (how is this used?)
GrouperContext.createNewDefaultContext(GrouperEngineBuiltin.GSH, false, true)

// signals expecting to print to screen (can't find any uses though)
GrouperStartup.runFromMain = true

// only used by GrouperDdlUtils
GrouperShell.runFromGsh = true;

// Grouper start up
GrouperStartup.startup()

// Start root hibernate session
gs = GrouperSession.startRootSession()

findSubject = { id -> 
	SubjectFinder.findById(id, true);
}

getGroups = { name ->
	root = StemFinder.findRootStem(gs)
	filter = new GroupNameFilter(name, root)
	query = GrouperQuery.createQuery(gs,filter)
	return query.getGroups()
}
