Summary:	sends and receives faxes over class 1 or class 2 modems
Summary(de):	sendet und empfängt Faxe über Modems der Klassen 1 und 2
Summary(fr):	envoie et reçoit des faxs sur des modems classe 1 ou 2
Summary(pl):	wysy³anie i odbieranie faxów modemami klasy 1 oraz 2
Summary(tr):	1 veya 2 sýnýfý modemler üzerinden fax gönderir
Name:		efax
Version:	0.9
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/comm/fax/efax-0.9.tar.gz
Patch:		efax-0.9.patch
Patch3:		efax-08a-64bit.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a program to send and receive faxes over class 1 or
class 2 fax modems.  It has a nice interface to help 
facilitate faxing.

%description -l de
Dies ist ein Programm zum Versenden und Empfangen von 
Faxnachrichten über Faxmodems der Klasse 2. Dank
seiner attraktiven Bedieneroberfläche wird das Faxen zum
Kinderspiel

%description -l fr
C'est un programme pour envoyer et recevoir des messages sur des modems de
classe 1 ou 2. Il posséde une interface agréable pour faciliter l'envoi
des fax.

%description -l pl
Program umo¿liwiaj±cy wysy³anie i odbieranie faxów faxmodemami klasy 1 
oraz 2. Program ten posiada ³atwy interface u³atwiaj±cy faxowanie.

%description -l tr
Bu program ile 1 veya 2 sýnýfý modemlerle fax gönderilebilir. Fax
iletiþimini kolaylaþtýrmak için programýn güzel bir kullanýcý arayüzü
bulunmaktadýr.

%prep
%setup
%patch -p1

#%ifarch alpha
#%patch3 -p1
#%endif

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
make install BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man
gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README COPYING
%config %attr(755,root,root) /usr/bin/fax
%attr(755,root,root) /usr/bin/efax
%attr(755,root,root) /usr/bin/efix
/usr/man/man1/*.gz

%changelog
* Wed Apr  7 1999 Jacek Smyda <smyda@posexperts.com.pl>
  [0.9-1]
- finally 0.9
- translations for pl
- gzip man pages

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- cleaned spec file to new standard, confirmed package is up to date

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added efax-08a-64bit.patch from David Mosberger
