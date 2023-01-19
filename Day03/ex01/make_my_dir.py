from local_lib.path import *

def	make_my_dir():
	Path( "./my_folder" ).mkdir_p()
	Path( "./my_folder/test" ).touch().write_text( "test" )

if __name__ == "__main__":
	make_my_dir()
