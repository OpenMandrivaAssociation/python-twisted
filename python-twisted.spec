%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:	Event-based framework for internet applications
Name:		python-twisted
Version:	18.7.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://twistedmatrix.com/
Source0:	https://twistedmatrix.com/Releases/Twisted/%{mainver}/Twisted-%{version}.tar.bz2
Patch1:	TwistedCore-13.0.0-sagemath.patch
Patch2: Twisted-18.4.0-python-3.7.patch
BuildRequires:	python3egg(incremental) >= 16.10.1
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(zope.interface)
BuildRequires:	python-pkg-resources
BuildRequires:	pkgconfig(python)
BuildRequires:	pythonegg(zope.interface)
BuildRequires:	python2-pkg-resources
Requires:	pycrypto
Requires:	python-OpenSSL
Requires:	python3egg(zope.interface)

%rename %{name}-core
%rename %{name}-web
%rename %{name}-names

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

%package  doc
Group:		Development/Python
Summary:	%{name} documentation

%description  doc
Documentation files for %name.
This consist mainly of the twist api for the core component.

%package -n python2-twisted
Summary:	Event-based framework for internet applications for Python 2.x
Group:		Development/Python

%description -n python2-twisted
Twisted is a framework, written in Python 2, for writing networked
applications. It includes implementations of a number of commonly used
network services such as a web server, an IRC chat server, a mail
server, a relational database interface and an object broker. Developers
can build applications using all of these services as well as custom
services that they write themselves. Twisted also includes a user
authentication system that controls access to services and provides
services with user context information to implement their own security
models.

%prep
%setup -qn Twisted-%{version}
%apply_patches

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

# No need to install those C source files
find %{buildroot} -name "*.c" -o -name "*.h" -delete

install -d %{buildroot}%{_mandir}/man1
install -m 644 docs/*/man/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(0644,root,root,0755)
%doc python3/LICENSE
%{py_platsitedir}/twisted
%{py_platsitedir}/*.egg-info

%files -n python2-twisted
%{py2_platsitedir}/twisted
%{py2_platsitedir}/*.egg-info
%{_bindir}/*
%{_mandir}/man1/*

%files doc
# ChangeLog.Old is here as this is big
%doc python3/docs/
