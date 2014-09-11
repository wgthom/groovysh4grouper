
(import '(edu.internet2.middleware.grouper GrouperSession SubjectFinder GroupFinder StemFinder))
(import '(edu.internet2.middleware.grouper.filter GroupNameFilter GrouperQuery StemNameAnyFilter))

(defn getRootSession []
    (. GrouperSession startRootSession))

(defn findSubject [subjectId]
    (. SubjectFinder findById subjectId))

(defn getGroup [session group & {:keys [exception-if-not-found?] :or {exception-if-not-found? true}}]
    ( . GroupFinder findByName session group exception-if-not-found?))

(defn getStem [session name & {:keys [exception-if-not-found?] :or {exception-if-not-found? true}}]
    (. StemFinder findByName session name exception-if-not-found?))

(defn addGroup [session stemName extension displayExtension & args]
    (. (apply getStem session stemName args) addChildGroup extension displayExtension))

(defn delGroup [session name & args]
    (. (apply getGroup session name args) delete))

(defn delStem [session name & args]
    (. (apply getStem session name args) delete))

(defn _addStem [e d p]
    (. p addChildStem e d))

(defn addStem 
    ([session extension displayExtension] (_addStem extension displayExtension (. StemFinder findRootStem session)))
    ([session extension displayExtension parentStem] (_addStem extension displayExtension parentStem)))

(defn getGroups [session name]
    (. 
        (. GrouperQuery 
            createQuery 
            session 
            (new GroupNameFilter 
                name 
                (. StemFinder findRootStem session)
            )
        ) 
        getGroups))

(defn getMembers [session groupName & args]
    (. (apply getGroup session groupName args) getMembers))

(defn getStems [session name]
    (. 
        (. 
            GrouperQuery 
            createQuery 
            session 
            (new 
                StemNameAnyFilter 
                name 
                (. 
                    StemFinder 
                    findRootStem 
                    session
                )
            )
        ) getStems
    )) 
