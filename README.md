# What?

Trying to analyze Twitter Archive file especially tweet.js with [analyze-tweet](analyze-tweet.py) using python and change it to json object.

# Parsing Arguments in Python

## Debugging

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["--help"],
            "justMyCode": true
        }
    ]
}
```

use **args** to parse through vscode debugger using launch.js config file.