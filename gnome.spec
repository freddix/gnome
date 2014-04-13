Summary:	GNOME desktop
Name:		gnome
Version:	3.12.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Requires:	accountsservice >= 0.6.37
Requires:	baobab >= 3.12.0
Requires:	bijiben >= 3.12.0
Requires:	brasero
Requires:	browser-plugin-gnome-shell >= 3.12.0
Requires:	browser-plugin-totem >= 3.12.0
Requires:	caribou
Requires:	cheese >= 3.12.0
Requires:	colord
Requires:	dconf >= 0.20.0
Requires:	dconf-editor
Requires:	empathy >= 3.12.0
Requires:	eog >= 3.12.0
Requires:	epiphany >= 3.12.0
Requires:	evince >= 3.12.0
Requires:	evolution >= 3.12.0
Requires:	file-roller >= 3.12.0
Requires:	folks
Requires:	fonts-OTF-Cantarell
Requires:	gnome-calculator >= 3.12.0
Requires:	gdk-pixbuf-rsvg >= 2.30.7
Requires:	gdm >= 3.12.0
Requires:	gedit >= 3.12.0
Requires:	gedit-plugin-zeitgeist
Requires:	gedit-plugins-python3
Requires:	gjs >= 1.40.0
Requires:	glib-networking >= 2.40.0
Requires:	gnome-backgrounds >= 3.12.0
Requires:	gnome-bluetooth >= 3.12.0
Requires:	gnome-clocks >= 3.12.0
Requires:	gnome-color-manager >= 3.12.0
Requires:	gnome-contacts >= 3.12.0
Requires:	gnome-contacts-shell-search-provider
Requires:	gnome-control-center >= 3.12.0
Requires:	gnome-desktop >= 3.12.0
Requires:	gnome-dictionary
Requires:	gnome-disk-utility
Requires:	gnome-documents >= 3.12.0
Requires:	gnome-documents-shell-search-provider
Requires:	gnome-font-viewer >= 3.12.0
Requires:	gnome-icon-theme >= 3.12.0
Requires:	gnome-keyring >= 3.12.0
Requires:	gnome-maps >= 3.12.0
Requires:	gnome-menus >= 3.10.0
Requires:	gnome-music >= 3.12.0
Requires:	gnome-online-accounts >= 3.12.0
Requires:	gnome-photos >= 3.12.0
Requires:	gnome-power-manager >= 3.12.0
Requires:	gnome-screenshot >= 3.12.0
Requires:	gnome-session >= 3.12.0
Requires:	gnome-settings-daemon >= 3.12.0
Requires:	gnome-shell >= 3.12.0
Requires:	gnome-shell-extensions >= 3.12.0
Requires:	gnome-logs
Requires:	gnome-terminal >= 3.12.0
Requires:	gnome-terminal-shell-search-provider
Requires:	gnome-themes-standard >= 3.12.0
Requires:	gnome-tweak-tool >= 3.12.0
Requires:	gnome-user-docs  >= 3.12.0
Requires:	gnome-weather >= 3.12.0
Requires:	grilo-plugins
Requires:	gsettings-desktop-schemas >= 3.12.0
Requires:	gucharmap >= 3.12.0
Requires:	gvfs >= 1.20.0
Requires:	gvfs-archive
Requires:	gvfs-backend-recent-files
Requires:	gvfs-cdio
Requires:	gvfs-dnssd
Requires:	gvfs-fuse
Requires:	gvfs-gnome-online-accounts
Requires:	gvfs-mtp
Requires:	gvfs-smb
Requires:	libcanberra-runtime
Requires:	libgnomekbd-runtime
Requires:	libproxy-gnome3
Requires:	libsocialweb
Requires:	mutter >= 3.12.0
Requires:	nautilus >= 3.12.0
Requires:	nautilus-extension-brasero
Requires:	nautilus-extension-evince
Requires:	nautilus-extension-file-roller
Requires:	nautilus-extension-terminal
Requires:	nautilus-extension-totem
Requires:	nautilus-extension-tracker
Requires:	nautilus-shell-search-provider
Requires:	notification-daemon
Requires:	polari
Requires:	pulseaudio
Requires:	seahorse >= 3.12.0
Requires:	seahorse-shell-search-provider
Requires:	seahorse-shell-search-provider
Requires:	shared-color-profiles
Requires:	simple-scan >= 3.12.0
Requires:	sushi
Requires:	telepathy-service
Requires:	totem >= 3.12.0
Requires:	totem-plugins
Requires:	tracker >= 1.0.0
Requires:	vinagre >= 3.12.0
Requires:	yelp >= 3.12.0
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

