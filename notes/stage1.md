What is a syscall?
A syscall (system call) is a request a program makes to the operating system kernel to perform a task, such as reading files, displaying output, or accessing the network.
Three programs I traced
ls: 154 syscalls. I noticed it uses system calls to read directory contents and display file names.
Python loop: 391 syscalls. I noticed that even a simple Python program makes many system calls behind the scenes.
curl: 729 syscalls. I noticed it makes many network-related system calls to connect to servers and transfer data.
