#!/usr/bin/env python
"""sparql_tokens_table - For use with sparql_tokens.py."""
# Automatically generated by sparql_tokens.py

import re

tokens = [u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_BASE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_PREFIX',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_SELECT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_DISTINCT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_TIMES',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_CONSTRUCT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_DESCRIBE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_ASK',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_FROM',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_NAMED',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_WHERE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_ORDER',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_BY',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_ASC',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_DESC',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_LIMIT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_OFFSET',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_OPTIONAL',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_GRAPH',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_UNION',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_FILTER',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_LBRACKET',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_LPAREN',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_RBRACKET',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_RPAREN',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_SEMI',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_COMMA',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_a',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_OR',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_AND',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_EQUAL',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_NEQUAL',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_LT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_GT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_LE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_GE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_PLUS',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_MINUS',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_DIVIDE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_NOT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_STR',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_LANG',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_DATATYPE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_BOUND',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_isURI',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_isBLANK',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_isLITERAL',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_REGEX',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#GT_DTYPE',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_true',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#IT_false',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#QuotedIRIref',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#QNAME_NS',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#QNAME',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#BNODE_LABEL',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#VAR1',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#VAR2',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#LANGTAG',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#INTEGER',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#FLOATING_POINT',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL1',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL2',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL_LONG1',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL_LONG2',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#Dot',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#OpenCurly',
 u'http://www.w3.org/2000/10/swap/grammar/sparql#CloseCurly',
 u'http://www.w3.org/2000/10/swap/grammar/bnf#eof',
 u'http://www.w3.org/2000/10/swap/grammar/bnf#PASSED_TOKENS']
regexps = {
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DATATYPE': u'DATATYPE', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_TIMES': u'\\*', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#CloseCurly': u'\\}', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_REGEX': re.compile(u'REGEX', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#LANGTAG': re.compile(u'@[a-zA-Z]+(?:-[a-zA-Z0-9]+)*', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_COMMA': u',', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_CONSTRUCT': u'CONSTRUCT', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_DTYPE': re.compile(u'\\^\\^', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_WHERE': u'WHERE', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#INTEGER': u'[0-9]+', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#INTEGER': re.compile(u'[0-9]+', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_isURI': u'isURI', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_OPTIONAL': u'OPTIONAL', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#VAR2': re.compile(u'\\$[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_MINUS': u'-', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DISTINCT': re.compile(u'DISTINCT', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_BASE': re.compile(u'BASE', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_LIMIT': re.compile(u'LIMIT', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_NEQUAL': u'!=', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL_LONG1': u"'''(?:(?:[^'\\\\])|(?:(?:(?:\\\\[^\\r\\n]))|(?:(?:(?:'[^']))|(?:(?:''[^'])))))*'''", 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL_LONG2': u'"""(?:(?:[^"\\\\])|(?:(?:(?:\\\\[^\\r\\n]))|(?:(?:(?:"[^"]))|(?:(?:""[^"])))))*"""', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_STR': u'STR', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL1': re.compile(u"'(?:(?:[^'\\\\\\n\\r])|(?:(?:\\\\[^\\r\\n])))*'", re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_PREFIX': re.compile(u'PREFIX', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_GT': re.compile(u'>', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_NOT': re.compile(u'!', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#BNODE_LABEL': u'_:[_A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL2': re.compile(u'"(?:(?:[^"\\\\\\n\\r])|(?:(?:\\\\[^\\r\\n])))*"', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_GRAPH': u'GRAPH', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DESCRIBE': u'DESCRIBE', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_DTYPE': u'\\^\\^', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_SEMI': u';', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_GE': re.compile(u'>=', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_OR': re.compile(u'\\|\\|', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL_LONG2': re.compile(u'"""(?:(?:[^"\\\\])|(?:(?:(?:\\\\[^\\r\\n]))|(?:(?:(?:"[^"]))|(?:(?:""[^"])))))*"""', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_false': u'false', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_ASK': u'ASK', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_CONSTRUCT': re.compile(u'CONSTRUCT', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DESCRIBE': re.compile(u'DESCRIBE', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#QNAME': re.compile(u'(?:[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*)?:(?:[_A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*)?', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_true': u'true', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_RBRACKET': re.compile(u'\\]', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LBRACKET': re.compile(u'\\[', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_a': u'a', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_FILTER': re.compile(u'FILTER', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#OpenCurly': re.compile(u'\\{', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_BY': re.compile(u'BY', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_AND': re.compile(u'&&', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_OFFSET': u'OFFSET', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DISTINCT': u'DISTINCT', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_BASE': u'BASE', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_isURI': re.compile(u'isURI', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_PLUS': re.compile(u'\\+', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_MINUS': re.compile(u'-', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_EQUAL': u'=', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_NAMED': re.compile(u'NAMED', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_LANG': u'LANG', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_DIVIDE': u'/', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_isBLANK': u'isBLANK', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_LIMIT': u'LIMIT', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_FILTER': u'FILTER', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_NOT': u'!', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DESC': u'DESC', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_AND': u'&&', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_OPTIONAL': re.compile(u'OPTIONAL', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LBRACKET': u'\\[', 
   u'c_http://www.w3.org/2000/10/swap/grammar/bnf#PASSED_TOKENS': re.compile(u'(?:(?:(?:\\t)|(?:(?:\\n)|(?:(?:\\r)|(?:(?:[ ])|(?:(?:\xa0)|(?:(?:[\u2000-\u200b])|(?:(?:\u202f)|(?:(?:\u205f)|(?:\u3000)))))))))+)|(?:#[^\\n]*\\n)', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#FLOATING_POINT': u'(?:[0-9]+\\.[0-9]*(?:[eE][\\+-]?[0-9]+)?)|(?:(?:\\.[0-9]+(?:[eE][\\+-]?[0-9]+)?)|(?:[0-9]+(?:[eE][\\+-]?[0-9]+)))', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#BNODE_LABEL': re.compile(u'_:[_A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_SELECT': u'SELECT', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_PREFIX': u'PREFIX', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_isLITERAL': re.compile(u'isLITERAL', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#QNAME': u'(?:[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*)?:(?:[_A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*)?', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_BOUND': re.compile(u'BOUND', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#CloseCurly': re.compile(u'\\}', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_UNION': re.compile(u'UNION', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_COMMA': re.compile(u',', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_WHERE': re.compile(u'WHERE', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#QNAME_NS': re.compile(u'(?:[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*)?:', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#FLOATING_POINT': re.compile(u'(?:[0-9]+\\.[0-9]*(?:[eE][\\+-]?[0-9]+)?)|(?:(?:\\.[0-9]+(?:[eE][\\+-]?[0-9]+)?)|(?:[0-9]+(?:[eE][\\+-]?[0-9]+)))', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_ASK': re.compile(u'ASK', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LPAREN': u'\\(', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_ASC': re.compile(u'ASC', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_REGEX': u'REGEX', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#VAR1': u'\\?[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#VAR2': u'\\$[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_ASC': u'ASC', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LT': u'<', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_PLUS': u'\\+', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_UNION': u'UNION', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_EQUAL': re.compile(u'=', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#VAR1': re.compile(u'\\?[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_FROM': re.compile(u'FROM', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LE': u'<=', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_OFFSET': re.compile(u'OFFSET', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_RPAREN': u'\\)', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_RPAREN': re.compile(u'\\)', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_NEQUAL': re.compile(u'!=', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_true': re.compile(u'true', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_BOUND': u'BOUND', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_SELECT': re.compile(u'SELECT', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DATATYPE': re.compile(u'DATATYPE', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_ORDER': re.compile(u'ORDER', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/bnf#PASSED_TOKENS': u'(?:(?:(?:\\t)|(?:(?:\\n)|(?:(?:\\r)|(?:(?:[ ])|(?:(?:\xa0)|(?:(?:[\u2000-\u200b])|(?:(?:\u202f)|(?:(?:\u205f)|(?:\u3000)))))))))+)|(?:#[^\\n]*\\n)', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_a': re.compile(u'a', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_DIVIDE': re.compile(u'/', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_DESC': re.compile(u'DESC', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_ORDER': u'ORDER', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#QNAME_NS': u'(?:[A-Za-z\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff][_\\-\\.0-9A-Za-z\xb7\xc0-\xd6\xd8-\xf6\xf8-\u02ff\u0300-\u036f\u0370-\u037d\u037f-\u1fff\u200c-\u200d\u203f-\u2040\u2070-\u218f\u2c00-\u2fef\u3001-\ud7ff\uf900-\ufdcf\ufdf0-\ufffd\U00010000-\U000effff]*)?:', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_RBRACKET': u'\\]', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_OR': u'\\|\\|', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LE': re.compile(u'<=', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_LANG': re.compile(u'LANG', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_GRAPH': re.compile(u'GRAPH', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_SEMI': re.compile(u';', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#QuotedIRIref': re.compile(u'<[^> ]*>', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LT': re.compile(u'<', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL_LONG1': re.compile(u"'''(?:(?:[^'\\\\])|(?:(?:(?:\\\\[^\\r\\n]))|(?:(?:(?:'[^']))|(?:(?:''[^'])))))*'''", re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_FROM': u'FROM', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_false': re.compile(u'false', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#QuotedIRIref': u'<[^> ]*>', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#Dot': u'\\.', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_GE': u'>=', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#LANGTAG': u'@[a-zA-Z]+(?:-[a-zA-Z0-9]+)*', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_STR': re.compile(u'STR', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_LPAREN': re.compile(u'\\(', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_NAMED': u'NAMED', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#GT_GT': u'>', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL2': u'"(?:(?:[^"\\\\\\n\\r])|(?:(?:\\\\[^\\r\\n])))*"', 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#STRING_LITERAL1': u"'(?:(?:[^'\\\\\\n\\r])|(?:(?:\\\\[^\\r\\n])))*'", 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#OpenCurly': u'\\{', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#Dot': re.compile(u'\\.', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_isLITERAL': u'isLITERAL', 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#GT_TIMES': re.compile(u'\\*', re.I), 
   u'c_http://www.w3.org/2000/10/swap/grammar/sparql#IT_isBLANK': re.compile(u'isBLANK', re.I), 
   u't_http://www.w3.org/2000/10/swap/grammar/sparql#IT_BY': u'BY', 
}

if __name__=="__main__": 
   print __doc__
