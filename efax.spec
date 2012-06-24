Summary:	sends and receives faxes over class 1 or class 2 modems
Summary(de):	sendet und empf�ngt Faxe �ber Modems der Klassen 1 und 2
Summary(fr):	envoie et re�oit des faxs sur des modems classe 1 ou 2
Summary(pl):	wysy�anie i odbieranie fax�w modemami klasy 1 oraz 2
Summary(tr):	1 veya 2 s�n�f� modemler �zerinden fax g�nderir
Name:		efax
Version:	0.9
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/comm/fax/%{name}-%{version}.tar.gz
Patch0:		efax.patch
Requires:	ghostscript
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a program to send and receive faxes over class 1 or
class 2 fax modems.  It has a nice interface to help 
facilitate faxing.

%description -l de
Dies ist ein Programm zum Versenden und Empfangen von 
Faxnachrichten �ber Faxmodems der Klasse 2. Dank
seiner attraktiven Bedieneroberfl�che wird das Faxen zum
Kinderspiel

%description -l fr
C'est un programme pour envoyer et recevoir des messages sur des modems de
classe 1 ou 2. Il poss�de une interface agr�able pour faciliter l'envoi
des fax.

%description -l pl
Program umo�liwiaj�cy wysy�anie i odbieranie fax�w faxmodemami klasy 1 
oraz 2. Program ten posiada �atwy interface u�atwiaj�cy faxowanie.

%description -l tr
Bu program ile 1 veya 2 s�n�f� modemlerle fax g�nderilebilir. Fax
ileti�imini kolayla�t�rmak i�in program�n g�zel bir kullan�c� aray�z�
bulunmaktad�r.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
install -d $RPM_BUILD_ROOT/etc/sysconfig

make install \
	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install efax.conf $RPM_BUILD_ROOT/etc/sysconfig/efax

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc *.gz
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/efax
%attr(755,root,root) /usr/bin/fax
%attr(755,root,root) /usr/bin/efax
%attr(755,root,root) /usr/bin/efix
%{_mandir}/man1/*.gz

%changelog
* Tue Apr 13 1999 Jacek Smyda <smyda@posexperts.com.pl>
  [0.9-1]
- split /usr/bin/fax into two files: fax and config
- move fax config file to /etc/sysconfig
- change "Requires: ghostscript"

* Wed Apr  7 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9-1]
- gzipping %doc and removed COPYNG from %doc (copyright statment is in
  Copyright field),
- added "rm -rf $RPM_BUILD_ROOT" on top %install,
- added "Requires: gs".

* Wed Apr  7 1999 Jacek Smyda <smyda@posexperts.com.pl>
- finally 0.9
- translations for pl
- gzip man pages

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- cleaned spec file to new standard, confirmed package is up to date

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added efax-08a-64bit.patch from David Mosberger
