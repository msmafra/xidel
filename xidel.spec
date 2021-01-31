Name:           xidel
Version:        0.9.8
Release:        1%{?dist}
Summary:        Command line tool to download and extract data from HTML/XML pages or JSON-APIs.

License:        GPL-3.0 License
URL:            https://github.com/msmafra/xidel/
Source0:        https://github.com/benibela/xidel/

BuildRequires:  fpc
#Requires:

%description
Benito van der Zander (benibela)'s Xidel

Xidel is a command line tool to download and extract data from HTML/XML pages using CSS selectors, XPath/XQuery 3.0, as well as querying JSON files or APIs (e.g. REST) using JSONiq.

There are dependency-free binaries for Windows, Linux and Mac.

It is a wrapper around my Pascal Internet Tools (see repository internettools), so it supports XPath 2.0, XPath 3.0, XQuery 1.0, XQuery 3.0, JSONiq, CSS selectors and my own extensions/languages (e.g. pattern matching) and if you can compile that project, you can compile Xidel.

%prep
%autosetup


%build
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
