@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set "SPHINXBUILD=sphinx-build"
)
set SOURCEDIR=source
set BUILDDIR=build\%1

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

%SPHINXBUILD% -a -b %1 "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
if "%1" == "html" (
	rmdir /S /Q "%~dp0/docs"
	move /Y "%BUILDDIR%" "%~dp0/docs"
)

goto :end

:help
%SPHINXBUILD% --help

:end
popd
