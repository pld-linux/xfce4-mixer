Summary:	Volume control plugin for the XFce panel
Summary(pl):	Wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce
Name:		xfce4-mixer
Version:	4.0.0
Release:	1
License:	BSD
Group:		X11/Applications/Sound
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	1c5038b557f144b3230b1898b2c96889
URL:		http://www.xfce.org/
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	xfce4-panel-devel >= %{version}
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
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
