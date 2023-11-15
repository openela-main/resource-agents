#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

# Below is the script used to generate a new source file
# from the resource-agent upstream git repo.
#
# TAG=$(git log --pretty="format:%h" -n 1)
# distdir="ClusterLabs-resource-agents-${TAG}"
# TARFILE="${distdir}.tar.gz"
# rm -rf $TARFILE $distdir
# git archive --prefix=$distdir/ HEAD | gzip > $TARFILE
#

%global upstream_prefix ClusterLabs-resource-agents
%global upstream_version 55a4e2c9

# bundles
%global bundled_lib_dir		bundled
## google cloud
# google-cloud-sdk bundle
%global googlecloudsdk		google-cloud-sdk
%global googlecloudsdk_version	360.0.0
%global googlecloudsdk_dir	%{bundled_lib_dir}/gcp/%{googlecloudsdk}
# python-pyroute2 bundle
%global pyroute2		pyroute2
%global pyroute2_version	0.4.13
%global pyroute2_dir		%{bundled_lib_dir}/gcp/%{pyroute2}
# python-httplib2 bundle
%global httplib2		httplib2
%global httplib2_version	0.20.4
## alibaba cloud
# python-colorama bundle
%global colorama		colorama
%global colorama_version	0.3.3
%global colorama_dir		%{bundled_lib_dir}/aliyun/%{colorama}
# python-pycryptodome bundle
%global pycryptodome		pycryptodome
%global pycryptodome_version	3.6.4
%global pycryptodome_dir	%{bundled_lib_dir}/aliyun/%{pycryptodome}
# python-aliyun-sdk-core bundle
%global aliyunsdkcore		aliyun-python-sdk-core
%global aliyunsdkcore_version	2.13.1
%global aliyunsdkcore_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkcore}
# python-aliyun-sdk-ecs bundle
%global aliyunsdkecs		aliyun-python-sdk-ecs
%global aliyunsdkecs_version	4.9.3
%global aliyunsdkecs_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkecs}
# python-aliyun-sdk-vpc bundle
%global aliyunsdkvpc		aliyun-python-sdk-vpc
%global aliyunsdkvpc_version	3.0.2
%global aliyunsdkvpc_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkvpc}
# aliyuncli bundle
%global aliyuncli		aliyun-cli
%global aliyuncli_version	2.1.10
%global aliyuncli_dir		%{bundled_lib_dir}/aliyun/%{aliyuncli}

# determine the ras-set to process based on configure invokation
%bcond_with rgmanager
%bcond_without linuxha

Name:		resource-agents
Summary:	Open Source HA Reusable Cluster Resource Scripts
Version:	4.9.0
Release:	48%{?rcver:%{rcver}}%{?numcomm:.%{numcomm}}%{?alphatag:.%{alphatag}}%{?dirty:.%{dirty}}%{?dist}
License:	GPLv2+ and LGPLv2+
URL:		https://github.com/ClusterLabs/resource-agents
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Source0:	%{upstream_prefix}-%{upstream_version}.tar.gz
Source1:	%{googlecloudsdk}-%{googlecloudsdk_version}-linux-x86_64.tar.gz
Source2:	%{pyroute2}-%{pyroute2_version}.tar.gz
Source3:	pyparsing-2.4.7-py2.py3-none-any.whl
Source4:	%{httplib2}-%{httplib2_version}.tar.gz
Source5:	%{colorama}-%{colorama_version}.tar.gz
Source6:	%{pycryptodome}-%{pycryptodome_version}.tar.gz
Source7:	%{aliyunsdkcore}-%{aliyunsdkcore_version}.tar.gz
Source8:	%{aliyunsdkecs}-%{aliyunsdkecs_version}.tar.gz
Source9:	%{aliyunsdkvpc}-%{aliyunsdkvpc_version}.tar.gz
Source10:	%{aliyuncli}-%{aliyuncli_version}.tar.gz
Patch0: 	nova-compute-wait-NovaEvacuate.patch
Patch1: 	bz1872754-pgsqlms-new-ra.patch
Patch2: 	bz1995178-storage-mon-fix-typo.patch
Patch3: 	bz2008333-gcp-pd-move-gcp-vpc-move-route-dont-fail-due-to-incorrect-rc.patch
Patch4: 	bz2003117-all-agents-set-correct-agent-ocf-version.patch
Patch5: 	bz2014415-nfsserver-add-nfs_server_scope-parameter.patch
Patch6: 	bz2015789-gcp-ilb-1-fix-log_enable.patch
Patch7: 	bz2015789-gcp-ilb-2-only-check-log_cmd-if-log-enabled.patch
Patch8: 	bz2015789-gcp-ilb-3-use-bundled-gcloud.patch
Patch9: 	bz2027591-nfsnotify-fix-notify_args-default.patch
Patch10:	bz2012057-Route-return-OCF_NOT_RUNNING-missing-route.patch
Patch11:	bz2029706-1-db2-crm_attribute-use-forever.patch
Patch12:	bz2029706-2-db2-fixes.patch
Patch13:	bz1992661-mysql-use-ssl-mode.patch
Patch14:	bz2064342-1-IPsrcaddr-dhcp-warning.patch
Patch15:	bz2064342-2-IPsrcaddr-error-message-route-not-found.patch
Patch16:	bz2064342-3-IPsrcaddr-fix-indentation.patch
Patch17:	bz2064342-4-IPsrcaddr-fixes.patch
Patch18:	bz1908146-bz1908147-bz1908148-bz1949114-update-openstack-agents.patch
Patch19:	bz2072043-LVM-activate-fix-fence-issue.patch
Patch20:	bz2049414-Filesystem-1-fix-uuid-label-device-whitespace.patch
Patch21:	bz2049414-Filesystem-2-improve-uuid-label-device-logic.patch
Patch22:	bz2086889-lvmlockd-fail-when-use_lvmlockd-not-set.patch
Patch23:	bz2093214-aws-vpc-move-ip-add-interface-label-support.patch
Patch24:	bz1908148-openstack-info-fix-bashism.patch
Patch25:	bz1908146-bz1908147-bz1949114-openstack-agents-fixes.patch
Patch26:	bz1908146-bz1908147-bz1908148-bz1949114-openstack-agents-warn-when-openstackcli-slow.patch
Patch27:	bz2103370-ocf-tester-1-update.patch
Patch28:	bz2103370-ocf-tester-2-remove-deprecated-lrmd-lrmadmin-code.patch
Patch29:	bz1908146-bz1908147-bz1908148-bz1949114-openstack-agents-set-domain-parameters-default.patch
Patch30:	bz2090370-CTDB-move-process-to-root-cgroup-if-rt-enabled.patch
Patch31:	bz2116941-ethmonitor-ovsmonitor-pgsql-fix-attrd_updater-q.patch
Patch32:	bz2109159-storage_mon-1-exit-after-help.patch
Patch33:	bz2109159-storage_mon-2-fix-specified-scores-count.patch
Patch34:	bz2109159-storage_mon-3-fix-child-process-exit.patch
Patch35:	bz2109159-storage_mon-4-fix-possible-false-negatives.patch
Patch36:	bz1905820-LVM-activate-fix-return-codes.patch
Patch37:	bz1977012-azure-events-az-new-ra.patch
Patch38:	bz2133682-IPsrcaddr-proto-metric-scope-default-route-fixes.patch
Patch39:	bz2141836-vdo-vol-dont-fail-probe-action.patch
Patch40:	bz2049319-Filesystem-add-support-for-Amazon-EFS.patch
Patch41:	bz2127117-nfsserver-nfsv4_only-parameter.patch
Patch42:	bz2139131-mysql-common-return-error-if-kill-fails.patch
Patch43:	bz2157873-1-all-ras-validate-all-OCF_CHECK_LEVEL-10.patch
Patch44:	bz2157873-2-Filesystem-CTDB-validate-all-improvements.patch
Patch45:	bz2157873-3-pgsqlms-validate-all-OCF_CHECK_LEVEL-10.patch
Patch46:	bz2157873-4-exportfs-pgsql-validate-all-fixes.patch
Patch47:	bz2157873-5-pgsqlms-alidate-all-OCF_CHECK_LEVEL-10.patch
Patch48:	bz2040110-IPaddr2-IPsrcaddr-1-support-policy-based-routing.patch
Patch49:	bz2149970-lvmlockd-add-use_lvmlockd-if-missing.patch
Patch50:	bz2154727-ethmonitor-dont-log-iface-doesnt-exist-monitor.patch
Patch51:	bz2039692-mysql-1-replication-fixes.patch
Patch52:	bz2181019-azure-events-1-fix-no-transition-summary.patch
Patch53:	bz2181019-azure-events-2-improve-logic.patch
Patch54:	bz2183152-Filesystem-fail-efs-utils-not-installed.patch
Patch55:	bz2039692-mysql-2-fix-demoted-score-bounce.patch
Patch56:	bz2040110-IPaddr2-IPsrcaddr-2-fix-table-parameter.patch
Patch57:	bz2189243-Filesystem-1-improve-stop-action.patch
Patch58:	bz2189243-Filesystem-2-fix-incorrect-parameter-types.patch
Patch59:	bz2189243-Filesystem-3-fix-signal_delay-default-value.patch
Patch60:	bz2040110-IPaddr2-IPsrcaddr-3-dont-use-table-parameter.patch

# bundle patches
Patch1000:	7-gcp-bundled.patch
Patch1001:	9-google-cloud-sdk-oauth2client-python-rsa-to-cryptography.patch
Patch1002:	10-gcloud-support-info.patch
Patch1003:	gcp-configure-skip-bundled-lib-checks.patch
Patch1004:	bz1691456-gcloud-dont-detect-python2.patch
Patch1005:	aliyun-vpc-move-ip-4-bundled.patch
Patch1006:	python3-syntax-fixes.patch
Patch1007:	aliyuncli-python3-fixes.patch
Patch1008:	bz1935422-python-pygments-fix-CVE-2021-20270.patch
Patch1009:	bz1943464-python-pygments-fix-CVE-2021-27291.patch

Obsoletes:	heartbeat-resources <= %{version}
Provides:	heartbeat-resources = %{version}

# Build dependencies
BuildRequires: automake autoconf gcc
BuildRequires: perl-interpreter python3-devel
BuildRequires: libxslt glib2-devel
BuildRequires: systemd
BuildRequires: which

%ifarch x86_64
BuildRequires: python3-pip
%endif

%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
#BuildRequires: cluster-glue-libs-devel
BuildRequires: docbook-style-xsl docbook-dtds
%if 0%{?rhel} == 0
BuildRequires: libnet-devel
%endif
%endif

## Runtime deps
# system tools shared by several agents
Requires: /bin/bash /usr/bin/grep /bin/sed /bin/gawk
Requires: /bin/ps /usr/bin/pkill /usr/bin/hostname /usr/bin/netstat
Requires: /usr/sbin/fuser /bin/mount

# Filesystem / fs.sh / netfs.sh
Requires: /sbin/fsck
Requires: /usr/sbin/fsck.ext2 /usr/sbin/fsck.ext3 /usr/sbin/fsck.ext4
Requires: /usr/sbin/fsck.xfs
Requires: /sbin/mount.nfs /sbin/mount.nfs4
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: /usr/sbin/mount.cifs
%else
Recommends: /usr/sbin/mount.cifs
%endif
%endif

# IPaddr2
Requires: /sbin/ip

# LVM / lvm.sh
Requires: /usr/sbin/lvm

# nfsserver / netfs.sh
Requires: /usr/sbin/rpc.nfsd /sbin/rpc.statd /usr/sbin/rpc.mountd

# ocf.py
Requires: python3

# rgmanager
%if %{with rgmanager}
# ip.sh
Requires: /usr/sbin/ethtool
Requires: /sbin/rdisc /usr/sbin/arping /bin/ping /bin/ping6

# nfsexport.sh
Requires: /sbin/findfs
Requires: /sbin/quotaon /sbin/quotacheck
%endif

%description
A set of scripts to interface with several services to operate in a
High Availability environment for both Pacemaker and rgmanager
service managers.

%ifarch x86_64
%package aliyun
License:	GPLv2+ and LGPLv2+ and ASL 2.0 and BSD and MIT
Summary:	Alibaba Cloud (Aliyun) resource agents
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:	%{name} = %{version}-%{release}
Requires:	python3-jmespath >= 0.9.0
Requires:	python3-urllib3
# python-colorama bundle
Provides:	bundled(python-%{colorama}) = %{colorama_version}
# python-pycryptodome bundle
Provides:	bundled(python-%{pycryptodome}) = %{pycryptodome_version}
# python-aliyun-sdk-core bundle
Provides:	bundled(python-aliyun-sdk-core) = %{aliyunsdkcore_version}
# python-aliyun-sdk-ecs bundle
Provides:	bundled(python-aliyun-sdk-ecs) = %{aliyunsdkecs_version}
# python-aliyun-sdk-vpc bundle
Provides:	bundled(python-aliyun-sdk-vpc) = %{aliyunsdkvpc_version}
# aliyuncli bundle
Provides:	bundled(aliyuncli) = %{aliyuncli_version}

%description aliyun
Alibaba Cloud (Aliyun) resource agents allows Alibaba Cloud
(Aliyun) instances to be managed in a cluster environment.
%endif

%ifarch x86_64
%package gcp
License:	GPLv2+ and LGPLv2+ and BSD and ASL 2.0 and MIT and Python
Summary:	Google Cloud Platform resource agents
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:	%{name} = %{version}-%{release}
Requires:	python3-google-api-client
Requires:	socat
# google-cloud-sdk bundle
Requires:	python3-cryptography >= 1.7.2
Requires:	python3-dateutil >= 2.6.0
Provides:	bundled(%{googlecloudsdk}) = %{googlecloudsdk_version}
Provides:	bundled(python-antlr3) = 3.1.1
Provides:	bundled(python-appdirs) = 1.4.0
Provides:	bundled(python-argparse) = 1.2.1
Provides:	bundled(python-chardet) = 2.3.0
Provides:	bundled(python-dulwich) = 0.10.2
Provides:	bundled(python-ipaddress) = 1.0.16
Provides:	bundled(python-ipaddr) = 2.1.11
Provides:	bundled(python-mako) = 1.0.7
Provides:	bundled(python-oauth2client) = 3.0.0
Provides:	bundled(python-prompt_toolkit) = 1.0.13
Provides:	bundled(python-pyasn1) = 0.4.2
Provides:	bundled(python-pyasn1_modules) = 0.2.1
Provides:	bundled(python-pygments) = 2.2.0
Provides:	bundled(python-pyparsing) = 2.1.10
Provides:	bundled(python-requests) = 2.10.0
Provides:	bundled(python-six) = 1.11.0
Provides:	bundled(python-uritemplate) = 3.0.0
Provides:	bundled(python-urllib3) = 1.15.1
Provides:	bundled(python-websocket) = 0.47.0
Provides:	bundled(python-yaml) = 3.12
# python-pyroute2 bundle
Provides:	bundled(%{pyroute2}) = %{pyroute2_version}
# python-httplib2 bundle
Provides:	bundled(%{httplib2}) = %{httplib2_version}

%description gcp
The Google Cloud Platform resource agents allows Google Cloud
Platform instances to be managed in a cluster environment.
%endif

%package paf
License:	PostgreSQL
Summary:	PostgreSQL Automatic Failover (PAF) resource agent
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:	%{name} = %{version}-%{release}
Requires:	perl-interpreter

%description paf
PostgreSQL Automatic Failover (PAF) resource agents allows PostgreSQL
databases to be managed in a cluster environment.

%prep
%if 0%{?suse_version} == 0 && 0%{?fedora} == 0 && 0%{?centos_version} == 0 && 0%{?rhel} == 0
%{error:Unable to determine the distribution/version. This is generally caused by missing /etc/rpm/macros.dist. Please install the correct build packages or define the required macros manually.}
exit 1
%endif
%setup -q -n %{upstream_prefix}-%{upstream_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1

chmod 755 heartbeat/nova-compute-wait
chmod 755 heartbeat/NovaEvacuate
chmod 755 heartbeat/pgsqlms

# bundles
mkdir -p %{bundled_lib_dir}/gcp
mkdir -p %{bundled_lib_dir}/aliyun

# google-cloud-sdk bundle
%ifarch x86_64
tar -xzf %SOURCE1 -C %{bundled_lib_dir}/gcp
# gcp*: append bundled-directory to search path, gcloud-ra
%patch1000 -p1
# replace python-rsa with python-cryptography
%patch1001 -p1
# gcloud support info
%patch1002 -p1
# configure: skip bundled gcp lib checks
%patch1003 -p1 -F1
# gcloud remove python 2 detection
%patch1004 -p1
# rename gcloud
mv %{googlecloudsdk_dir}/bin/gcloud %{googlecloudsdk_dir}/bin/gcloud-ra
# keep googleapiclient
mv %{googlecloudsdk_dir}/platform/bq/third_party/googleapiclient %{googlecloudsdk_dir}/lib/third_party
# only keep gcloud
rm -rf %{googlecloudsdk_dir}/bin/{anthoscli,bootstrapping,bq,dev_appserver.py,docker-credential-gcloud,endpointscfg.py,git-credential-gcloud.sh,gsutil,java_dev_appserver.sh} %{googlecloudsdk_dir}/{completion.*,deb,install.*,path.*,platform,properties,RELEASE_NOTES,rpm,VERSION}
# remove Python 2 code
rm -rf %{googlecloudsdk_dir}/lib/third_party/*/python2
# remove python-rsa
rm -rf %{googlecloudsdk_dir}/lib/third_party/rsa
# remove grpc
rm -rf %{googlecloudsdk_dir}/lib/third_party/grpc
# remove dateutil
rm -rf %{googlecloudsdk_dir}/lib/third_party/dateutil
# docs/licenses
cp %{googlecloudsdk_dir}/README %{googlecloudsdk}_README
cp %{googlecloudsdk_dir}/lib/third_party/argparse/README.txt %{googlecloudsdk}_argparse_README.txt
cp %{googlecloudsdk_dir}/LICENSE %{googlecloudsdk}_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/httplib2/LICENSE %{googlecloudsdk}_httplib2_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/contextlib2/LICENSE %{googlecloudsdk}_contextlib2_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/concurrent/LICENSE %{googlecloudsdk}_concurrent_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/yaml/LICENSE %{googlecloudsdk}_yaml_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/pyu2f/LICENSE %{googlecloudsdk}_pyu2f_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/ml_sdk/LICENSE %{googlecloudsdk}_ml_sdk_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/ml_sdk/pkg/LICENSE %{googlecloudsdk}_pkg_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/ipaddr/LICENSE %{googlecloudsdk}_ipaddr_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/urllib3/LICENSE %{googlecloudsdk}_urllib3_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/ipaddress/LICENSE %{googlecloudsdk}_ipaddress_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/requests/LICENSE %{googlecloudsdk}_requests_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/docker/LICENSE %{googlecloudsdk}_docker_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/monotonic/LICENSE %{googlecloudsdk}_monotonic_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/websocket/LICENSE %{googlecloudsdk}_websocket_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/fasteners/LICENSE %{googlecloudsdk}_fasteners_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/wcwidth/LICENSE %{googlecloudsdk}_wcwidth_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/pygments/LICENSE %{googlecloudsdk}_pygments_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/oauth2client/LICENSE %{googlecloudsdk}_oauth2client_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/uritemplate/LICENSE %{googlecloudsdk}_uritemplate_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/dulwich/LICENSE %{googlecloudsdk}_dulwich_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/mako/LICENSE %{googlecloudsdk}_mako_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/packaging/LICENSE %{googlecloudsdk}_packaging_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/socks/LICENSE %{googlecloudsdk}_socks_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/antlr3/LICENSE %{googlecloudsdk}_antlr3_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/argparse/LICENSE.txt %{googlecloudsdk}_argparse_LICENSE.txt
cp %{googlecloudsdk_dir}/lib/third_party/chardet/LICENSE %{googlecloudsdk}_chardet_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/ruamel/LICENSE %{googlecloudsdk}_ruamel_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/appdirs/LICENSE %{googlecloudsdk}_appdirs_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/argcomplete/LICENSE %{googlecloudsdk}_argcomplete_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/pyasn1_modules/LICENSE %{googlecloudsdk}_pyasn1_modules_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/setuptools/LICENSE %{googlecloudsdk}_setuptools_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/google/LICENSE %{googlecloudsdk}_google_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/google/protobuf/LICENSE %{googlecloudsdk}_protobuf_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/six/LICENSE %{googlecloudsdk}_six_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/dns/LICENSE %{googlecloudsdk}_dns_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/enum/LICENSE %{googlecloudsdk}_enum_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/gae_ext_runtime/LICENSE %{googlecloudsdk}_gae_ext_runtime_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/fancy_urllib/LICENSE %{googlecloudsdk}_fancy_urllib_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/pyasn1/LICENSE %{googlecloudsdk}_pyasn1_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/apitools/LICENSE %{googlecloudsdk}_apitools_LICENSE
cp %{googlecloudsdk_dir}/lib/third_party/containerregistry/LICENSE %{googlecloudsdk}_containerregistry_LICENSE

# python-pyroute2 bundle
tar -xzf %SOURCE2 -C %{bundled_lib_dir}/gcp
mv %{bundled_lib_dir}/gcp/%{pyroute2}-%{pyroute2_version} %{pyroute2_dir}
cp %{pyroute2_dir}/README.md %{pyroute2}_README.md
cp %{pyroute2_dir}/README.license.md %{pyroute2}_README.license.md
cp %{pyroute2_dir}/LICENSE.Apache.v2 %{pyroute2}_LICENSE.Apache.v2
cp %{pyroute2_dir}/LICENSE.GPL.v2 %{pyroute2}_LICENSE.GPL.v2

# python-colorama bundle
tar -xzf %SOURCE5 -C %{bundled_lib_dir}/aliyun
mv %{bundled_lib_dir}/aliyun/%{colorama}-%{colorama_version} %{colorama_dir}
cp %{colorama_dir}/LICENSE.txt %{colorama}_LICENSE.txt
cp %{colorama_dir}/README.rst %{colorama}_README.rst

pushd %{colorama_dir}
# remove bundled egg-info
rm -rf *.egg-info
popd

# python-pycryptodome bundle
tar -xzf %SOURCE6 -C %{bundled_lib_dir}/aliyun
mv %{bundled_lib_dir}/aliyun/%{pycryptodome}-%{pycryptodome_version} %{pycryptodome_dir}
cp %{pycryptodome_dir}/README.rst %{pycryptodome}_README.rst
cp %{pycryptodome_dir}/LICENSE.rst %{pycryptodome}_LICENSE.rst

# python-aliyun-sdk-core bundle
tar -xzf %SOURCE7 -C %{bundled_lib_dir}/aliyun
mv %{bundled_lib_dir}/aliyun/%{aliyunsdkcore}-%{aliyunsdkcore_version} %{aliyunsdkcore_dir}
cp %{aliyunsdkcore_dir}/README.rst %{aliyunsdkcore}_README.rst

# python-aliyun-sdk-ecs bundle
tar -xzf %SOURCE8 -C %{bundled_lib_dir}/aliyun
mv %{bundled_lib_dir}/aliyun/%{aliyunsdkecs}-%{aliyunsdkecs_version} %{aliyunsdkecs_dir}
cp %{aliyunsdkecs_dir}/README.rst %{aliyunsdkecs}_README.rst

# python-aliyun-sdk-vpc bundle
tar -xzf %SOURCE9 -C %{bundled_lib_dir}/aliyun
mv %{bundled_lib_dir}/aliyun/%{aliyunsdkvpc}-%{aliyunsdkvpc_version} %{aliyunsdkvpc_dir}
cp %{aliyunsdkvpc_dir}/README.rst %{aliyunsdkvpc}_README.rst

# aliyuncli bundle
tar -xzf %SOURCE10 -C %{bundled_lib_dir}/aliyun
mv %{bundled_lib_dir}/aliyun/%{aliyuncli}-%{aliyuncli_version} %{aliyuncli_dir}
cp %{aliyuncli_dir}/README.rst %{aliyuncli}_README.rst
cp %{aliyuncli_dir}/LICENSE %{aliyuncli}_LICENSE
# aliyun*: use bundled libraries
%patch1005 -p1

# aliyun Python 3 fixes
%patch1006 -p1
%patch1007 -p1

# fix CVE's in python-pygments
pushd %{googlecloudsdk_dir}/lib/third_party
%patch1008 -p1 -F2
%patch1009 -p1 -F2
popd
%endif

%build
if [ ! -f configure ]; then
	./autogen.sh
fi

%if 0%{?fedora} >= 11 || 0%{?centos_version} > 5 || 0%{?rhel} > 5
CFLAGS="$(echo '%{optflags}')"
%global conf_opt_fatal "--enable-fatal-warnings=no"
%else
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
%global conf_opt_fatal "--enable-fatal-warnings=yes"
%endif

%if %{with rgmanager}
%global rasset rgmanager
%endif
%if %{with linuxha}
%global rasset linux-ha
%endif
%if %{with rgmanager} && %{with linuxha}
%global rasset all
%endif

export CFLAGS

%configure BASH_SHELL="/bin/bash" \
	PYTHON="%{__python3}" \
	%{conf_opt_fatal} \
%if %{defined _unitdir}
    SYSTEMD_UNIT_DIR=%{_unitdir} \
%endif
%if %{defined _tmpfilesdir}
    SYSTEMD_TMPFILES_DIR=%{_tmpfilesdir} \
    --with-rsctmpdir=/run/resource-agents \
%endif
	--with-pkg-name=%{name} \
	--with-ras-set=%{rasset}

%if %{defined jobs}
JFLAGS="$(echo '-j%{jobs}')"
%else
JFLAGS="$(echo '%{_smp_mflags}')"
%endif

make $JFLAGS

%ifarch x86_64
# python-pyroute2 bundle
pushd %{pyroute2_dir}
%{__python3} setup.py build
popd

# python-colorama bundle
pushd %{colorama_dir}
%{__python3} setup.py build
popd

# python-pycryptodome bundle
pushd %{pycryptodome_dir}
%{__python3} setup.py build
popd

# python-aliyun-sdk-core bundle
pushd %{aliyunsdkcore_dir}
%{__python3} setup.py build
popd

# python-aliyun-sdk-ecs bundle
pushd %{aliyunsdkecs_dir}
%{__python3} setup.py build
popd

# python-aliyun-sdk-vpc bundle
pushd %{aliyunsdkvpc_dir}
%{__python3} setup.py build
popd

# aliyuncli bundle
pushd %{aliyuncli_dir}
%{__python3} setup.py build
popd
%endif

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# byte compile ocf.py
%py_byte_compile %{__python3} %{buildroot}%{_usr}/lib/ocf/lib/heartbeat

# google-cloud-sdk bundle
%ifarch x86_64
pushd %{googlecloudsdk_dir}
mkdir -p %{buildroot}/usr/lib/%{name}/%{googlecloudsdk_dir}
cp -a bin data lib %{buildroot}/usr/lib/%{name}/%{googlecloudsdk_dir}
mkdir %{buildroot}/%{_bindir}
ln -s /usr/lib/%{name}/%{googlecloudsdk_dir}/bin/gcloud-ra %{buildroot}/%{_bindir}
popd

# python-pyroute2 bundle
pushd %{pyroute2_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/gcp
popd

# python-httplib2 bundle
%{__python3} -m pip install --user --no-index --find-links %{_sourcedir} pyparsing
%{__python3} -m pip install --target %{buildroot}/usr/lib/%{name}/%{bundled_lib_dir}/gcp --no-index --find-links %{_sourcedir} %{httplib2}

# python-colorama bundle
pushd %{colorama_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/aliyun
popd

# python-pycryptodome bundle
pushd %{pycryptodome_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-core bundle
pushd %{aliyunsdkcore_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-ecs bundle
pushd %{aliyunsdkecs_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-vpc bundle
pushd %{aliyunsdkvpc_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/aliyun
popd

# aliyuncli bundle
pushd %{aliyuncli_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/%{name}/%{bundled_lib_dir}/aliyun
sed -i -e "/^import sys/asys.path.insert(0, '/usr/lib/%{name}/%{bundled_lib_dir}/aliyun')\nsys.path.insert(1, '/usr/lib/%{name}/%{bundled_lib_dir}/aliyun/aliyuncli')" %{buildroot}/%{_bindir}/aliyuncli
mv %{buildroot}/%{_bindir}/aliyuncli %{buildroot}/%{_bindir}/aliyuncli-ra
# aliyun_completer / aliyun_zsh_complete.sh
rm %{buildroot}/%{_bindir}/aliyun_*
popd
%endif

## tree fixup
# remove docs (there is only one and they should come from doc sections in files)
rm -rf %{buildroot}/usr/share/doc/resource-agents

##
# Create symbolic link between IPAddr and IPAddr2
##
rm -f %{buildroot}/usr/lib/ocf/resource.d/heartbeat/IPaddr
ln -s /usr/lib/ocf/resource.d/heartbeat/IPaddr2 %{buildroot}/usr/lib/ocf/resource.d/heartbeat/IPaddr

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.GPLv3 COPYING.LGPL ChangeLog
%if %{with linuxha}
%doc heartbeat/README.galera
%doc doc/README.webapps
%doc %{_datadir}/%{name}/ra-api-1.dtd
%doc %{_datadir}/%{name}/metadata.rng
%endif

%if %{with rgmanager}
%{_datadir}/cluster
%{_sbindir}/rhev-check.sh
%endif

%if %{with linuxha}
%dir %{_usr}/lib/ocf
%dir %{_usr}/lib/ocf/resource.d
%dir %{_usr}/lib/ocf/lib

%{_usr}/lib/ocf/lib/heartbeat

%{_usr}/lib/ocf/resource.d/heartbeat
%{_usr}/lib/ocf/resource.d/openstack
%if %{with rgmanager}
%{_usr}/lib/ocf/resource.d/redhat
%endif

%{_datadir}/pkgconfig/%{name}.pc

%if %{defined _unitdir}
%{_unitdir}/resource-agents-deps.target
%endif
%if %{defined _tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%endif

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ocft
%{_datadir}/%{name}/ocft/configs
%{_datadir}/%{name}/ocft/caselib
%{_datadir}/%{name}/ocft/README
%{_datadir}/%{name}/ocft/README.zh_CN
%{_datadir}/%{name}/ocft/helpers.sh
%exclude %{_datadir}/%{name}/ocft/runocft
%exclude %{_datadir}/%{name}/ocft/runocft.prereq

%{_sbindir}/ocf-tester
%{_sbindir}/ocft

%{_includedir}/heartbeat

%if %{defined _tmpfilesdir}
%dir %attr (1755, root, root)	/run/resource-agents
%else
%dir %attr (1755, root, root)	%{_var}/run/resource-agents
%endif

%{_mandir}/man7/*.7*
%{_mandir}/man8/ocf-tester.8*

###
# Supported, but in another sub package
###
%exclude /usr/lib/ocf/resource.d/heartbeat/aliyun-vpc-move-ip*
%exclude %{_mandir}/man7/*aliyun-vpc-move-ip*
%exclude /usr/lib/ocf/resource.d/heartbeat/gcp*
%exclude %{_mandir}/man7/*gcp*
%exclude /usr/lib/%{name}/%{bundled_lib_dir}
%exclude /usr/lib/ocf/resource.d/heartbeat/pgsqlms
%exclude %{_mandir}/man7/*pgsqlms*
%exclude %{_usr}/lib/ocf/lib/heartbeat/OCF_*.pm

###
# Moved to separate packages
###
%exclude /usr/lib/ocf/resource.d/heartbeat/SAP*
%exclude /usr/lib/ocf/lib/heartbeat/sap*
%exclude %{_mandir}/man7/*SAP*

###
# Unsupported
###
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/AoEtarget
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/AudibleAlarm
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ClusterMon
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/EvmsSCC
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/Evmsd
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ICP
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/LVM
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/LinuxSCSI
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ManageRAID
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ManageVE
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/Pure-FTPd
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/Raid1
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ServeRAID
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/SphinxSearchDaemon
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/Stateful
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/SysInfo
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/VIPArip
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/WAS
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/WAS6
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/WinPopup
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/Xen
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ZFS
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/anything
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/asterisk
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/clvm
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/dnsupdate
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/docker-compose
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/dovecot
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/dummypy
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/eDir88
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/fio
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ids
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/iface-bridge
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ipsec
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/iscsi
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/jboss
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/jira
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/kamailio
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ldirectord
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/lxc
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/lxd-info
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/machine-info
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/mariadb
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/mdraid
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/minio
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/mpathpersist
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/mysql-proxy
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/nvmet-*
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/ovsmonitor
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/pgagent
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/pingd
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/pound
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/proftpd
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/rkt
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/rsyslog
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/scsi2reservation
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/sfex
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/sg_persist
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/smb-share
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/syslog-ng
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/varnish
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/vmware
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/vsftpd
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/zabbixserver
%exclude %{_mandir}/man7/ocf_heartbeat_AoEtarget.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_AudibleAlarm.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ClusterMon.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_EvmsSCC.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Evmsd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ICP.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_IPaddr.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_LVM.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_LinuxSCSI.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ManageRAID.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ManageVE.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Pure-FTPd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Raid1.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ServeRAID.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_SphinxSearchDaemon.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Stateful.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_SysInfo.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_VIPArip.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WAS.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WAS6.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WinPopup.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Xen.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ZFS.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_anything.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_asterisk.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_clvm.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_dnsupdate.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_docker-compose.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_dovecot.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_dummypy.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_eDir88.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_fio.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ids.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_iface-bridge.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ipsec.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_iscsi.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_jboss.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_jira.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_kamailio.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_lxc.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_lxd-info.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_machine-info.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_mariadb.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_mdraid.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_minio.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_mpathpersist.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_mysql-proxy.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_nvmet-*.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ovsmonitor.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pgagent.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pingd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pound.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_proftpd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_rkt.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_rsyslog.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_scsi2reservation.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_sfex.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_sg_persist.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_smb-share.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_syslog-ng.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_varnish.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_vmware.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_vsftpd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_zabbixserver.7.gz

###
# Other excluded files.
###
# ldirectord is not supported
%exclude /etc/ha.d/resource.d/ldirectord
%exclude /etc/init.d/ldirectord
%exclude %{_unitdir}/ldirectord.service
%exclude /etc/logrotate.d/ldirectord
%exclude /usr/sbin/ldirectord
%exclude %{_mandir}/man8/ldirectord.8.gz

# For compatability with pre-existing agents
%dir %{_sysconfdir}/ha.d
%{_sysconfdir}/ha.d/shellfuncs

%{_libexecdir}/heartbeat
%endif

%if %{with rgmanager}
%post -n resource-agents
ccs_update_schema > /dev/null 2>&1 ||:
%endif

%ifarch x86_64
%files aliyun
%doc aliyun*_README* %{colorama}_README.rst %{pycryptodome}_README.rst
%license %{aliyuncli}_LICENSE %{colorama}_LICENSE.txt %{pycryptodome}_LICENSE.rst
%defattr(-,root,root)
/usr/lib/ocf/resource.d/heartbeat/aliyun-vpc-move-ip*
%{_mandir}/man7/*aliyun-vpc-move-ip*
# bundle
%{_bindir}/aliyuncli-ra
%dir /usr/lib/%{name}
/usr/lib/%{name}/%{bundled_lib_dir}/aliyun
%endif

%ifarch x86_64
%files gcp
%doc %{googlecloudsdk}_*README*
%license %{googlecloudsdk}_*LICENSE*
%doc %{pyroute2}_README*
%license %{pyroute2}_LICENSE*
%defattr(-,root,root)
/usr/lib/ocf/resource.d/heartbeat/gcp-ilb
%{_mandir}/man7/*gcp-ilb*
/usr/lib/ocf/resource.d/heartbeat/gcp-vpc-move-vip*
%{_mandir}/man7/*gcp-vpc-move-vip*
/usr/lib/ocf/resource.d/heartbeat/gcp-vpc-move-route*
%{_mandir}/man7/*gcp-vpc-move-route*
/usr/lib/ocf/resource.d/heartbeat/gcp-pd-move*
%{_mandir}/man7/*gcp-pd-move*
# bundle
%{_bindir}/gcloud-ra
%dir /usr/lib/%{name}
/usr/lib/%{name}/%{bundled_lib_dir}/gcp
%endif

%files paf
%doc paf_README.md
%license paf_LICENSE
%defattr(-,root,root)
%{_usr}/lib/ocf/resource.d/heartbeat/pgsqlms
%{_mandir}/man7/*pgsqlms*
%{_usr}/lib/ocf/lib/heartbeat/OCF_*.pm

%changelog
* Thu Oct  5 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-48
- IPaddr2/IPsrcaddr: support policy-based routing

  Resolves: rhbz#2040110

* Thu Jul 20 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-47
- Filesystem: improve stop-action and allow setting term/kill signals
  and signal_delay for large filesystems

  Resolves: rhbz#2189243

* Wed Jun 14 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-43
- mysql: fix replication issues

  Resolves: rhbz#2039692

* Mon May  1 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-42
- azure-events*: fix for no "Transition Summary" for Pacemaker 2.1+
- Filesystem: fail if AWS efs-utils not installed when fstype=efs

  Resolves: rhbz#2181019
  Resolves: rhbz#2183152

* Wed Mar 22 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-41
- lvmlockd: add "use_lvmlockd = 1" if it's commented out or missing
- ethmonitor: dont log "Interface does not exist" for monitor-action

  Resolves: rhbz#2149970
  Resolves: rhbz#2154727

* Tue Jan 17 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-40
- all agents: dont check notify/promotable settings during
  validate-action

  Resolves: rhbz#2157873

* Thu Nov 24 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-35
- mysql-common: return error in stop-action if kill fails to stop
  the process, so the node can get fenced

  Resolves: rhbz#2139131

* Tue Nov 22 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-34
- nfsserver: add nfsv4_only parameter to make it run without
  rpc-statd/rpcbind services

  Resolves: rhbz#2127117

* Mon Nov 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-33
- Filesystem: add support for Amazon EFS (Elastic File System)
- vdo-vol: dont fail probe action when the underlying device doesnt
  exist

  Resolves: rhbz#2049319
  Resolves: rhbz#2141836

* Fri Oct 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-31
- IPsrcaddr: proto, metric, scope and default route fixes

  Resolves: rhbz#2133682

* Thu Sep  8 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-30
- storage_mon: fix specified scores count and possible false negatives
- LVM-activate: use correct return codes to fix unexpected behaviour
- azure-events-az: new resource agent

  Resolves: rhbz#2109159
  Resolves: rhbz#1905820
  Resolves: rhbz#1977012

* Wed Aug 10 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-29
- ethmonitor/pgsql: remove attrd_updater "-q" parameter to solve issue
  with Pacemaker 2.1.3+ not ignoring it

  Resolves: rhbz#2116941

* Thu Aug  4 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-28
- CTDB: move process to root cgroup if realtime scheduling is enabled

  Resolves: rhbz#2090370

* Thu Jul 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-27
- ocf-tester: add testing tool

  Resolves: rhbz#2103370

* Thu Jul 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-26
- openstack-cinder-volume/openstack-floating-ip/openstack-info/
  openstack-virtual-ip: new resource agents

  Resolves: rhbz#1908146, rhbz#1908147, rhbz#1908148, rhbz#1949114

* Thu Jun 16 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-22
- gcp-vpc-move-route/gcp-vpc-move-vip: upgrade bundled
  python-httplib2 to fix SSL issue

  Resolves: rhbz#2097462

* Thu Jun  9 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-21
- aws-vpc-move-ip: add interface label support

  Resolves: rhbz#2093214

* Wed Jun  8 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-20
- lvmlockd: fail when use_lvmlockd has not been set

  Resolves: rhbz#2086889

* Thu Apr 21 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-19
- Filesystem: fix UUID/label device support when there's whitespace
  between parameter and UUID/label

  Resolves: rhbz#2049414

* Thu Apr  7 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-18
- LVM-activate: use correct return code to fence failed node

  Resolves: rhbz#2072043

* Thu Mar  3 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-16
- IPsrcaddr: add warning about possible issues when used with DHCP,
  and add error message when matching route not found

  Resolves: rhbz#2064342

* Thu Feb 24 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-15
- db2: use -l forever to fix crm_attribute issue

  Resolves: rhbz#2029706

* Thu Jan 20 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-13
- mysql: add support for local SSL connection

  Resolves: rhbz#1992661

* Tue Dec  7 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-12
- Route: return OCF_NOT_RUNNING for probe action when interface
  or route doesnt exist

  Resolves: rhbz#2012057

* Tue Nov 30 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-11
- nfsnotify: fix default value for "notify_args"

  Resolves: rhbz#2027591

* Tue Nov  9 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-10
- gcp-ilb: new resource agent

  Resolves: rhbz#2015789

* Thu Oct 28 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-6
- Route: return NOT_RUNNING if interface doesnt exist

  Resolves: rhbz#2002764

* Tue Oct 19 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-5
- All agents: set correct agent and OCF version in metadata
- nfsserver: add nfs_server_scope parameter

  Resolves: rhbz#2003117
  Resolves: rhbz#2014415

* Thu Oct 14 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-4
- gcp-vpc-move-route/gcp-vpc-move-vip: add serviceaccount JSON file
  support

  Resolves: rhbz#1704348

* Thu Sep 30 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-3
- Rebase to resource-agents 4.9.0 upstream release.
- gcp-pd-move/gcp-vpc-move-route: dont fail with configuration rc
  when it might be a network hickup

  Resolves: rhbz#1995178, rhbz#2008333

* Mon Aug 30 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-98
- storage-mon: new resource agent

  Resolves: rhbz#1509319

* Thu Jun 17 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-97
- podman: fix possible race during container creation

  Resolves: rhbz#1972743

* Tue Jun 15 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-96
- LVM-activate: fix drop-in check to avoid re-creating drop-in

  Resolves: rhbz#1972035

* Fri Jun 11 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-95
- lvmlockd: remove cmirrord support, as cmirrord is incompatible w/lvmlockd

  Resolves: rhbz#1969968

* Wed May 12 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-94
- gcp-vpc-move-vip: add retry logic

  Resolves: rhbz#1957765

* Wed Apr 28 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-93
- db2: add PRIMARY/REMOTE_CATCHUP_PENDING/CONNECTED status to promote-check
- pgsqlms: new resource agent
- python-pygments: fix CVE-2021-27291 and CVE-2021-20270

  Resolves: rhbz#1872754, rhbz#1934651, rhbz#1935422, rhbz#1943464

* Thu Apr  8 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-91
- ethmonitor: fix vlan regex
- iface-vlan: make vlan parameter not unique
- nfsserver: error-check unmount
- VirtualDomain: fix pid status regex
- podman: return NOT_RUNNING when monitor cmd fails
- awsvip: dont partially match similar IPs during
- aws agents: dont spam log files
- aws-vpc-move-ip: add ENI lookup

  Resolves: rhbz#1891883, rhbz#1902045, rhbz#1924363, rhbz#1932863
  Resolves: rhbz#1920698, rhbz#1939992, rhbz#1940094, rhbz#1939281

* Mon Mar 22 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-90
- galera/rabbitmq-cluster/redis: run crm_mon without validation when
  running in bundle (1940363)

* Thu Mar 11 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-89
- azure-lb: redirect to avoid nc dying with EPIPE error (1937142)

* Thu Feb 25 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-87
- gcp-vpc-move-route, gcp-vpc-move-vip: add project parameter and
  make vpc_network parameter optional

  Resolves: rhbz#1913932

* Thu Dec  3 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-81
- ocf-shellfuncs: fix traceback redirection for Bash 5+

  Resolves: rhbz#1903677

* Tue Dec  1 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-80
- crypt: support symlink devices, and dont run sanity checks for probes

  Resolves: rhbz#1901357

* Mon Nov 30 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-79
- LVM-activate: add drop-in during start-action to avoid getting
  fenced during reboot

  Resolves: rhbz#1902208

* Wed Nov 25 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-77
- NovaEvacuate: set delay_evacuate to 0 when it's not set

  Resolves: rhbz#1899551

* Tue Nov 24 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-76
- podman: recover from killed conmon process
- podman: recover from podman's storage being out of sync
- crypt: make key_file and crypt_type parameters not unique

  Resolves: rhbz#1886262
  Resolves: rhbz#1900015
  Resolves: rhbz#1898690

* Fri Nov 13 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-75
- AWS agents: add support for IMDSv2

  Resolves: rhbz#1897570

* Wed Nov 11 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-74
- aws-vpc-move-ip: don't warn for expected scenarios

  Resolves: rhbz#1895811

* Mon Nov  2 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-73
- crypt: new resource agent

  Resolves: rhbz#1471182

* Wed Oct 28 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-72
- sybaseASE: Run verify_all() for start operation only
- sybaseASE: add logfile parameter
- galera: set bootstrap attribute before promote
- galera: recover after network split in a 2-node cluster

  Resolves: rhbz#1848025
  Resolves: rhbz#1861001
  Resolves: rhbz#1891835
  Resolves: rhbz#1891855

* Tue Oct 27 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-71
- redis: parse password correctly based on version
- all agents: fix pcs syntax in manpage for pcs 0.10+
- gcp-pd-move: dont stop partially matched "disk_name"

  Resolves: rhbz#1815013
  Resolves: rhbz#1763249
  Resolves: rhbz#1890068

* Wed Oct  7 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-70
- galera: recover from joining a non existing cluster

  Resolves: rhbz#1881114

* Wed Sep 23 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-69
- pgsql: ignore masters re-promote
- pgsql: add PostgreSQL 12 support
- Make Samba/CIFS dependency weak
- Filesystem: Support whitespace in device or directory name
- aws-vpc-move-ip: add region parameter

  Resolves: rhbz#1640587
  Resolves: rhbz#1795535
  Resolves: rhbz#1828600
  Resolves: rhbz#1858752
  Resolves: rhbz#1872999

* Thu Aug 20 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-68
- azure-lb: fix redirect issue

  Resolves: rhbz#1850778

* Wed Aug 19 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-67
- gcp-vpc-move-vip: add support for multiple alias IPs

  Resolves: rhbz#1846733

* Thu Jul 30 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-65
- azure-events: handle exceptions in urlopen

  Resolves: rhbz#1845574

* Mon Jul 27 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-64
- nfsserver: fix NFSv4-only support
- azure-events: new resource agent for Azure

  Resolves: rhbz#1818997
  Resolves: rhbz#1819965

* Thu Jun 25 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-60
- Upgrade bundled python-httplib2 to fix CVE-2020-11078

  Resolves: rhbz#1850990

* Wed Jun 17 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-59
- pgsql: support Pacemaker v2.03+ output

  Resolves: rhbz#1836186

* Thu Jun 11 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-56
- Filesystem: set "fast_stop" default to "no" for GFS2 filesystems

  Resolves: rhbz#1814896

* Wed Jun 10 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-55
- nfsserver: dont log error message when /etc/sysconfig/nfs does not exist
- exportfs: describe clientspec format in metadata

  Resolves: rhbz#1845581
  Resolves: rhbz#1845583

* Tue Jun  9 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-54
- exportfs: add symlink support
- aliyun-vpc-move-ip: log output when failing

  Resolves: rhbz#1820523
  Resolves: rhbz#1843999

* Tue Jun  2 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-53
- podman: force remove container if remove fails

  Resolves: rhbz#1839721

* Thu May 28 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-52
- gcp-pd-move: new resource agent for Google Cloud

  Resolves: rhbz#1633251

* Wed May 27 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-51
- NovaEvacuate: suppress expected initial error message
- db2 (HADR): promote standby node when master node disappears

  Resolves: rhbz#1830716
  Resolves: rhbz#1836945

* Thu May  7 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-50
- rabbitmq-cluster: increase rabbitmqctl wait timeout during start

  Resolves: rhbz#1832321

* Tue Apr 28 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-49
- aws-vpc-route53: new resource agent for AWS
- pgsql: improve checks to prevent incorrect status, and set initial
  score for primary and hot standby

  Resolves: rhbz#1759115
  Resolves: rhbz#1744190

* Mon Apr  6 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-47
- aws-vpc-move-ip: delete remaining route entries

  Resolves: rhbz#1819021

* Fri Mar 27 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-46
- use safe temp file location
- ocf-shellfuncs: ocf_is_clone(): fix to return true when clone-max
  is set to 0

  Resolves: rhbz#1817432
  Resolves: rhbz#1817598

* Wed Mar 18 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-45
- azure-lb: support using socat instead of nc
- aws-vpc-move-ip: add "routing_table_role" parameter
- redis: fix validate-all action and run it during start

  Resolves: rhbz#1804658
  Resolves: rhbz#1810466
  Resolves: rhbz#1792237

* Fri Mar  6 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-44
- lvmlockd: automatically remove locking_type from lvm.conf for LVM
  v2.03+

  Resolves: rhbz#1808468

* Tue Jan 28 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-43
- rabbitmq-cluster: delete nodename when stop fails

  Resolves: rhbz#1792196

* Thu Jan 23 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-42
- IPsrcaddr: add destination and table parameters

  Resolves: rhbz#1744224

* Mon Jan 13 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-40
- podman: improve image exist check
- IPaddr2: add CLUSTERIP not supported info to metadata/manpage
- Filesystem: refresh UUID if block device doesnt exist

  Resolves: rhbz#1788889
  Resolves: rhbz#1767916
  Resolves: rhbz#1777381

* Wed Nov 27 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-38
- IPaddr2: add noprefixroute parameter

  Resolves: rhbz#1741042

* Wed Nov 13 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-36
- exportfs: allow multiple exports with same fsid
- mysql/galera: fix incorrect rc

  Resolves: rhbz#1764888
  Resolves: rhbz#1765128

* Mon Oct 14 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-35
- Route: dont fence when parameters not set
- LVM-activate: add partial-activation support

  Resolves: rhbz#1750261
  Resolves: rhbz#1741843

* Wed Oct  2 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-34
- LVM/clvm: remove manpages for excluded agents
- LVM-activate: return NOT_RUNNING when node rejoins cluster
- LVM-activate: detect systemid volume without reboot
- Filesystem: add symlink support
- Filesystem: avoid corrupt mount-list and dont kill incorrect processes
  for bind-mounts
- IPsrcaddr: make proto optional to fix regression when used without
  NetworkManager
- docker: fix stop issues
- rabbitmq-cluster: also restore users in single node mode
- IPaddr2: sanitize compressed IPv6 IPs
- nfsserver: systemd performance improvements
- NovaEvacuate: add "evacuate_delay" parameter

  Resolves: rhbz#1694392
  Resolves: rhbz#1695039
  Resolves: rhbz#1738428
  Resolves: rhbz#1744103
  Resolves: rhbz#1744140
  Resolves: rhbz#1757837
  Resolves: rhbz#1748768
  Resolves: rhbz#1750352
  Resolves: rhbz#1751700
  Resolves: rhbz#1751962
  Resolves: rhbz#1755760

* Tue Aug 27 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-33
- rabbitmq-cluster: fail monitor when node is in minority partition,
  fix stop regression, retry start when cluster join fails, ensure
  node attributes are removed

  Resolves: rhbz#1745713

* Mon Aug 12 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-32
- mysql/galera: use runuser/su to avoid using DAC_OVERRIDE

  Resolves: rhbz#1692960

* Wed Aug  7 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-31
- podman: add drop-in dependency support

  Resolves: rhbz#1736746

* Wed Jul 31 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-30
- iSCSITarget/iSCSILogicalUnit: only create iqn/acls when it doesnt
  exist

  Resolves: rhbz#1692413

* Tue Jul 30 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-29
- CTDB: add support for v4.9+

  Resolves: rhbz#1732867

* Tue Jul 23 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-28
- podman: fixes to avoid bundle resources restarting when probing
  takes too long
- LVM-activate: fix monitor to avoid hang caused by validate-all call

  Resolves: rhbz#1718219
  Resolves: rhbz#1730455

* Wed Jun 19 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-27
- ocf_log: do not log debug messages when HA_debug unset
- Filesystem: remove notify-action from metadata
- dhcpd keep SELinux context in chroot

  Resolves: rhbz#1707969
  Resolves: rhbz#1717759
  Resolves: rhbz#1719684

* Tue Jun 11 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-26
- sap/sap-hana: split subpackages into separate packages

  Resolves: rhbz#1705767

* Wed May 29 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-24
- Squid: fix PID file issue

  Resolves: rhbz#1689184

* Tue May 28 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-23
- Route: make family parameter optional
- redis: mute password warning

  Resolves: rhbz#1669140
  Resolves: rhbz#1683548

* Thu May 23 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-22
- aws-vpc-move-ip: add multi route-table support and fix issue
  w/multiple NICs

  Resolves: rhbz#1697559

* Fri Apr  5 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-21
- gcp-vpc-move-route/gcp-vpc-move-vip: fix Python 3 encoding issue

  Resolves: rhbz#1695656

* Mon Apr  1 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-20
- aws-vpc-move-ip: use "--query" to avoid a possible race condition
- gcloud-ra: fix Python 3 issue and remove Python 2 detection

  Resolves: rhbz#1693662
  Resolves: rhbz#1691456

* Thu Mar 21 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-19
- Add CI gating tests
- LVM-activate: support LVs from same VG
- tomcat: use systemd when catalina.sh is unavailable
- Fixed python-devel/perl build dependencies

  Resolves: rhbz#1682136
  Resolves: rhbz#1667414
  Resolves: rhbz#1666691
  Resolves: rhbz#1595854

* Thu Mar  7 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-18
- aliyun-vpc-move-ip: exclude from main package
- aliyuncli-ra: upgrade bundled python-aliyun-sdk-core and fix Python 3 issues
- ocf.py: byte compile

  Resolves: rhbz#1677204
  Resolves: rhbz#1677981
  Resolves: rhbz#1678874

* Tue Feb  5 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-17
- LVM-activate: dont require locking_type

  Resolves: rhbz#1658664

* Fri Jan 11 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-16
- vdo-vol: fix monitor-action
- LVM-activate: dont fail initial probe

  Resolves: rhbz#1662466
  Resolves: rhbz#1643307

* Tue Oct 23 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-15
- nfsserver: fix start-issues when nfs_shared_infodir parameter is
  changed

  Resolves: rhbz#1642027

* Mon Oct  8 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-14
- redis: use basename in pidof to avoid issues in containers

  Resolves: rhbz#1635785

* Wed Sep 26 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-11
- Remove grpc from bundle

  Resolves: rhbz#1630627

* Fri Sep 21 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-10
- systemd-tmpfiles: change path to /run/resource-agents

  Resolves: rhbz#1631291

* Fri Aug 24 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-9
- podman: new resource agent

  Resolves: rhbz#1607607

* Wed Aug 22 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-8
- LVM: fix missing dash in activate_options
- LVM-activate: warn about incorrect vg_access_mode
- lvmlockd: add cmirrord support

* Wed Aug  1 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-7
- findif: only match lines containing netmasks

* Mon Jul 30 2018 Florian Weimer <fweimer@redhat.com> - 4.1.1-6
- Rebuild with fixed binutils

* Fri Jul 27 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-5
- vdo-vol: new resource agent

  Resolves: rhbz#1552330

* Wed Jul  4 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-4
- VirtualDomain: add stateless support
- Exclude unsupported agents

* Thu Jun 28 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-3
- Added SAPHana and OpenStack agents

* Fri May 25 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-2
- Remove unsupported clvm and LVM agents

* Tue Mar 13 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-1
- Rebase to resource-agents 4.1.1 upstream release.

* Mon Feb 19 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.0-2
- Add gcc to BuildRequires

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.0-1.1
- Escape macros in %%changelog

* Wed Jan 10 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.0-1
- Rebase to resource-agents 4.1.0 upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.1-1
- Rebase to resource-agents 4.0.1 upstream release.

* Wed Feb  1 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.0-2
- galera: remove "long SST monitoring" support due to corner-case issues

* Tue Jan 31 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.0-1
- Rebase to resource-agents 4.0.0 upstream release.

* Thu Dec 15 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.7-6
- Add netstat dependency

* Tue Feb  9 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.7-4
- Rebase to resource-agents 3.9.7 upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.6-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.6-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 David Vossel <dvossel@redhat.com> - 3.9.6-2
- Rebase to latest upstream code in order to pull in rabbitmq-cluster agent

* Fri Feb 13 2015 David Vossel <dvossel@redhat.com> - 3.9.6-1
- Rebase to resource-agents 3.9.6 upstream release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.5-12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.5-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 David Vossel <dvossel@redhat.com> - 3.9.5-12
- Sync with latest upstream.

* Thu Jan 2 2014 David Vossel <dvossel@redhat.com> - 3.9.5-11
- Sync with latest upstream.

* Sun Oct 20 2013 David Vossel <dvossel@redhat.com> - 3.9.5-10
- Fix build system for rawhide.

* Wed Oct 16 2013 David Vossel <dvossel@redhat.com> - 3.9.5-9
- Remove rgmanager agents from build. 

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.9.5-7
- Perl 5.18 rebuild

* Tue Jun 18 2013 David Vossel <dvossel@redhat.com> - 3.9.5-6
- Restores rsctmp directory to upstream default.

* Tue Jun 18 2013 David Vossel <dvossel@redhat.com> - 3.9.5-5
- Merges redhat provider into heartbeat provider. Remove
  rgmanager's redhat provider.

  Resolves: rhbz#917681
  Resolves: rhbz#928890
  Resolves: rhbz#952716
  Resolves: rhbz#960555

* Tue Mar 12 2013 David Vossel <dvossel@redhat.com> - 3.9.5-3
- Fixes build system error with conditional logic involving
  IPv6addr and updates spec file to build against rhel 7 as
  well as fedora 19.

* Mon Mar 11 2013 David Vossel <dvossel@redhat.com> - 3.9.5-2
- Resolves rhbz#915050

* Mon Mar 11 2013 David Vossel <dvossel@redhat.com> - 3.9.5-1
- New upstream release.

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> - 3.9.2-5
- Fix cifs mount requires

* Mon Nov 12 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-4
- Removed version number after dist

* Mon Oct 29 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-3.8
- Remove cluster-glue-libs-devel
- Disable IPv6addr & sfex to fix deps on libplumgpl & libplum (due to
  disappearance of cluster-glue in F18)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-3.4
- Fix location of lvm (change from /sbin to /usr/sbin)

* Wed Apr 04 2012 Jon Ciesla <limburgher@gmail.com> - 3.9.2-3.3
- Rebuilt to fix rawhide dependency issues (caused by move of fsck from
  /sbin to /usr/sbin).

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 3.9.2-3.1
- libnet rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul  8 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-2
- add post call to resource-agents to integrate with cluster 3.1.4

* Thu Jun 30 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-1
- new upstream release
- fix 2 regressions from 3.9.1

* Mon Jun 20 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.1-1
- new upstream release
- import spec file from upstream

* Tue Mar  1 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.1-1
- new upstream release 3.1.1 and 1.0.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.0-1
- new upstream release
- spec file update:
  Update upstream URL
  Update source URL
  use standard configure macro
  use standard make invokation

* Thu Oct  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.17-1
- new upstream release
  Resolves: rhbz#632595, rhbz#633856, rhbz#632385, rhbz#628013
  Resolves: rhbz#621313, rhbz#595383, rhbz#580492, rhbz#605733
  Resolves: rhbz#636243, rhbz#591003, rhbz#637913, rhbz#634718
  Resolves: rhbz#617247, rhbz#617247, rhbz#617234, rhbz#631943
  Resolves: rhbz#639018

* Thu Oct  7 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.16-2
- new upstream release of the Pacemaker agents: 71b1377f907c

* Thu Sep  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.16-1
- new upstream release
  Resolves: rhbz#619096, rhbz#614046, rhbz#620679, rhbz#619680
  Resolves: rhbz#621562, rhbz#621694, rhbz#608887, rhbz#622844
  Resolves: rhbz#623810, rhbz#617306, rhbz#623816, rhbz#624691
  Resolves: rhbz#622576

* Thu Jul 29 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.14-1
- new upstream release
  Resolves: rhbz#553383, rhbz#557563, rhbz#578625, rhbz#591003
  Resolves: rhbz#593721, rhbz#593726, rhbz#595455, rhbz#595547
  Resolves: rhbz#596918, rhbz#601315, rhbz#604298, rhbz#606368
  Resolves: rhbz#606470, rhbz#606480, rhbz#606754, rhbz#606989
  Resolves: rhbz#607321, rhbz#608154, rhbz#608887, rhbz#609181
  Resolves: rhbz#609866, rhbz#609978, rhbz#612097, rhbz#612110
  Resolves: rhbz#612165, rhbz#612941, rhbz#614127, rhbz#614356
  Resolves: rhbz#614421, rhbz#614457, rhbz#614961, rhbz#615202
  Resolves: rhbz#615203, rhbz#615255, rhbz#617163, rhbz#617566
  Resolves: rhbz#618534, rhbz#618703, rhbz#618806, rhbz#618814

* Mon Jun  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.13-1
- new upstream release
  Resolves: rhbz#592103, rhbz#593108, rhbz#578617, rhbz#594626
  Resolves: rhbz#594511, rhbz#596046, rhbz#594111, rhbz#597002
  Resolves: rhbz#599643

* Tue May 18 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.12-2
- libnet is not available on RHEL
- Do not package ldirectord on RHEL
  Resolves: rhbz#577264

* Mon May 10 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- new upstream release
  Resolves: rhbz#585217, rhbz#586100, rhbz#581533, rhbz#582753
  Resolves: rhbz#582754, rhbz#585083, rhbz#587079, rhbz#588890
  Resolves: rhbz#588925, rhbz#583789, rhbz#589131, rhbz#588010
  Resolves: rhbz#576871, rhbz#576871, rhbz#590000, rhbz#589823

* Mon May 10 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.12-1
- New pacemaker agents upstream release: a7c0f35916bf
  + High: pgsql: properly implement pghost parameter
  + High: RA: mysql: fix syntax error
  + High: SAPInstance RA: do not rely on op target rc when monitoring clones (lf#2371)
  + High: set the HA_RSCTMP directory to /var/run/resource-agents (lf#2378)
  + Medium: IPaddr/IPaddr2: add a description of the assumption in meta-data
  + Medium: IPaddr: return the correct code if interface delete failed
  + Medium: nfsserver: rpc.statd as the notify cmd does not work with -v (thanks to Carl Lewis)
  + Medium: oracle: reduce output from sqlplus to the last line for queries (bnc#567815)
  + Medium: pgsql: implement "config" parameter
  + Medium: RA: iSCSITarget: follow changed IET access policy

* Wed Apr 21 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.11-1
- new upstream release
  Resolves: rhbz#583945, rhbz#581047, rhbz#576330, rhbz#583017
  Resolves: rhbz#583019, rhbz#583948, rhbz#584003, rhbz#582017
  Resolves: rhbz#555901, rhbz#582754, rhbz#582573, rhbz#581533
- Switch to file based Requires.
  Also address several other problems related to missing runtime
  components in different agents.
  With the current Requires: set, we guarantee all basic functionalities
  out of the box for lvm/fs/clusterfs/netfs/networking.
  Resolves: rhbz#570008

* Sat Apr 17 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.10-2
- New pacemaker agents upstream release
  + High: RA: vmware: fix set_environment() invocation (LF 2342)
  + High: RA: vmware: update to version 0.2
  + Medium: Filesystem: prefer /proc/mounts to /etc/mtab for non-bind mounts (lf#2388)
  + Medium: IPaddr2: don't bring the interface down on stop (thanks to Lars Ellenberg)
  + Medium: IPsrcaddr: modify the interface route (lf#2367)
  + Medium: ldirectord: Allow multiple email addresses (LF 2168)
  + Medium: ldirectord: fix setting defaults for configfile and ldirectord (lf#2328)
  + Medium: meta-data: improve timeouts in most resource agents
  + Medium: nfsserver: use default values (lf#2321)
  + Medium: ocf-shellfuncs: don't log but print to stderr if connected to a terminal
  + Medium: ocf-shellfuncs: don't output to stderr if using syslog
  + Medium: oracle/oralsnr: improve exit codes if the environment isn't valid
  + Medium: RA: iSCSILogicalUnit: fix monitor for STGT
  + Medium: RA: make sure that OCF_RESKEY_CRM_meta_interval is always defined (LF 2284)
  + Medium: RA: ManageRAID: require bash
  + Medium: RA: ManageRAID: require bash
  + Medium: RA: VirtualDomain: bail out early if config file can't be read during probe (Novell 593988)
  + Medium: RA: VirtualDomain: fix incorrect use of __OCF_ACTION
  + Medium: RA: VirtualDomain: improve error messages
  + Medium: RA: VirtualDomain: spin on define until we definitely have a domain name
  + Medium: Route: add route table parameter (lf#2335)
  + Medium: sfex: don't use pid file (lf#2363,bnc#585416)
  + Medium: sfex: exit with success on stop if sfex has never been started (bnc#585416)

* Fri Apr  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.10-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#519491, rhbz#570525, rhbz#571806, rhbz#574027
  Resolves: rhbz#574215, rhbz#574886, rhbz#576322, rhbz#576335
  Resolves: rhbz#575103, rhbz#577856, rhbz#577874, rhbz#578249
  Resolves: rhbz#578625, rhbz#578626, rhbz#578628, rhbz#578626
  Resolves: rhbz#579621, rhbz#579623, rhbz#579625, rhbz#579626
  Resolves: rhbz#579059

* Wed Mar 24 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.9-2
- Resolves: rhbz#572993 - Patched build process to correctly generate ldirectord man page
- Resolves: rhbz#574732 - Add libnet-devel as a dependancy to ensure IPaddrv6 is built

* Mon Mar  1 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#455300, rhbz#568446, rhbz#561862, rhbz#536902
  Resolves: rhbz#512171, rhbz#519491

* Mon Feb 22 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.8-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#548133, rhbz#565907, rhbz#545602, rhbz#555901
  Resolves: rhbz#564471, rhbz#515717, rhbz#557128, rhbz#536157
  Resolves: rhbz#455300, rhbz#561416, rhbz#562237, rhbz#537201
  Resolves: rhbz#536962, rhbz#553383, rhbz#556961, rhbz#555363
  Resolves: rhbz#557128, rhbz#455300, rhbz#557167, rhbz#459630
  Resolves: rhbz#532808, rhbz#556603, rhbz#554968, rhbz#555047
  Resolves: rhbz#554968, rhbz#555047
- spec file update:
  * update spec file copyright date
  * use bz2 tarball

* Fri Jan 15 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Add python as BuildRequires

* Mon Jan 11 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#526286, rhbz#533461

* Mon Jan 11 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.6-2
- Update Pacameker agents to upstream version: c76b4a6eb576
  + High: RA: VirtualDomain: fix forceful stop (LF 2283)
  + High: apache: monitor operation of depth 10 for web applications (LF 2234)
  + Medium: IPaddr2: CLUSTERIP/iptables rule not always inserted on failed monitor (LF 2281)
  + Medium: RA: Route: improve validate (LF 2232)
  + Medium: mark obsolete RAs as deprecated (LF 2244)
  + Medium: mysql: escalate stop to KILL if regular shutdown doesn't work

* Mon Dec 7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New rgmanager resource agents upstream release
- spec file update:
  * use global instead of define
  * use new Source0 url
  * use %%name macro more aggressively

* Mon Dec 7 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.5-2
- Update Pacameker agents to upstream version: bc00c0b065d9
  + High: RA: introduce OCF_FUNCTIONS_DIR, allow it to be overridden (LF2239)
  + High: doc: add man pages for all RAs (LF2237)
  + High: syslog-ng: new RA
  + High: vmware: make meta-data work and several cleanups (LF 2212)
  + Medium: .ocf-shellfuncs: add ocf_is_probe function
  + Medium: Dev: make RAs executable (LF2239)
  + Medium: IPv6addr: ifdef out the ip offset hack for libnet v1.1.4 (LF 2034)
  + Medium: add mercurial repository version information to .ocf-shellfuncs
  + Medium: build: add perl-MailTools runtime dependency to ldirectord package (LF 1469)
  + Medium: iSCSITarget, iSCSILogicalUnit: support LIO
  + Medium: nfsserver: use check_binary properly in validate (LF 2211)
  + Medium: nfsserver: validate should not check if nfs_shared_infodir exists (thanks to eelco@procolix.com) (LF 2219)
  + Medium: oracle/oralsnr: export variables properly
  + Medium: pgsql: remove the previous backup_label if it exists
  + Medium: postfix: fix double stop (thanks to Dinh N. Quoc)
  + RA: LVM: Make monitor operation quiet in logs (bnc#546353)
  + RA: Xen: Remove instance_attribute "allow_migrate" (bnc#539968)
  + ldirectord: OCF agent: overhaul

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New rgmanager resource agents upstream release
- Allow pacemaker to use rgmanager resource agents

* Wed Oct 28 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.4-2
- Update Pacameker agents to upstream version: e2338892f59f
  + High: send_arp - turn on unsolicited mode for compatibilty with the libnet version's exit codes
  + High: Trap sigterm for compatibility with the libnet version of send_arp
  + Medium: Bug - lf#2147: IPaddr2: behave if the interface is down
  + Medium: IPv6addr: recognize network masks properly
  + Medium: RA: VirtualDomain: avoid needlessly invoking "virsh define"

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New rgmanager resource agents upstream release

* Mon Oct 12 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.3-3
- Update Pacameker agents to upstream version: 099c0e5d80db
  + Add the ha_parameter function back into .ocf-shellfuncs.
  + Bug bnc#534803 - Provide a default for MAILCMD
  + Fix use of undefined macro @HA_NOARCHDATAHBDIR@
  + High (LF 2138): IPsrcaddr: replace 0/0 with proper ip prefix (thanks to Michael Ricordeau and Michael Schwartzkopff)
  + Import shellfuncs from heartbeat as badly written RAs use it
  + Medium (LF 2173): nfsserver: exit properly in nfsserver_validate
  + Medium: RA: Filesystem: implement monitor operation
  + Medium: RA: VirtualDomain: loop on status if libvirtd is unreachable
  + Medium: RA: VirtualDomain: loop on status if libvirtd is unreachable (addendum)
  + Medium: RA: iSCSILogicalUnit: use a 16-byte default SCSI ID
  + Medium: RA: iSCSITarget: be more persistent deleting targets on stop
  + Medium: RA: portblock: add per-IP filtering capability
  + Medium: mysql-proxy: log_level and keepalive parameters
  + Medium: oracle: drop spurious output from sqlplus
  + RA: Filesystem: allow configuring smbfs mounts as clones

* Wed Sep 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- New rgmanager resource agents upstream release

* Thu Aug 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.1-1
- New rgmanager resource agents upstream release

* Tue Aug 18 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.0-16
- Create an ldirectord package
- Update Pacameker agents to upstream version: 2198dc90bec4
  + Build: Import ldirectord.
  + Ensure HA_VARRUNDIR has a value to substitute
  + High: Add findif tool (mandatory for IPaddr/IPaddr2)
  + High: IPv6addr: new nic and cidr_netmask parameters
  + High: postfix: new resource agent
  + Include license information
  + Low (LF 2159): Squid: make the regexp match more precisely output of netstat
  + Low: configure: Fix package name.
  + Low: ldirectord: add dependency on $remote_fs.
  + Low: ldirectord: add mandatory required header to init script.
  + Medium (LF 2165): IPaddr2: remove all colons from the mac address before passing it to send_arp
  + Medium: VirtualDomain: destroy domain shortly before timeout expiry
  + Medium: shellfuncs: Make the mktemp wrappers work.
  + Remove references to Echo function
  + Remove references to heartbeat shellfuncs.
  + Remove useless path lookups
  + findif: actually include the right header. Simplify configure.
  + ldirectord: Remove superfluous configure artifact.
  + ocf-tester: Fix package reference and path to DTD.

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.0.0-15
- Use bzipped upstream hg tarball.

* Wed Jul 29 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-14
- Merge Pacemaker cluster resource agents:
  * Add Source1.
  * Drop noarch. We have real binaries now.
  * Update BuildRequires.
  * Update all relevant prep/build/install/files/description sections.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-12
- spec file updates:
  * Update copyright header
  * final release.. undefine alphatag

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-11.rc4
- New upstream release.

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-10.rc3
- New upstream release.

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-9.rc2
- New upstream release + git94df30ca63e49afb1e8aeede65df8a3e5bcd0970

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-8.rc1
- New upstream release.
- Update BuildRoot usage to preferred versions/names

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-7.beta1
- New upstream release.

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-6.alpha7
- New upstream release.

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-5.alpha6
- New upstream release.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-4.alpha5
- Drop Conflicts with rgmanager.

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-3.alpha5
- New upstream release.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-2.alpha4
- Add comments on how to build this package.

* Thu Feb  5 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha4
- New upstream release.
- Fix datadir/cluster directory ownership.

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha3
  - Initial packaging
