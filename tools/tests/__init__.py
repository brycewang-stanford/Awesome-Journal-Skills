"""Unit tests for the maintenance tools.

Run them with ``python3 -m unittest discover -s tools/tests`` from the repository
root, or let ``tools/run_checks.py`` run them as the first hard gate.

Everything here is stdlib-only and offline, like the tools themselves. Tests that
need an index build one in a temporary directory rather than reading the committed
743-venue files: a test that reads generated data cannot distinguish "the code is
right" from "the code and the committed output are wrong in the same way", which is
exactly the hole the ``--check`` generators leave open.
"""
