%bcond_with check

Name:           sd
Version:        1.0.0
Release:        %autorelease
Summary:        Intuitive find & replace CLI (sed alternative)
License:        MIT

URL:            https://github.com/chmln/sd
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -p1
cargo vendor --locked
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc CHANGELOG.md
%doc README.md
%doc RELEASE.md
%{_bindir}/sd

%changelog
%autochangelog