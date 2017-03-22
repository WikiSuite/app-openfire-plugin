
Name: app-openfire-plugin
Epoch: 1
Version: 1.1.2
Release: 1%{dist}
Summary: Openfire Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Packager: eGloo
Vendor: WikiSuite
Source: app-openfire-plugin-%{version}.tar.gz
Buildarch: noarch

%description
Openfire Policies provide access control for the Openfire app.

%package core
Summary: Openfire Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
Openfire Policies provide access control for the Openfire app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/openfire_plugin
cp -r * %{buildroot}/usr/clearos/apps/openfire_plugin/

install -D -m 0644 packaging/openfire.php %{buildroot}/var/clearos/accounts/plugins/openfire.php

%post core
logger -p local6.notice -t installer 'app-openfire-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/openfire_plugin/deploy/install ] && /usr/clearos/apps/openfire_plugin/deploy/install
fi

[ -x /usr/clearos/apps/openfire_plugin/deploy/upgrade ] && /usr/clearos/apps/openfire_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-openfire-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/openfire_plugin/deploy/uninstall ] && /usr/clearos/apps/openfire_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/openfire_plugin/packaging
%exclude /usr/clearos/apps/openfire_plugin/unify.json
%dir /usr/clearos/apps/openfire_plugin
/usr/clearos/apps/openfire_plugin/deploy
/usr/clearos/apps/openfire_plugin/language
/var/clearos/accounts/plugins/openfire.php
