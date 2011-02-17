Summary:	Volume control plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sterująca głośnością dla panelu Xfce
Name:		xfce4-mixer
Version:	4.6.1
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a99e2455445480ef5081fe69454a46fc
URL:		http://www.xfce.org/projects/xfce4-mixer/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.14
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	xfconf-devel >= %{version}
Requires:	xfce4-panel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-mixer is the volume control plugin for the Xfce panel. Includes
a simple sound mixer.

%description -l pl.UTF-8
xfce4-mixer to wtyczka sterująca głośnością dla panelu Xfce. Zawiera
prosty mikser dźwięku.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-mixer
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-mixer-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-mixer-plugin.desktop
%{_datadir}/xfce4-mixer
%{_desktopdir}/xfce4-mixer.desktop
%{_pixmapsdir}/xfce4-mixer
