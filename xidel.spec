Name:           xidel
Version:        0.9.8
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        

BuildRequires:  fpc
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Sun Jan 31 2021 Marcelo dos Santos Mafra <msmafra@gmail.com>
- 
