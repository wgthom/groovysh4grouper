=============================================
Jython Shell Wrapper For Grouper Installation
=============================================

------------
Installation
------------
* Copy `gsh.jython` and `jython_grouper.py` into your `$GROUPER_HOME/bin/` folder.

-------
Running
-------

Run the `$GROUPER_HOME/bin/gsh.jython` script.  You should be able to interact with Grouper
objects::

    Using GROUPER_HOME: /opt/grouper/grouper.apiBinary-2.2.0
    Using GROUPER_CONF: /opt/grouper/grouper.apiBinary-2.2.0/conf
    Using JAVA: java
    using MEMORY: 64m-750m
    >>> session = getRootSession()   
    Grouper starting up: version: 2.2.0, build date: 2014/07/05 12:00:03, env: <no label configured>
    grouper.properties read from: /var/opt/grouper/grouper.apiBinary-2.2.0/conf/grouper.properties
    Grouper current directory is: /var/opt/grouper/grouper.apiBinary-2.2.0
    log4j.properties read from:   /var/opt/grouper/grouper.apiBinary-2.2.0/conf/log4j.properties
    Grouper logs are not using log4j: class org.apache.commons.logging.impl.SLF4JLocationAwareLog
    grouper.hibernate.properties: /var/opt/grouper/grouper.apiBinary-2.2.0/conf/grouper.hibernate.properties
    grouper.hibernate.properties: sa@jdbc:hsqldb:hsql://localhost:9001/grouper
    sources.xml read from:        /var/opt/grouper/grouper.apiBinary-2.2.0/conf/sources.xml
    sources.xml groupersource id: g:gsa
    sources.xml ldap source id:   ldap: ldap.properties
    sources.xml groupersource id: grouperEntities
    sources.xml jdbc source id:   jdbc: GrouperJdbcConnectionProvider
    >>> subj = getSubject("waldbiec")
    >>> print subj                   
    Subject id: waldbiec, sourceId: ldap, name: waldbiec
    >>> 

