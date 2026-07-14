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
%global upstream_version fd0720f7

# Whether this platform defaults to using systemd as an init system
# (needs to be evaluated prior to BuildRequires being enumerated and
# installed as it's intended to conditionally select some of these, and
# for that there are only few indicators with varying reliability:
# - presence of systemd-defined macros (when building in a full-fledged
#   environment, which is not the case with ordinary mock-based builds)
# - systemd-aware rpm as manifested with the presence of particular
#   macro (rpm itself will trivially always be present when building)
# - existence of /usr/lib/os-release file, which is something heavily
#   propagated by systemd project
# - when not good enough, there's always a possibility to check
#   particular distro-specific macros (incl. version comparison)
%define systemd_native (%{?_unitdir:1}%{!?_unitdir:0}%{nil \
  } || %{?__transaction_systemd_inhibit:1}%{!?__transaction_systemd_inhibit:0}%{nil \
  } || %(test -f /usr/lib/os-release; test $? -ne 0; echo $?))

# determine the ras-set to process based on configure invokation
%bcond_with rgmanager
%bcond_without linuxha

Name:		resource-agents
Summary:	Open Source HA Reusable Cluster Resource Scripts
Version:	4.10.0
Release:	111%{?rcver:%{rcver}}%{?numcomm:.%{numcomm}}%{?alphatag:.%{alphatag}}%{?dirty:.%{dirty}}%{?dist}.5
License:	GPLv2+ and LGPLv2+
URL:		https://github.com/ClusterLabs/resource-agents
Source0:	%{upstream_prefix}-%{upstream_version}.tar.gz
Patch0: 	nova-compute-wait-NovaEvacuate.patch
Patch1: 	bz1952005-pgsqlms-new-ra.patch
Patch2: 	bz2021125-gcp-ilb-1-fix-log_enable.patch
Patch3: 	bz2021125-gcp-ilb-2-only-check-log_cmd-if-log-enabled.patch
Patch4: 	bz2029796-Route-return-OCF_NOT_RUNNING-missing-route.patch
Patch5: 	bz2029704-1-db2-crm_attribute-use-forever.patch
Patch6: 	bz2029704-2-db2-fixes.patch
Patch7: 	bz2029753-podman-remove-anonymous-volumes.patch
Patch8: 	bz2055016-1-IPsrcaddr-dhcp-warning.patch
Patch9: 	bz2055016-2-IPsrcaddr-error-message-route-not-found.patch
Patch10:	bz2055016-3-IPsrcaddr-fix-indentation.patch
Patch11:	bz2055016-4-IPsrcaddr-fixes.patch
Patch12:	bz2069270-corosync-qnetd-new-ra.patch
Patch13:	bz2065125-LVM-activate-fix-fence-issue.patch
Patch14:	bz2065138-IPaddr2-enable-more-control-for-IPv6-addresses.patch
Patch15:	bz2072371-Filesystem-1-fix-uuid-label-device-whitespace.patch
Patch16:	bz2072371-Filesystem-2-improve-uuid-label-device-logic.patch
Patch17:	bz2083081-bz2083086-bz2083090-bz2083092-update-openstack-agents.patch
Patch18:	bz2081585-NovaEvacuate-add-user_domain-project_domain.patch
Patch19:	bz2094828-lvmlockd-fail-when-use_lvmlockd-not-set.patch
Patch20:	bz2093213-aws-vpc-move-ip-add-interface-label-support.patch
Patch21:	bz2063877-all-agents-use-promotable-terms.patch
Patch22:	bz2083090-openstack-info-fix-bashism.patch
Patch23:	bz2083081-bz2083086-bz2083092-openstack-agents-fixes.patch
Patch24:	bz2083081-bz2083086-bz2083090-bz2083092-openstack-agents-warn-when-openstackcli-slow.patch
Patch25:	bz2083081-bz2083086-bz2083090-bz2083092-openstack-agents-set-domain-parameters-default.patch
Patch26:	bz2103374-ocf-tester-1-update.patch
Patch27:	bz2103374-ocf-tester-2-remove-deprecated-lrmd-lrmadmin-code.patch
Patch28:	bz2110452-ethmonitor-ovsmonitor-pgsql-fix-attrd_updater-q.patch
Patch29:	bz2109161-storage_mon-1-exit-after-help.patch
Patch30:	bz2109161-storage_mon-2-fix-specified-scores-count.patch
Patch31:	bz2109161-storage_mon-3-fix-child-process-exit.patch
Patch32:	bz2109161-storage_mon-4-fix-possible-false-negatives.patch
Patch33:	bz2102126-LVM-activate-fix-return-codes.patch
Patch34:	bz2111147-azure-events-az-new-ra.patch
Patch35:	bz2134411-IPsrcaddr-proto-metric-scope-default-route-fixes.patch
Patch36:	bz2142002-Filesystem-add-support-for-Amazon-EFS.patch
Patch37:	bz2127121-nfsserver-nfsv4_only-parameter.patch
Patch38:	bz2145260-mysql-common-return-error-if-kill-fails.patch
Patch39:	bz2157872-1-all-ras-validate-all-OCF_CHECK_LEVEL-10.patch
Patch40:	bz2157872-2-Filesystem-CTDB-validate-all-improvements.patch
Patch41:	bz2157872-3-pgsqlms-validate-all-OCF_CHECK_LEVEL-10.patch
Patch42:	bz2157872-4-exportfs-pgsql-validate-all-fixes.patch
Patch43:	bz2157872-5-pgsqlms-alidate-all-OCF_CHECK_LEVEL-10.patch
Patch44:	bz2142518-IPaddr2-IPsrcaddr-1-support-policy-based-routing.patch
Patch45:	bz2149968-lvmlockd-add-use_lvmlockd-if-missing.patch
Patch46:	bz2174896-ethmonitor-dont-log-iface-doesnt-exist-monitor.patch
Patch47:	bz2179003-mysql-1-replication-fixes.patch
Patch48:	bz2174911-LVM-activate-failover-with-missing-pvs.patch
Patch49:	bz2182415-azure-events-1-fix-no-transition-summary.patch
Patch50:	bz2182415-azure-events-2-improve-logic.patch
Patch51:	bz2183133-Filesystem-fail-efs-utils-not-installed.patch
Patch52:	bz2184779-Filesystem-systemd-drop-in-net-fs.patch
Patch53:	bz2179003-mysql-2-fix-demoted-score-bounce.patch
Patch54:	bz2142518-IPaddr2-IPsrcaddr-2-fix-table-parameter.patch
Patch55:	bz2207567-Filesystem-1-improve-stop-action.patch
Patch56:	bz2207567-Filesystem-2-fix-incorrect-parameter-types.patch
Patch57:	bz2209433-Delay-1-increase-default-timeouts.patch
Patch58:	bz2209433-Delay-2-remove-incorrect-statement.patch
Patch59:	bz2207567-Filesystem-3-fix-signal_delay-default-value.patch
Patch60:	bz2110038-mysql-common-improve-error-message.patch
Patch61:	rhel-979-storage-mon-1-daemon-mode.patch
Patch62:	rhel-979-storage-mon-2-remove-unnecessary-code.patch
Patch63:	RHEL-15301-1-exportfs-make-fsid-optional.patch
Patch64:	RHEL-15301-2-ocft-exportfs-remove-fsid-required-test.patch
Patch65:	RHEL-15304-1-findif.sh-fix-loopback-handling.patch
Patch66:	RHEL-16247-aws-vpc-move-ip-aws-vpc-route53-awseip-awsvip-auth_type-role.patch
Patch67:	RHEL-17072-1-storage_mon-findif-leak-unitialized-values-EOS-fixes.patch
Patch68:	RHEL-17072-2-storage_mon-use-memset-to-fix-covscan-error.patch
Patch69:	RHEL-15304-2-findif.sh-dont-use-table-parameter.patch
Patch70:	RHEL-31763-galera-fix-joiner-promotion-fails-issue.patch
Patch71:	RHEL-16246-aws-agents-use-curl_retry.patch
Patch72:	RHEL-34777-Filesystem-fail-when-incorrect-device-mounted.patch
Patch73:	RHEL-24683-1-Filesystem-fail-leading-trailing-whitespace.patch
Patch74:	RHEL-24683-2-Filesystem-return-success-stop-action.patch
Patch75:	RHEL-32265-1-findif.sh-fix-corner-cases.patch
Patch76:	RHEL-32265-2-IPsrcaddr-add-IPv6-support.patch
Patch77:	RHEL-32265-3-IPaddr2-only-set-metric-value-for-IPv6-when-detected.patch
Patch78:	RHEL-32265-4-findif.sh-ignore-unreachable-blackhole-prohibit-routes.patch
Patch79:	RHEL-32265-5-IPsrcaddr-specify-dev-for-default-route.patch
Patch80:	RHEL-40393-Filesystem-1-dont-kill-unrelated-processes.patch
Patch81:	RHEL-40393-Filesystem-2-update-bsd-logic.patch
Patch82:	RHEL-32829-db2-fix-OCF_SUCESS-typo.patch
Patch83:	RHEL-43579-galera-mysql-redis-remove-Unpromoted-monitor-action.patch
Patch84:	RHEL-22715-LVM-activate-fix-false-positive.patch
Patch85:	RHEL-58038-Filesystem-dont-sleep-no-processes-only-send-force-net-fs-after-kill.patch
Patch86:	RHEL-59576-Filesystem-try-umount-first-avoid-arguments-list-too-long.patch
Patch87:	RHEL-59172-nfsserver-also-stop-rpc-statd-for-nfsv4_only.patch
Patch88:	RHEL-58008-podman-force-remove-container-if-necessary.patch
Patch89:	RHEL-61888-ocf-shellfuncs-only-create-update-reload-systemd-drop-in-if-needed.patch
Patch90:	RHEL-62200-IPaddr2-improve-fail-logic-check-ip_status-after-adding-IP.patch
Patch91:	RHEL-40589-azure-events-az-update-API-versions-add-retry-for-metadata.patch
Patch92:	RHEL-58632-azure-events-use-node-name-from-cluster.patch
Patch93:	RHEL-42513-1-powervs-subnet-new-ra.patch
Patch94: 	RHEL-66292-1-aws-agents-reuse-imds-token-until-it-expires.patch
Patch95: 	RHEL-66292-2-aws-agents-reuse-imds-token-improvements.patch
Patch96: 	RHEL-68739-awsvip-add-interface-parameter.patch
Patch97:	RHEL-69734-1-openstack-cinder-volume-wait-for-volume-to-be-available.patch
Patch98:	RHEL-69734-2-openstack-cinder-volume-fix-detach-not-working-during-start-action.patch
Patch99:	RHEL-85056-tomcat-fix-CATALINA_PID-not-set-and-parameter-defaults.patch
Patch100: 	RHEL-76038-1-storage-mon-remove-unused-variables.patch
Patch101: 	RHEL-76038-2-storage-mon-fix-daemon-mode-bug-that-caused-delayed-initial-score.patch
Patch102: 	RHEL-76038-3-storage-mon-only-use-underscores-in-functions.patch
Patch103:	RHEL-76038-4-storage-mon-check-if-daemon-is-already-running.patch
Patch104:	RHEL-76038-5-storage-mon-log-storage_mon-is-already-running-in-start-action.patch
Patch105:	RHEL-79819-portblock-fix-version-detection.patch
Patch106:	RHEL-88035-Filesystem-add-support-for-aznfs.patch
Patch107:	RHEL-88429-1-podman-etcd-new-ra.patch
Patch108:	RHEL-88429-2-podman-etcd-remove-unused-actions-from-metadata.patch
Patch109:	RHEL-88429-3-podman-etcd-fix-listen-peer-urls-binding.patch
Patch110:	RHEL-70044-IPaddr2-IPsrcaddr-avoid-duplicate-route-issues.patch
Patch111:	RHEL-7688-IPaddr2-add-link-status-DOWN-LOWERLAYERDOWN-check.patch
Patch112:	RHEL-97123-Filesystem-fix-issue-with-Vormetric-mounts.patch
Patch113:	RHEL-102727-ocf-shellfuncs-remove-extra-sleep-from-curl_retry.patch
Patch114:	RHEL-102610-podman-etcd-add-oom-parameter.patch
Patch115:	RHEL-42513-2-build-dont-build-powervs-subnet-if-dependencies-are-missing.patch
Patch116:	RHEL-114489-1-powervs-move-ip-new-ra.patch
Patch117:	RHEL-114489-2-powervs-move-ip-set-bundled-path.patch
Patch118:	RHEL-115785-RHEL-115782-1-db2-add-skip_basic_sql_health_check-and-monitor-parameters.patch
Patch119:	RHEL-113767-podman-etcd-wrap-ipv6-address-in-brackets.patch
Patch120:	RHEL-113766-podman-etcd-preserve-containers-for-debugging.patch
Patch121:	RHEL-116206-podman-etcd-add-cluster-wide-force_new_cluster-attribute-check.patch
Patch122:	RHEL-116151-1-ocf-shellfuncs-add-ocf_promotion_score.patch
Patch123:	RHEL-116151-2-portblock-add-promotable-support.patch
Patch124:	RHEL-116151-3-portblock-fixes-add-method-and-status_check-parameters.patch
Patch125:	RHEL-119495-podman-etcd-add-automatic-learner-member-promotion.patch
Patch126:	RHEL-118624-db2-use-reintegration-flag-to-avoid-race-condition-on-cluster-reintegration.patch
Patch127:	RHEL-123887-podman-etcd-certificate-rotation.patch
Patch128:	RHEL-123906-podman-etcd-compute-dynamic-revision-bump-from-maxRaftIndex.patch
Patch129:	RHEL-115785-RHEL-115782-2-db2-fix-variable-name.patch
Patch130:	RHEL-118621-MailTo-add-s-nail-support-for-multiple-recipients.patch
Patch131:	RHEL-64949-oracle-improve-monpassword-description.patch
Patch132:	RHEL-109485-1-nfsserver-support-non-clustered-kerberized-mounts.patch
Patch133:	RHEL-109485-2-nfsserver-fix-error-message.patch
Patch134:	RHEL-114489-3-powervs-move-ip-add-iflabel-parameter.patch
Patch135:	RHEL-127006-storage_mon-fix-handling-of-4k-block-devices.patch
Patch136:	RHEL-127891-podman-etcd-exclude-stopping-resources-from-active-count.patch
Patch137:	RHEL-126087-1-podman-etcd-add-container-crash-detection-with-coordinated-recovery.patch
Patch138:	RHEL-121986-Filesystem-speed-up-get-PIDs.patch
Patch139:	RHEL-130580-1-podman-etcd-prevent-last-active-member-from-leaving.patch
Patch140:	RHEL-130580-2-podman-etcd-remove-test-code.patch
Patch141:	RHEL-126087-2-podman-etcd-fix-count-of-fnc-holders-in-container_health_check.patch
Patch142:	RHEL-131185-podman-etcd-prevent-learner-from-starting-before-cluster-is-ready.patch
Patch143:	RHEL-132052-podman-etcd-prevent-retries-on-fatal-errors.patch
Patch144:	RHEL-133937-podman-etcd-align-variable-names-with-etcd-3.6-pod-manifest.patch
Patch145:	RHEL-139519-podman-etcd-verify-no-containers-running-or-being-deleted.patch
Patch146:	RHEL-42513-powervs-subnet-wait-for-IP.patch
Patch147:	RHEL-143527-powervs-move-ip-powervs-subnet-fix-error-logging.patch
Patch148:	RHEL-145628-podman-etcd-enhance-etcd-data-backup-with-snapshots-and-retention.patch
Patch149:	RHEL-150700-podman-etcd-set-attributes-if-they-fail-during-force-new-cluster.patch
Patch150:	RHEL-151828-portblock-check-inverse-action.patch
Patch151:	RHEL-156808-podman-etcd-ignore-learners-when-considering-which-node-has-higher-revision.patch
Patch152:	RHEL-157145-podman-etcd-handle-existing-peer-URLs-gracefully-during-force_new_cluster-recovery.patch
Patch153:	RHEL-159202-podman-etcd-hardened-monitor-stop-actions.patch
Patch154:	RHEL-157273-db2-set-reintegration-when-promotion-is-successful.patch
Patch155:	RHEL-166183-1-db2-fix-bashism.patch
Patch156:	RHEL-166183-2-db2-do-not-use-db2stop-to-avoid-divergence-in-the-log.patch
Patch157:	RHEL-177849-podman-etcd-fix-port-2380-binding-race.patch
Patch158:	RHEL-177838-podman-etcd-fix-machine-deletion-deadlock.patch
Patch159:	RHEL-177843-podman-etcd-fix-learner-start-deadlock.patch
Patch160:	RHEL-188107-podman-etcd-remove-cert-monitoring.patch

# bundled ha-cloud-support libs
Patch500:	ha-cloud-support-aliyun.patch
Patch501:	ha-cloud-support-gcloud.patch
Patch502:	ha-cloud-support-ibm.patch

Obsoletes:	heartbeat-resources <= %{version}
Provides:	heartbeat-resources = %{version}

# Build dependencies
BuildRequires: make
BuildRequires: automake autoconf pkgconfig gcc
BuildRequires: libxslt glib2-devel libqb-devel
BuildRequires: systemd
BuildRequires: which

%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
BuildRequires: python3-devel
%else
BuildRequires: python-devel
%endif

# for pgsqlms
BuildRequires: perl-devel perl-English perl-FindBin

%ifarch x86_64 ppc64le
BuildRequires: ha-cloud-support
%endif

%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
BuildRequires: docbook-style-xsl docbook-dtds
%if 0%{?rhel} == 0
BuildRequires: libnet-devel
%endif
%endif

%if 0%{?suse_version}
BuildRequires:  libnet-devel
BuildRequires:  libglue-devel
BuildRequires:  libxslt docbook_4 docbook-xsl-stylesheets
%endif

## Runtime deps
# system tools shared by several agents
Requires: /bin/bash /usr/bin/grep /bin/sed /bin/gawk
Requires: /bin/ps /usr/bin/pkill /usr/bin/hostname /usr/bin/netstat
Requires: /usr/sbin/fuser /bin/mount
Requires: which

# Filesystem / fs.sh / netfs.sh
Requires: /sbin/fsck
Requires: /usr/sbin/fsck.ext2 /usr/sbin/fsck.ext3 /usr/sbin/fsck.ext4
Requires: /usr/sbin/fsck.xfs
%if 0%{?fedora} > 40 || 0%{?rhel} > 9 || 0%{?suse_version}
Recommends: /usr/sbin/mount.nfs /usr/sbin/mount.nfs4
%else
%if 0%{?rhel} > 8
Recommends: /sbin/mount.nfs /sbin/mount.nfs4
%else
Requires: /sbin/mount.nfs /sbin/mount.nfs4
%endif
%endif
%if (0%{?fedora} && 0%{?fedora} < 33) || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
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
%if 0%{?fedora} > 40 || 0%{?rhel} > 9 || 0%{?suse_version}
Recommends: /usr/sbin/rpc.statd
%else
%if 0%{?rhel} > 8
Recommends: /sbin/rpc.statd
%else
Requires: /sbin/rpc.statd
%endif
%endif
%if 0%{?fedora} > 40 || 0%{?rhel} > 8 || 0%{?suse_version}
Recommends: /usr/sbin/rpc.nfsd /usr/sbin/rpc.mountd
%else
Requires: /usr/sbin/rpc.nfsd /usr/sbin/rpc.mountd
%endif

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

%ifarch x86_64 ppc64le
%package cloud
License:	GPLv2+ and LGPLv2+
Summary:	Cloud resource agents
Requires:	%{name} = %{version}-%{release}
Requires:	ha-cloud-support >= 4.10.0-110.el9_8.1
Requires:	socat
Provides:	resource-agents-aliyun
Obsoletes:	resource-agents-aliyun <= %{version}
Provides:	resource-agents-gcp
Obsoletes:	resource-agents-gcp <= %{version}

%description cloud
Cloud resource agents allows Cloud instances to be managed
in a cluster environment.
%endif

%package paf
License:	PostgreSQL
Summary:	PostgreSQL Automatic Failover (PAF) resource agent
Requires:	%{name} = %{version}-%{release}
Requires:	perl-interpreter perl-lib perl-English perl-FindBin

%description paf
PostgreSQL Automatic Failover (PAF) resource agents allows PostgreSQL
databases to be managed in a cluster environment.

%prep
%if 0%{?suse_version} == 0 && 0%{?fedora} == 0 && 0%{?centos} == 0 && 0%{?rhel} == 0
%{error:Unable to determine the distribution/version. This is generally caused by missing /etc/rpm/macros.dist. Please install the correct build packages or define the required macros manually.}
exit 1
%endif
%setup -q -n %{upstream_prefix}-%{upstream_version}
%patch -p1 -P 0 -F1
%patch -p1 -P 1
%patch -p1 -P 2
%patch -p1 -P 3
%patch -p1 -P 4
%patch -p1 -P 5
%patch -p1 -P 6
%patch -p1 -P 7
%patch -p1 -P 8
%patch -p1 -P 9
%patch -p1 -P 10
%patch -p1 -P 11
%patch -p1 -P 12
%patch -p1 -P 13
%patch -p1 -P 14
%patch -p1 -P 15
%patch -p1 -P 16
%patch -p1 -P 17
%patch -p1 -P 18
%patch -p1 -P 19
%patch -p1 -P 20
%patch -p1 -P 21
%patch -p1 -P 22
%patch -p1 -P 23
%patch -p1 -P 24
%patch -p1 -P 25
%patch -p1 -P 26
%patch -p1 -P 27
%patch -p1 -P 28
%patch -p1 -P 29
%patch -p1 -P 30
%patch -p1 -P 31
%patch -p1 -P 32
%patch -p1 -P 33
%patch -p1 -P 34
%patch -p1 -P 35
%patch -p1 -P 36
%patch -p1 -P 37
%patch -p1 -P 38
%patch -p1 -P 39
%patch -p1 -P 40
%patch -p1 -P 41
%patch -p1 -P 42
%patch -p1 -P 43
%patch -p1 -P 44
%patch -p1 -P 45
%patch -p1 -P 46
%patch -p1 -P 47
%patch -p1 -P 48
%patch -p1 -P 49
%patch -p1 -P 50
%patch -p1 -P 51
%patch -p1 -P 52
%patch -p1 -P 53
%patch -p1 -P 54
%patch -p1 -P 55
%patch -p1 -P 56
%patch -p1 -P 57
%patch -p1 -P 58
%patch -p1 -P 59
%patch -p1 -P 60
%patch -p1 -P 61
%patch -p1 -P 62
%patch -p1 -P 63
%patch -p1 -P 64
%patch -p1 -P 65
%patch -p1 -P 66
%patch -p1 -P 67
%patch -p1 -P 68
%patch -p1 -P 69
%patch -p1 -P 70
%patch -p1 -P 71
%patch -p1 -P 72
%patch -p1 -P 73
%patch -p1 -P 74
%patch -p1 -P 75
%patch -p1 -P 76
%patch -p1 -P 77
%patch -p1 -P 78
%patch -p1 -P 79
%patch -p1 -P 80
%patch -p1 -P 81
%patch -p1 -P 82
%patch -p1 -P 83
%patch -p1 -P 84
%patch -p1 -P 85
%patch -p1 -P 86
%patch -p1 -P 87
%patch -p1 -P 88
%patch -p1 -P 89
%patch -p1 -P 90
%patch -p1 -P 91
%patch -p1 -P 92
%patch -p1 -P 93
%patch -p1 -P 94
%patch -p1 -P 95
%patch -p1 -P 96
%patch -p1 -P 97
%patch -p1 -P 98
%patch -p1 -P 99
%patch -p1 -P 100
%patch -p1 -P 101
%patch -p1 -P 102
%patch -p1 -P 103
%patch -p1 -P 104
%patch -p1 -P 105
%patch -p1 -P 106
%patch -p1 -P 107 -F1
%patch -p1 -P 108
%patch -p1 -P 109
%patch -p1 -P 110
%patch -p1 -P 111
%patch -p1 -P 112
%patch -p1 -P 113
%patch -p1 -P 114
%patch -p1 -P 115 -F2
%patch -p1 -P 116
%patch -p1 -P 117
%patch -p1 -P 118
%patch -p1 -P 119
%patch -p1 -P 120
%patch -p1 -P 121
%patch -p1 -P 122
%patch -p1 -P 123
%patch -p1 -P 124
%patch -p1 -P 125
%patch -p1 -P 126
%patch -p1 -P 127
%patch -p1 -P 128
%patch -p1 -P 129
%patch -p1 -P 130
%patch -p1 -P 131
%patch -p1 -P 132
%patch -p1 -P 133
%patch -p1 -P 134
%patch -p1 -P 135
%patch -p1 -P 136
%patch -p1 -P 137 -F2
%patch -p1 -P 138
%patch -p1 -P 139
%patch -p1 -P 140
%patch -p1 -P 141
%patch -p1 -P 142
%patch -p1 -P 143
%patch -p1 -P 144
%patch -p1 -P 145
%patch -p1 -P 146
%patch -p1 -P 147
%patch -p1 -P 148
%patch -p1 -P 149
%patch -p1 -P 150
%patch -p1 -P 151
%patch -p1 -P 152
%patch -p1 -P 153
%patch -p1 -P 154
%patch -p1 -P 155
%patch -p1 -P 156
%patch -p1 -P 157
%patch -p1 -P 158
%patch -p1 -P 159
%patch -p1 -P 160

# bundled ha-cloud-support libs
%patch -p1 -P 500
%patch -p1 -P 501
%patch -p1 -P 502

chmod 755 heartbeat/nova-compute-wait
chmod 755 heartbeat/NovaEvacuate
chmod 755 heartbeat/pgsqlms

%build
sed -i -e "s/#PYTHON3_VERSION#/%{python3_version}/" heartbeat/*.in

if [ ! -f configure ]; then
	./autogen.sh
fi

%if 0%{?fedora} >= 11 || 0%{?centos} > 5 || 0%{?rhel} > 5
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

%configure \
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
	PYTHON="%{__python3}" \
%endif
%ifarch x86_64
	PYTHONPATH="%{_usr}/lib/fence-agents/support/google/lib/python%{python3_version}/site-packages" \
%endif
%ifarch ppc64le
	PYTHONPATH="%{_usr}/lib/fence-agents/support/ibm/lib/python%{python3_version}/site-packages" \
%endif
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

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

## tree fixup
# remove docs (there is only one and they should come from doc sections in files)
rm -rf %{buildroot}/usr/share/doc/resource-agents

%files
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
%exclude /usr/lib/ocf/resource.d/heartbeat/aws*
%exclude /usr/lib/ocf/resource.d/heartbeat/azure-*
%exclude %{_mandir}/man7/*aliyun-vpc-move-ip*
%exclude /usr/lib/ocf/resource.d/heartbeat/gcp*
%exclude %{_mandir}/man7/*gcp*
%exclude /usr/lib/ocf/resource.d/heartbeat/powervs-*
%exclude %{_mandir}/man7/*powervs-*
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
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/IPaddr
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
%exclude %{_usr}/lib/ocf/resource.d/heartbeat/docker*
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
%exclude %{_mandir}/man7/ocf_heartbeat_docker*.7.gz
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
%exclude %{_sysconfdir}/init.d/ldirectord
%exclude %{_sysconfdir}/rc.d/init.d/ldirectord
%exclude %{_unitdir}/ldirectord.service
%exclude /etc/logrotate.d/ldirectord
%exclude /usr/sbin/ldirectord
%exclude %{_mandir}/man8/ldirectord.8.gz

# For compatability with pre-existing agents
%dir %{_sysconfdir}/ha.d
%{_sysconfdir}/ha.d/shellfuncs

%{_libexecdir}/heartbeat
%endif

%ifarch x86_64 ppc64le
%files cloud
%ifarch x86_64
/usr/lib/ocf/resource.d/heartbeat/aliyun-*
%{_mandir}/man7/*aliyun-*
/usr/lib/ocf/resource.d/heartbeat/aws*
%{_mandir}/man7/*aws*
/usr/lib/ocf/resource.d/heartbeat/azure-*
%{_mandir}/man7/*azure-*
/usr/lib/ocf/resource.d/heartbeat/gcp-*
%{_mandir}/man7/*gcp-*
%exclude /usr/lib/ocf/resource.d/heartbeat/gcp-vpc-move-ip
%exclude %{_mandir}/man7/*gcp-vpc-move-ip*
%endif
%ifarch ppc64le
/usr/lib/ocf/resource.d/heartbeat/powervs-*
%{_mandir}/man7/*powervs-*
%endif
%endif

%files paf
%doc paf_README.md
%license paf_LICENSE
%defattr(-,root,root)
%{_usr}/lib/ocf/resource.d/heartbeat/pgsqlms
%{_mandir}/man7/*pgsqlms*
%{_usr}/lib/ocf/lib/heartbeat/OCF_*.pm

%changelog
* Thu Jun 25 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-111.5
- podman-etcd: remove cert monitoring

  Resolves: RHEL-188107

* Wed May 20 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-111.4
- podman-etcd: fix port 2380 binding race
- podman-etcd: fix machine deletion deadlock
- podman-etcd: fix learner start deadlock

  Resolves: RHEL-177849, RHEL-177838, RHEL-177843

* Mon Apr 20 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-111.3
- Cloud agents: change bundled lib paths to match changes in
  ha-cloud-support

  Resolves: RHEL-168565

* Fri Apr 10 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-111.2
- db2: do not use db2stop to avoid divergence in the log

  Resolves: RHEL-166183

* Wed Apr  8 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-111.1
- portblock: check inverse action state file for non-promotable
  resources to avoid issues when doing e.g. block followed by unblock
- podman-etcd: ignore learners when considering which node has higher revision
- podman-etcd: handle existing peer URLs gracefully during force_new_cluster recovery
- podman-etcd: hardened monitor/stop actions
- db2: set reintegration when promotion is successful

  Resolves: RHEL-151828, RHEL-156808, RHEL-157145, RHEL-159202, RHEL-157273

* Fri Mar  6 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-108
- podman-etcd: set attributes if they fail during force-new-cluster

  Resolves: RHEL-150700

* Wed Feb  4 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-107
- podman-etcd: enhance etcd data backup with snapshots and retention

  Resolves: RHEL-145628

* Thu Jan 22 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-106
- powervs-move-ip/powervs-subnet: fix error logging

  Resolves: RHEL-143527

* Wed Jan 14 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-105
- powervs-subnet: new resource agent

  Resolves: RHEL-42513

* Thu Jan  8 2026 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-104
- podman-etcd: verify that no static pod containers are running or
  being deleted before starting

  Resolves: RHEL-139519

* Mon Dec  8 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-103
- podman-etcd: align environment variable names with Etcd v3.6 Pod
  manifest

  Resolves: RHEL-133937

* Tue Dec  2 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-102
- podman-etcd: prevent retries on fatal errors

  Resolves: RHEL-132052

* Thu Nov 27 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-101
- podman-etcd: prevent learner from starting before cluster is ready

  Resolves: RHEL-131185

* Tue Nov 25 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-100
- podman-etcd: add container crash detection with coordinated recovery

  Resolves: RHEL-126087

* Mon Nov 24 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-99
- podman-etcd: prevent last active member from leaving the etcd member
  list

  Resolves: RHEL-130580

* Thu Nov 20 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-98
- Filesystem: speed up get PIDs

  Resolves: RHEL-121986

* Thu Nov 13 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-97
- podman-etcd: exclude stopping resources from active count

  Resolves: RHEL-127891

* Mon Nov 10 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-96
- storage_mon: fix handling of 4k block devices

  Resolves: RHEL-127006

* Mon Nov  3 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-95
- powervs-move-ip: new resource agent

  Resolves: RHEL-114489

* Fri Oct 31 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-94
- nfsserver: add ability to set e.g. "pipefs-directory=/run/nfs/rpc_pipefs"
  in /etc/nfs.conf to avoid issues with non-clustered Kerberized mounts

  Resolves: RHEL-109485

* Wed Oct 29 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-92
- MailTo: add s-nail support for multiple recipients
- oracle: improve monpassword description

  Resolves: RHEL-118621, RHEL-64949

* Wed Oct 29 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-91
- db2: add "skip_basic_sql_health_check" parameter to avoid failing on
  systems with high load
- db2: add "monitor_retries", "monitor_sleep", and "monitor_retry_all_errors"
  parameters to be able to avoid failing on first try

  Resolves: RHEL-115785, RHEL-115782

* Tue Oct 28 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-90
- podman-etcd: add support for cert rotation
- podman-etcd: compute dynamic revision bump from maxRaftIndex

  Resolves: RHEL-123887, RHEL-123906

* Wed Oct 22 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-89
- portblock: add promotable support, and method and status_check
  parameters
- db2: use reintegration flag to avoid race condition on cluster
  reintegration

  Resolves: RHEL-116151, RHEL-118624

* Thu Oct  9 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-88
- podman-etcd: add automatic learner member promotion

  Resolves: RHEL-119495

* Wed Oct  8 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-87
- build: make nfs-utils a weak dependency

  Resolves: RHEL-116100

* Mon Sep 22 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-85
- podman-etcd: wrap ipv6 address in brackets
- podman-etcd: preserve containers for debugging
- podman-etcd: add cluster-wide force_new_cluster attribute check

  Resolves: RHEL-113767, RHEL-113766, RHEL-116206

* Tue Sep  9 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-81
- podman-etcd: add oom parameter to be able to tune the Out-Of-Memory (OOM)
  score for etcd containers

  Resolves: RHEL-102610

* Tue Jul 15 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-80
- ocf-shellfuncs/AWS agents: dont sleep after the final try in
  curl_retry()

  Resolves: RHEL-102727

* Thu Jul  3 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-78
- Filesystem: fix issue with Vormetric mounts

  Resolves: RHEL-97123

* Tue Jun 17 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-77
- IPaddr2/IPsrcaddr: fix to avoid duplicate route issues
- IPaddr2: add link status DOWN/LOWERLAYERDOWN check

  Resolves: RHEL-70044, RHEL-7688

* Tue May 20 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-76
- podman-etcd: new resource agent

  Resolves: RHEL-88429

* Tue Apr 22 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-74
- Filesystem: add support for aznfs

  Resolves: RHEL-88035

* Wed Apr  9 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-73
- storage-mon: fix daemon mode bug that caused delayed initial score
- portblock: fix iptables version detection

  Resolves: RHEL-76038, RHEL-79819

* Tue Apr  1 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-72
- tomcat: fix CATALINA_PID not set, and catalina_base and catalina_out
  parameter defaults

  Resolves: RHEL-85056

* Fri Jan 10 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-71
- openstack-cinder-volume: wait for volume to be available

  Resolves: RHEL-69734

* Wed Nov 27 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-69
- AWS agents: reuse IMDS token until it expires
- awsvip: add interface parameter

  Resolves: RHEL-66292
  Resolves: RHEL-68739

* Wed Oct 23 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-68
- powervs-subnet: new resource agent

  Resolves: RHEL-42513

* Mon Oct 14 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-67
- ocf-shellfuncs: only create/update and reload systemd drop-in if
  needed
- IPaddr2: improve fail logic and check ip_status after adding IP
- azure-events-az: update API versions, and add retry functionality
  for metadata requests
- azure-events*: use node name from cluster instead of hostname to
  avoid failing if they're not the same

  Resolves: RHEL-61888
  Resolves: RHEL-62200
  Resolves: RHEL-40589
  Resolves: RHEL-58632

* Wed Oct  2 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-66
- nfsserver: also stop rpc-statd for nfsv4_only to avoid stop failing
  in some cases
- podman: force-remove containers in stopping state if necessary

  Resolves: RHEL-59172
  Resolves: RHEL-58008

* Wed Sep 25 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-65
- Filesystem: dont sleep during stop-action when there are no
  processes to kill, and only use force argument for network
  filesystems after sending kill_signals
- Filesystem: try umount first during stop-action, and avoid potential
  "Argument list too long" for force_unmount=safe
- AWS agents: use awscli2

  Resolves: RHEL-58038
  Resolves: RHEL-59576
  Resolves: RHEL-46233

* Thu Aug 29 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-64
- IPsrcaddr: add IPv6 support

  Resolves: RHEL-32265

* Tue Aug 13 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-61
- LVM-activate: fail when both "system_id_source" and "volume_list"
  are set in lvm.conf to avoid false positive activation of the VG

  Resolves: RHEL-22715

* Fri Jun 28 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-60
- galera/mysql/redis: remove Unpromoted monitor-action

  Resolves: RHEL-43579

* Tue Jun 25 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-59
- Filesystem: fail when leading or trailing whitespace is present in
  device or directory parameters

  Resolves: RHEL-24683

* Tue Jun 11 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-58
- Filesystem: dont kill unrelated processes during stop-action
- db2: fix OCF_SUCESS typo

  Resolves: RHEL-40393
  Resolves: RHEL-32829

* Wed May 15 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-57
- Filesystem: fail when incorrect device mounted on mountpoint, and
  dont unmount the mountpoint in this case, or if mountpoint set to "/"

  Resolves: RHEL-34777

* Tue Apr 30 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-56
- AWS agents: retry failed metadata requests to avoid instantly
  failing when there is a hiccup in the network or metadata service

  Resolves: RHEL-16246

* Wed Apr 10 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-54
- galera: fix issue where joiner promotion fails is the node reports
  being in non-primary state

  Resolves: RHEL-31763

* Wed Mar  6 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-53
- aliyun-vpc-move-ip: use new aliyun-cli

  Resolves: RHEL-26666

* Thu Feb  8 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-52
- findif.sh: fix loopback IP handling

  Resolves: RHEL-15304

* Wed Nov 22 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-51
- storage_mon/findif: fix handler out of scope leak, unitialized value
  and check that netmaskbits != EOS

  Resolves: RHEL-17072

* Fri Nov 17 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-49
- aws-vpc-move-ip/aws-vpc-route53/awseip/awsvip: add auth_type parameter
  and AWS Policy based authentication type

  Resolves: RHEL-16247

* Thu Nov  2 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-47
- exportfs: make "fsid" parameter optional

  Resolves: RHEL-15301

* Mon Oct  2 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-46
- storage-mon: add daemon-mode to deal with I/O hangs

  Resolves: RHEL-979

* Wed Sep  6 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-44
- mysql-common: improve error message

  Resolves: rhbz#2110038

* Thu Jul 20 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-43
- Filesystem: improve stop-action and allow setting term/kill signals
  and signal_delay for large filesystems

  Resolves: rhbz#2207567

* Tue Jul 18 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-42
- Delay: increase stop, status and monitor timeouts to 40s to avoid
  failing with default values

  Resolves: rhbz#2209433

* Wed Jun 21 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-40
- IPaddr2/IPsrcaddr: support policy-based routing

  Resolves: rhbz#2142518

* Wed Jun 14 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-39
- mysql: fix replication issues

  Resolves: rhbz#2179003

* Mon May 22 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-38
- resource-agents-paf: add perl-lib dependency
- Filesystem: create systemd drop-in for network filesystems

  Resolves: rhbz#2203813
  Resolves: rhbz#2184779

* Mon May  1 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-37
- azure-events*: fix for no "Transition Summary" for Pacemaker 2.1+
- Filesystem: fail if AWS efs-utils not installed when fstype=efs

  Resolves: rhbz#2182415
  Resolves: rhbz#2183133

* Tue Mar 21 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-36
- LVM-activate: failover with missing PVs

  Resolves: rhbz#2174911

* Tue Mar 21 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-35
- lvmlockd: add "use_lvmlockd = 1" if it's commented out or missing
- ethmonitor: dont log "Interface does not exist" for monitor-action

  Resolves: rhbz#2149968
  Resolves: rhbz#2174896

* Wed Jan 25 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-34
- all agents: dont check notify/promotable settings during
  validate-action

  Resolves: rhbz#2157872

* Thu Nov 24 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-28
- mysql-common: return error in stop-action if kill fails to stop
  the process, so the node can get fenced

  Resolves: rhbz#2145260

* Tue Nov 22 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-27
- nfsserver: add nfsv4_only parameter to make it run without
  rpc-statd/rpcbind services

  Resolves: rhbz#2127121

* Mon Nov 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-26
- Filesystem: add support for Amazon EFS (Elastic File System)

  Resolves: rhbz#2142002

* Fri Oct 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-25
- IPsrcaddr: proto, metric, scope and default route fixes

  Resolves: rhbz#2134411

* Thu Sep  8 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-24
- storage_mon: fix specified scores count and possible false negatives
- LVM-activate: use correct return codes to fix unexpected behaviour
- azure-events-az: new resource agent

  Resolves: rhbz#2109161
  Resolves: rhbz#2102126
  Resolves: rhbz#2111147

* Tue Jul 26 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-23
- ethmonitor/pgsql: remove attrd_updater "-q" parameter to solve issue
  with Pacemaker 2.1.3+ not ignoring it

  Resolves: rhbz#2110452

* Thu Jul 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-22
- ocf-tester: add testing tool

  Resolves: rhbz#2103374

* Thu Jul 14 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-20
- openstack-cinder-volume/openstack-floating-ip/openstack-info/
  openstack-virtual-ip: new resource agents

  Resolves: rhbz#2083081, rhbz#2083086, rhbz#2083090, rhbz#2083092

* Mon Jun 20 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-18
- all agents: use promotable terms

  Resolves: rhbz#2063877

* Thu Jun  9 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-17
- lvmlockd: fail when use_lvmlockd has not been set
- aws-vpc-move-ip: add interface label support

  Resolves: rhbz#2094828
  Resolves: rhbz#2093213

* Tue May 17 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-15
- NovaEvacuate: add user_domain and project_domain parameters

  Resolves: rhbz#2081585

* Thu Apr 21 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-12
- Filesystem: fix UUID/label device support when there's whitespace
  between parameter and UUID/label

  Resolves: rhbz#2072371

* Tue Apr  5 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-11
- LVM-activate: use correct return code to fence failed node
- IPaddr2: enable more control for IPv6 addresses

  Resolves: rhbz#2065125
  Resolves: rhbz#2065138

* Tue Mar 29 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-10
- corosync-qnetd: new resource agent
- spec: remove Samba/CIFS dependency

  Resolves: rhbz#2069270
  Resolves: rhbz#1826455

* Thu Mar  3 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-8
- IPsrcaddr: add warning about possible issues when used with DHCP,
  and add error message when matching route not found

  Resolves: rhbz#2055016

* Wed Feb 23 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-7
- db2: use -l forever to fix crm_attribute issue

  Resolves: rhbz#2029704

* Wed Jan  5 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-5
- podman: remove anonymous volumes

  Resolves: rhbz#2029753

* Tue Dec  7 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-4
- Route: return OCF_NOT_RUNNING for probe action when interface
  or route doesnt exist

  Resolves: rhbz#2029796

* Tue Nov  9 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-3
- gcp-ilb: new resource agent

  Resolves: rhbz#2021125

* Wed Nov  3 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.10.0-1
- Rebase to resource-agents 4.10.0 upstream release.
- nfsserver: add nfs_server_scope parameter

  Resolves: rhbz#1995918
  Resolves: rhbz#2015171

* Thu Oct  7 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.9.0-2
- Rebase to resource-agents 4.9.0 upstream release.
- Add "which" dependency
- All agents: set correct agent and OCF version in metadata

  Resolves: rhbz#1995918
  Resolves: rhbz#2011142
  Resolves: rhbz#2003118

* Thu Aug 26 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-13
- nfsnotify: fix default value for "notify_args"

  Resolves: rhbz#1998039

* Wed Aug 25 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-12
- Create cloud subpackage
- Add nova-compute-wait/NovaEvacuate
- nfsserver: fix nfs-convert issue

  Resolves: rhbz#1997548, rhbz#1997576, rhbz#1991855

* Mon Aug 16 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-11
- Filesystem: force_unmount: remove "Default value" text from metadata

  Resolves: rhbz#1993900

* Tue Aug 10 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-10
- pgsqlms: new resource agent

  Resolves: rhbz#1952005

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 4.8.0-8.1
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 29 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-8
- Exclude SAP agents that are in separate -sap subpackage

  Resolves: rhbz#1977208

* Mon May 17 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-3
- Remove redhat-lsb-core dependency (lsb_release)

  Resolves: rhbz#1961539

* Wed Apr 21 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.8.0-2
- Solve build issues

  Resolves: rhbz#1951253

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 4.8.0-1.1
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 16 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.0-7
- Filesystem: change force_unmount default to safe for RHEL9+ (1843578)

* Wed Mar  3 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.0-5
- Exclude unsupported agents

* Wed Feb 24 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.0-4
- remove ldirectord subpackage

  Resolves: rhbz#1932218

* Tue Feb 16 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.0-3
- add BuildRequires for google lib
- use HA cloud support supplied awscli

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.7.0-1
- Rebase to resource-agents 4.7.0 upstream release.

* Mon Aug 24 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.6.1-4
- spec: improvements from upstream project

* Mon Aug 24 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.6.1-3
- ldirectord: add dependency for perl-IO-Socket-INET6

  Resolves: rhbz#1868063

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.6.1-2
- Make Samba/CIFS dependency weak for Fedora 32 and remove the
  dependency from 33+

* Thu Jun 18 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.6.1-1
- Rebase to resource-agents 4.6.1 upstream release.

* Thu Jun 18 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.6.0-1
- Rebase to resource-agents 4.6.0 upstream release.

* Mon Mar  9 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.5.0-1
- Rebase to resource-agents 4.5.0 upstream release.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.4.0-1
- Rebase to resource-agents 4.4.0 upstream release.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.3.0-1
- Rebase to resource-agents 4.3.0 upstream release.

* Fri May 24 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.0-4
- Fix build issues

* Fri Mar 15 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.0-3
- systemd-tmpfiles: change path to /run/resource-agents

  Resolves: rhbz#1688865

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.0-1
- Rebase to resource-agents 4.2.0 upstream release.
- spec: fix missing systemd config files

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.1.1-1.1
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

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
