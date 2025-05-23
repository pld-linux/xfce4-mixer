%define		xfce_version	4.16.0
Summary:	Volume control plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sterująca głośnością dla panelu Xfce
Name:		xfce4-mixer
Version:	4.20.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	https://archive.xfce.org/src/apps/xfce4-mixer/4.20/%{name}-%{version}.tar.xz
# Source0-md5:	84335d6b89cc9bb19ba8d5da74df6076
URL:		https://www.xfce.org/projects/xfce4-mixer/
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	keybinder3-devel >= 0.3
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel >= 0.9.19
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
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

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/xfce4-mixer
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmixer.so
%{_datadir}/xfce4/panel/plugins/mixer.desktop
%{_datadir}/xfce4/mixer
%{_desktopdir}/xfce4-mixer.desktop
%{_mandir}/man1/xfce4-mixer.1*
