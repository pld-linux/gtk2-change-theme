%define		_rnam gtk-chtheme
Summary:	Gtk+2 theme changer
Summary(hu.UTF-8):	Gtk+2 theme változtató
Summary(pl.UTF-8):	Program zmieniający motyw Gtk+2
Name:		gtk2-change-theme
Version:	0.3.1
Release:	4
License:	GPL v2
Group:		Applications
Source0:	http://plasmasturm.org/programs/gtk-chtheme/%{_rnam}-%{version}.tar.bz2
# Source0-md5:	f688053bf26dd6c4f1cd0bf2ee33de2a
Source1:	gtk-chtheme.desktop
Source2:	gtk-chtheme.xpm
Patch0:		gtk-chtheme-build-fix.patch
Patch1:		gtk-chtheme-new-api.patch
Patch2:		gtk-chtheme-nostrip.patch
URL:		http://plasmasturm.org/programs/gtk-chtheme/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk+ 2.0 Change Theme provides an easy way to change Gtk+2 theme on
the fly.

%description -l hu.UTF-8
Gtk+ 2.0 Change Theme egy egyszerű utat biztosít, hogy a Gtk+2 témát
változtasd meg röptében.

%description -l pl.UTF-8
Gtk+ 2.0 Change Theme umożliwia w łatwy sposób zmianę w locie motywu
Gtk+2.

%prep
%setup -q -n %{_rnam}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
