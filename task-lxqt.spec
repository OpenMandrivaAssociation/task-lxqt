Summary:	Metapackage for the LXQt (LXDE-Qt) desktop environment
Name:		task-lxqt
Version:	0.8.0
Release:	1
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://www.lxqt.org
# LXQt itself
Requires:	lxqt-about
Requires:	lxqt-common
Requires:	lxqt-config
Requires:	lxqt-config-randr
Requires:	lxqt-globalkeys
Requires:	lxqt-notificationd
Requires:	lxqt-openssh-askpass
Requires:	lxqt-panel
Requires:	lxqt-policykit
Requires:	lxqt-powermanagement
Requires:	lxqt-qtplugin
Requires:	lxqt-runner
Requires:	lxqt-session
Requires:	pcmanfm-qt
# Other stuff
Requires:	openbox
Suggests:	qterminal
Suggests:	trojita
Suggests:	qupzilla
Suggests:	calligra
Suggests:	clementine
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
all LXQt applications and libraries.

%files

#----------------------------------------------------------------------------

%prep

%build

%install

