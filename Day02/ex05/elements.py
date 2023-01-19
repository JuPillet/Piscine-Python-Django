from elem import *

class Head( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "head", attr, content )

class Body( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "body", attr, content )

class Html( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "html", attr, content )

class Title( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "title", attr, content)

class Meta( Elem ):
	def __init__( self, attr={} ):
		super().__init__( "meta", attr, tag_type = 'simple' )

class Img( Elem ):
	def __init__( self, attr={} ):
		super().__init__( "img", attr, tag_type = 'simple' )

class Table( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "table", attr,content )

class Th( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "th", attr,content )

class Tr( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "tr", attr,content )

class Td( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "td", attr,content )

class Ul( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "ul", attr,content )

class Ol( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "ol", attr,content )

class Li( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "li", attr,content )

class H1( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "h1", attr,content )

class H2( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "h2", attr,content )

class P( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "p", attr,content )

class Div( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "div", attr,content )

class Span( Elem ):
	def __init__( self, content = None, attr={} ):
		super().__init__( "span", attr,content )

class Img( Elem ):
	def __init__( self, attr={} ):
		super().__init__( "img", attr, tag_type = 'simple' )

class Hr( Elem ):
	def __init__( self, attr={} ):
		super().__init__( "hr", attr, tag_type = 'simple' )

class Br( Elem ):
	def __init__( self, attr={} ):
		super().__init__( "br", attr, tag_type = 'simple' )

if __name__ == '__main__':
	title = Title( Text ( "Hello ground!" ) )
	head = Head( [title] )

	h1 = H1( Text ( "Oh no, not again!" ) )
	img = Img( dict( {"src": "http://i.imgur.com/pfp3T.jpg"} ) )
#	img = Elem("img", {"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type = 'simple' )
	body = Body( [h1, img] )

	html = Html( [head, body] )
	print( html )