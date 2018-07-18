#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-broom
Version  : 0.5.0
Release  : 14
URL      : https://cran.r-project.org/src/contrib/broom_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/broom_0.5.0.tar.gz
Summary  : Convert Statistical Analysis Objects into Tidy Tibbles
Group    : Development/Tools
License  : MIT
Requires: R-lfe
Requires: R-mclust
Requires: R-robust
Requires: R-rsample
BuildRequires : R-AER
BuildRequires : R-Lahman
BuildRequires : R-brms
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-lfe
BuildRequires : R-lme4
BuildRequires : R-mclust
BuildRequires : R-plyr
BuildRequires : R-psych
BuildRequires : R-reshape2
BuildRequires : R-robust
BuildRequires : R-rsample
BuildRequires : R-tidyr
BuildRequires : clr-R-helpers

%description
tibbles. This makes it easy to report results, create plots and consistently
    work with large numbers of models at once. Broom provides three verbs that 
    each provide different types of information about a model. tidy()
    summarizes information about model components such as coefficients of
    a regression. glance() reports information about an entire model, such as
    goodness of fit measures like AIC and BIC. augment() adds information
    about individual observations to a dataset, such as fitted values or
    influence measures.

%prep
%setup -q -c -n broom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531885137

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1531885137
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library broom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library broom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library broom
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library broom|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/broom/DESCRIPTION
/usr/lib64/R/library/broom/INDEX
/usr/lib64/R/library/broom/LICENSE
/usr/lib64/R/library/broom/Meta/Rd.rds
/usr/lib64/R/library/broom/Meta/data.rds
/usr/lib64/R/library/broom/Meta/features.rds
/usr/lib64/R/library/broom/Meta/hsearch.rds
/usr/lib64/R/library/broom/Meta/links.rds
/usr/lib64/R/library/broom/Meta/nsInfo.rds
/usr/lib64/R/library/broom/Meta/package.rds
/usr/lib64/R/library/broom/Meta/vignette.rds
/usr/lib64/R/library/broom/NAMESPACE
/usr/lib64/R/library/broom/NEWS.md
/usr/lib64/R/library/broom/R/broom
/usr/lib64/R/library/broom/R/broom.rdb
/usr/lib64/R/library/broom/R/broom.rdx
/usr/lib64/R/library/broom/R/sysdata.rdb
/usr/lib64/R/library/broom/R/sysdata.rdx
/usr/lib64/R/library/broom/data/Rdata.rdb
/usr/lib64/R/library/broom/data/Rdata.rds
/usr/lib64/R/library/broom/data/Rdata.rdx
/usr/lib64/R/library/broom/doc/adding-tidiers.R
/usr/lib64/R/library/broom/doc/adding-tidiers.Rmd
/usr/lib64/R/library/broom/doc/adding-tidiers.html
/usr/lib64/R/library/broom/doc/available-methods.R
/usr/lib64/R/library/broom/doc/available-methods.Rmd
/usr/lib64/R/library/broom/doc/available-methods.html
/usr/lib64/R/library/broom/doc/bootstrapping.R
/usr/lib64/R/library/broom/doc/bootstrapping.Rmd
/usr/lib64/R/library/broom/doc/bootstrapping.html
/usr/lib64/R/library/broom/doc/broom.R
/usr/lib64/R/library/broom/doc/broom.Rmd
/usr/lib64/R/library/broom/doc/broom.html
/usr/lib64/R/library/broom/doc/broom_and_dplyr.R
/usr/lib64/R/library/broom/doc/broom_and_dplyr.Rmd
/usr/lib64/R/library/broom/doc/broom_and_dplyr.html
/usr/lib64/R/library/broom/doc/glossary.R
/usr/lib64/R/library/broom/doc/glossary.Rmd
/usr/lib64/R/library/broom/doc/glossary.html
/usr/lib64/R/library/broom/doc/index.html
/usr/lib64/R/library/broom/doc/kmeans.R
/usr/lib64/R/library/broom/doc/kmeans.Rmd
/usr/lib64/R/library/broom/doc/kmeans.html
/usr/lib64/R/library/broom/extdata/8schools.stan
/usr/lib64/R/library/broom/extdata/rstan_example.rda
/usr/lib64/R/library/broom/help/AnIndex
/usr/lib64/R/library/broom/help/aliases.rds
/usr/lib64/R/library/broom/help/broom.rdb
/usr/lib64/R/library/broom/help/broom.rdx
/usr/lib64/R/library/broom/help/figures/logo.png
/usr/lib64/R/library/broom/help/paths.rds
/usr/lib64/R/library/broom/html/00Index.html
/usr/lib64/R/library/broom/html/R.css
