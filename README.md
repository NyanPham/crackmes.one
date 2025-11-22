# My Reverse Engineering Journey

Welcome! This repo is where I'm tracking my adventures in reverse engineering. I'm tackling various "crackme" challenges to sharpen my skills in assembly, software security, and the art of taking things apart to see how they tick. Think of it as my personal lab notebook.

Hi, I'm Nyan. This is the repo where I track my adventrues in reverse engineering, specifically various "crackme" challenges from the site [Crackmes.one](https://crackmes.one).
I mainly target C/C++ binaries on Linux based x86-64 architecture.

## Progress Tracker

I have this file [**`0.LIST.md`**](./0.LIST.md) to remind myself which next item to tackle on the list, and probably get back to previous crackmes that need revisiting as well.

## Repository Structure

The crackmes are categorized in several levels of difficulty. They are organized in the folders' name. For example, folder "2" stores all the crackmes that a marked "Difficulty level 2" by the time I downloaded them, and folder "2_3" means the difficulty > 2 and < 3.

Each Crackme has its own folder, with their names (and possibly author's name concatenated in front). In the folder, there are a binary file (crackme), a folder named sols containing other's write-ups to help me when I get stuck, and some other files in _txt_ or _py_ as my own notes, write-ups and solutions.

## My Toolkit

These are the tools I find myself reaching for most often:

-   **Disassemblers/Decompilers**:
    -   IDA Pro
    -   Ghidra
-   **Debuggers**:
    -   GDB (GNU Debugger)
-   **CLI Magic**:
    -   `objdump`, `strings`, `ltrace`, `strace`
-   **Scripting**:
    -   Python for whipping up keygens and automating the boring stuff.
