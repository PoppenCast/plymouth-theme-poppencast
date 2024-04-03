%global forgeurl https://github.com/emansom/plymouth-theme-poppencast

Version: 0.0.2

%forgemeta

Name:    plymouth-theme-poppencast
Release: 1%{?dist}
Summary: Plymouth theme with PoppenCast branding

License: GPL-3.0-or-later
URL:	 %{forgeurl}
Source:  %{forgesource}

Requires: plymouth
Requires: plymouth-theme-script

BuildRequires: plymouth
BuildRequires: plymouth-theme-script
BuildArch:     noarch

%description
Site specific branding for PoppenCast appliances

%prep
%forgesetup

%build
# not needed, just copying files

%install
install -d %{buildroot}/%{_datadir}/plymouth/themes/poppencast
install -Dm 644 poppencast/* %{buildroot}/%{_datadir}/plymouth/themes/poppencast

%check
# not needed, just copying files

%files
%{_datadir}/plymouth/themes/poppencast
%doc README.md
%license LICENSE

%post
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
%{_sbindir}/plymouth-set-default-theme poppencast

%postun
export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
%{_sbindir}/plymouth-set-default-theme --reset

%changelog
* Thu Apr 04 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.2-1
- Add dependencies to spec file (ewout@vanmansom.name)

* Thu Apr 04 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.1-1
- new package built with tito

