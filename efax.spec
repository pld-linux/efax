Summary:	Sends and receives faxes over class 1 or class 2 modems
Summary(de.UTF-8):	Sendet und empfängt Faxe über Modems der Klassen 1 und 2
Summary(fr.UTF-8):	Envoie et reçoit des faxs sur des modems classe 1 ou 2
Summary(pl.UTF-8):	Wysyłanie i odbieranie faksów modemami klasy 1 oraz 2
Summary(tr.UTF-8):	1 veya 2 sınıfı modemler üzerinden fax gönderir
Name:		efax
Version:	0.9a
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.cce.com/efax/download/%{name}-%{version}-001114.tar.gz
# Source0-md5:	28abef47d9700eb1c20bf5770565aa7d
Patch0:		%{name}.patch
Patch1:		%{name}-nullptr.patch
URL:		http://www.cce.com/efax/
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program to send and receive faxes over class 1 or class 2
fax modems. It has a nice interface to help facilitate faxing.

%description -l de.UTF-8
Dies ist ein Programm zum Versenden und Empfangen von Faxnachrichten
über Faxmodems der Klasse 2. Dank seiner attraktiven
Bedieneroberfläche wird das Faxen zum Kinderspiel

%description -l fr.UTF-8
C'est un programme pour envoyer et recevoir des messages sur des
modems de classe 1 ou 2. Il posséde une interface agréable pour
faciliter l'envoi des fax.

%description -l pl.UTF-8
Program umożliwiający wysyłanie i odbieranie faksów faksmodemami klasy
1 oraz 2. Program ten posiada łatwy interfejs ułatwiający faksowanie.

%description -l tr.UTF-8
Bu program ile 1 veya 2 sınıfı modemlerle fax gönderilebilir. Fax
iletişimini kolaylaştırmak için programın güzel bir kullanıcı arayüzü
bulunmaktadır.

%prep
%setup -q -n %{name}-%{version}-001114
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
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/efax
%attr(755,root,root) %{_bindir}/fax
%attr(755,root,root) %{_bindir}/efax
%attr(755,root,root) %{_bindir}/efix
%{_mandir}/man1/*
/var/spool/fax
