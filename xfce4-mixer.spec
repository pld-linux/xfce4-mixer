Summary:	Volume control plugin for the XFce panel
Summary(pl):	Wtyczka steruj±ca g³o¶no¶ci± dla panelu XFce
Name:		xfce4-mixer
Version:	4.0.5
Release:	1
License:	BSD
Group:		X11/Applications/Sound
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	01d5e15d3740b87a8860557af07d5fbb
URL:		http://www.xfce.org/
BuildRequires:	automake
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
cp -f /usr/share/automake/config.sub .
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
