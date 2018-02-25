def environments():
		import os
		envs=[]
		envdir = os.path.expanduser("~")
		envdir = os.path.join( envdir, "anaconda3", "envs" )
		if not os.path.exists(envdir):
			raise Exception("You must first set up a personal anaconda environment")
		for o in os.scandir( envdir ):
			if o.is_dir():
				envs.append(o)
		return envs

def activate(env):
	import os
	import sys
	envdir = os.path.expanduser("~")
	envdir = os.path.join( envdir, "anaconda3", "envs", env )
	if( not os.path.exists(envdir) ):
		raise Exception("Environment [%s] not found" % ( env,) )

	sys.path  = [ 
			os.path.join( envdir, "lib", "python3.6" ),
			os.path.join( envdir, "lib", "python3.6", "site-packages" ) 
		] + sys.path

	os.environ["PATH"] =  os.path.join( envdir, "bin" ) + ":" + os.environ["PATH"]
	print("Environment %s activated" % (env, ) ) 	
	

	
