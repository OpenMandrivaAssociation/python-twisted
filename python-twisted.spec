%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:	Event-based framework for internet applications
Name:		python-twisted
Version:	25.5.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://twistedmatrix.com/
Source0:	https://files.pythonhosted.org/packages/source/t/twisted/twisted-%{version}.tar.gz
BuildRequires:	python3dist(incremental) >= 16.10.1
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(zope.interface)
BuildRequires:	python-pkg-resources
BuildRequires:	tiff-devel
Requires:	python3dist(pycryptodome)
Requires:	python-OpenSSL
Requires:	python3dist(zope.interface)
BuildArch:	noarch

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

%prep
%autosetup -p1 -n twisted-%{version}

%build
%py_build

%install
%py_install

# No need to install those C source files
find %{buildroot} -name "*.c" -o -name "*.h" -delete

install -d %{buildroot}%{_mandir}/man1
install -m 644 docs/*/man/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(0644,root,root,0755)
%license LICENSE
%{_bindir}/*
%{py_sitedir}/twisted
%{py_sitedir}/*.egg-info
%{_mandir}/man1/*

%files doc
# ChangeLog.Old is here as this is big
%doc docs/
