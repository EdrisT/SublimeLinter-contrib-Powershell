from SublimeLinter.lint import Linter
import os

script = """
Import-Module PSScriptAnalyzer;
"\\$ErrorActionPreference" = \\"SilentlyContinue\\" ;
if (Test-Path PSScriptAnalyzerSettings.psd1)
{
    "\\$FullResult" = Invoke-ScriptAnalyzer ${temp_file} -Setting PSScriptAnalyzerSettings.psd1
}
else
{
    if ("\\$Env:PSScriptAnalyzerSettingsPath")
    {
        "\\$FullResult" = Invoke-ScriptAnalyzer ${temp_file} -Setting "\\$Env:PSScriptAnalyzerSettingsPath"
    }
    elseif ("\\$GlobalPSScriptAnalyzerSettingsPath")
    {
        "\\$FullResult" = Invoke-ScriptAnalyzer ${temp_file} -Setting "\\$GlobalPSScriptAnalyzerSettingsPath"
    }
    else
    {
        "\\$FullResult" = Invoke-ScriptAnalyzer -Path ${temp_file}
    }
};

foreach ("\\$Result" in "\\$FullResult")
{
    "\\$Line"       =   "\\$Result.Line" ;
    "\\$Message"    =   "\\$Result.Message" ;
    "\\$RuleName"   =   "\\$Result.RuleName" ;
    "\\$Severity"   =   "\\$Result.Severity" ;
    "\\$Column"     =   "\\$Result.column" ;
    "\\$Extent"     =   "\\$Result.Extent.Text.trim()" ;
    "\\$Suggestion" =   "\\$Result.SuggestedCorrections.description" ;

    if ("\\$Extent")
    {
        Write-Host '"Line:\\$Line RuleName:\\$RuleName Severity:\\$Severity Extent:\\$Extent Message:\\$Message \\$Suggestion"'
    }
    else
    {
        Write-Host '"Line:\\$Line RuleName:\\$RuleName Severity:\\$Severity Column:\\$Column Message:\\$Message \\$Suggestion"'
    }
}"""


class Powershell(Linter):

    if os.name == 'nt':
        cmd = 'powershell.exe -nol -c {}; '.format(script)
    else:
        cmd = 'pwsh -nol -c {}; '.format(script)

    regex = (
        r'Line:(?P<line>\d+)\sRuleName:(?P<code>\w+)\sSeverity:((?P<error>\S*?Error)|'
        r'(?P<warning>Warning|Information))\s(Column:(?P<col>\d+)|Extent:(?P<near>.*?))\sMessage:(?P<message>.*)'
    )

    tempfile_suffix = 'ps'
    multiline = False
    word_re = r'^([-\S]+|\s+$)'
    defaults = {
        "selector": "source.powershell"
    }
