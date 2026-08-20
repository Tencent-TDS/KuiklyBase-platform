#!/usr/bin/env python3
"""Host-side check: OHOS okio patch must pass octal 0o666 to POSIX open().

No Harmony device required. Kotlin 666 is decimal (0o1232), not POSIX 0666.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

PATCH = Path(__file__).with_name("okio.patch")
OPEN_MODE_RE = re.compile(
    r"^\+\s*val fid = open\(file\.toString\(\), flags, ([^)]+)\)",
    re.MULTILINE,
)


class PosixOpenModeTest(unittest.TestCase):
    def test_kotlin_666_is_decimal_not_posix_0666(self) -> None:
        self.assertNotEqual(666, 0o666)
        self.assertEqual(0o666, 438)
        self.assertEqual(666, 0o1232)

    def test_patch_uses_octal_0o666_not_decimal_666(self) -> None:
        text = PATCH.read_text(encoding="utf-8")
        added_modes = OPEN_MODE_RE.findall(text)
        self.assertEqual(
            added_modes,
            ["0o666"],
            f"expected variantOpenReadWrite to use 0o666, got {added_modes}",
        )
        self.assertNotIn(
            "open(file.toString(), flags, 666)",
            text,
            "decimal 666 must not be passed to POSIX open()",
        )


if __name__ == "__main__":
    unittest.main()
