#!/usr/bin/python
import sys
sys.path+='.'
import llyn
import notation3
import term
import __builtin__
import diag

class BI_Python(term.HeavyBuiltIn,term.ReverseFunction):
    def __init__(self, resource, fragid):
        term.Term.__init__(self, resource.store)
        self.resource = resource
        self.fragid = fragid

    def evalSubj(self, obj, queue, bindings, proof, query):
        func=self.pythonCallFunc
        return self.store._fromPython(func(*obj.value()))

def newinternFrag(self, fragid, thetype):
    if fragid and self.uri.startswith('python://') and \
           not (self.fragments.has_key(fragid) \
                and hasattr(self.fragments[fragid],'pythonCallFunc')):
        imports=self.uri.split('python://',1)
        if len(imports)>1 and imports[1]:
            module=__import__(imports[1])
            func=getattr(module,fragid)
        else:
            func=getattr(__builtin__,fragid)
        self.fragments[fragid]=BI_Python(self,fragid)
        self.fragments[fragid].pythonCallFunc=func
        return self.fragments[fragid]
    else:
        return self._oldinternFrag(fragid, thetype)
        

# MonkeyPatch
if not hasattr(term.Symbol,'_oldinternFrag'):
    term.Symbol._oldinternFrag=term.Symbol.internFrag
    term.Symbol.internFrag=newinternFrag

store=llyn.RDFStore()

dest=store.newFormula()
filt=None
orig=store.load('teste.n3')
llyn.applyRules(orig,filt,dest)
orig.reopen()
llyn.think(orig)
outSink=notation3.ToN3(sys.stdout.write)
#store.dumpNested(orig,outSink)
store.dumpNested(dest,outSink)
#relation=store.intern((llyn.SYMBOL,"http://www.w3.org/2000/01/rdf-schema#commentnotEqualIgnoringCase"))
#match=f.statementsMatching(pred=relation)
#print 50
