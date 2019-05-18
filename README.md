SublimeLinter-contrib-powershell
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer). It will be used with files that have the “PowerShell” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `PSScriptAnalyzer` is installed on your system.  

PSScriptAnalyzer can be installed with `Install-Module -Name PSScriptAnalyzer` from a powershell prompt, which automatically makes the module available on powershell startup.  

If PSScriptAnalyzer is downloaded and installed manually you have to make sure the module is loaded on powershell startup.  

This plugin works on Windows PowerShell 3.0 or greater and PowerShell Core 6.1.0 or greater on Windows/Linux/macOS.  
You can check your powershell version with `$PSVersionTable.PSVersion` from a powershell prompt.

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
