#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: 750e50d
#
Name     : R-ggstats
Version  : 0.5.1
Release  : 3
URL      : https://cran.r-project.org/src/contrib/ggstats_0.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggstats_0.5.1.tar.gz
Summary  : Extension to 'ggplot2' for Plotting Stats
Group    : Development/Tools
License  : GPL-3.0
Requires: R-broom.helpers
Requires: R-cli
Requires: R-dplyr
Requires: R-forcats
Requires: R-ggplot2
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-patchwork
Requires: R-purrr
Requires: R-rlang
Requires: R-scales
Requires: R-stringr
Requires: R-tidyr
BuildRequires : R-broom.helpers
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-forcats
BuildRequires : R-ggplot2
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-patchwork
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : R-stringr
BuildRequires : R-tidyr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
'ggplot2' and a suite of functions to facilitate the creation of 
    statistical plots.

%prep
%setup -q -n ggstats
pushd ..
cp -a ggstats buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707101842

%install
export SOURCE_DATE_EPOCH=1707101842
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggstats/DESCRIPTION
/usr/lib64/R/library/ggstats/INDEX
/usr/lib64/R/library/ggstats/Meta/Rd.rds
/usr/lib64/R/library/ggstats/Meta/features.rds
/usr/lib64/R/library/ggstats/Meta/hsearch.rds
/usr/lib64/R/library/ggstats/Meta/links.rds
/usr/lib64/R/library/ggstats/Meta/nsInfo.rds
/usr/lib64/R/library/ggstats/Meta/package.rds
/usr/lib64/R/library/ggstats/Meta/vignette.rds
/usr/lib64/R/library/ggstats/NAMESPACE
/usr/lib64/R/library/ggstats/NEWS.md
/usr/lib64/R/library/ggstats/R/ggstats
/usr/lib64/R/library/ggstats/R/ggstats.rdb
/usr/lib64/R/library/ggstats/R/ggstats.rdx
/usr/lib64/R/library/ggstats/WORDLIST
/usr/lib64/R/library/ggstats/doc/ggcoef_model.R
/usr/lib64/R/library/ggstats/doc/ggcoef_model.Rmd
/usr/lib64/R/library/ggstats/doc/ggcoef_model.html
/usr/lib64/R/library/ggstats/doc/gglikert.R
/usr/lib64/R/library/ggstats/doc/gglikert.Rmd
/usr/lib64/R/library/ggstats/doc/gglikert.html
/usr/lib64/R/library/ggstats/doc/index.html
/usr/lib64/R/library/ggstats/doc/stat_cross.R
/usr/lib64/R/library/ggstats/doc/stat_cross.Rmd
/usr/lib64/R/library/ggstats/doc/stat_cross.html
/usr/lib64/R/library/ggstats/doc/stat_prop.R
/usr/lib64/R/library/ggstats/doc/stat_prop.Rmd
/usr/lib64/R/library/ggstats/doc/stat_prop.html
/usr/lib64/R/library/ggstats/doc/stat_weighted_mean.R
/usr/lib64/R/library/ggstats/doc/stat_weighted_mean.Rmd
/usr/lib64/R/library/ggstats/doc/stat_weighted_mean.html
/usr/lib64/R/library/ggstats/help/AnIndex
/usr/lib64/R/library/ggstats/help/aliases.rds
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-10-1.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-4-2.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-7-1.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-8-1.png
/usr/lib64/R/library/ggstats/help/figures/README-unnamed-chunk-9-1.png
/usr/lib64/R/library/ggstats/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/ggstats/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/ggstats/help/ggstats.rdb
/usr/lib64/R/library/ggstats/help/ggstats.rdx
/usr/lib64/R/library/ggstats/help/paths.rds
/usr/lib64/R/library/ggstats/html/00Index.html
/usr/lib64/R/library/ggstats/html/R.css
/usr/lib64/R/library/ggstats/tests/spelling.R
/usr/lib64/R/library/ggstats/tests/testthat.R
/usr/lib64/R/library/ggstats/tests/testthat/test-geom_stripped.R
/usr/lib64/R/library/ggstats/tests/testthat/test-ggcoef_model.R
/usr/lib64/R/library/ggstats/tests/testthat/test-gglikert.R
/usr/lib64/R/library/ggstats/tests/testthat/test-position_likert.R
/usr/lib64/R/library/ggstats/tests/testthat/test-stat_cross.R
/usr/lib64/R/library/ggstats/tests/testthat/test-stat_prop.R
/usr/lib64/R/library/ggstats/tests/testthat/test-stat_weighted_mean.R
/usr/lib64/R/library/ggstats/tests/testthat/test-utilities.R
/usr/lib64/R/library/ggstats/tests/testthat/test_ggsurvey.R
