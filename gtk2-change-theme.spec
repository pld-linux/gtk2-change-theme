%define		_rnam gtk-chtheme
Summary:	Gtk+2 theme changer
Summary(pl):	Program zmieniaj±cy motyw Gtk+2
Name:		gtk2-change-theme
Version:	0.3.1
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://plasmasturm.org/programs/gtk-chtheme/%{_rnam}-%{version}.tar.bz2
# Source0-md5:	f688053bf26dd6c4f1cd0bf2ee33de2a
URL:		http://plasmasturm.org/programs/gtk-chtheme/
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk+ 2.0 Change Theme provides an easy way to change Gtk+2 theme on
the fly.

%description -l pl
Gtk+ 2.0 Change Theme umo¿liwia w ³atwy sposób zmianê w locie motywu
Gtk+2.

%prep
%setup -q -n %{_rnam}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
