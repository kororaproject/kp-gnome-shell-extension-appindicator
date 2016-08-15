%global uuid appindicatorsupport@rgcjonas.gmail.com
%global gittag b8e5545289e4737f6df27a38ad91042ec3ae3450
%global gitshorttag b8e5545

Name:		gnome-shell-extension-appindicator
Version:	3.20
Release:	1.git%{gitshorttag}%{?dist}
Summary:	Show indicator icons in the panel

License:	GPLv2+
URL:		https://github.com/rgcjonas/gnome-shell-extension-appindicator
Source0:	https://github.com/rgcjonas/gnome-shell-extension-appindicator/archive/%{gittag}.tar.gz
Patch0:		make_install.patch
Patch1:		gnome-shell-3.20.patch

Requires: gnome-shell >= 3.16

%description
This extension integrates Ubuntu AppIndicators and
KStatusNotifierItems (KDE's blessed successor of the systray)
into GNOME Shell.


%prep
%setup -q -n gnome-shell-extension-appindicator-%{gittag}
%patch0 -p1
%patch1 -p1


%install
make install INSTALLBASE=%{buildroot}%{_datadir}/gnome-shell/extensions/


%files
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Mon Aug 15 2016 Michael Donnelly <mike@donnellyonline.com> - 3.20-1.gitb8e5545
- Initial package
