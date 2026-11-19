<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=Python%20Bytecode%20Inspector&fontColor=ffffff&fontSize=34" alt="Python Bytecode Inspector banner"/></p>
<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=620&lines=Inspect%20Python%20bytecode%3BRead%20.pyc%20headers%20safely%3BDisassemble%20without%20execution" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/python-bytecode-inspector?style=flat-square"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-bytecode-inspector?style=flat-square"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/python-bytecode-inspector?style=flat-square"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-bytecode-inspector?style=flat-square"/></p>
<p align="center"><img src="assets/mark.svg" width="520" alt="Python Bytecode Inspector illustration"/></p>

## 🧭 Overview
Python Bytecode Inspector reads `.pyc` header metadata and, when the magic number matches the running interpreter, disassembles the marshalled code object. It never executes the bytecode.

## ✨ Features
- 🧬 Show magic number, flags, and timestamp/hash header mode
- 🧩 Check compatibility with the current Python interpreter
- 🔬 Disassemble compatible code objects using `dis`
- 🛡️ Never execute the inspected bytecode

## 🖥️ Demo
No hosted demo is provided. Run the project locally using the quick-start command.

## 🚀 Quick Start
Requires Python 3.10 or newer.

```bash
python main.py path/to/module.pyc
```

Run checks with `python -m unittest discover -s tests -v`.

## 🧰 Tech Stack
- Python standard library
- `argparse` CLI and `unittest`
- Read-only inspection by default

## 🗂️ Folder Structure
```text
.
├── .github/workflows/ci.yml
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap
- [ ] Add more edge-case fixtures
- [ ] Improve machine-readable output
- [ ] Keep the core workflow lightweight and local-first

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser and reporting changes.

## 📄 License
MIT License. See [LICENSE](LICENSE).
<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=100&section=footer" alt="Animated wave footer"/></p>
