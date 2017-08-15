from nose.tools import *
from ex48 import parser
from ex48 import lexicon
def test():
	assert_equal(parser.peek(lexicon.scan('go kill the princess')),'verb')
	assert_equal(parser.match(lexicon.scan('go kill the princess'),'verb'),('verb','go'))
	assert_equal(parser.skip(lexicon.scan('go kill the princess'),'verb'),None)
	assert_equal(parser.parse_verb(lexicon.scan('go kill the princess')),('verb','go'))
	assert_raises(parser.ParserError,parser.parse_verb,('noun','princess'))
	assert_equal(parser.parse_object(lexicon.scan('the princess')),('noun','princess'))
	assert_equal(parser.parse_object(lexicon.scan('the north')),('direction','north'))
	assert_raises(parser.ParserError,parser.parse_object,lexicon.scan('go kill the princess'))
	subj='bear'
	assert_equal(parser.parse_sentence(lexicon.scan('the bear eat the princess')).subject,subj)
	ver='eat'
	assert_equal(parser.parse_sentence(lexicon.scan('the bear eat the princess')).verb,ver)
	obj='princess'
	assert_equal(parser.parse_sentence(lexicon.scan('the bear eat the princess')).object,obj)