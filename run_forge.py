import os 
import subprocess

def init(project):
    # Create a forge project for this solidity code
    cmd = f'forge init {project} --no-commit'
    os.system(cmd)

def write(project, code):
    # Write the code to a file 
    codefile = open(f"./{project}/src/Counter.sol", "w")
    a = codefile.write(code)
    codefile.close()
    
def build(project):
    os.chdir(f"./{project}")
    
    # Build the project using foundry
    cmd = 'forge build'
    output = os.system(cmd)
    
    # Now let's get the error for use in a prompt
    try:
        so = subprocess.check_output(['forge', 'build'], stderr=subprocess.STDOUT) # , stderr=subprocess.STDOUT
        return 'build successful'
    except subprocess.CalledProcessError as err:
        return err
