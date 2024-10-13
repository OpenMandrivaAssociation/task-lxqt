Summary:	Metapackage for the LXQt (LXDE-Qt) desktop environment
Name:		task-lxqt
Version:	2.0.0
Release:	2
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://www.lxqt.org
# LXQt itself
Requires:	lxqt-about
Requires:	lxqt-admin
Requires:	lxqt-config
Requires:	lxqt-globalkeys
Obsoletes:	lxqt-l10n < %{EVRD}
Requires:	lxqt-notificationd
Requires:	lxqt-openssh-askpass
Requires:	lxqt-panel >= %{version}
Requires:	lxqt-policykit
Requires:	lxqt-powermanagement
Requires:	lxqt-qtplugin
Requires:	lxqt-runner
Requires:	lxqt-session
Requires:	lxqt-sudo
Requires:	lxqt-themes
Requires:	lxqt-archiver
Requires:	xdg-desktop-portal-lxqt
Requires:	pcmanfm-qt >= %{version}
# Other stuff
Requires:	xdg-user-dirs
Requires:	distro-release-desktop
Requires:	distro-release-desktop-LXQt
Requires:	distro-release-theme
Requires:	lxmenu-data
Requires:	menu-cache
Suggests:	notepadqq
Suggests:	lximage-qt
Requires:	qterminal
Requires:	pavucontrol-qt
Requires:	screengrab
Suggests:	trojita
Requires:	falkon
Requires:	qps >= 1.10.18
Suggests:	calligra
Suggests:	elisa
Suggests:	xscreensaver
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
all LXQt applications and libraries.

%files

#----------------------------------------------------------------------------

%prep

%build

%install
