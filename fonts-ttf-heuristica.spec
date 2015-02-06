%define pkgname heuristica-ttf

Summary:	Extended version of Adobe Utopia font
Name:		fonts-ttf-heuristica
Version:	1.0.1
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		http://code.google.com/p/evristika/
Source0:	http://evristika.googlecode.com/files/%{pkgname}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	freetype-tools
%rename		fonts-ttf-heuristika

%description
Heuristica is a font, based on the “Adobe Utopia” font that was released
to the TeX Users Group.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/heuristica

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/heuristica
ttmkfdir %{buildroot}%{_xfontdir}/TTF/heuristica -o %{buildroot}%{_xfontdir}/TTF/heuristica/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/heuristica/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/heuristica \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-heuristica:pri=50

%files
%doc OFL.txt OFL-FAQ.txt FontLog.txt
%dir %{_xfontdir}/TTF/heuristica
%{_xfontdir}/TTF/heuristica/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/heuristica/fonts.dir
%{_xfontdir}/TTF/heuristica/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-heuristica:pri=50


%changelog
* Mon Aug 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0.1-1
+ Revision: 814526
- rename to heuristica to match upstream name
- update to 1.0.1
- some minor fixes
- rename package to match upstream font name

* Wed Dec 07 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.4-1
+ Revision: 738641
- imported package fonts-ttf-heuristika

