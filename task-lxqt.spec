Summary:	Metapackage for the LXQt (LXDE-Qt) desktop environment
Name:		task-lxqt
Version:	0.13.0
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://www.lxqt.org
# LXQt itself
Requires:	lxqt-about
Requires:	lxqt-admin
Requires:	lxqt-config >= %{version}
Requires:	lxqt-globalkeys
Requires:	lxqt-l10n
Requires:	lxqt-notificationd
Requires:	lxqt-openssh-askpass
Requires:	lxqt-panel >= %{version}
Requires:	lxqt-policykit
Requires:	lxqt-powermanagement
Requires:	lxqt-qtplugin
Requires:	lxqt-runner
Requires:	lxqt-session >= %{version}
Requires:	lxqt-sudo
Requires:	lxqt-themes
Requires:	pcmanfm-qt >= %{version}
# Other stuff
Requires:	xdg-user-dirs
Requires:	desktop-common-data
Requires:	distro-theme-OpenMandriva
Requires:	lxmenu-data
Requires:	menu-cache
Requires:	breeze
Requires:	breeze-icons
Requires:	openbox
Requires:	obconf-qt
Suggests:	notepadqq
Suggests:	lximage-qt
Requires:	qterminal
Requires:	pavucontrol-qt
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
