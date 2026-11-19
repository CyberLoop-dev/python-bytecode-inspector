import py_compile
import tempfile
import unittest
from pathlib import Path
from main import inspect_pyc

class BytecodeInspectorTests(unittest.TestCase):
    def test_inspects_current_interpreter_pyc(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "sample.py"
            output = Path(folder) / "sample.pyc"
            source.write_text("answer = 42\n",encoding="utf-8")
            py_compile.compile(str(source),cfile=str(output),doraise=True)
            result = inspect_pyc(output.read_bytes())
            self.assertTrue(result["matches_current_interpreter"])
            self.assertIn("answer",result["disassembly"])
    def test_rejects_short_header(self):
        with self.assertRaises(ValueError):
            inspect_pyc(b"tiny")

if __name__ == "__main__":
    unittest.main()
