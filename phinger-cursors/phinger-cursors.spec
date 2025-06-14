Name:           phinger-cursors
Version:        2.1
Release:        %autorelease
Summary:        Most likely the most over engineered cursor theme. 
License:        CC-BY-SA-4.0
BuildArch:      noarch

URL:            https://github.com/phisch/phinger-cursors
Source:         %{url}/releases/download/v%{version}/phinger-cursors-variants.tar.bz2

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%setup -c

%build

%install
install -Ddm755 %{buildroot}%{_iconsdir}
for dir in $(find . -mindepth 1 -maxdepth 1 -type d); do
    cp -dr --no-preserve=ownership "$dir" %{buildroot}%{_iconsdir}
done

%files
%dir %{_iconsdir}/phinger-cursors-dark/
%{_iconsdir}/phinger-cursors-dark/*x*
%{_iconsdir}/phinger-cursors-dark/cursors
%dir %{_iconsdir}/phinger-cursors-dark-left
%{_iconsdir}/phinger-cursors-dark-left/*x*
%{_iconsdir}/phinger-cursors-dark-left/cursors
%dir %{_iconsdir}/phinger-cursors-light
%{_iconsdir}/phinger-cursors-light/*x*
%{_iconsdir}/phinger-cursors-light/cursors
%dir %{_iconsdir}/phinger-cursors-light-left
%{_iconsdir}/phinger-cursors-light-left/*x*
%{_iconsdir}/phinger-cursors-light-left/cursors

%changelog
%autochangelog