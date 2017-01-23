# Usage: ENTRYPOINT application "argument", "argument", ..
# Remember: arguments are optional. They can be provided by CMD
#           or during the creation of a container. 
ENTRYPOINT echo

CMD "Hello docker!"
ENTRYPOINT echo  
MAINTAINER authors_name

RUN apt-get update


