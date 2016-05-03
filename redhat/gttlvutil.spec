#
# GUARDTIME CONFIDENTIAL
#
# Copyright (C) [2015] Guardtime, Inc
# All Rights Reserved
#
# NOTICE:  All information contained herein is, and remains, the
# property of Guardtime Inc and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to Guardtime Inc and its suppliers and may be
# covered by U.S. and Foreign Patents and patents in process,
# and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this
# material is strictly forbidden unless prior written permission
# is obtained from Guardtime Inc.
# "Guardtime" and "KSI" are trademarks or registered trademarks of
# Guardtime Inc.
#

Summary: Guardtime TLV Utils 
Name: gttlvutil
Version: 0.3.67
Release: 1 
License: ASL 2.0
Source: http://download.guardtime.com/%{name}-%{version}.tar.gz
URL: http://www.guardtime.com
Vendor: Guardtime AS
Packager: Guardtime AS <info@guardtime.com>

%description
Utils for TLV manipulation.

%prep
%setup

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gttlvdump
%attr(755,root,root) %{_bindir}/gttlvundump
%attr(755,root,root) %{_bindir}/gttlvgrep
%attr(755,root,root) %{_bindir}/gttlvwrap
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ksi.desc
%{_datadir}/%{name}/logsig.desc
