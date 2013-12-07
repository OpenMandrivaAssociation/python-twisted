Summary:	Event-based framework for internet applications
Name:		python-twisted
Version:	13.0.0
Release:	4
License:	MIT
Group:		Development/Python
Url:		http://www.twistedmatrix.com/
BuildArch:	noarch
Requires:	python-twisted-conch 
Requires:	python-twisted-lore 
Requires:	python-twisted-mail 
Requires:	python-twisted-names  
Requires:	python-twisted-news 
Requires:	python-twisted-runner 
Requires:	python-twisted-web 
Requires:	python-twisted-words 
# add the pythonegg provides manually as this is a meta package, so the rpm auto-provides
# scripts won't work here
Provides:	pythonegg(twisted)

%description
Twisted is a framework, written in Python, for writing networked
applications. It includes implementations of a number of commonly used
network services such as a web server, an IRC chat server, a mail
server, a relational database interface and an object broker. Developers
can build applications using all of these services as well as custom
services that they write themselves. Twisted also includes a user
authentication system that controls access to services and provides
services with user context information to implement their own security
models.

This package is just a empty rpm with requires on all twisted sub-modules,
in order to allows smooth upgrade and easy installation of the whole
framework.

%build
cat >  README.mdv <<EOF
This package is just a empty rpm with requires on all twisted sub-modules,
in order to allows smooth upgrade and easy installation of the whole
framework.
EOF

%files
%doc README.mdv
