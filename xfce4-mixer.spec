%define		xfce_version	4.12.0
Summary:	Volume control plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sterująca głośnością dla panelu Xfce
Name:		xfce4-mixer
Version:	4.11.0
Release:	10
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://archive.xfce.org/src/apps/xfce4-mixer/4.11/%{name}-%{version}.tar.bz2
# Source0-md5:	1b3753b91224867a3a2dfddda239c28d
Patch0:		git.patch
URL:		http://www.xfce.org/projects/xfce4-mixer/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.25
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfce4-panel-devel >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
Requires:	xfce4-panel >= %{xfce_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-mixer is the volume control plugin for the Xfce panel. Includes
a simple sound mixer.

%description -l pl.UTF-8
xfce4-mixer to wtyczka sterująca głośnością dla panelu Xfce. Zawiera
prosty mikser dźwięku.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libmixer.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xfce4-mixer
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmixer.so
%{_datadir}/xfce4/panel/plugins/mixer.desktop
%{_datadir}/xfce4/mixer
%{_desktopdir}/xfce4-mixer.desktop
%{_pixmapsdir}/xfce4-mixer
%{_mandir}/man1/xfce4-mixer.1*
