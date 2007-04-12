Summary:        Event-based framework for internet applications
Name:           python-twisted
Version: 2.0.0
Release: %mkrel 3
License:        MIT
Group:          Development/Python
URL:            http://www.twistedmatrix.com/
BuildRoot:      %{_tmppath}/%{name}-buildroot
Requires: python-twisted-conch python-twisted-flow
Requires: python-twisted-lore python-twisted-mail python-twisted-names
Requires: python-twisted-pair python-twisted-runner python-twisted-web 
Requires: python-twisted-words python-twisted-xish
BuildArch: noarch

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
%defattr(-,root,root)
%doc README.mdv

%clean

