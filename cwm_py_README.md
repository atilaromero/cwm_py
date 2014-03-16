cwm_py
======

CWM (Closed World Machine) extension. Adds support to "python://" URIs, as a way to call arbitrary python functions as if they were built-ins.

When a URI like <python://mymodule#myfunction> is found in a rule,
it imports the module and uses the function as a built-in.

Example:
teste.n3:

    :c :input ("All these worlds are yours except europa") .

    {?x :input (?y).
        ?z1b <python://#unicode.upper> (?y) .
        ?z2 <python://#unicode.rsplit> ( ?z1b " " 2 ) .
    }=>{
        ?x :output ?z2.
    }.

cwm_py --think --data teste.n3

     @prefix : <#> .

    :c     :input  (
        "All these worlds are yours except europa" );
         :output  (
        "ALL THESE WORLDS ARE YOURS"
        "EXCEPT"
        "EUROPA" ) .

The equivalent python code would be y.upper.rsplit(" ", 2)

Another example, a little more useful, would be to put a custom function in a file, like teste.py
and use that function as a built-in:

teste.py:

    import subprocess
    def callExt(arglist):
        return subprocess.Popen(arglist,stdout=subprocess.PIPE).communicate()[0]

teste.n3:

    @prefix teste: <python://teste#>.
    :d :input ().
    {?x :input ().
        ?z1 teste:callExt (("ls" "-l" "../")) .
    }=>{
        ?x :output ?z1.
    }.

cwm_py --think --data teste.n3

     @prefix : <#> .

    :d     :input ();
         :output """total 16
    drwxrwxr-x  2 atila.alr atila.alr  4096 Mai  9 08:52 CVS
    drwxrwxr-x 26 atila.alr atila.alr 12288 Mai 17 17:54 swap
    """ .

To "install" the extension, it should suffice to put cwm_py in the cwm folder.
Then, to use it, call cwm_py like you would call cwm.
Internally, all the extension does is to monkeypatch an internal function (so it understand "python://" URI)
and then pass the ball to cwm.

Sure, the idea of call any function is not very production-security-friendly, but it may come handy in a controlled environment.
