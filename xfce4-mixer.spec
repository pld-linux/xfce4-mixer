Summary:	Volume control plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sterująca głośnością dla panelu Xfce
Name:		xfce4-mixer
Version:	4.4.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	0d7b402acaffdb5d8b292f2ce3ea1441
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= 4.4.0.1
BuildRequires:	xfce4-panel-devel >= %{version}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	alsa-lib >= 1.0.11
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
%patch0 -p1

mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--with-sound=alsa

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/xfce4-mixer
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
# why no -avoid-version?
%attr(755,root,root) %{_libdir}/xfce4/modules/lib*.so*
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-mixer-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-mixer.desktop
%{_iconsdir}/hicolor/*/*/*

%{_desktopdir}/xfce-mixer-settings.desktop
