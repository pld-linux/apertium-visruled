Summary:	Apertium Visual Rule Editor
Summary(pl.UTF-8):	Graficzny edytor reguł Apertium
Name:		apertium-visruled
Version:	0.0.2
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/%{name}-%{version}.tar.gz
# Source0-md5:	e92631a8a2292b20005433af75d9f108
Patch0:		%{name}-paths.patch
URL:		http://apertium.sourceforge.net/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtXml-devel >= 4
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apertium Visual Rule Editor.

%description -l pl.UTF-8
Graficzny edytor reguł Apertium.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 \
	BINDIR=%{_bindir} \
	DATADIR=%{_datadir} \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog 
%attr(755,root,root) %{_bindir}/apertium-visruled
%{_datadir}/apertium-visruled
%{_desktopdir}/apertium-visruled.desktop
%{_pixmapsdir}/apertium-visruled.png
