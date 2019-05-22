SublimeLinter-contrib-powershell
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer). It will be used with files that have the “PowerShell” syntax.  

This linter works on Windows PowerShell 3.0 or greater and PowerShell Core 6.1.0 or greater on Windows/Linux/macOS.  
You can check your powershell version with `$PSVersionTable.PSVersion` from a powershell prompt.  

## Installation
SublimeLinter must be installed in order to use this plugin. 
Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that [PSScriptAnalyzer](https://www.powershellgallery.com/packages/PSScriptAnalyzer) is installed on your system and available on powershell startup.  

PSScriptAnalyzer can be installed with `Install-Module -Name PSScriptAnalyzer` from a powershell prompt, which automatically makes the module available on powershell startup.  

## Settings
The simplest way to change the [ScriptAnalyzer settings](https://github.com/PowerShell/PSScriptAnalyzer#settings-support-in-scriptanalyzer) is from a settings file.  
An example [settings file](https://github.com/EdrisT/SublimeLinter-contrib-Powershell/blob/master/PSScriptAnalyzerSettings.psd1) with commented options is located in this plugins root folder. The provided example settings file checks for compatibility with powershell 3.0 and excludes the check for trailing spaces.  

**The linter will decide which settings to use in the following order:**  
1. If a valid [PSScriptAnalyzerSettings.psd1](https://github.com/EdrisT/SublimeLinter-contrib-Powershell/blob/master/PSScriptAnalyzerSettings.psd1) file exists in your project folder, those settings will have precedence over all other settings. This enables you to use different settings for different projects.

2.  If the variable `$GlobalPSScriptAnalyzerSettingsPath` exists in your powershell environment and is populated with the full path to a valid settings file, those settings will be used. This enables you to use global custom settings. For persistency, set this variable in your powershell profile.

3. If no settings file is found in your project folder and the `$GlobalPSScriptAnalyzerSettingsPath` variable is not set, default settings of PSScriptAnalyzer will be used. (all default rules enabled and no compatibility checks)

### SublimeLinter settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
