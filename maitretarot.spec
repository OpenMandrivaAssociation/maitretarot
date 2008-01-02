%define name maitretarot
%define version 0.1.98
%define release %mkrel 4

Summary: The Maitretarot Server
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://www.nongnu.org/download/maitretarot/%{name}.pkg/%{version}/%{name}-%{version}.tar.bz2
URL: http://www.nongnu.org/maitretarot/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: glib2-devel libmaitretarot-devel

%description
Maitretarot is a tarot server game. It needs libmaitretarot 
that is a library for both the server and any client.

Warning: To play, you need to install one maitretarot-client.

%description -l fr
Maitretarot est le serveur pour un jeu de tarot. Il nécessite 
libmaitretarot qui est une bibliothèque pour le serveur comme 
pour certains clients.

Attention: pour jouer, vous devez installer un des packages
maitretarot-client.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*


