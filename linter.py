from SublimeLinter.lint import Linter
import os

script = """
Import-Module PSScriptAnalyzer;
"\\$FullResult = Invoke-ScriptAnalyzer -Path ${temp_file}";
"foreach (\\$Result in \\$FullResult)"
{
    "\\$Line = \\$Result.Line";
    "\\$Message = \\$Result.Message";
    "\\$RuleName = \\$Result.RuleName";
    "\\$Severity = \\$Result.Severity";
    "\\$Column = \\$Result.column";
    '\"\\$Line   \\$Message   \\$Severity   \\$Column   \\$RuleName\"'
}"""


class Powershell(Linter):

    if os.name == 'nt':
        cmd = 'powershell.exe -nol -c {}'.format(script)
    else:
        cmd = 'pwsh -nol -c {}'.format(script)

    regex = (
        r'(?P<line>\d+)\s\s\s(?P<message>.*?)\s\s\s((?P<error>\S*Error)|'
        r'(?P<warning>Warning|Information))\s\s\s(?P<col>\d+)\s\s\s(?P<code>.*)'
    )

    tempfile_suffix = '.tempPS1'
    multiline = False
    word_re = r'^([-\S]+|\s+$)'
    defaults = {
        'selector': 'source.powershell'
    }
