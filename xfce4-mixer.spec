#
# TODO there's not a single word about startup-notification
# in configure.ac
Summary:	Volume control plugin for the XFce panel
Summary(pl):	Wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce
Name:		xfce4-mixer
Version:	4.1.99.1
Release:	1
License:	BSD
Group:		X11/Applications/Sound
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	935091fdd3860ea51db949fdec14cc75
URL:		http://www.xfce.org/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
#BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	xfce4-panel-devel >= 4.1.0
Requires:	alsa-lib >= 0.9.0
#Requires:	startup-notification >= 0.4
Requires:	xfce4-panel >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-mixer is the volume control plugin for the XFce panel.
Includes a simple sound mixer.

%description -l pl
xfce4-mixer to wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce. Zawiera
prosty mikser d¼wiêku.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/xfce4-mixer
%attr(755,root,root) %{_libdir}/xfce4/*/*.so*
%{_iconsdir}/hicolor/*/*/*

%{_desktopdir}/xfce-mixer-settings.desktop
