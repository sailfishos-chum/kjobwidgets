%global kf5_version 5.107.0

Name: opt-kf5-kjobwidgets
Version: 5.107.0
Release: 1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for KJobs

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/kjobwidgets
Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-kcoreaddons >= %{kf5_version}
Requires: opt-kf5-kwidgetsaddons >= %{kf5_version}

%description
KDE Frameworks 5 Tier 2 addon for KJobs

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
Requires: opt-kf5-kcoreaddons-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../

%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 kjobwidgets5_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kjobwidgets.*
%{_opt_kf5_libdir}/libKF5JobWidgets.so.*
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KJobWidgets/
%{_opt_kf5_libdir}/libKF5JobWidgets.so
%{_opt_kf5_libdir}/cmake/KF5JobWidgets/
%{_opt_kf5_datadir}/dbus-1/interfaces/*.xml
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KJobWidgets.pri
