%define pkgname heuristica-ttf

Summary:	Extended version of Adobe Utopia font
Name:		fonts-ttf-heuristika
Version:	0.4
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		http://code.google.com/p/evristika/
Source0:	http://evristika.googlecode.com/files/%{pkgname}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
Heuristica is a font, based on the “Adobe Utopia” font that was released to the TeX Users Group.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/heuristika

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/heuristika
ttmkfdir %{buildroot}%{_xfontdir}/TTF/heuristika > %{buildroot}%{_xfontdir}/TTF/heuristika/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/heuristika/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/heuristika \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-heuristika:pri=50

%files
%doc OFL.txt OFL-FAQ.txt FontLog.txt
%dir %{_xfontdir}/TTF/heuristika
%{_xfontdir}/TTF/heuristika/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/heuristika/fonts.dir
%{_xfontdir}/TTF/heuristika/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-heuristika:pri=50
