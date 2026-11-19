import argparse
import dis
import importlib.util
import io
import marshal
import types
from contextlib import redirect_stdout
from pathlib import Path

HEADER_SIZE = 16

def inspect_pyc(data):
    if len(data) < HEADER_SIZE:
        raise ValueError("File is too small to contain a modern .pyc header.")
    magic = data[:4]
    flags = int.from_bytes(data[4:8],"little")
    result = {"magic_hex":magic.hex(),"current_magic_hex":importlib.util.MAGIC_NUMBER.hex(),
              "matches_current_interpreter":magic == importlib.util.MAGIC_NUMBER,
              "flags":flags,"header_mode":"hash-based" if flags & 1 else "timestamp-based",
              "checked_hash":bool(flags & 2) if flags & 1 else None,"disassembly":None}
    if not result["matches_current_interpreter"]:
        result["warning"] = "Magic number differs; payload was not unmarshalled."
        return result
    try:
        code = marshal.loads(data[HEADER_SIZE:])
    except (EOFError,ValueError,TypeError) as exc:
        result["warning"] = f"Could not decode payload: {exc}"
        return result
    if not isinstance(code,types.CodeType):
        result["warning"] = "Payload is not a Python code object."
        return result
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        dis.dis(code)
    result["disassembly"] = buffer.getvalue()
    return result

def main():
    parser = argparse.ArgumentParser(description="Inspect a .pyc header and disassemble compatible bytecode.")
    parser.add_argument("file",type=Path)
    args = parser.parse_args()
    try:
        result = inspect_pyc(args.file.read_bytes())
    except (OSError,ValueError) as exc:
        parser.error(str(exc))
    for key,value in result.items():
        if key == "disassembly" and value:
            print("\nDisassembly:\n" + value)
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
