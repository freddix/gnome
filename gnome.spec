Summary:	GNOME desktop
Name:		gnome
Version:	3.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Requires:	accountsservice
Requires:	baobab
Requires:	brasero
Requires:	browser-plugin-gnome-shell
Requires:	browser-plugin-totem
Requires:	caribou
Requires:	cheese
Requires:	colord
Requires:	dconf
Requires:	dconf-editor
Requires:	empathy
Requires:	eog
Requires:	epiphany
Requires:	epiphany-extensions
Requires:	evince
Requires:	evolution
Requires:	file-roller
Requires:	folks
Requires:	fonts-OTF-Cantarell
Requires:	fonts-OTF-Cantarell
Requires:	gcalctool
Requires:	gdm
Requires:	gedit
Requires:	gjs
Requires:	glib-networking
Requires:	gnome-backgrounds
Requires:	gnome-bluetooth
Requires:	gnome-color-manager
Requires:	gnome-contacts
Requires:	gnome-contacts-shell-search-provider
Requires:	gnome-control-center
Requires:	gnome-desktop
Requires:	gnome-dictionary
Requires:	gnome-disk-utility
Requires:	gnome-documents
Requires:	gnome-documents-shell-search-provider
Requires:	gnome-font-viewer
Requires:	gnome-icon-theme
Requires:	gnome-keyring
Requires:	gnome-menus
Requires:	gnome-online-accounts
Requires:	gnome-panel
Requires:	gnome-power-manager
Requires:	gnome-screensaver
Requires:	gnome-screenshot
Requires:	gnome-session
Requires:	gnome-settings-daemon
Requires:	gnome-shell
Requires:	gnome-system-log
Requires:	gnome-terminal
Requires:	gnome-themes-standard
Requires:	gnome-tweak-tool
Requires:	gnome-user-docs
Requires:	grilo-plugins
Requires:	gsettings-desktop-schemas
Requires:	gucharmap
Requires:	gvfs
Requires:	gvfs-archive
Requires:	gvfs-cdio
Requires:	gvfs-dnssd
Requires:	gvfs-fuse
Requires:	gvfs-gphoto2
Requires:	gvfs-smb
Requires:	libcanberra-runtime
Requires:	libgnomekbd-runtime
Requires:	libproxy-gnome3
Requires:	libsocialweb
Requires:	metacity
Requires:	mutter
Requires:	nautilus
Requires:	nautilus-extension-brasero
Requires:	nautilus-extension-evince
Requires:	nautilus-extension-file-roller
Requires:	nautilus-extension-totem
Requires:	nautilus-extension-tracker
Requires:	nautilus-sendto-burn
Requires:	nautilus-sendto-empathy
Requires:	nautilus-shell-search-provider
Requires:	notification-daemon
Requires:	notification-daemon
Requires:	polkit-gnome
Requires:	pulseaudio
Requires:	seahorse
Requires:	shared-color-profiles
Requires:	simple-scan
Requires:	sound-juicer
Requires:	sushi
Requires:	telepathy-service
Requires:	totem
Requires:	totem-plugins
Requires:	tracker
Requires:	yelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
GNOME desktop.

%prep
%build
%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

