# 🌊 Cloyster Framework 🐚

<p align="left">
  <strong>Interactive CLI wrapper for Donut shellcode generation</strong><br>
  Windows payload generation • multiple architectures • reusable configs • clean terminal workflow
</p>

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey">
  <img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-green">
</p>

```xml
>python cloysterframework.py

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##%@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##%%%%##@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**%%%%%###*%@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**#%%%%%#####+@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@#*#%%%%%%#####*#@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@#*+=+@@@%@%***++#@@@@@@@@@@@%*#%%%%#######*%@@@@@@@@@@@@          
@#@@%%%#**#@@@@@@@@@@@%@%-------=+@#*******@@@@@@@@@@**#########*%@@@@@@@@@@@@@@          
@@@#%%%%%%%%##**###%%@@#@---------*@#***##****%@@@@#*+***#####*@@@@@@@@@@@@@@@@@          
@@@@@%#%%%%%%##**+++=#@@@#+=-------+%#++*#####**#%%%#****%%%#@@@@@@@@@@@@@@@@@@@          
@@@@@@@@*####*+++++=--+#%@@@@%%*-=+=:-*%%#+#%%%%#*****+%@@@@@@@@@@@@@@@@@@@@@@@@          
@@@@@@@@@@@###++=++++*@@--=#%%%%%%%#+#+++++*##*#%%#*******@@@@@@@@@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@#*##**%%#----==*%%%%%#*+#%+++++*@####*+++++**%@@@@%@@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@*@#--------+*--**+++==-%%==+=%@*###%%%#**+*#*++++*@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@*@#-=------+#=---+*##**++==##=%@+########+=****++++*@@@@@@@@@@@@          
@@@@@@@@@@@@@@@=%*-=----=#*--=#%%###*++=--:-#*%%+%%#*#*++*****===+@@@@@@@@@@@@@@         
@@@@@@@@@@@@@@@*+*#=----*@===*###**#**+==--*@#@+##*%%%%##******-++=#@@@@@@@@@@@@          
@@@@@@@@@@@@@@@%==%+-=-*@=++*****++++===-*@@@%@==+#*#%%%%%###################%#@          
@@@@@@@@@@@@@@@@@*%*==-@#-=*@@%=======-%@@@@@%%-===#*#%%%#####################*@          
@@@@@@@@@@@@@@@@@#@#==-%%---#@@@@===----:-=--=#+===***####*+*****##*******#%@@@@          
@@@@@@@@@@@@@@%+=@%====-+#----------:::::-**-::*#--+#*####****+*=+++**%@@@@@@@@@          
@@@@@@@@@@*++++++@*-------**-::::+%@@@@@@*=:::::-*+@#*#####****+==++*+@@@@@@@@@@          
@@@@@@@@@@*+++++=@#==-----=#*-:::::::::::::::::::#@#*##**********=++#@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@*%*=+++===*#=--=-:::::::::::::-#%*#**####++****+=+@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@##*+==+=*@=-======----====+*+*#+####%%%#++*=-==#@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@+=*%#=-=**+======-----=%#++=#***#####*++=++**%@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@#**+=@%+------*===----=#*=+++%***====-=+*++*%@@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@++++%#=-----=+=-----*#++#@%*####**+***%@@@@@@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@#%%+++===--==::--+%@***#####*******+#@@@@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@++=+#%%+--------=*@#********+*+******#+%@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@*+++++%@@#@#=-----=*@********=@@@@@@%**#%%%@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@+*++*@@@@@@@%%=---=###%+***+*@@@@@@@@@@@@%%@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**=%@@@@%#*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

╔══════════════════════════════════════════════════════════════════════════════╗
║                               CLOYSTER FRAMEWORK                             ║
║                          Advanced Offensive Generator                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

[*] Cloyster Framework initialized
[+] Readline loaded (command history + tab completion enabled)
[*] Payloads loaded: 24
[*] Output formats: 11
[*] Type 'help' for available commands
[*] Use 'use <number>' to select a payload
[COMMAND]: menu | show options | use

[😈] cloyste>
```

---

## Overview

**Cloyster Framework** is an interactive command-line framework written in Python that provides a structured interface for working with **Donut**.

Instead of memorizing command flags every time, Cloyster lets you:

- browse supported payload types
- configure generation options interactively
- save/load reusable profiles
- organize generated payloads
- manage plugin/decoy files
- inspect current configuration before generation

The project was designed for:

- malware research labs
- Windows internals study
- red-team simulation labs
- shellcode format conversion workflows
- repeatable testing environments

---

## Credits

Cloyster is built as a CLI layer on top of:

Donut is the core project responsible for generating position-independent shellcode.

Cloyster adds:

- interactive UX
- command history + readline
- profile management
- structured payload menus
- easier workflow for repeatable testing

Huge credit to the original Donut authors.

---

## Features

### Interactive shell

```bash
[😈] cloyster>
```

Built-in commands:

```bash
help
menu
info
show options
use <number>
set <OPTION> <value>
unset <OPTION>
generate
save config
load config
history
plugin
```

---

### Payload categories

Supports:

### x86

- EXE
- DLL
- .NET
- VBScript
- JScript
- Raw shellcode
- Staged payloads
- Module overloading

### x64

- EXE
- DLL
- .NET
- VBScript
- JScript
- Raw shellcode
- Staged payloads
- Module overloading

### Universal

- x86 + x64 combined

---

### Output formats

Generate as:

- `.bin`
- Base64
- C array
- Python bytes
- PowerShell
- C#
- Hex
- UUID
- Go
- Rust

---

### Configuration profiles

Save reusable configs:

```bash
save config win64_lab
```

Load later:

```bash
load config win64_lab
```

Stored in:

```bash
configs/
```

---

### Plugin workspace

Quick copy helper:

```bash
plugin mymodule.dll
```

Moves files into:

```bash
plugin/
```

---

### Payload output folder

Generated output:

```bash
payloads/
```

---

### Command history + tab completion

Automatic history:

```bash
~/.cloyster_history
```

Linux/macOS:

```bash
readline
```

Windows:

```bash
pyreadline3
```

---

## Project structure

```bash
cloyster/
│
├── cloyster.py
├── donut.exe
│
├── configs/
├── payloads/
├── plugin/
│
├── README.md
└── LICENSE
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourname/cloyster-framework.git
cd cloyster-framework
```

Install Python dependency (Windows recommended):

```bash
pip install pyreadline3
```

Download Donut:

👉 https://github.com/TheWover/donut/releases

Place:

```bash
donut.exe
```

next to:

```bash
cloyster.py
```

---

## Usage

Start:

```bash
python cloyster.py
```

Example:

```bash
use 9
set INPUT_FILE calc.exe
set OUTPUT_FILE calc.bin
generate
```

View config:

```bash
show options
```

---

## Example workflow

### 1 Select payload

```bash
use 11
```

### 2 Set input

```bash
set INPUT_FILE payload.dll
```

### 3 Set exported method

```bash
set METHOD RunMe
```

### 4 Configure output

```bash
set OUTPUT_FILE payload.bin
```

### 5 Generate

```bash
generate
```

---

## Safety / Intended use

This project is intended for:

- education
- controlled lab environments
- Windows internals research
- authorized red-team simulations

The author does **not** encourage unauthorized use.

Always verify permissions before testing against any environment.

---

## License

Apache License 2.0

See:

```bash
LICENSE
```

---

## Author

**Guilherme Alexander**

GitHub:
https://github.com/Guilherme-alexander
