
%define		_snap 20040806

Summary:	Volume control plugin for the XFce panel
Summary(pl):	Wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce
Name:		xfce4-mixer
Version:	4.2.0
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Applications/Sound
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	90c7df7024eb97dbd569caa1ec2b6b12
URL:		http://www.xfce.org/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	xfce4-panel-devel >= %{version}
Requires:	alsa-lib >= 0.9.0
Requires:	startup-notification >= 0.4
Requires:	xfce4-panel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-mixer is the volume control plugin for the XFce panel.
Includes a simple sound mixer.

%description -l pl
xfce4-mixer to wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce. Zawiera
prosty mikser d¼wiêku.

%prep
%setup -q -n %{name}

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
