Summary:	Volume control plugin for the XFce 4 panel
Summary(pl):	Wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce 4
Name:		xfce4-mixer
Version:	3.99.3
Release:	1
License:	BSD
Group:		X11/Applications/Sound
Source0:	http://www.xfce.org/archive/xfce4-rc3/src/%{name}-%{version}.tar.gz
# Source0-md5:	c9c5e7fb04b57e743005f5e2660ff58f
URL:		http://www.xfce.org/
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	xfce4-panel-devel >= 3.99.3
Requires:	startup-notification >= 0.4
Requires:	xfce4-panel >= 3.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-mixer is the volume control plugin for the XFce 4 panel.
Includes a simple sound mixer.

%description -l pl
xfce4-mixer to wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce 4. Zawiera
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
