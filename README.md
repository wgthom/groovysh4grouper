Groovy Shell for Grouper
========================

Groovy Shell for Grouper is an exploration of using the stock `groovysh` as a command line interface to Grouper. Feedback, pull requests, etc are welcome.

Demo: https://www.youtube.com/watch?v=YabTBzWc1Ec

Installing
==========

Install Groovy
--------------

Install groovy - http://groovy.codehaus.org/Installing+Groovy.  `brew install groovy` also works on OS X.

Update JVM security policy to accept JMX
--------------------------

Update `$JAVA_HOME/jre/lib/security/java.policy` with:

```
    grant {
    // JMX Java Management eXtensions
    permission javax.management.MBeanTrustPermission "register";
    };
```

See: https://community.oracle.com/thread/1022366?tstart=0

Copy config directory
---------------------

Copy and rename the config directory to `$GROUPER_HOME/grouper.apiBinary-2.2.0/conf/.groovy`

Put ggsh in the bin directory
-----------------------------

Copy `{path to groovysh4grouper}/ggsh` to `$GROUPER_HOME/grouper.apiBinary-2.2.0/bin`.

Running
=======

First check that the regular gsh command is working.  If you are starting from scratch or want an isolated testbed use the [Grouper Installer](https://spaces.internet2.edu/display/Grouper/Grouper+Downloads) and load the sample database when prompted.

If gsh is working you should be able to run:
`./ggsh` to start up groovysh4grouper.

If you've loaded the sample data, try:

```
    groovy:000> getGroups "all students"
```

which should return

```
    ===> [Group[name=qsuob:all,uuid=30c2a93f-3494-4022-a2f5-b92682586482], Group[name=qsuob:all_students,uuid=7959b1fe-c63b-45de-a603-9dc0fdda8206]]
```
