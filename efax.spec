Summary:	sends and receives faxes over class 1 or class 2 modems
Summary(de):	sendet und empf�ngt Faxe �ber Modems der Klassen 1 und 2
Summary(fr):	envoie et re�oit des faxs sur des modems classe 1 ou 2
Summary(pl):	wysy�anie i odbieranie fax�w modemami klasy 1 oraz 2
Summary(tr):	1 veya 2 s�n�f� modemler �zerinden fax g�nderir
Name:		efax
Version:	0.9
Release:	8
License:	GPL
Group:		Applications/Communications
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/comm/fax/%{name}-%{version}.tar.gz
# Source0-md5: 23bd3767f87c455c58ccae7f88bce725
Patch0:		%{name}.patch
Patch1:		%{name}-nullptr.patch
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program to send and receive faxes over class 1 or class 2
fax modems. It has a nice interface to help facilitate faxing.

%description -l de
Dies ist ein Programm zum Versenden und Empfangen von Faxnachrichten
�ber Faxmodems der Klasse 2. Dank seiner attraktiven
Bedieneroberfl�che wird das Faxen zum Kinderspiel

%description -l fr
C'est un programme pour envoyer et recevoir des messages sur des
modems de classe 1 ou 2. Il poss�de une interface agr�able pour
faciliter l'envoi des fax.

%description -l pl
Program umo�liwiaj�cy wysy�anie i odbieranie faks�w faksmodemami klasy
1 oraz 2. Program ten posiada �atwy interfejs u�atwiaj�cy faksowanie.

%description -l tr
Bu program ile 1 veya 2 s�n�f� modemlerle fax g�nderilebilir. Fax
ileti�imini kolayla�t�rmak i�in program�n g�zel bir kullan�c� aray�z�
bulunmaktad�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -ansi" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/sysconfig,/var/spool/fax}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install efax.conf $RPM_BUILD_ROOT/etc/sysconfig/efax

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/efax
%attr(755,root,root) %{_bindir}/fax
%attr(755,root,root) %{_bindir}/efax
%attr(755,root,root) %{_bindir}/efix
%{_mandir}/man1/*
/var/spool/fax
