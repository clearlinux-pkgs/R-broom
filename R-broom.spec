#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-broom
Version  : 0.5.1
Release  : 22
URL      : https://cran.r-project.org/src/contrib/broom_0.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/broom_0.5.1.tar.gz
Summary  : Convert statistical analysis objects into tidy data frames.
Group    : Development/Tools
License  : MIT
Requires: R-betareg
Requires: R-glmnet
Requires: R-highr
BuildRequires : R-AER
BuildRequires : R-Lahman
BuildRequires : R-betareg
BuildRequires : R-binGroup
BuildRequires : R-brms
BuildRequires : R-dplyr
BuildRequires : R-emmeans
BuildRequires : R-gam
BuildRequires : R-geepack
BuildRequires : R-generics
BuildRequires : R-ggplot2
BuildRequires : R-glmnet
BuildRequires : R-highr
BuildRequires : R-joineRML
BuildRequires : R-lfe
BuildRequires : R-lme4
BuildRequires : R-lsmeans
BuildRequires : R-mclust
BuildRequires : R-plyr
BuildRequires : R-poLCA
BuildRequires : R-psych
BuildRequires : R-reshape2
BuildRequires : R-robust
BuildRequires : R-rsample
BuildRequires : R-speedglm
BuildRequires : R-tidyr
BuildRequires : buildreq-R

%description
broom <img src="man/figures/logo.png" align="right" width="100" height="100" />
===============================================================================

%prep
%setup -q -c -n broom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552723968

%install
export SOURCE_DATE_EPOCH=1552723968
rm -rf %{buildroot}
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
R CMD check --no-manual --no-examples --no-codoc  broom || :


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
/usr/lib64/R/library/broom/tests/test-all.R
/usr/lib64/R/library/broom/tests/testthat/helper-tests.R
/usr/lib64/R/library/broom/tests/testthat/test-aer.R
/usr/lib64/R/library/broom/tests/testthat/test-auc.R
/usr/lib64/R/library/broom/tests/testthat/test-base.R
/usr/lib64/R/library/broom/tests/testthat/test-bbmle.R
/usr/lib64/R/library/broom/tests/testthat/test-betareg.R
/usr/lib64/R/library/broom/tests/testthat/test-biglm.R
/usr/lib64/R/library/broom/tests/testthat/test-bingroup.R
/usr/lib64/R/library/broom/tests/testthat/test-boot.R
/usr/lib64/R/library/broom/tests/testthat/test-btergm.R
/usr/lib64/R/library/broom/tests/testthat/test-car.R
/usr/lib64/R/library/broom/tests/testthat/test-caret.R
/usr/lib64/R/library/broom/tests/testthat/test-deprecating.R
/usr/lib64/R/library/broom/tests/testthat/test-emmeans.R
/usr/lib64/R/library/broom/tests/testthat/test-ergm.R
/usr/lib64/R/library/broom/tests/testthat/test-gam.R
/usr/lib64/R/library/broom/tests/testthat/test-gamlss.R
/usr/lib64/R/library/broom/tests/testthat/test-geepack.R
/usr/lib64/R/library/broom/tests/testthat/test-glmnet.R
/usr/lib64/R/library/broom/tests/testthat/test-gmm.R
/usr/lib64/R/library/broom/tests/testthat/test-hmisc.R
/usr/lib64/R/library/broom/tests/testthat/test-joineRML.R
/usr/lib64/R/library/broom/tests/testthat/test-kendall.R
/usr/lib64/R/library/broom/tests/testthat/test-ks.R
/usr/lib64/R/library/broom/tests/testthat/test-lavaan.R
/usr/lib64/R/library/broom/tests/testthat/test-lfe.R
/usr/lib64/R/library/broom/tests/testthat/test-list-irlba.R
/usr/lib64/R/library/broom/tests/testthat/test-list-optim.R
/usr/lib64/R/library/broom/tests/testthat/test-list-svd.R
/usr/lib64/R/library/broom/tests/testthat/test-list-xyz.R
/usr/lib64/R/library/broom/tests/testthat/test-list.R
/usr/lib64/R/library/broom/tests/testthat/test-lmodel2.R
/usr/lib64/R/library/broom/tests/testthat/test-lmtest.R
/usr/lib64/R/library/broom/tests/testthat/test-maps.R
/usr/lib64/R/library/broom/tests/testthat/test-mass-fitdistr.R
/usr/lib64/R/library/broom/tests/testthat/test-mass-polr.R
/usr/lib64/R/library/broom/tests/testthat/test-mass-ridgelm.R
/usr/lib64/R/library/broom/tests/testthat/test-mass-rlm.R
/usr/lib64/R/library/broom/tests/testthat/test-mclust.R
/usr/lib64/R/library/broom/tests/testthat/test-mgcv.R
/usr/lib64/R/library/broom/tests/testthat/test-muhaz.R
/usr/lib64/R/library/broom/tests/testthat/test-multcomp.R
/usr/lib64/R/library/broom/tests/testthat/test-nnet.R
/usr/lib64/R/library/broom/tests/testthat/test-null-and-default.R
/usr/lib64/R/library/broom/tests/testthat/test-orcutt.R
/usr/lib64/R/library/broom/tests/testthat/test-ordinal.R
/usr/lib64/R/library/broom/tests/testthat/test-plm.R
/usr/lib64/R/library/broom/tests/testthat/test-polca.R
/usr/lib64/R/library/broom/tests/testthat/test-psych.R
/usr/lib64/R/library/broom/tests/testthat/test-quantreg-nlrq.R
/usr/lib64/R/library/broom/tests/testthat/test-quantreg-rq.R
/usr/lib64/R/library/broom/tests/testthat/test-quantreg-rqs.R
/usr/lib64/R/library/broom/tests/testthat/test-robust.R
/usr/lib64/R/library/broom/tests/testthat/test-sp.R
/usr/lib64/R/library/broom/tests/testthat/test-speedglm.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-anova.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-arima.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-decompose.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-factanal.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-glm.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-htest.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-kmeans.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-lm.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-loess.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-nls.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-prcomp.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-smooth.spline.R
/usr/lib64/R/library/broom/tests/testthat/test-stats-time-series.R
/usr/lib64/R/library/broom/tests/testthat/test-stats.R
/usr/lib64/R/library/broom/tests/testthat/test-survey.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-aareg.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-cch.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-coxph.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-pyears.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-survdiff.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-survexp.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-survfit.R
/usr/lib64/R/library/broom/tests/testthat/test-survival-survreg.R
/usr/lib64/R/library/broom/tests/testthat/test-tseries.R
/usr/lib64/R/library/broom/tests/testthat/test-utilities.R
/usr/lib64/R/library/broom/tests/testthat/test-zoo.R
